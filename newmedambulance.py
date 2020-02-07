from flask import Flask,request,abort
from flask_socketio import SocketIO,emit
import uuid
import json
#import socketio
# from googlegeocoder import GoogleGeocoder
from math import sin,cos,sqrt,atan2,radians
from decimal import Decimal
import json
import numpy as np
import pymysql
import requests
import databasefile
import commonfile
import json
import pymysql
from flask_cors import CORS
from datetime import datetime
import pytz 
import pytz
from config import Connection
import commonfile


from flask import Flask, render_template
from flask_socketio import SocketIO

import socketio

# standard Python
sio = socketio.Client()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")
# sio = socketio.Client()

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)

# geocoder = GoogleGeocoder("AIzaSyB0Pz6VjrQmWPCCbDbWDuyjo79GhDJPOlI")





@app.route('/addUser', methods=['POST'])
def addUser():
    try:
        inputdata =  commonfile.DecodeInputdata(request.get_data()) 
        startlimit,endlimit="",""
        keyarr = ['name','mobile','userTypeId','email','password','currentLocation','currentLocationlatlong']
        commonfile.writeLog("addUser",inputdata,0)
        msg = commonfile.CheckKeyNameBlankValue(keyarr,inputdata)
       
        if msg == "1":
            imeiNo,country,city,deviceName,deviceId,deviceType="","","","","",""
            os,appVersion,notificationToken,ipAddress,userAgent="","","","",""
            
            Name = inputdata["name"]
            userTypeId = inputdata["userTypeId"]
            Mobile=inputdata["mobile"]
            Email = inputdata["email"]
            password = inputdata["password"]
            currentLocation=inputdata["currentLocation"]
            currentLocationlatlong=inputdata["currentLocationlatlong"]

            
           

           

            UserId = commonfile.CreateHashKey(Mobile,Name)
            
            WhereCondition = " and mobile = '" + str(Mobile) + "' and password = '" + str(password) + "'"
            count = databasefile.SelectCountQuery("userMaster",WhereCondition,"")
            
            if int(count) > 0:
                return commonfile.EmailMobileAlreadyExistMsg()
            else:
                if 'imeiNo' in inputdata:
                    imeiNo=inputdata["imeiNo"] 

                if 'deviceName' in inputdata:
                    deviceName=inputdata["deviceName"]

                if 'country' in inputdata:
                    country=inputdata["country"]

                if 'city' in inputdata:
                    city=inputdata["city"]

                if 'ipAddress' in inputdata:
                    ipAddress=inputdata["ipAddress"]

                if 'userAgent' in inputdata:
                    userAgent=inputdata["userAgent"]


                if 'deviceId' in inputdata:
                    deviceId=inputdata["deviceId"]

                
                if 'os' in inputdata:
                    os=inputdata["os"]

                
                if 'deviceType' in inputdata:
                    deviceType=inputdata["deviceType"]

                if 'appVersion' in inputdata:
                    appVersion=inputdata["appVersion"] 


                if 'notificationToken' in inputdata:
                    notificationToken=inputdata["notificationToken"]



 


                column="name,password,mobile,userId,imeiNo,deviceName,currentLocation,currentLocationlatlong,usertypeId,email,country,city, "
                column=column+ "ipAddress,userAgent,deviceId,os,deviceType,appVersion,notificationToken"

                values =  "'"+str(Name)+"','"+str(password)+"','"
                values= values +str(Mobile)+"','"+str(UserId)+"','"+str(imeiNo)+"','"+str(deviceName)+"','"
                values= values+str(currentLocation)+"','"+str(currentLocationlatlong)+"','"+str(userTypeId)+"','"
                values= values+str(Email)+"','"+str(country)+"','"+str(city)+"','"
                values= values+str(ipAddress)+"','"+str(userAgent)+"','"+str(deviceId)+"','"
                values= values+str(os)+"','"+str(deviceType)+"','"+str(appVersion)+ "','"+str(notificationToken)+ "'"
                data=databasefile.InsertQuery("userMaster",column,values)
             

                if data != "0":
                    column = '*'
                    
                    data = databasefile.SelectQuery2("userMaster",column,WhereCondition,"",startlimit,endlimit)
                    print(data)
                    Data = {"status":"true","message":"","result":data["result"]}                  
                    return Data
                else:
                    return commonfile.Errormessage()
                        
        else:
            return msg 
    except Exception as e :
        print("Exception---->" +str(e))           
        output = {"status":"false","message":"something went wrong","result":""}
        return output



@app.route('/addDriver', methods=['POST'])
def addDriver():
    try:
        data1 = commonfile.DecodeInputdata(request.get_data())
        
        column = " * "
        whereCondition= "mobile='"+str(data1["mobile"])+ "' and usertypeId='3'"
        data= databasefile.SelectQuery("userMaster",column,whereCondition)
        if data !=None:
            column="name,mobile,driverId,ambulanceModeId,ambulanceId,panCardNo,DlNo,currentLocation,currentLocationlatlong,vehicleNo"
            values=  "'"+str(data["name"])+"','"+str(data["mobile"])+"','"+str(data["userId"])+"','"+str(data1["ambulanceModeId"])+"','"
            values=values +str(data1["ambulanceId"])+"','"+str(data1["panCardNo"])+"','"+str(data1["DlNo"])+"','"
            values=values+str(data["currentLocation"])+"','"+str(data["currentLocationlatlong"])+"','"+str(data1["vehicleNo"])+"'"
            insertdata=databasefile.InsertQuery("driverMaster",column,values)
            column = " * "
            whereCondition= "mobile='"+str(data1["mobile"])+ "'"
            data17= databasefile.SelectQuery1("driverMaster",column,whereCondition)
            output= {"result":"Revert You Soon,After Verification","status":"true"}
            return output
        else:
            output = {"result":"User Already Added Existed ","status":"false"}
            return output
    except Exception as e :
        print("Exception---->" + str(e))    
        output = {"result":"something went wrong","status":"false"}
        return output


#Login
@app.route('/Login', methods=['POST'])
def login():
    try:
        inputdata =  commonfile.DecodeInputdata(request.get_data())
        startlimit,endlimit="",""
        keyarr = ['password','mobile']
        commonfile.writeLog("Login",inputdata,0)
        msg = commonfile.CheckKeyNameBlankValue(keyarr,inputdata)
        if msg == "1":
            mobile = inputdata["mobile"]
            password = inputdata["password"]
            column=  "us.mobile,us.name,um.usertype,us.userId"
            whereCondition= "us.mobile = '" + str(mobile) + "' and us.password = '" + password + "'  and  us.usertypeId=um.Id"
            loginuser=databasefile.SelectQuery1("userMaster as us,usertypeMaster as um",column,whereCondition)
            if (loginuser!=0):   
                Data = {"result":loginuser,"status":"true"}                  
                return Data
            else:
                data={"status":"Failed","result":"Login Failed"}
                return data

        else:
            return msg 
    except KeyError as e:
        print("Exception---->" +str(e))        
        output = {"result":"Input Keys are not Found","status":"false"}
        return output    
    except Exception as e :
        print("Exception---->" +str(e))           
        output = {"result":"something went wrong","status":"false"}
        return output
#select(resonder,driver,user,)

@app.route('/selectusertypeMaster', methods=['GET'])
def usertypeMaster():
    try:
        msg="1"
        if msg == "1":
            column="id,usertype"
            whereCondition=""
            data=databasefile.SelectQuery1("usertypeMaster",column,whereCondition)
            if (data!=0):           
                Data = {"result":data,"status":"true","message":""}
                return Data
            else:
                output = {"message":"No Data Found","status":"false","result":""}
                return output
                        
        else:
            return msg 

    except Exception as e :
        print("Exception---->" + str(e))    
        output = {"result":"something went wrong","status":"false"}
        return output         

@app.route('/addambulanceMode', methods=['POST'])
def addambulanceMode():
    try:
        inputdata =  commonfile.DecodeInputdata(request.get_data())
        startlimit,endlimit="",""
        keyarr = ['ambulanceType']
        commonfile.writeLog("addambulanceMode",inputdata,0)
        msg = commonfile.CheckKeyNameBlankValue(keyarr,inputdata)
        if msg == "1":
            ambulanceType = inputdata["ambulanceType"]
            column = " * "
            whereCondition= "ambulanceType='"+str(ambulanceType)+ "'"
            data = databasefile.SelectQuery("ambulanceMode",column,whereCondition)
            print(data,'==data')
            if data == 0:
                column="ambulanceType"
                values="'"+str(ambulanceType)+"'"
                insertdata=databasefile.InsertQuery("ambulanceMode",column,values)
                column="*"
                whereCondition= "ambulanceType='"+str(ambulanceType)+ "'"
                data8= databasefile.SelectQuery1("ambulanceMode",column,whereCondition)
                output= {"result":"User Added Successfully","ambulance Details":data8[-1],"status":"true"}
                return output
            else:
                output = {"result":"User Already Added Existed ","status":"true","ambulance Details":data}
                return output
        else:
            return msg 
    except Exception as e :
        print("Exception---->" + str(e))    
        output = {"result":"something went wrong","status":"false"}
        return output         


@app.route('/selectambulanceMode', methods=['GET'])
def ambulanceMode():
    try:
        msg = "1"
        if msg =="1":
            column="id ,ambulanceType"
            whereCondition=""
            data=databasefile.SelectQuery1("ambulanceMode",column,whereCondition)
            if (data!=0):           
                Data = {"result":data,"status":"true"}
                return Data
            else:
                output = {"result":"No Data Found","status":"false"}
                return output
        else:
            return msg

    except Exception as e :
        print("Exception---->" + str(e))    
        output = {"result":"something went wrong","status":"false"}
        return output


@app.route('/updateambulanceMode', methods=['POST'])
def updateambulanceMode():
    try:
        inputdata =  commonfile.DecodeInputdata(request.get_data())
        startlimit,endlimit="",""
        keyarr = ['ambulanceType','id']
        commonfile.writeLog("updateambulanceMode",inputdata,0)
        msg = commonfile.CheckKeyNameBlankValue(keyarr,inputdata)
        if msg=="1":
            ambulanceType = inputdata["ambulanceType"]
            id = inputdata["id"]
            column= " * "
            whereCondition="id = '" + str(id)+ "'"
            data1 = databasefile.SelectQuery("ambulanceMode",column,whereCondition)
            print(data1,"data1")
            if data1 != 0:
                column = ""
                whereCondition = ""
                column= " ambulanceType='" + str(ambulanceType) + "'"
                whereCondition="id = '" + str(id)+ "'"
                data = databasefile.UpdateQuery("ambulanceMode",column,whereCondition)
                print(data,'===')
                output = {"result":"Updated Successfully","status":"true"}
                return output
            else:
                output = {"result":"Data Not Found","status":"true"}
                return output
        else:
            return msg 
    except KeyError :
        print("Key Exception---->")   
        output = {"result":"key error","status":"false"}
        return output  

    except Exception as e :
        print("Exception---->" +str(e))    
        output = {"result":"somthing went wrong","status":"false"}
        return output



       


@app.route('/addambulance', methods=['POST'])
def addambulance():
    try:
        inputdata =  commonfile.DecodeInputdata(request.get_data())
        startlimit,endlimit="",""
        keyarr = ['ambulanceType']
        commonfile.writeLog("addambulance",inputdata,0)
        msg = commonfile.CheckKeyNameBlankValue(keyarr,inputdata)
        if msg == "1":
            ambulanceType = inputdata["ambulanceType"]
            column="*"
            whereCondition="ambulanceType='"+str(ambulanceType)+"'"
            data= databasefile.SelectQuery("ambulanceMaster",column,whereCondition)
            print(data,"==data")
            if data==0:
                column="ambulanceType"
                values="'"+str(ambulanceType)+"'"
                insertdata=databasefile.InsertQuery("ambulanceMaster",column,values)
                column="*"
                whereCondition="ambulanceType='"+str(ambulanceType)+"'"
                data1= databasefile.SelectQuery1("ambulanceMaster",column,whereCondition)
                output= {"result":"User Added Successfully","ambulance Details":data1[-1],"status":"true"}
                return output
            else:
                output = {"result":"User Already Added Existed ","status":"true","ambulance Details":data}
                return output 
        else:
            return msg
    except Exception as e :
        print("Exception---->" + str(e))    
        output = {"result":"something went wrong","status":"false"}
        return output
 

@app.route('/selectambulanceMaster', methods=['GET'])
def ambulanceMaster():
    try:
        msg = "1"
        if msg=="1":
            column="id ,ambulanceType"
            whereCondition=""
            data=databasefile.SelectQuery1("ambulanceMaster",column,whereCondition)
            if (data!=0):           
                Data = {"result":data,"status":"true"}
                return Data
            else:
                output = {"result":"No Data Found","status":"false"}
                return output
        else:
            return msg
    except Exception as e :
        print("Exception---->" + str(e))    
        output = {"result":"something went wrong","status":"false"}
        return output  


@app.route('/updateambulanceMaster', methods=['POST'])
def updateambulanceMaster():
    try:
        inputdata =  commonfile.DecodeInputdata(request.get_data())
        startlimit,endlimit="",""
        keyarr = ['ambulanceType','id']
        commonfile.writeLog("updateambulanceMaster",inputdata,0)
        msg = commonfile.CheckKeyNameBlankValue(keyarr,inputdata)
        if msg=="1":
            ambulanceType = inputdata["ambulanceType"]
            id = inputdata["id"]
            column= " * "
            whereCondition="id = '" + str(id)+ "'"
            data1 = databasefile.SelectQuery("ambulanceMaster",column,whereCondition)
            print(data1,"data1")
            if data1 != 0:
                column = ""
                whereCondition = ""
                column= " ambulanceType='" + str(ambulanceType) + "'"
                whereCondition="id = '" + str(id)+ "'"
                data = databasefile.UpdateQuery("ambulanceMaster",column,whereCondition)
                print(data,'===')
                output = {"result":"Updated Successfully","status":"true"}
                return output
            else:
                output = {"result":"Data Not Found","status":"true"}
                return output
        else:
            return msg 
    except KeyError :
        print("Key Exception---->")   
        output = {"result":"key error","status":"false"}
        return output  
    except Exception as e :
        print("Exception---->" +str(e))    
        output = {"result":"somthing went wrong","status":"false"}
        return output


@app.route('/allusers', methods=['GET'])
def allusers():
    try:
        msg = "1"
        
        if msg =="1":
            column="*"
            whereCondition="usertypeId='2' "
            data=databasefile.SelectQuery1("userMaster",column,whereCondition)
            if (data!=0):           
                Data = {"result":data,"status":"true"}
                return Data
            else:
                output = {"result":"No Data Found","status":"false"}
                return output
        else:
            return msg

    except Exception as e :
        print("Exception---->" + str(e))    
        output = {"result":"something went wrong","status":"false"}
        return output

@app.route('/alldriver', methods=['GET'])
def alldrivers():
    try:
        msg = "1"
        if msg =="1":
            column="*"
            whereCondition="usertypeId='3' "
            data=databasefile.SelectQuery1("userMaster",column,whereCondition)
            if (data!=0):           
                Data = {"result":data,"status":"true"}
                return Data
            else:
                output = {"result":"No Data Found","status":"false"}
                return output
        else:
            return msg
    except Exception as e :
        print("Exception---->" + str(e))    
        output = {"result":"something went wrong","status":"false"}
        return output


@app.route('/addhospital', methods=['POST'])
def addhospital():
    try:
        inputdata =  commonfile.DecodeInputdata(request.get_data())
        startlimit,endlimit="",""
        keyarr = ['hospitalName','address','ambulanceId']
        commonfile.writeLog("addhospital",inputdata,0)
        msg = commonfile.CheckKeyNameBlankValue(keyarr,inputdata)
        if msg=="1":
            hospitalName = inputdata["hospitalName"]
            address = inputdata["address"]
            ambulanceId = inputdata["ambulanceId"]

            column=" * "
            whereCondition= "hospitalName='"+str(hospitalName)+ "'"
            data= databasefile.SelectQuery("hospitalMaster",column,whereCondition)
            print(data,'===data')
            if data==0:
                print('A')
                column="hospitalName,address"
                values="'"+str(hospitalName)+"','"+str(address)+"'"
                insertdata=databasefile.InsertQuery("hospitalMaster",column,values)
                column=" id as hospitalId "
                whereCondition="hospitalName= '"+str(hospitalName)+ "' and  address='"+str(address)+ "'"
                data= databasefile.SelectQuery1("hospitalMaster",column,whereCondition)
                print(data[-1],'data1111')
                yu=data[-1]
                mainId=yu["hospitalId"]
                print(mainId,'mainId')
                ambulanceId1 = ambulanceId
                print(ambulanceId1,'ambulance')
                print('B')
                column=" * "
                whereCondition="ambulance_Id='"+str(ambulanceId1)+"'  and hospital_Id='"+str(mainId)+"'"
                userHospitalMappingdata = databasefile.SelectQuery1("hospitalambulanceMapping",column,whereCondition)
                print(userHospitalMappingdata,'lets see')
                if userHospitalMappingdata==0:
                    print('C')
                    column="hospital_Id,ambulance_Id"
                    values="'"+str(mainId)+"','"+str(ambulanceId1)+"'"
                    insertdata=databasefile.InsertQuery("hospitalambulanceMapping",column,values)                
                    output = {"result":"data inserted successfully","status":"true"}
                    return output
                else:
                    output = {"result":"Data already existed in mapping table","status":"true"}
                    return output
            else:
                output = {"result":"Hospital Already  Existed ","status":"true"}
                return output
        else:
            return msg 
    except Exception as e :
        print("Exception---->" + str(e))    
        output = {"result":"something went wrong","status":"false"}
        return output

@app.route('/addbookingambulance', methods=['POST'])
def addbooking():
    try:
        data1 = json.loads(data.decode("utf-8"))
        pickup=str(data1["pickup"])
        Drop=str(data1["dropoff"])
        search = geocoder.get(pickup)
        search2=geocoder.get(Drop)
        search[0].geometry.location
        search2[0].geometry.location
        fromlatitude= search[0].geometry.location.lat
        fromlongitude=search[0].geometry.location.lng
        tolatitude= search2[0].geometry.location.lat
        tolongitude= search2[0].geometry.location.lng
        bookingId=uuid.uuid1()
        bookingId=bookingId.hex
        R = 6373.0
        fromlongitude2= Decimal(fromlongitude)
        fromlatitude2 = Decimal(fromlatitude)
        # print(fromlongitude2,fromlatitude2)
        distanceLongitude = tolongitude - fromlongitude
        distanceLatitude = tolatitude - fromlatitude
        a = sin(distanceLatitude / 2)**2 + cos(fromlatitude) * cos(tolatitude) * sin(distanceLongitude / 2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        distance = R * c
        distance2=distance/100
        Distance=distance2*1.85
        d=round(Distance)
        d2 =str(d) +' Km'

        column=" * "
        whereCondition="userId='"+str(data1["userId"])+ "' and status<>'2'"
        data=databasefile.SelectQuery("bookAmbulance",column,whereCondition)
        if data==None:
            column="driverId,currentLocationlatlong,mobile"
            whereCondition="verificationStatus<>'F'"
            datavv= databasefile.SelectQuery1("driverMaster",column,whereCondition)
            for da in datavv:
                da.split(",")
                driverlattitude=int(da[0])
                driverlongitude=int(da[2])
                distanceLongitude = tolongitude - driverlongitude
                distanceLatitude = tolatitude - driverlattitude
                a = sin(distanceLatitude / 2)**2 + cos(driverlattitude) * cos(tolatitude) * sin(driverlongitude/ 2)**2
                c = 2 * atan2(sqrt(a), sqrt(1 - a))
                distanceDriver = R * c
                distance1=distanceDriver/100
                distanceD=distance2*1.85
                d1=round(distanceD)
                d9 =str(d) +' Km'
                if d1 <2:
                    driverId=da['driverId']
                    driverMobile=da['mobile']
           
            column="usermobile,pickup,pickupLongitudeLatitude,dropoff,dropoffLongitudeLatitude,selectBookingDate,bookingType,patientMedicalCondition,ambulanceId,userId,bookingId,finalAmount,totalDistance"
            values="'"+str(data1["mobile"])+"','"+str(data1["pickup"])+"','"+str(fromlatitude,fromlongitude)+"','"+str(data1["dropoff"])+"','"+str(tolatitude,tolongitude)+"','"+str(data1["selectBookingDate"])+"','"+str(data1["patientMedicalCondition"])+"','"+str(data1["userId"])+"','"+str(bookingId)+"','"+str(data1["finalAmount"])+"','"+str(d3)+"'"
            insertdata=databasefile.InsertQuery("bookAmbulance",column,values)
            column=" * "
            whereCondition="userId='"+str(data1["userId"])+ "' and status<>'2'"
            data=databasefile.SelectQuery1("bookAmbulance",column,whereCondition)
            yu=data[-1]
            mainId=yu["bookingId"]
            pickuplocation=yu["pickup"]
            userid=yu["userId"]
            column="bookingId,driverId,farDistance,pickup,userId"
            values="'"+str(mainId)+"','"+str(driverId)+"','"+str(d9)+"','"+str(pickuplocation)+"','"+str(userid)+"'"
            insertdata=databasefile.InsertQuery("driverBookingMapping",column,values)
            ambulanceId = data1["addsOnId"]
            for i in ambulanceId:
                column=" * "
                whereCondition="addsOnId='"+str(i)+"'  and bookingId='"+str(mainId)+"'"
                userHospitalMappingdata=databasefile.SelectQuery1("addsOnbookambulanceMapping",column,whereCondition)
                if userHospitalMappingdata==():
                    column="addsOnId,bookingId"
                    values="'"+str(mainId)+"','"+str(i)+"'"
                    insertdata=databasefile.InsertQuery("addsOnbookambulanceMapping",column,values)
            output = {"result":"data inserted successfully","status":"true","ride Details":data[-1]}
            return output
           
        else:
            output = {"result":"Hospital Already  Existed ","status":"false"}
            return output 
    except Exception as e :
        print("Exception---->" + str(e))    
        output = {"result":"something went wrong","status":"false"}
        return output


#track Ambulance
@app.route('/trackAmbulance', methods=['POST'])
def trackAmbulance():
    try:
        inputdata =  commonfile.DecodeInputdata(request.get_data())
        startlimit,endlimit="",""
        keyarr = ['bookingId']
        commonfile.writeLog("trackAmbulance",inputdata,0)
        msg = commonfile.CheckKeyNameBlankValue(keyarr,inputdata)
        if msg=="1":
            bookingId = inputdata["bookingId"]       
            column="dm.name,dm.mobile,dbm.farDistance,dm.currentLocation"
            whereCondition="dbm.driverId=dm.driverId and dbm.bookingId='" + str(bookingId) + "'"
            data=databasefile.SelectQuery1("driverMaster as dm ,driverBookingMapping as dbm",column,whereCondition)
            print(data,'==data')
            if (data!=0):           
                Data = {"result":data,"status":"true"}
                return Data
            else:
                output = {"result":"No Data Found","status":"false"}
                return output

    except Exception as e :
        print("Exception---->" + str(e))    
        output = {"result":"something went wrong","status":"false"}
        return output
        


@app.route('/addRiderBooking', methods=['POST'])
def addRiderBooking():
    try:
        data1 = commonfile.DecodeInputdata(request.get_data())
        pickup=str(data1["pickup"])
        search = geocoder.get(pickup)
        search[0].geometry.location
        fromlatitude= search[0].geometry.location.lat
        fromlongitude=search[0].geometry.location.lng
        
        bookingId=uuid.uuid1()
        bookingId=bookingId.hex
        R = 6373.0
        column=" * "
        whereCondition="userId='"+str(data1["userId"])+ "' and status<>'2'"
        data=databasefile.SelectQuery("responderBooking",column,whereCondition)
        if data==None:
            column="responderId,currentLocationlatlong,mobile"
            whereCondition="verificationStatus<>'F'"
            datavv=databasefile.SelectQuery1("responderMaster",column,whereCondition)
            for da in datavv:
                da.split(",")
                driverlattitude=int(da[0])
                driverlongitude=int(da[2])
                distanceLongitude = driverlongitude-fromlongitude
                distanceLatitude = driverlattitude-fromlattitude
                a = sin(distanceLatitude / 2)**2 + cos(driverlattitude) * cos(fromlatitude) * sin(driverlongitude/ 2)**2
                c = 2 * atan2(sqrt(a), sqrt(1 - a))
                distanceDriver = R * c
                distance1=distanceDriver/100
                distanceD=distance2*1.85
                d1=round(distanceD)
                d9 =str(d) +' Km'
                if d1 <2:
                    riderId=da['responderId']
                    driverMobile=da['mobile']
           
            column="usermobile,pickup,pickupLongitudeLatitude,selectBookingDate,bookingType,patientMedicalCondition,ambulanceId,userId,bookingId,finalAmount,totalDistance"
            values="'"+str(data1["mobile"])+"','"+str(data1["pickup"])+"','"+str(fromlatitude,fromlongitude)+"','"+str(data1["selectBookingDate"])+"','"+str(data1["patientMedicalCondition"])+"','"+str(data1["userId"])+"','"+str(bookingId)+"','"+str(data1["finalAmount"])+"','"+str(d9)+"'"
            insertdata=databasefile.InsertQuery("responderBooking",column,values)
            column=" * "
            whereCondition="userId='"+str(data1["userId"])+ "' and status<>'2'"
            data=databasefile.SelectQuery1("responderBooking",column,whereCondition)
            yu=data[-1]
            mainId=yu["bookingId"]
            pickuplocation=yu["pickup"]
            userid=yu["userId"]
            column="bookingId,responderId,farDistance,pickup,userId"
            values="'"+str(mainId)+"','"+str(riderId)+"','"+str(d9)+"','"+str(pickuplocation)+"','"+str(userid)+"'"
            insertdata=databasefile.InsertQuery("responderBookingMapping",column,values)              
            output = {"result":"data inserted successfully","status":"true","ride Details":data[-1]}
            return output
           
        else:
            output = {"result":"Hospital Already  Existed ","status":"false"}
            return output 
    except Exception as e :
        print("Exception---->" + str(e))    
        output = {"result":"something went wrong","status":"false"}
        return output






@app.route('/allresponder', methods=['GET'])
def alldresponder():
    try:
        msg="1"
        if msg=="1":
            column="*"
            whereCondition="usertypeId='4' "
            data=databasefile.SelectQuery1("userMaster",column,whereCondition)
            if (data!=0):           
                Data = {"result":data,"status":"true"}
                return Data
            else:
                output = {"result":"No Data Found","status":"false"}
                return output
        else:
            return msg

    except Exception as e :
        print("Exception---->" + str(e))    
        output = {"result":"something went wrong","status":"false"}
        return output 


@app.route('/responderMode', methods=['GET'])
def responderMode():
    try:
        msg="1"
        if msg=="1":
            column="id ,responderType"
            whereCondition=""
            data=databasefile.SelectQuery1("responderMode",column,whereCondition)
            if (data!=0):           
                Data = {"result":data,"status":"true"}
                return Data
            else:
                output = {"result":"No Data Found","status":"false"}
                return output
        else:
            return msg

    except Exception as e :
        print("Exception---->" + str(e))    
        output = {"result":"something went wrong","status":"false"}
        return output


#update riderMode(g,p,h)

@app.route('/updateresponderMode', methods=['POST'])
def updateresponderMode():
    try:
        inputdata =  commonfile.DecodeInputdata(request.get_data())
        startlimit,endlimit="",""
        keyarr = ['responderType','id']
        commonfile.writeLog("updateresponderMode",inputdata,0)
        msg = commonfile.CheckKeyNameBlankValue(keyarr,inputdata)
        if msg=="1":
            responderType = inputdata["responderType"]
            id = inputdata["id"]
            column= " * "
            whereCondition="id = '" + str(id)+ "'"
            data1 = databasefile.SelectQuery("responderMode",column,whereCondition)
            print(data1,"data1")
            if data1 != 0:
                column = ""
                whereCondition = ""
                column= " responderType='" + str(responderType) + "'"
                whereCondition="id = '" + str(id)+ "'"
                data = databasefile.UpdateQuery("responderMode",column,whereCondition)
                print(data,'===')
                output = {"result":"Updated Successfully","status":"true"}
                return output
            else:
                output = {"result":"Data Not Found","status":"true"}
                return output
        else:
            return msg 
    except KeyError :
        print("Key Exception---->")   
        output = {"result":"key error","status":"false"}
        return output  

    except Exception as e :
        print("Exception---->" +str(e))    
        output = {"result":"somthing went wrong","status":"false"}
        return output


#(rider(ALs,BLS,PVT,DBT,AIR))

@app.route('/addriderType', methods=['POST'])
def addriderType():
    try:
        inputdata =  commonfile.DecodeInputdata(request.get_data())
        startlimit,endlimit="",""
        keyarr = ['responderType']
        commonfile.writeLog("addriderType",inputdata,0)
        msg = commonfile.CheckKeyNameBlankValue(keyarr,inputdata)
        if msg=="1":
            responderType = inputdata["responderType"]
            column="*"
            whereCondition="responderType='"+str(responderType)+"'"
            data= databasefile.SelectQuery("responderTypeMaster",column,whereCondition)
            print(data,'printit')
            if data==0:
                column="responderType"
                values="'"+str(responderType)+"'"
                insertdata=databasefile.InsertQuery("responderTypeMaster",column,values)
                column="*"
                whereCondition="responderType='"+str(responderType)+"'"
                data1= databasefile.SelectQuery1("responderTypeMaster",column,whereCondition)
                print(data1,'data1')
                output= {"result":"User Added Successfully","responder Details":data1,"status":"true"}
                return output
            else:
                return msg
        else:
            output = {"result":"User Already Added Existed ","status":"true","ambulance Details":data}
            return output 
    except Exception as e :
        print("Exception---->" + str(e))    
        output = {"result":"something went wrong","status":"false"}
        return output
 
#(select  rider)
@app.route('/responderType', methods=['GET'])
def responderType():
    try:
        msg="1"
        if msg=="1":
            column="id ,responderType"
            whereCondition=""
            data=databasefile.SelectQuery1("responderTypeMaster",column,whereCondition)
            if (data!=0):           
                Data = {"result":data,"status":"true"}
                return Data
            else:
                output = {"result":"No Data Found","status":"false"}
                return output
        else:
                return msg

    except Exception as e :
        print("Exception---->" + str(e))    
        output = {"result":"something went wrong","status":"false"}
        return output



#update rider
@app.route('/updateriderType', methods=['POST'])
def updateriderType():
    try:
        inputdata =  commonfile.DecodeInputdata(request.get_data())
        startlimit,endlimit="",""
        keyarr = ['responderType','id']
        commonfile.writeLog("updateriderType",inputdata,0)
        msg = commonfile.CheckKeyNameBlankValue(keyarr,inputdata)
        if msg=="1":
            responderType = inputdata["responderType"]
            id = inputdata["id"]
            column= " * "
            whereCondition="id = '" + str(id)+ "'"
            data1 = databasefile.SelectQuery("responderTypeMaster",column,whereCondition)
            print(data1,"data1")
            if data1 != 0:
                column = ""
                whereCondition = ""
                column= " responderType='" + str(responderType) + "'"
                whereCondition="id = '" + str(id)+ "'"
                data = databasefile.UpdateQuery("responderTypeMaster",column,whereCondition)
                print(data,'===')
                output = {"result":"Updated Successfully","status":"true"}
                return output
            else:
                output = {"result":"Data Not Found","status":"true"}
                return output
        else:
            return msg 
    except KeyError :
        print("Key Exception---->")   
        output = {"result":"key error","status":"false"}
        return output  

    except Exception as e :
        print("Exception---->" +str(e))    
        output = {"result":"somthing went wrong","status":"false"}
        return output

#addOns
@app.route('/addOns', methods=['POST'])
def addOns():
    try:
        inputdata =  commonfile.DecodeInputdata(request.get_data())
        startlimit,endlimit="",""
        keyarr = ['name']
        commonfile.writeLog("addOns",inputdata,0)
        msg = commonfile.CheckKeyNameBlankValue(keyarr,inputdata)
        if msg=="1":
            name = inputdata["name"]
            column="name"
            whereCondition= " name='"+str(name)+ "'"
            data=databasefile.SelectQuery("addOns",column,whereCondition)
            print(data,'A')
            if data==0:
                print('B')
                column="name"
                values="'"+str(name)+"' "
                insertdata=databasefile.InsertQuery("addOns",column,values)
                column="*"
                whereCondition= " name='"+str(name)+ "'"
                data1=databasefile.SelectQuery1("addOns",column,whereCondition)
                print(data1,'C')
                output= {"result":"User Added Successfully","addons Details":data1,"status":"true"}
                return output 
            else:
                output = {"result":"User Already Added Existed ","status":"true","ambulance Details":data}
                return output 
        else:
            return msg
    except Exception as e :
        print("Exception---->" + str(e))    
        output = {"result":"something went wrong","status":"false"}
        return output

#select addOns
@app.route('/addOnsSelect', methods=['GET'])
def addsOn():
    try:
        msg="1"
        if msg=="1":
            column="id ,name"
            whereCondition=""
            data=databasefile.SelectQuery1("addOns",column,whereCondition)
            if (data!=0):           
                Data = {"result":data,"status":"true"}
                return Data
            else:
                output = {"result":"No Data Found","status":"false"}
                return output
        else:
            return msg

    except Exception as e :
        print("Exception---->" + str(e))    
        output = {"result":"something went wrong","status":"false"}
        return output



@app.route('/updateaddOns', methods=['POST'])
def updateaddOns():
    try:
        inputdata =  commonfile.DecodeInputdata(request.get_data())
        startlimit,endlimit="",""
        keyarr = ['name','id']
        commonfile.writeLog("updateaddOns",inputdata,0)
        msg = commonfile.CheckKeyNameBlankValue(keyarr,inputdata)
        if msg=="1":
            name = inputdata["name"]
            id = inputdata["id"]
            column= " * "
            whereCondition="id = '" + str(id)+ "'"
            data1 = databasefile.SelectQuery("addOns",column,whereCondition)
            print(data1,"data1")
            if data1 != 0:
                column = ""
                whereCondition = ""
                column= " name='" + str(name) + "'"
                whereCondition="id = '" + str(id)+ "'"
                data = databasefile.UpdateQuery("addOns",column,whereCondition)
                print(data,'===')
                output = {"result":"Updated Successfully","status":"true"}
                return output
            else:
                output = {"result":"Data Not Found","status":"true"}
                return output
        else:
            return msg 
    except KeyError :
        print("Key Exception---->")   
        output = {"result":"key error","status":"false"}
        return output  

    except Exception as e :
        print("Exception---->" +str(e))    
        output = {"result":"somthing went wrong","status":"false"}
        return output



#finalPayment

@app.route('/finalPayment', methods=['POST'])
def finalPayment():
    try:
        # inputdata =  commonfile.DecodeInputdata(request.get_data())
        # startlimit,endlimit="",""
        # keyarr = ['userId','paymentmodeId','totalAmount']
        # commonfile.writeLog("finalPayment",inputdata,0)
        # msg = commonfile.CheckKeyNameBlankValue(keyarr,inputdata)
        # if msg=="1":
        #     userId = inputdata["userId"]
        #     paymentmodeId = inputdata["paymentmodeId"]
        #     totalAmount = inputdata["totalAmount"]
        #     column="userId,paymentTypeId,totalAmount"
        #     values=  " '"+str(userId)+"','"+str(paymentmodeId)+"','"+str(totalAmount)+ "'"
        #     insertdata=databasefile.InsertQuery("finalPayment",column,values)
        #     column=""
        #     column=" * "
        #     WhereCondition= "userId='"+str(userId)+ "' "
        #     data2=databasefile.SelectQuery1("finalPayment",column,values)
        #     if data2 == 0:
        #         output = {"result":"Payment Unsuccessfull","status":"false"}
        #         return output
        #     else:
        #         output= {"result":"Payment Successfull","patient Details":data2,"status":"true"}
        #         return output   
        # else:
        #     return msg
    except Exception as e :
        print("Exception---->" + str(e))    
        output = {"result":"something went wrong","status":"false"}
        return output   



@app.route('/updatepaymentType', methods=['POST'])
def updatepaymentType():
    try:
        data=commonfile.DecodeInputdata(request.get_data())  
        column= " paymentType='" + str(data["paymentType"]) + "'"
        whereCondition= "id = '" + str(data["id"])+ "'"
        databasefile.UpdateQuery("paymentTypeMaster",column,whereCondition)
       

        output = {"result":"Updated Successfully","status":"true"}
        return output  
    except KeyError :
        print("Key Exception---->")   
        output = {"result":"key error","status":"false"}
        return output  

    except Exception as e :
        print("Exception---->" +str(e))    
        output = {"result":"somthing went wrong","status":"false"}
        return output

@app.route('/paymentTypeMaster', methods=['GET'])
def paymentTypeMaster():
    try:
        column="id ,paymentType"
        whereCondition=""
        data=databasefile.SelectQuery1("paymentTypeMaster",column,whereCondition)
       
        if (data!=0):           
            Data = {"result":data,"status":"true"}
            return Data
        else:
            output = {"result":"No Data Found","status":"false"}
            return output

    except Exception as e :
        print("Exception---->" + str(e))    
        output = {"result":"something went wrong","status":"false"}
        return output


@app.route('/addpaymentType', methods=['POST'])
def addpaymentType():
    try:
        data1=commonfile.DecodeInputdata(request.get_data())  
        column="*"
        whereCondition= "paymentType='"+str(data1["paymentType"])+ "'"
        data=databasefile.SelectQuery("paymentTypeMaster",column,whereCondition)
        if data==None:
            column="paymentType"
            values="('"+str(data1["paymentType"])+"' "
            insertdata=databasefile.InsertQuery("paymentTypeMaster",column,values)
            column="*"
            whereCondition= " paymentType='"+str(data1["paymentType"])+ "'"
            data1=databasefile.SelectQuery1("paymentTypeMaster",column,whereCondition)

            output= {"result":"User Added Successfully","ambulance Details":data1[-1],"status":"true"}
            return output


               
            
        else:
            output = {"result":"User Already Added Existed ","status":"true","ambulance Details":data}
            return output 
    except Exception as e :
        print("Exception---->" + str(e))    
        output = {"result":"something went wrong","status":"false"}
        return output




@app.route('/allHospital', methods=['GET'])
def allHospital():
    try:
        ambulanceType=""

        if 'ambulanceType' in request.args:
            ambulanceType=request.args["ambulanceType"]

        column= "hosp.id,hosp.hospitalName,hosp.address,am.ambulanceType "   

        WhereCondition=  " hosp.id=ahm.hospital_Id and am.id=ahm.ambulance_Id and  ambulanceType   = '" + ambulanceType + "'  "
        data=databasefile.SelectQuery1("hospitalMaster as hosp,hospitalambulanceMapping as ahm,ambulanceMaster as am",column,WhereCondition)
        print(data)
        
        
        
        if (data!=0): 
            print(data)          
            Data = {"result":data,"status":"true"}
            return Data
        else:
            print("ssssssssssss")
            output = {"result":"No Data Found","status":"false"}
            return output

    except Exception as e :
        print("Exception---->" + str(e))    
        output = {"result":"something went wrong","status":"false"}
        return output

@app.route('/updateDriverMasterlocation', methods=['POST'])
def updateDriverMasterlocation():
    try:
        data=commonfile.DecodeInputdata(request.get_data())  
        column= " currentLocation ='" + str(data["currentLocation"]) + "',currentLocationlatlong='" + str(data["currentLocationlatlong"]) + "' "
        whereCondition= "driverId = '" + str(data["driverId"])+ "' and ambulanceId='" + str(data["ambulanceId"]) + "'"
        databasefile.UpdateQuery("driverMaster",column,whereCondition)
        output = {"result":"Updated Successfully","status":"true"}
        return output  
    except KeyError :
        print("Key Exception---->")   
        output = {"result":"key error","status":"false"}
        return output  

    except Exception as e :
        print("Exception---->" +str(e))    
        output = {"result":"somthing went wrong","status":"false"}
        return output 
@app.route('/DriverTraceUser', methods=['POST'])
def DriverTraceUser():
    try:
        data=commonfile.DecodeInputdata(request.get_data())  
        column="um.name,um.mobile,dbm.farDistance,dbm.pickup,dbm.bookingId "
        whereCondition=" dbm.userId=dm.userId and dbm.driverId='" + str(data["driverId"]) + "'"
        data=databasefile.SelectQuery(" driverBookingMapping as dbm,userMaster as  um")
        if (data!=0):           
            Data = {"result":data,"status":"true"}
            return Data
        else:
            output = {"result":"No Data Found","status":"false"}
            return output

    except Exception as e :
        print("Exception---->" + str(e))    
        output = {"result":"something went wrong","status":"false"}
        return output


@app.route('/ResponderTraceUser', methods=['GET'])
def ResponderTraceUser():
    try:
        data=commonfile.DecodeInputdata(request.get_data())  
        column="um.name,um.mobile,dbm.farDistance,dbm.pickup,dbm.bookingId "
        whereCondition="dbm.userId=dm.userId and dbm.responderId='" + str(data["responderId"]) + "'"
        data=databasefile.SelectQuery1("responderbookingMapping as dbm,userMaster as  um",column,whereCondition)
        if (data!=0):           
            Data = {"result":data,"status":"true"}
            return Data
        else:
            output = {"result":"No Data Found","status":"false"}
            return output

    except Exception as e :
        print("Exception---->" + str(e))    
        output = {"result":"something went wrong","status":"false"}
        return output 


@app.route('/trackResponder', methods=['GET'])
def trackRider():
    try:
        
        data=commonfile.DecodeInputdata(request.get_data())
        column="dm.name,dm.mobile,dbm.farDistance,dm.currentLocation"
        whereCondition= "dbm.responderId=dm.responderId and dbm.bookingId='" + str(data["bookingId"]) + "'"
        data=databasefile.SelectQuery1(" responderMaster as dm ,responderBookingMapping as dbm",column,whereCondition)
        
        query = "select dm.name,dm.mobile,dbm.farDistance,dm.currentLocation from responderMaster as dm ,responderBookingMapping as dbm where dbm.responderId=dm.responderId and dbm.bookingId='" + str(data["bookingId"]) + "'"
        conn=Connection()
        cursor = conn.cursor()
        cursor.execute(query)
        data = cursor.fetchone()
        if (data!=0):           
            Data = {"result":data,"status":"true"}
            return Data
        else:
            output = {"result":"No Data Found","status":"false"}
            return output

    except Exception as e :
        print("Exception---->" + str(e))    
        output = {"result":"something went wrong","status":"false"}
        return output
















if __name__ == "__main__":
    CORS(app, support_credentials=True)
    app.run(host='0.0.0.0',port=5077,debug=True)
    socketio.run(app)        
