from flask import Flask,request,abort
from flask_socketio import SocketIO,emit
import uuid
import json
#import socketio
from googlegeocoder import GoogleGeocoder
from math import sin,cos,sqrt,atan2,radians
from decimal import Decimal
import json
import numpy as np
import pymysql
import requests
import math, random
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
import ConstantData

from flask import Flask, render_template
from flask_socketio import SocketIO
import pyotp
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

geocoder = GoogleGeocoder("AIzaSyB0Pz6VjrQmWPCCbDbWDuyjo79GhDJPOlI")





# @app.route('/addUser', methods=['POST'])
# def addUser():
#     try:
#         inputdata =  commonfile.DecodeInputdata(request.get_data()) 
#         startlimit,endlimit="",""
#         keyarr = ['name','mobileNo','userTypeId','email','password']
#         commonfile.writeLog("addUser",inputdata,0)
#         msg = commonfile.CheckKeyNameBlankValue(keyarr,inputdata)
       
#         if msg == "1":
#             imeiNo,country,city,deviceName,deviceId,deviceType="","","","","",""
#             os,appVersion,notificationToken,ipAddress,userAgent="","","","",""
#             currentLocation,currentLocation="",""
            
#             Name = inputdata["name"]
#             userTypeId = inputdata["userTypeId"]
#             mobileNo=inputdata["mobileNo"]
#             Email = inputdata["email"]
#             password = inputdata["password"]
#             # currentLocation=inputdata["currentLocation"]
#             # currentLocationlatlong=inputdata["currentLocationlatlong"]

            
           

           

#             UserId = commonfile.CreateHashKey(mobileNo,Name)
            
#             WhereCondition = " and mobileNo = '" + str(mobileNo) + "' and password = '" + str(password) + "'"
#             count = databasefile.SelectCountQuery("userMaster",WhereCondition,"")
            
#             if int(count) > 0:
#                 return commonfile.EmailMobileAlreadyExistMsg()
#             else:
#                 if 'imeiNo' in inputdata:
#                     imeiNo=inputdata["imeiNo"] 

#                 if 'deviceName' in inputdata:
#                     deviceName=inputdata["deviceName"]

#                 if 'country' in inputdata:
#                     country=inputdata["country"]

#                 if 'city' in inputdata:
#                     city=inputdata["city"]

#                 if 'ipAddress' in inputdata:
#                     ipAddress=inputdata["ipAddress"]

#                 if 'userAgent' in inputdata:
#                     userAgent=inputdata["userAgent"]


#                 if 'deviceId' in inputdata:
#                     deviceId=inputdata["deviceId"]

                
#                 if 'os' in inputdata:
#                     os=inputdata["os"]

                
#                 if 'deviceType' in inputdata:
#                     deviceType=inputdata["deviceType"]

#                 if 'appVersion' in inputdata:
#                     appVersion=inputdata["appVersion"] 


#                 if 'notificationToken' in inputdata:
#                     notificationToken=inputdata["notificationToken"]



 
#                 currentLocationlatlong=""

#                 column="name,password,mobileNo,userId,imeiNo,deviceName,currentLocation,currentLocationlatlong,usertypeId,email,country,city, "
#                 column=column+ "ipAddress,userAgent,deviceId,os,deviceType,appVersion,notificationToken"

#                 values =  "'"+str(Name)+"','"+str(password)+"','"
#                 values= values +str(mobileNo)+"','"+str(UserId)+"','"+str(imeiNo)+"','"+str(deviceName)+"','"
#                 values= values+str(currentLocation)+"','"+str(currentLocationlatlong)+"','"+str(userTypeId)+"','"
#                 values= values+str(Email)+"','"+str(country)+"','"+str(city)+"','"
#                 values= values+str(ipAddress)+"','"+str(userAgent)+"','"+str(deviceId)+"','"
#                 values= values+str(os)+"','"+str(deviceType)+"','"+str(appVersion)+ "','"+str(notificationToken)+ "'"
#                 data=databasefile.InsertQuery("userMaster",column,values)
             

#                 if data != "0":
#                     column = '*'
                    
#                     data = databasefile.SelectQuery2("userMaster",column,WhereCondition,"",startlimit,endlimit)
#                     print(data)
#                     Data = {"status":"true","message":"","result":data["result"]}                  
#                     return Data
#                 else:
#                     return commonfile.Errormessage()
                        
#         else:
#             return msg 
#     except Exception as e :
#         print("Exception---->" +str(e))           
#         output = {"status":"false","message":"something went wrong","result":""}
#         return output

@app.route('/userSignup', methods=['POST'])
def userSignup():
    try:
        inputdata =  commonfile.DecodeInputdata(request.get_data()) 
        startlimit,endlimit="",""
        keyarr = ['mobileNo','userTypeId']
        commonfile.writeLog("userSignup",inputdata,0)
        msg = commonfile.CheckKeyNameBlankValue(keyarr,inputdata)
       
        if msg == "1":
            imeiNo,country,city,deviceName,deviceId,deviceType="","","","","",""
            os,appVersion,notificationToken,ipAddress,userAgent="","","","",""
            currentLocation,currentLocation="",""
            column,values="",""
            
           
            userTypeId = inputdata["userTypeId"]
            mobileNo=inputdata["mobileNo"]
            
            # currentLocation=inputdata["currentLocation"]
            # currentLocationlatlong=inputdata["currentLocationlatlong"]

            
            digits = "0123456789"
            otp = ""
            for i in range(4):
                otp += digits[math.floor(random.random() * 10)]

            
            # totp = pyotp.TOTP('base32secret3232')
            # print("Current OTP:", totp.now()[0:4])
            # otp=int(totp.now()[0:4])

            UserId = (commonfile.CreateHashKey(mobileNo,userTypeId)).hex
            
            
            WhereCondition = " and mobileNo = '" + str(mobileNo) + "'"
            count = databasefile.SelectCountQuery("userMaster",WhereCondition,"")
            
            if int(count) > 0:
                WhereCondition = " mobileNo = '" + str(mobileNo) + "'"
                column = " otp = '" + str(otp)  + "'"
                updateOtp = databasefile.UpdateQuery("userMaster",column,WhereCondition)
                print(updateOtp,'updatedata')
                if updateOtp != "0":
                    column = '*'
                    data = databasefile.SelectQuery("userMaster",column,WhereCondition)                  
                    return data
                else:
                    return commonfile.Errormessage()
                
            else:
                if 'imeiNo' in inputdata:
                    imeiNo=inputdata["imeiNo"] 
                    column=column+",imeiNo "
                    values=values+"','"+str(deviceName)

                if 'deviceName' in inputdata:
                    deviceName=inputdata["deviceName"]
                    column=column+" ,deviceName "
                    values=values+"','"+str(deviceName)
                
                if 'country' in inputdata:
                    country=inputdata["country"]
                    column=column+" ,country "
                    values=values+"','"+str(deviceName)
                
                if 'city' in inputdata:
                    city=inputdata["city"]
                    column=column+" ,city"
                    values=values+"','"+str(deviceName)

                if 'ipAddress' in inputdata:
                    ipAddress=inputdata["ipAddress"]
                    column=column+" ,ipAddress"
                    values=values+"','"+str(deviceName)

                if 'userAgent' in inputdata:
                    userAgent=inputdata["userAgent"]
                    column=column+" ,userAgent"
                    values=values+"','"+str(deviceName)


                if 'deviceId' in inputdata:
                    deviceId=inputdata["deviceId"]
                    column=column+" ,deviceId"
                    values=values+"','"+str(deviceName)

                
                if 'os' in inputdata:
                    os=inputdata["os"]
                    column=column+" ,os"
                    values=values+"','"+str(deviceName)

                
                if 'deviceType' in inputdata:
                    deviceType=inputdata["deviceType"]
                    column=column+" ,deviceType"
                    values=values+"','"+str(deviceName)

                if 'appVersion' in inputdata:
                    appVersion=inputdata["appVersion"] 
                    column=column+" ,appVersion"
                    values=values+"','"+str(deviceName)


                if 'notificationToken' in inputdata:
                    notificationToken=inputdata["notificationToken"]
                    column=column+" ,appVersion"
                    values=values+"','"+str(deviceName)

                if 'email' in inputdata:
                    email=inputdata["email"]
                    column=column+" ,email"
                    values=values+"','"+str(email)
                if 'password' in inputdata:
                    password=inputdata["password"]
                    column=column+" ,password"
                    values=values+"','"+str(password)


 
                currentLocationlatlong=""

                column="mobileNo,userId,userTypeId,otp"+column
                
                
                values=  "'"+str(mobileNo)+"','"+str(UserId)+"','"+str(userTypeId)+"','"+str(otp)+values+ "'"
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


@app.route('/verifyOtp', methods=['POST'])
def verifyOtp():
    try:
        inputdata =  commonfile.DecodeInputdata(request.get_data())
        startlimit,endlimit="",""
        keyarr = ['otp','mobileNo']
        print(inputdata,"B")
        commonfile.writeLog("verifyOtp",inputdata,0)
        msg = commonfile.CheckKeyNameBlankValue(keyarr,inputdata)
        if msg =="1":
            otp=str(inputdata['otp'])
            mobileNo=str(inputdata['mobileNo'])

            column="mobileNo,otp"
            whereCondition= "  otp='" + otp+ "' and mobileNo='" + mobileNo+"'"
            verifyOtp=databasefile.SelectQuery(" userMaster ",column,whereCondition)
            print("verifyOtp======",verifyOtp)
            if  (verifyOtp["status"]!="false") or verifyOtp!=None: 
                return verifyOtp
            else:
                return verifyOtp 
        else:
            return msg         
 
    except KeyError :
        print("Key Exception---->")   
        output = {"result":"key error","status":"false"}
        return output  

    except Exception as e :
        print("Exceptio`121QWAaUJIHUJG n---->" +str(e))    
        output = {"result":"somthing went wrong","status":"false"}
        return output  


@app.route('/addDriver', methods=['POST'])
def addDriver():
    try:
        print('Hello')
        inputdata=request.form.get('data')
        print(inputdata,'inputdata')
        keyarr = ['name','mobileNo','key','flag']
        inputdata=json.loads(inputdata)
        # inputdata =  commonfile.DecodeInputdata(request.get_data()) 
        startlimit,endlimit="",""

        commonfile.writeLog("addDriver",inputdata,0)
        msg = commonfile.CheckKeyNameBlankValue(keyarr,inputdata)
        print(msg,'msg')
       
        if msg == "1":
            mobileNo=inputdata['mobileNo']
           
            key = inputdata["key"]
            flag = inputdata["flag"]
            column = " * "
            whereCondition= " and mobileNo='"+str(mobileNo)+ "' and usertypeId='3'"
            data= databasefile.SelectQuery("userMaster",column,whereCondition)
            print(data,'data')

            name= data["name"]
            mobileNo= data["mobileNo"]
            driverId=data['userId']
            
            DlNo,dlFrontFilename,DlFrontPicPath,dlBackFilename,DlBackPicPath,PIDType,PIDNo,PIDFrontFilename,PIDFrontPicPath,PIDBackFilename,PIDBackPicPath,TransportType,TransportModel,Color,AmbulanceRegistrationFuel,TypeNo,AIFilename,AIPicPath,AmbulanceModeId,AmbulanceId="","","","","","","","","","","","","","","","","","","",""

            if 'DlNo' in inputdata:
                DlNo=inputdata["DlNo"]

            if 'DlFrontImage' in request.files:
                    print("immmmmmmmmmmmmmmmm")
                    file = request.files.get('DlFrontImage')        
                    filename = file.filename or ''  
                    print(filename)               
                    dlFrontFilename= str(str(data["userId"])+"Front"+".png")
                    
                    print(dlFrontFilename,'Changed_filename')
                    DlFrontFolderPath = ConstantData.GetdlImagePath(dlFrontFilename)
                    DlFrontfilepath = '/DLImage/' + dlFrontFilename 
                    file.save(DlFrontFolderPath)
                    DlFrontPicPath = DlFrontfilepath
                    print(DlFrontPicPath)
                    

            if 'DlBackImage' in request.files:
                    print("immmmmmmmmmmmmmmmm")
                    file = request.files.get('DlBackImage')        
                    filename = file.filename or ''  
                    print(filename)               
                    dlBackFilename=  str(str(data["userId"])+"Back"+".png")
                  
                    DlBackFolderPath = ConstantData.GetdlImagePath(dlBackFilename)
                    DlBackfilepath = '/DLImage/' + dlBackFilename 
                    file.save(DlBackFolderPath)
                    DlBackPicPath = DlBackfilepath
                    print(DlBackPicPath)

            if 'PIDType' in inputdata:
                PIDType=inputdata["PIDType"]

            if 'PIDNo' in inputdata:
                PIDNo=inputdata["PIDNo"]

            if 'PIDFrontImage' in request.files:
                    print("immmmmmmmmmmmmmmmm")
                    file = request.files.get('PIDFrontImage')        
                    filename = file.filename or ''  
                    print(filename)               
                    PIDFrontFilename= str(str(data["userId"])+"Front"+".png")
                  
                    print(PIDFrontFilename,'Changed_filename')
                    PIDFrontFolderPath = ConstantData.GetPIDImagePath(PIDFrontFilename)
                    PIDFrontfilepath = '/PIDImage/' + PIDFrontFilename 
                    file.save(DlFrontFolderPath)
                    PIDFrontPicPath = PIDFrontfilepath
                    print(PIDFrontPicPath)
                    

            if 'PIDBackImage' in request.files:
                    print("immmmmmmmmmmmmmmmm")
                    file = request.files.get('PIDBackImage')        
                    filename = file.filename or ''  
                    print(filename)               
                    PIDBackFilename= str(str(data["userId"])+"Back"+".png")
                  
                    PIDBackFolderPath = ConstantData.GetPIDImagePath(PIDBackFilename)
                    PIDBackfilepath = '/PIDImage/' + PIDBackFilename 
                    file.save(PIDBackFolderPath)
                    PIDBackPicPath = PIDBackfilepath
                    print(PIDBackPicPath)

            if 'TransportType' in inputdata:
                TransportType=inputdata["TransportType"]
            
            if 'TransportModel' in inputdata:
                TransportModel=inputdata["TransportModel"]

            if 'Color' in inputdata:
                Color=inputdata["Color"]

            if 'AmbulanceRegistrationFuel' in inputdata:
                AmbulanceRegistrationFuel=inputdata["AmbulanceRegistrationFuel"]
            
            if 'TypeNo' in inputdata:
                TypeNo=inputdata["TypeNo"]

            if 'AmbulanceModeId' in inputdata:
                AmbulanceModeId=inputdata["AmbulanceModeId"]

            if 'AmbulanceNo' in inputdata:
                AmbulanceNo=inputdata["AmbulanceNo"]

            if 'AmbulanceTypeId' in inputdata:
                AmbulanceId=inputdata["AmbulanceTypeId"]

            if 'lat' in inputdata:
                lat=inputdata["lat"]

            if 'lng' in inputdata:
                lng=inputdata["lng"]


            if 'AmbulanceImage' in request.files:
                    print("immmmmmmmmmmmmmmmm")
                    file = request.files.get('AmbulanceImage')        
                    filename = file.filename or ''  
                    print(filename)               
                    AIFilename=  str(str(data["userId"])+".png")
                   
                    AIFolderPath = ConstantData.GetAmbulanceImagePath(AIFilename)
                    AIfilepath = '/AmbulanceImage/' + AIFilename 
                    file.save(AIFolderPath)
                    AIPicPath = AIfilepath
                    print(AIPicPath)

            if data !=0:
                
                if flag == 'i':
                    if key == "A":
                        columns = " name,mobileNo,dlNo,dlFrontFilename,dlFrontFilepath,dlBackFilename,dlBackFilepath,driverId"          
                        values = " '" + str(name) + "','" + str(mobileNo) + "','" + str(DlNo) + "','" + str( dlFrontFilename) + "','" + str(DlFrontPicPath) + "','" + str(dlBackFilename) + "', "            
                        values = values + " '" + str(DlBackPicPath) + "','" + str(driverId) + "'"
                        data = databasefile.InsertQuery("driverMaster",columns,values)
                        if data != "0":
                            column = '*'
                            WhereCondition = " mobileNo = '" + str(mobileNo) +  "'"
                            
                            data11 = databasefile.SelectQuery("driverMaster",column,WhereCondition)
                            return data11
                    if key == "B":
                        columns = " name,mobileNo,pIDType,pIDNo,pIDFrontFilename,pIDFrontFilepath,pIDBackFilename,pIDBackFilepath,driverId"          
                        values = " '" + str(name) + "','" + str(mobileNo) + "','" + str(PIDType) + "','" + str(PIDNo) + "','" + str(PIDFrontFilename) + "','" + str(PIDFrontPicPath) + "','" + str(PIDBackFilename) + "', "            
                        values = values + " '" + str(PIDBackPicPath)+ "','" + str(driverId) + "'"
                        data = databasefile.InsertQuery("driverMaster",columns,values)
                        if data != "0":
                            column = '*'
                            WhereCondition = " mobileNo = '" + str(mobileNo) +  "'"
                            
                            data11 = databasefile.SelectQuery("driverMaster",column,WhereCondition)
                            return data11
                    
                    if key == "C":

                        columns = " name,mobileNo,driverId"          
                        values = " '" + str(name) + "','" + str(mobileNo) + "','" + str(driverId) + "'"
                        
                        data = databasefile.InsertQuery("driverMaster",columns,values)
                        columns2= "ambulanceNo,transportType,transportModel,color,ambulanceRegistrationFuel,typeNo,ambulanceFilename,ambulanceFilepath,ambulanceModeId,ambulanceTypeId,driverId"
                        values2="'" + str(AmbulanceId) + "','" + str(TransportModel) + "','" + str(Color) + "','" + str(AmbulanceRegistrationFuel) + "','" + str(TypeNo) + "','" + str(AIFilename) + "','" + str(AIPicPath) + "','" + str(AmbulanceModeId) + "', "            
                        values2 = values2 + " '" + str(AmbulanceId) + "','" + str(driverId) + "'"
                        data=databasefile.InsertQuery("ambulanceMaster",columns2,values2)
                        if data != "0":
                            column = '*'
                            WhereCondition = " mobileNo = '" + str(mobileNo) +  "'"
                            whereCondition="   driverId='" + str(driverId) +  "' "
                            columns22="ambulanceId,transportType,transportModel,color,ambulanceRegistrationFuel,typeNo,ambulanceFilename,ambulanceFilepath,ambulanceModeId,ambulanceId"
                            
                            data11 = databasefile.SelectQuery("driverMaster",column,WhereCondition)
                            data12=databasefile.SelectQuery("ambulanceMaster",column22,whereCondition)
                            ambulanceId=data12['ambulanceId']
                            columns23='ambulanceId,lat,lng'
                            values23 = " '" + str(ambulanceId) + "','" + str(lat) + "','" + str(lng) + "'"
                            data122=databasefile.InsertQuery('ambulanceRideStatus',columns23,values23)
                            whereCondition222= " ambulanceId=  '" + str(ambulanceId) +  "' "
                            columns239="lat,lng,onDuty,onTrip"
                            data12333=databasefile.SelectQuery('ambulanceRideStatus',columns239,whereCondition222)



                            data11.update(data12)
                            data11.update(data12333)

                            return data11
                
                
                if flag == 'u':
                    if key == "A":
                        print('A')
                        WhereCondition = " mobileNo = '" + str(mobileNo) + "'"
                        column = " dlNo = '" + str(DlNo) + "',dlFrontFilename = '" + str(dlFrontFilename) + "',dlFrontFilepath = '" + str(DlFrontPicPath) + "',dlBackFilename = '" + str(dlBackFilename) + "',dlBackFilepath = '" + str(DlBackPicPath) + "'"
                        print(column,'column')
                        data = databasefile.UpdateQuery("driverMaster",column,WhereCondition)
                        print(data,'updatedata')
                        return data
                    if key == "B":
                        print('B')
                        WhereCondition = " mobileNo = '" + str(mobileNo) + "'"
                        column = " pIDType = '" + str(PIDType) + "',pIDNo = '" + str(PIDNo) + "',pIDFrontFilename = '" + str(PIDFrontFilename) + "',pIDFrontFilepath = '" + str(PIDFrontPicPath) + "',pIDBackFilename = '" + str(PIDBackFilename) + "',pIDBackFilepath = '" + str(PIDBackPicPath) + "'"
                        print(column,'column')
                        data = databasefile.UpdateQuery("driverMaster",column,WhereCondition)
                        print(data,'updatedata')
                        return data
                    if key == "C":
                        print('C')

                        # WhereCondition = " driverId = '" + str(driverId) + "'"
                        # column = " transportType = '" + str(TransportType) + "',transportModel = '" + str(TransportModel) + "',color = '" + str(Color) + "',ambulanceRegistrationFuel = '" + str(AmbulanceRegistrationFuel) + "',typeNo = '" + str(TypeNo) + "',ambulanceFilename = '" + str(AIFilename) + "',ambulanceFilepath = '" + str(AIPicPath) + "',ambulanceModeId = '" + str(AmbulanceModeId) + "',ambulanceTypeId = '" + str(AmbulanceId) + "'"
                        # print(column,'column')
                        # data = databasefile.UpdateQuery("ambulanceMaster",column,WhereCondition)
                        # return data
                else:
                    return commonfile.Errormessage()
        else:
            return msg
    except Exception as e :
        print("Exception---->" + str(e))    
        output = {"result":"something went wrong","status":"false"}
        return output



#user Login
@app.route('/Login', methods=['POST'])
def login():
    try:
        inputdata =  commonfile.DecodeInputdata(request.get_data())
        startlimit,endlimit="",""
        keyarr = ['password','mobileNo']
        commonfile.writeLog("Login",inputdata,0)
        msg = commonfile.CheckKeyNameBlankValue(keyarr,inputdata)
        if msg == "1":
            mobileNo = inputdata["mobileNo"]
            password = inputdata["password"]
            column=  "us.mobileNo,us.name,um.usertype,us.userId"
            whereCondition= "us.mobileNo = '" + str(mobileNo) + "' and us.password = '" + password + "'  and  us.usertypeId=um.Id"
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
            print(data,'==data===')
            if data['status'] == 'false':
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
            data= databasefile.SelectQuery("ambulanceTypeMaster",column,whereCondition)
            print(data,"==data")
            if data==0:
                column="ambulanceType"
                values="'"+str(ambulanceType)+"'"
                insertdata=databasefile.InsertQuery("ambulanceTypeMaster",column,values)
                column="*"
                whereCondition="ambulanceType='"+str(ambulanceType)+"'"
                data1= databasefile.SelectQuery1("ambulanceTypeMaster",column,whereCondition)
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
 

@app.route('/selectambulanceTypeMaster', methods=['GET'])
def ambulanceTypeMaster():
    try:
        msg = "1"
        if msg=="1":
            column="id ,ambulanceType"
            whereCondition=""
            data=databasefile.SelectQuery1("ambulanceTypeMaster",column,whereCondition)
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



@app.route('/allAmbulance', methods=['POST'])
def allAmbulance():
    try:
        msg = "1"
        if msg=="1":
            startlimit,endlimit="",""

            inputdata =  commonfile.DecodeInputdata(request.get_data())  
            if "startlimit" in inputdata:
                if inputdata['startlimit'] != "":
                    startlimit =str(inputdata["startlimit"])
                
            if "endlimit" in inputdata:
                if inputdata['endlimit'] != "":
                    endlimit =str(inputdata["endlimit"])

            column=" AM.ambulanceId,AM.lat,AM.lng,atm.ambulanceType,am.ambulanceType as category,AM.transportType,AM.transportModel,AM.color,AM.ambulanceRegistrationFuel as fueltype,AM.typeNo,AM.ambulanceFilename,AM.ambulanceFilepath,AM.ambulanceModeId,AM.ambulanceTypeId "
           
            whereCondition=" and  AM.ambulanceTypeId=atm.id and AM.ambulanceModeId=am.id"
            data=databasefile.SelectQuery2("ambulanceMaster as AM, ambulanceTypeMaster  as atm,ambulanceMode as am",column,whereCondition,"",startlimit,endlimit)
            print(data)
            if (data['status']!='false'):           
                Data = {"result":data['result'],'message':"","status":"true"}
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


@app.route('/updateambulanceTypeMaster', methods=['POST'])
def updateambulanceTypeMaster():
    try:
        inputdata =  commonfile.DecodeInputdata(request.get_data())
        startlimit,endlimit="",""
        keyarr = ['ambulanceType','id']
        commonfile.writeLog("updateambulanceTypeMaster",inputdata,0)
        msg = commonfile.CheckKeyNameBlankValue(keyarr,inputdata)
        if msg=="1":
            ambulanceType = inputdata["ambulanceType"]
            id = inputdata["id"]
            column= " * "
            whereCondition="id = '" + str(id)+ "'"
            data1 = databasefile.SelectQuery("ambulanceTypeMaster",column,whereCondition)
            print(data1,"data1")
            if data1 != 0:
                column = ""
                whereCondition = ""
                column= " ambulanceType='" + str(ambulanceType) + "'"
                whereCondition="id = '" + str(id)+ "'"
                data = databasefile.UpdateQuery("ambulanceTypeMaster",column,whereCondition)
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
        print('A')
        inputdata =  commonfile.DecodeInputdata(request.get_data())
        startlimit,endlimit="",""
        keyarr = ['hospitalName','address','ambulanceId','latitude','longitude']
        commonfile.writeLog("addhospital",inputdata,0)
        msg = commonfile.CheckKeyNameBlankValue(keyarr,inputdata)
        if msg=="1":
            hospitalName = inputdata["hospitalName"]
            address = inputdata["address"]
            ambulanceId = inputdata["ambulanceId"]
            
            latitude=inputdata['latitude']

            longitude=inputdata['longitude']

            column=" * "
            whereCondition= "hospitalName='"+str(hospitalName)+ "'"
            data= databasefile.SelectQuery("hospitalMaster",column,whereCondition)

            print(data['status'],'===data')

            if data['status'] =='false':
                
                print('AA')
                column="hospitalName,address,latitude,longitude"
                values="'"+str(hospitalName)+"','"+str(address)+"','"+str(latitude)+"','"+str(longitude)+"'"
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
                print('BB')
                column=" * "
                whereCondition="ambulance_Id='"+str(ambulanceId1)+"'  and hospital_Id='"+str(mainId)+"'"
                userHospitalMappingdata = databasefile.SelectQuery1("hospitalambulanceMapping",column,whereCondition)
                print(userHospitalMappingdata,'lets see')
                if userHospitalMappingdata==0:
                    print('CC')
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

# @app.route('/addbookingambulance', methods=['POST'])
# def addbooking():
#     try:
#         print('Entered')
#         inputdata =  commonfile.DecodeInputdata(request.get_data())
#         startlimit,endlimit="",""
#         keyarr = ['pickup','drop','userId','mobileNo','selectBookingDate','ambulanceId']
#         commonfile.writeLog("addbookingambulance",inputdata,0)
#         msg = commonfile.CheckKeyNameBlankValue(keyarr,inputdata)
#         if msg=="1":
#             pickup = inputdata["pickup"]
#             drop = inputdata["drop"]
#             userId = inputdata["userId"]
#             mobileNo = inputdata["mobileNo"]
#             selectBookingDate = inputdata["selectBookingDate"]
#             ambulanceId = inputdata["ambulanceId"]
#             #bookingId =  commonfile.CreateHashKey(mobileNo,pickup)

#             search = geocoder.get(pickup)
#             print(search,'searchpickup')
#             search2=geocoder.get(drop)
#             print(search2,'searchdrop')
#             search[0].geometry.location
#             search2[0].geometry.location
#             fromlatitude= search[0].geometry.location.lat
#             print(fromlatitude,'fromlat')
#             fromlongitude=search[0].geometry.location.lng
#             print(fromlongitude,'fromlng')
#             tolatitude= search2[0].geometry.location.lat
#             print(tolatitude,'tolat')
#             tolongitude= search2[0].geometry.location.lng
#             print(tolongitude,'tolng')
#             bookingId=uuid.uuid1()
#             bookingId=bookingId.hex
#             R = 6373.0
#             fromlongitude2= Decimal(fromlongitude)
#             print(fromlongitude2,'fromlng2')
#             fromlatitude2 = Decimal(fromlatitude)
#             print(fromlatitude2,'fromlat')
#             # print(fromlongitude2,fromlatitude2)
#             distanceLongitude = tolongitude - fromlongitude
#             print(distanceLongitude,'distancelng')
#             distanceLatitude = tolatitude - fromlatitude
#             print(distanceLongitude,'distancelat')
#             a = sin(distanceLatitude / 2)**2 + cos(fromlatitude) * cos(tolatitude) * sin(distanceLongitude / 2)**2
#             c = 2 * atan2(sqrt(a), sqrt(1 - a))
#             distance = R * c
#             distance2=distance/100
#             Distance=distance2*1.85
#             print(Distance,'distance')
#             d=round(Distance)
#             print(d,'d')
#             d2 =str(d) +' Km'
#             print(d2,'d2')

           
#             column="id,mobileNo"
#             whereCondition="verificationStatus<>'F'"
#             datavv= databasefile.SelectQuery1("driverMaster",column,whereCondition)
#             print(datavv,'data')
#             for da in datavv:
#                 print('A',da)
#                 da.split(",")
#                 driverlattitude=int(da[0])
#                 driverlongitude=int(da[2])
#                 distanceLongitude = tolongitude - driverlongitude
#                 distanceLatitude = tolatitude - driverlattitude
#                 a = sin(distanceLatitude / 2)**2 + cos(driverlattitude) * cos(tolatitude) * sin(driverlongitude/ 2)**2
#                 c = 2 * atan2(sqrt(a), sqrt(1 - a))
#                 distanceDriver = R * c
#                 distance1=distanceDriver/100
#                 distanceD=distance2*1.85
#                 d1=round(distanceD)
#                 d9 =str(d) +' Km'
#                 if d1 <2:
#                     print('B')
#                     driverId=da['driverId']
#                     driverMobile=da['mobileNo']
        
#                 column="usermobile,pickup,pickupLongitudeLatitude,dropoff,dropoffLongitudeLatitude,selectBookingDate,bookingType,patientMedicalCondition,ambulanceId,userId,bookingId,finalAmount,totalDistance"
#                 values="'"+str(data1["mobileNo"])+"','"+str(data1["pickup"])+"','"+str(fromlatitude,fromlongitude)+"','"+str(data1["dropoff"])+"','"+str(tolatitude,tolongitude)+"','"+str(data1["selectBookingDate"])+"','"+str(data1["patientMedicalCondition"])+"','"+str(data1["userId"])+"','"+str(bookingId)+"','"+str(data1["finalAmount"])+"','"+str(d3)+"'"
#                 insertdata=databasefile.InsertQuery("bookAmbulance",column,values)
#                 column=" * "
#                 whereCondition="userId='"+str(data1["userId"])+ "' and status<>'2'"
#                 data=databasefile.SelectQuery1("bookAmbulance",column,whereCondition)
#                 yu=data[-1]
#                 mainId=yu["bookingId"]
#                 pickuplocation=yu["pickup"]
#                 userid=yu["userId"]
#                 column="bookingId,driverId,farDistance,pickup,userId"
#                 values="'"+str(mainId)+"','"+str(driverId)+"','"+str(d9)+"','"+str(pickuplocation)+"','"+str(userid)+"'"
#                 insertdata=databasefile.InsertQuery("driverBookingMapping",column,values)
#                 ambulanceId = data1["addsOnId"]
#                 for i in ambulanceId:
#                     column=" * "
#                     whereCondition="addsOnId='"+str(i)+"'  and bookingId='"+str(mainId)+"'"
#                     userHospitalMappingdata=databasefile.SelectQuery1("addsOnbookambulanceMapping",column,whereCondition)
#                     if userHospitalMappingdata==():
#                         column="addsOnId,bookingId"
#                         values="'"+str(mainId)+"','"+str(i)+"'"
#                         insertdata=databasefile.InsertQuery("addsOnbookambulanceMapping",column,values)
#                         output = {"result":"data inserted successfully","status":"true","ride Details":data[-1]}
#                         return output
            
#                     else:
#                         output = {"result":"Hospital Already  Existed ","status":"false"}
#                         return output 
#         else:
#             return msg
#     except Exception as e :
#         print("Exception---->" + str(e))    
#         output = {"result":"something went wrong","status":"false"}
#         return output

# #changed
# @app.route('/addbookingambulance', methods=['POST'])
# def addbooking():
#     try:
#         print('Entered')
#         inputdata =  commonfile.DecodeInputdata(request.get_data())
#         startlimit,endlimit="",""
#         #keyarr = ['pickup','drop','userId','mobileNo','selectBookingDate','ambulanceId','driverlocation']
#         keyarr = ['pickup','drop','userId','mobileNo','ambulanceId']
#         commonfile.writeLog("addbookingambulance",inputdata,0)
#         msg = commonfile.CheckKeyNameBlankValue(keyarr,inputdata)
#         if msg=="1":
#             pickup = inputdata["pickup"]
#             drop = inputdata["drop"]
#             userId = inputdata["userId"]
#             mobileNo = inputdata["mobileNo"]
#             ##selectBookingDate = inputdata["selectBookingDate"]
#             ambulanceId = inputdata["ambulanceId"]
#             ###driverlocation = inputdata["driverlocation"]
#             #bookingId =  commonfile.CreateHashKey(mobileNo,pickup)

#             search = geocoder.get(pickup)
#             print(search,'searchpickup')
#             search2=geocoder.get(drop)
#             print(search2,'searchdrop')
            
#             # search3 = geocoder.get(driverlocation)
#             # search3[0].geometry.location
#             # driverlattitude= search3[0].geometry.location.lat
#             # print(driverlattitude,'driverfromlat')
#             # driverlongitude=search3[0].geometry.location.lng
#             # print(driverlongitude,'driverfromlng')

#             search[0].geometry.location
#             search2[0].geometry.location
#             fromlatitude= search[0].geometry.location.lat
#             print(fromlatitude,'fromlat')
#             fromlongitude=search[0].geometry.location.lng
#             print(fromlongitude,'fromlng')
#             tolatitude= search2[0].geometry.location.lat
#             print(tolatitude,'tolat')
#             tolongitude= search2[0].geometry.location.lng
#             print(tolongitude,'tolng')
#             bookingId=uuid.uuid1()
#             bookingId=bookingId.hex
#             print(bookingId,'bookingId')
#             R = 6373.0
#             fromlongitude2= Decimal(fromlongitude)
#             print(fromlongitude2,'fromlng2')
#             fromlatitude2 = Decimal(fromlatitude)
#             print(fromlatitude2,'fromlat')
#             # print(fromlongitude2,fromlatitude2)
#             distanceLongitude = tolongitude - fromlongitude
#             print(distanceLongitude,'distancelng')
#             distanceLatitude = tolatitude - fromlatitude
#             print(distanceLongitude,'distancelat')
#             a = sin(distanceLatitude / 2)**2 + cos(fromlatitude) * cos(tolatitude) * sin(distanceLongitude / 2)**2
#             c = 2 * atan2(sqrt(a), sqrt(1 - a))
#             distance = R * c
#             distance2=distance/100
#             Distance=distance2*1.85
#             print(Distance,'distance')
#             d=round(Distance)
#             print(d,'d')
#             d2 =str(d) +' Km'
#             print(d2,'d2')

           
#             column="id,mobileNo,currentlatlong,currentLocation"
#             whereCondition="drivingStatus<>'1'"
#             datavv= databasefile.SelectQuery1("driverMaster",column,whereCondition)
#             print(datavv,'data')
#             distanceLongitude = fromlongitude - driverlongitude
#             distanceLatitude = fromlatitude - driverlattitude
#             a = sin(distanceLatitude / 2)**2 + cos(driverlattitude) * cos(tolatitude) * sin(driverlongitude/ 2)**2
#             c = 2 * atan2(sqrt(a), sqrt(1 - a))
#             distanceDriver = R * c
#             distance1=distanceDriver/100
#             distanceD=distance2*1.85
#             d1=round(distanceD)
#             print(d1,'d1')
#             d9 =str(d) +' Km'
#             print(d9,'d9')
#             if d1 <2:
#                 print('B')
#                 driverId=datavv['id']
#                 driverMobile=datavv['mobileNo']
        
#             column="usermobile,pickup,pickupLongitudeLatitude,dropoff,dropoffLongitudeLatitude,selectBookingDate,bookingType,patientMedicalCondition,ambulanceId,userId,bookingId,finalAmount,totalDistance"
#             values="'"+str(data1["mobileNo"])+"','"+str(data1["pickup"])+"','"+str(fromlatitude,fromlongitude)+"','"+str(data1["dropoff"])+"','"+str(tolatitude,tolongitude)+"','"+str(data1["selectBookingDate"])+"','"+str(data1["patientMedicalCondition"])+"','"+str(data1["userId"])+"','"+str(bookingId)+"','"+str(data1["finalAmount"])+"','"+str(d3)+"'"
#             insertdata=databasefile.InsertQuery("bookAmbulance",column,values)
#             column=" * "
#             whereCondition="userId='"+str(data1["userId"])+ "' and status<>'2'"
#             data=databasefile.SelectQuery1("bookAmbulance",column,whereCondition)
#             yu=data[-1]
#             mainId=yu["bookingId"]
#             pickuplocation=yu["pickup"]
#             userid=yu["userId"]
#             column="bookingId,driverId,farDistance,pickup,userId"
#             values="'"+str(mainId)+"','"+str(driverId)+"','"+str(d9)+"','"+str(pickuplocation)+"','"+str(userid)+"'"
#             insertdata=databasefile.InsertQuery("driverBookingMapping",column,values)
#             ambulanceId = data1["addsOnId"]
#             for i in ambulanceId:
#                 column=" * "
#                 whereCondition="addsOnId='"+str(i)+"'  and bookingId='"+str(mainId)+"'"
#                 userHospitalMappingdata=databasefile.SelectQuery1("addsOnbookambulanceMapping",column,whereCondition)
#                 if userHospitalMappingdata==():
#                     column="addsOnId,bookingId"
#                     values="'"+str(mainId)+"','"+str(i)+"'"
#                     insertdata=databasefile.InsertQuery("addsOnbookambulanceMapping",column,values)
#                     output = {"result":"data inserted successfully","status":"true","ride Details":data[-1]}
#                     return output
        
#                 else:
#                     output = {"result":"Hospital Already  Existed ","status":"false"}
#                     return output 
#         else:
#             return msg
#     except Exception as e :
#         print("Exception---->" + str(e))    
#         output = {"result":"something went wrong","status":"false"}
#         return output


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
            column="dm.name,dm.mobileNo,dbm.farDistance,dm.currentLocation"
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
            column="responderId,currentLocationlatlong,mobileNo,currentLocation"
            whereCondition="drivingStatus<>'1'"
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
                    driverMobile=da['mobileNo']
           
            column="usermobile,pickup,pickupLongitudeLatitude,userId,bookingId,finalAmount,totalDistance"
            values="'"+str(data1["mobileNo"])+"','"+str(data1["pickup"])+"','"+str(fromlatitude,fromlongitude)+"','"+str(data1["userId"])+"','"+str(bookingId)+"','"+str(data1["finalAmount"])+"','"+str(d9)+"'"
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
            print(data,'data')
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
            if data['status']=='false':
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
        print('A')
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
            if data1['status'] == 'false':
                print('b')
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
        inputdata =  commonfile.DecodeInputdata(request.get_data())
        startlimit,endlimit="",""
        keyarr = ['userId','paymentmodeId','totalAmount']
        commonfile.writeLog("finalPayment",inputdata,0)
        msg = commonfile.CheckKeyNameBlankValue(keyarr,inputdata)
        if msg=="1":
            userId = inputdata["userId"]
            paymentmodeId = inputdata["paymentmodeId"]
            totalAmount = inputdata["totalAmount"]
            column="userId,paymentTypeId,totalAmount"
            values=  "'"+str(userId)+"','"+str(paymentmodeId)+"','"+str(totalAmount)+ "'"
            insertdata=databasefile.InsertQuery("finalPayment",column,values)
            column=" "
            WhereCondition=" "
            column=" * "
            WhereCondition= "userId='"+str(userId)+ "' "
            data2=databasefile.SelectQuery1("finalPayment",column,WhereCondition)
            if data2 == 0:
                output = {"result":"Payment Unsuccessfull","status":"false"}
                return output
            else:
                output= {"result":"Payment Successfull","patient Details":data2,"status":"true"}
                return output   
        else:
            return msg
    except Exception as e :
        print("Exception---->" + str(e))    
        output = {"result":"something went wrong","status":"false"}
        return output   



@app.route('/updatepaymentType', methods=['POST'])
def updatepaymentType():
    try:
        inputdata =  commonfile.DecodeInputdata(request.get_data())
        startlimit,endlimit="",""
        keyarr = ['paymentType','id']
        commonfile.writeLog("updatepaymentType",inputdata,0)
        msg = commonfile.CheckKeyNameBlankValue(keyarr,inputdata)
        if msg=="1":
            paymentType = inputdata["paymentType"]
            id = inputdata["id"]
            column= " * "
            whereCondition="id = '" + str(id)+ "'"
            data1 = databasefile.SelectQuery("paymentTypeMaster",column,whereCondition)
            print(data1,"data1")
            if data1 != 0:
                column = ""
                whereCondition = ""
                column= " paymentType='" + str(paymentType) + "'"
                whereCondition="id = '" + str(id)+ "'"
                data = databasefile.UpdateQuery("paymentTypeMaster",column,whereCondition)
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

@app.route('/paymentTypeMaster', methods=['GET'])
def paymentTypeMaster():
    try:
        msg = "1"
        if msg=="1":
            column="id ,paymentType"
            whereCondition=""
            data=databasefile.SelectQuery1("paymentTypeMaster",column,whereCondition)
        
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


@app.route('/addpaymentType', methods=['POST'])
def addpaymentType():
    try:
        inputdata =  commonfile.DecodeInputdata(request.get_data())
        startlimit,endlimit="",""
        keyarr = ['paymentType']
        commonfile.writeLog("addpaymentType",inputdata,0)
        msg = commonfile.CheckKeyNameBlankValue(keyarr,inputdata)
        if msg=="1":
            paymentType = inputdata["paymentType"]
            column="*"
            whereCondition= "paymentType='"+str(paymentType)+ "'"
            data=databasefile.SelectQuery("paymentTypeMaster",column,whereCondition)
            print(data,'data')
            if data['status']=='false':
                column="paymentType"
                values="'"+str(paymentType)+"' "
                insertdata=databasefile.InsertQuery("paymentTypeMaster",column,values)
                column="*"
                whereCondition= " paymentType='"+str(paymentType)+ "'"
                data1=databasefile.SelectQuery1("paymentTypeMaster",column,whereCondition)

                output= {"result":"User Added Successfully","ambulance Details":data1,"status":"true"}
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




@app.route('/allHospital', methods=['POST'])
def allHospital():
    try:
        msg="1"
        if msg=="1":
            ambulanceType=""
            if 'ambulanceType' in request.args:
                ambulanceType=request.args["ambulanceType"]
            column= "hosp.id,hosp.hospitalName,hosp.address,am.ambulanceType,hosp.longitude,hosp.latitude"   
            WhereCondition=  " hosp.id=ahm.hospital_Id and am.id=ahm.ambulance_Id and  ambulanceType   = '" + ambulanceType + "'  "
            data=databasefile.SelectQuery1("hospitalMaster as hosp,hospitalambulanceMapping as ahm,ambulanceTypeMaster as am",column,WhereCondition)
            print(data)
            if (data!=0): 
                print(data)          
                Data = {"result":data,"status":"true"}
                return Data
            else:
                print("ssssssssssss")
                output = {"result":"No Data Found","status":"false"}
                return output
        else:
            return msg

    except Exception as e :
        print("Exception---->" + str(e))    
        output = {"result":"something went wrong","status":"false"}
        return output

@app.route('/updateDriverMasterlocation', methods=['POST'])
def updateDriverMasterlocation():
    try:
        inputdata =  commonfile.DecodeInputdata(request.get_data())
        startlimit,endlimit="",""
        keyarr = ['currentLocation','currentLocationlatlong','driverId','ambulanceId']
        commonfile.writeLog("updateDriverMasterlocation",inputdata,0)
        msg = commonfile.CheckKeyNameBlankValue(keyarr,inputdata)
        if msg=="1":
            currentLocation = inputdata["currentLocation"]
            currentLocationlatlong = inputdata["currentLocationlatlong"]
            driverId = inputdata["driverId"]
            ambulanceId = inputdata["ambulanceId"]
            column= " * "
            whereCondition="driverId = '" + str(driverId)+ "' and ambulanceId='" + str(ambulanceId) + "'"
            data1 = databasefile.SelectQuery("driverMaster",column,whereCondition)
            print(data1,"data1")
            if data1 != 0:
                column = ""
                whereCondition = ""
                column= " currentLocation ='" + str(currentLocation) + "',currentlatlong ='" + str(currentLocationlatlong) + "' "
                whereCondition= "driverId = '" + str(driverId)+ "' and ambulanceId='" + str(ambulanceId) + "'"
                databasefile.UpdateQuery("driverMaster",column,whereCondition)
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
@app.route('/DriverTraceUser', methods=['POST'])
def DriverTraceUser():
    try:
        inputdata =  commonfile.DecodeInputdata(request.get_data())
        startlimit,endlimit="",""
        keyarr = ['driverId']
        commonfile.writeLog("updateDriverMasterlocation",inputdata,0)
        msg = commonfile.CheckKeyNameBlankValue(keyarr,inputdata)
        if msg=="1":
            driverId = inputdata["driverId"]
            column="um.name,um.mobileNo,dbm.farDistance,dbm.pickup,dbm.bookingId "
            whereCondition=" dbm.userId=um.userId and dbm.driverId='" + str(driverId) + "'"
            data=databasefile.SelectQuery(" driverBookingMapping as dbm,userMaster as  um",column,whereCondition)
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


@app.route('/ResponderTraceUser', methods=['POST'])
def ResponderTraceUser():
    try:
        inputdata =  commonfile.DecodeInputdata(request.get_data())
        startlimit,endlimit="",""
        keyarr = ['responderId']
        commonfile.writeLog("ResponderTraceUser",inputdata,0)
        msg = commonfile.CheckKeyNameBlankValue(keyarr,inputdata)
        if msg=="1":
            responderId = inputdata["responderId"]
            column="um.name,um.mobileNo,dbm.farDistance,dbm.pickup,dbm.bookingId "
            whereCondition="dbm.userId=um.userId and dbm.responderId='" + str(responderId) + "'"
            data=databasefile.SelectQuery1("responderBookingMapping as dbm,userMaster as  um",column,whereCondition)
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


@app.route('/trackResponder', methods=['POST'])
def trackRider():
    try:
        inputdata =  commonfile.DecodeInputdata(request.get_data())
        startlimit,endlimit="",""
        keyarr = ['bookingId']
        commonfile.writeLog("trackResponder",inputdata,0)
        msg = commonfile.CheckKeyNameBlankValue(keyarr,inputdata)
        if msg=="1":
            bookingId = inputdata["bookingId"]
            column="dm.name,dm.mobileNo,dbm.farDistance,dm.currentLocation"
            whereCondition= "dbm.responderId=dm.responderId and dbm.bookingId='" + str(bookingId) + "'"
            data=databasefile.SelectQuery(" responderMaster as dm ,responderBookingMapping as dbm",column,whereCondition)
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



@app.route('/getNearAmbulance', methods=['POST'])
def getNearAmbulance():
    try:
        inputdata =  commonfile.DecodeInputdata(request.get_data())
        startlimit,endlimit="",""
        keyarr = ['startLocationLat','startLocationLong']
        commonfile.writeLog("getNearAmbulance",inputdata,0)
        msg = commonfile.CheckKeyNameBlankValue(keyarr,inputdata)
        if msg == "1":
            startlat ,startlng,userId= inputdata["startLocationLat"],inputdata["startLocationLong"],""#,inputdata["userId"]
            column=  " d.name, d.mobileNo, a.ambulanceId, a.ambulanceNo, a.lat, a.lng,SQRT(POW(69.1 * (a.lat - "+str(startlat)+"), 2) +POW(69.1 * ("+str(startlng)+" - a.lng) * COS(a.lat / 57.3), 2)) AS distance "
            whereCondition= " and a.onTrip=0 and a.onDuty=1 and a.driverId=d.id HAVING distance > 25 "
            orderby="  distance "
            nearByAmbulance=databasefile.SelectQueryOrderbyAsc("ambulanceMaster a, driverMaster d",column,whereCondition,"",orderby,"","")
            
            if (nearByAmbulance!=0):   
                               
                return nearByAmbulance
            else:
                nearByAmbulance["message"]="No Ambulance Found"
                return nearByAmbulance
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





@app.route('/getNearAmbulance1', methods=['POST'])
def getNearAmbulance1():
    try:
        inputdata =  commonfile.DecodeInputdata(request.get_data())
        startlimit,endlimit="",""
        keyarr = ['startLocationLat','startLocationLong',"pickupLocationAddress",'dropLocationLat','dropLocationLong',"dropLocationAddress",]
        commonfile.writeLog("getNearAmbulance",inputdata,0)
        msg = commonfile.CheckKeyNameBlankValue(keyarr,inputdata)
        if msg == "1":
            startlat ,startlng,userId= inputdata["startLocationLat"],inputdata["startLocationLong"],""#,inputdata["userId"]
            column=  " d.name, d.mobileNo, a.ambulanceId, a.ambulanceNo, a.lat, a.lng,SQRT(POW(69.1 * (a.lat - "+str(startlat)+"), 2) +POW(69.1 * ("+str(startlng)+" - a.lng) * COS(a.lat / 57.3), 2)) AS distance "
            whereCondition= " and a.onTrip=0 and a.onDuty=1 and a.driverId=d.id HAVING distance < 1200 "
            orderby="  distance "
            nearByAmbulance=databasefile.SelectQueryOrderbyAsc("ambulanceMaster a, driverMaster d",column,whereCondition,"",orderby,"","")
            
            if (nearByAmbulance!=0):   
                               
                return nearByAmbulance
            else:
                
                return nearByAmbulance
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


@app.route('/bookRide', methods=['POST'])
def bookRide():
    try:
        inputdata =  commonfile.DecodeInputdata(request.get_data())
        startlimit,endlimit="",""
        #id is driverid
        keyarr = ["ambulanceId","id",'startLocationLat','startLocationLong',"pickupLocationAddress",'dropLocationLat','dropLocationLong',"dropLocationAddress","userId"]
        

        if "ambulanceId" in inputdata:
                if inputdata['ambulanceId'] != "":
                    ambulanceId =str(inputdata["ambulanceId"])
        if "id" in inputdata:
                if inputdata['id'] != "":
                    driverId =str(inputdata["id"])
        if "startLocationLat" in inputdata:
                if inputdata['startLocationLat'] != "":
                    startLocationLat =str(inputdata["startLocationLat"])
        if "startLocationLong" in inputdata:
                if inputdata['startLocationLong'] != "":
                    startLocationLong =str(inputdata["startLocationLong"])
        if "pickupLocationAddress" in inputdata:
                if inputdata['pickupLocationAddress'] != "":
                    pickupLocationAddress =str(inputdata["pickupLocationAddress"])
        if "dropLocationLat" in inputdata:
                if inputdata['dropLocationLat'] != "":
                    dropLocationLat =str(inputdata["dropLocationLat"])
        if "dropLocationLong" in inputdata:
                if inputdata['dropLocationLong'] != "":
                    dropLocationLong =str(inputdata["dropLocationLong"])
        if "dropLocationAddress" in inputdata:
                if inputdata['dropLocationAddress'] != "":
                    dropLocationAddress =str(inputdata["dropLocationAddress"])

        if "userId" in inputdata:
            if inputdata['userId'] != "":
                userId =str(inputdata["userId"])


        bookingId = (commonfile.CreateHashKey(driverId,userId)).hex


        commonfile.writeLog("bookRide",inputdata,0)
        msg = commonfile.CheckKeyNameBlankValue(keyarr,inputdata)
        
        if msg == "1":
            columns="mobileNo,name"
            whereCondition22=" and userId= '"+str(userId)+"' and userTypeId='2' "
            data1= databasefile.SelectQuery("userMaster",columns,whereCondition22)
            usermobile=data1['result']['mobileNo']


            whereCondition222=" and userId= '"+str(userId)+"' "
            data11= databasefile.SelectQuery("driverMaster",columns,whereCondition22)
            drivermobile=data11['result']['mobileNo']
            
            R = 6373.0
            fromlongitude2= Decimal(startLocationLong)
            fromlatitude2 = Decimal(startLocationLat)
            # print(fromlongitude2,fromlatitude2)
            distanceLongitude = dropLocationLong - fromlongitude2
            distanceLatitude = dropLocationLat - fromlatitude2
            a = sin(distanceLatitude / 2)**2 + cos(fromlatitude) * cos(dropLocationLat) * sin(distanceLongitude / 2)**2
            c = 2 * atan2(sqrt(a), sqrt(1 - a))
            distance = R * c
            distance2=distance/100
            Distance=distance2*1.85
            d=round(Distance)
            d2 =str(d) +' Km'


            finalAmount= d * 11+11




            #insertdata
            columnqq='userMobile,driverMobile,pickup,pickupLongitude,pickupLongitude,dropoff,dropOffLatitude,dropOffLongitude,ambulanceId,userId,driverId,bookingId,totalDistance,finalAmount'
            values111 = " '"+ str(usermobile) +"','" + str(drivermobile)+"','" + str(pickupLocationAddress)+"','" + str(startLocationLat) +"','" + str(startLocationLong) + "','" + str(dropLocationAddress) + "','" + str(dropLocationLat) + "'"
            values111=values111+"','" + str(dropLocationLong)+"','" + str(ambulanceId)+"','" + str(userId) +"','" + str(driverId) + "','" + str(bookingId)+ "','" + str(d2) + "','" + str(finalAmount)+"'"
            data111=databasefile.InsertQuery('bookAmbulance',columnqq,values111)
          

            if (data111!='0'):   
                bookRide["message"]="ride booked Successfully" 

                data={"result":{"userdata":data1['result'],"driverdata":data11['result']},"status":"true","message":"" }            
                return data
            else:
                data={"result":"","message":"No data Found","status":"false"}
                
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




@app.route('/startRide', methods=['POST'])
def startRide():
    try:
        inputdata =  commonfile.DecodeInputdata(request.get_data())
        startlimit,endlimit="",""
        keyarr = ["ambulanceId","bookingId"]
        commonfile.writeLog("endRide",inputdata,0)
        msg = commonfile.CheckKeyNameBlankValue(keyarr,inputdata)
        if msg == "1":
            ambulanceId= inputdata["ambulanceId"]
            bookingId=inputdata['bookingId']
            whereCondition=" ambulanceId= '"+ str(ambulanceId)+"' and bookingId='"+ str(bookingId)+"'"
            column=" status=1 "
            bookRide=databasefile.UpdateQuery("bookAmbulance",column,whereCondition)
            whereCondition222=  " ambulanceId= '"+ str(ambulanceId)+"' "
            columns= "onTrip=1"
            bookRide1=databasefile.UpdateQuery("ambulanceRideStatus",columns,whereCondition222)
            if (bookRide!=0):   
                bookRide["message"]="ride Ended Successfully"             
                return bookRide
            else:
                
                return bookRide
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

@app.route('/endRide', methods=['POST'])
def endRide():
    try:
        inputdata =  commonfile.DecodeInputdata(request.get_data())
        startlimit,endlimit="",""
        keyarr = ["ambulanceId","bookingId"]
        commonfile.writeLog("endRide",inputdata,0)
        msg = commonfile.CheckKeyNameBlankValue(keyarr,inputdata)
        if msg == "1":
            ambulanceId= inputdata["ambulanceId"]
            bookingId=inputdata['bookingId']
            whereCondition=" ambulanceId= '"+ str(ambulanceId)+"' and bookingId='"+ str(bookingId)+"'"
            column=" status=2 "
            bookRide=databasefile.UpdateQuery("bookAmbulance",column,whereCondition)
            whereCondition222=  " ambulanceId= '"+ str(ambulanceId)+"' "
            columns= "onTrip=0"
            bookRide1=databasefile.UpdateQuery("ambulanceRideStatus",columns,whereCondition222)
            if (bookRide!=0):   
                bookRide["message"]="ride Ended Successfully"             
                return bookRide
            else:
                
                return bookRide
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





@app.route('/cancelRide', methods=['POST'])
def cancelRide():
    try:
        inputdata =  commonfile.DecodeInputdata(request.get_data())
        startlimit,endlimit="",""
        keyarr = ["ambulanceId","bookingId","userId"]
        commonfile.writeLog("cancelRide",inputdata,0)
        msg = commonfile.CheckKeyNameBlankValue(keyarr,inputdata)
        if msg == "1":
            ambulanceId= inputdata["ambulanceId"]
            bookingId=inputdata['bookingId']
            userId=insertdata['userId']
            whereCondition=" ambulanceId= '"+ str(ambulanceId)+"' and bookingId='"+ str(bookingId)+"' and  canceledUserId='"+ str(userId)+"'"
            column=" status=3"
            bookRide=databasefile.UpdateQuery("bookAmbulance",column,whereCondition)
            whereCondition222=  " ambulanceId= '"+ str(ambulanceId)+"' "
            columns= "onTrip=0"
            bookRide1=databasefile.UpdateQuery("ambulanceRideStatus",columns,whereCondition222)
            if (bookRide!=0):   
                bookRide["message"]="ride Canceled Successfully"             
                return bookRide
            else:
                
                return bookRide
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


#driverLeave
@app.route('/driverLeave', methods=['POST'])
def driverLeave():
    try:
        inputdata =  commonfile.DecodeInputdata(request.get_data())
        startlimit,endlimit="",""
        keyarr = ["ambulanceId","driverId"]
        commonfile.writeLog("driverLeave",inputdata,0)
        msg = commonfile.CheckKeyNameBlankValue(keyarr,inputdata)
        if msg == "1":
            ambulanceId= inputdata["ambulanceId"]
           
            driverId=insertdata['driverId']
            whereCondition222=  " ambulanceId= '"+ str(ambulanceId)+"' and driverId='"+ str(driverId)+"'"
            columns= "ontrip=2 "
            bookRide1=databasefile.UpdateQuery("ambulanceRideStatus",columns,whereCondition222)
            if (bookRide!=0):   
                bookRide["message"]="Leave taken Successfully"             
                return bookRide
            else:
                
                return bookRide
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


# @app.route('/Dashboard', methods=['POST'])
# def Dashboard():
#     try:
#         inputdata =  commonfile.DecodeInputdata(request.get_data())
#         startlimit,endlimit="",""
#         keyarr = [""]
#         commonfile.writeLog("Dashboard",inputdata,0)
#         msg = commonfile.CheckKeyNameBlankValue(keyarr,inputdata)
#         if msg == "1":
#             column=  " d.name, d.mobileNo, a.ambulanceId, a.ambulanceNo, a.lat, a.lng,SQRT(POW(69.1 * (a.lat - "+str(startlat)+"), 2) +POW(69.1 * ("+str(startlng)+" - a.lng) * COS(a.lat / 57.3), 2)) AS distance "
#             whereCondition= " and a.onTrip=0 and a.onDuty=1 and a.driverId=d.id HAVING distance < 1200 "
#             orderby="  distance "
#             nearByAmbulance=databasefile.SelectQueryOrderbyAsc("ambulanceMaster a, driverMaster d",column,whereCondition,"",orderby,"","")
#             if (nearByAmbulance!=0):   
                               
#                 return nearByAmbulance
#             else:
                
#                 return nearByAmbulance
            
#         else:
#             return msg 
#     except KeyError as e:
#         print("Exception---->" +str(e))        
#         output = {"result":"Input Keys are not Found","status":"false"}
#         return output    
#     except Exception as e :
#         print("Exception---->" +str(e))           
#         output = {"result":"something went wrong","status":"false"}
#         return output










#==========================================admin==================================================

@app.route('/adminLogin', methods=['POST'])
def adminLogin():
    try:
        inputdata =  commonfile.DecodeInputdata(request.get_data())
        startlimit,endlimit="",""
        keyarr = ['email','password']
        commonfile.writeLog("adminLogin",inputdata,0)
        msg = commonfile.CheckKeyNameBlankValue(keyarr,inputdata)
        if msg == "1":
            email = inputdata["email"]
            password = inputdata["password"]
            column=  "us.mobileNo,us.name,us.userTypeId,um.usertype,us.userId"
            whereCondition= " us.email = '" + str(email) + "' and us.password = '" + str(password) + "'  and  us.userTypeId=um.id"
            loginuser=databasefile.SelectQuery("userMaster as us,usertypeMaster as um",column,whereCondition)
            if (loginuser!=0):   
                               
                return loginuser
            else:
                
                return loginuser
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

#==========================================admin==================================================









if __name__ == "__main__":
    CORS(app, support_credentials=True)
    app.run(host='0.0.0.0',port=5077,debug=True)
    socketio.run(app)        
