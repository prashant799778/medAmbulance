from flask import Flask,request,abort
from flask_socketio import SocketIO,emit
from flask import Flask, send_from_directory, abort
import uuid
import json
import notification
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
import paho.mqtt.client as mqtt
from flask import Flask, render_template
# standard Python
#sio = socketio.Client()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
#socketio = SocketIO(app, cors_allowed_origins="*")
# sio = socketio.Client()







client = mqtt.Client()
client.connect("localhost",1883,60)



class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)

geocoder = GoogleGeocoder("AIzaSyB0Pz6VjrQmWPCCbDbWDuyjo79GhDJPOlI")


@app.route("/profilePic/<image_name>")
def profilePic(image_name):
    try:
        return send_from_directory('profilePic', filename=image_name, as_attachment=False)
    except FileNotFoundError:
        abort(404)





@app.route("/DLImage/<image_name>")
def DLImage(image_name):
    try:
        return send_from_directory('DLImage', filename=image_name, as_attachment=False)
    except FileNotFoundError:
        abort(404)



@app.route("/AmbulanceImage/<image_name>")
def AmbulanceImage(image_name):
    try:
        return send_from_directory('AmbulanceImage', filename=image_name, as_attachment=False)
    except FileNotFoundError:
        abort(404)


@app.route("/PIDImage/<image_name>")
def PIDImage(image_name):
    try:
        return send_from_directory('PIDImage', filename=image_name, as_attachment=False)
    except FileNotFoundError:
        abort(404)







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
                    print(data,"===================")
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
                    Data = {"status":"true","message":"","result":data["result"][0]}                  
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

            column="mobileNo,otp,userTypeId,userId"
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
        keyarr = ['mobileNo','key','name']
        inputdata=json.loads(inputdata)
        # inputdata =  commonfile.DecodeInputdata(request.get_data()) 
        startlimit,endlimit="",""

        commonfile.writeLog("addDriver",inputdata,0)
        msg = commonfile.CheckKeyNameBlankValue(keyarr,inputdata)
        print(msg,'msg')
       
        if msg == "1":
            mobileNo=inputdata['mobileNo']
            name=inputdata['name']
           
            key = inputdata["key"]
            column = " * "
            whereCondition= " mobileNo='"+str(mobileNo)+ "' and usertypeId='3'"
            data= databasefile.SelectQuery("userMaster",column,whereCondition)

            column11="id,driverId"

            whereCondition1= " mobileNo='"+str(mobileNo)+ "'"
            data1= databasefile.SelectQuery("driverMaster",column11,whereCondition1)

            print(data1,'data--------------------------')

           
            mobileNo= inputdata["mobileNo"]
            driverId=data['result']['userId']
            
            DlNo,dlFrontFilename,DlFrontPicPath,dlBackFilename,DlBackPicPath,PIDType,PIDNo,PIDFrontFilename,PIDFrontPicPath,PIDBackFilename,PIDBackPicPath,TransportType,TransportModel,Color,AmbulanceRegistrationFuel,TypeNo,AIFilename,AIPicPath,AmbulanceModeId,AmbulanceId="","","","","","","","","","","","","","","","","","","",""

            if 'DlNo' in inputdata:
                DlNo=inputdata["DlNo"]

            if 'DlFrontImage' in request.files:
                    print("immmmmmmmmmmmmmmmm")
                    file = request.files.get('DlFrontImage')        
                    filename = file.filename or ''  
                    print(filename)               
                    dlFrontFilename= str(str(data['result']["userId"])+"Front"+".png")
                    
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
                    dlBackFilename=  str(str(data['result']["userId"])+"Back"+".png")
                  
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
                    PIDFrontFilename= str(str(data['result']["userId"])+"Front"+".png")
                  
                    print(PIDFrontFilename,'Changed_filename')
                    PIDFrontFolderPath = ConstantData.GetPIDImagePath(PIDFrontFilename)
                    PIDFrontfilepath = '/PIDImage/' + PIDFrontFilename 
                    file.save(PIDFrontFolderPath)
                    PIDFrontPicPath = PIDFrontfilepath
                    print(PIDFrontPicPath)
                    

            if 'PIDBackImage' in request.files:
                    print("immmmmmmmmmmmmmmmm")
                    file = request.files.get('PIDBackImage')        
                    filename = file.filename or ''  
                    print(filename)               
                    PIDBackFilename= str(str(data['result']["userId"])+"Back"+".png")
                  
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
                    AIFilename=  str(str(data['result']["userId"])+".png")
                   
                    AIFolderPath = ConstantData.GetAmbulanceImagePath(AIFilename)
                    AIfilepath = '/AmbulanceImage/' + AIFilename 
                    file.save(AIFolderPath)
                    AIPicPath = AIfilepath
                    print(AIPicPath)

            if data['status']!='false':
                
                if data1['status'] == 'false':
                    print('11')
                    if key == 1:
                        columns = "name,mobileNo,dlNo,dlFrontFilename,dlFrontFilepath,dlBackFilename,dlBackFilepath,driverId"          
                        values = " '" + str(name) + "','" + str(mobileNo) + "','" + str(DlNo) + "','" + str( dlFrontFilename) + "','" + str(DlFrontPicPath) + "','" + str(dlBackFilename) + "', "            
                        values = values + " '" + str(DlBackPicPath) + "','" + str(driverId) + "'"
                        data = databasefile.InsertQuery("driverMaster",columns,values)
                        if data != "0":
                            column = '*'
                            WhereCondition = " mobileNo = '" + str(mobileNo) +  "'"
                            
                            data11 = databasefile.SelectQuery("driverMaster",column,WhereCondition)
                            return data11
                    if key == 2:
                        columns = " name,mobileNo,pIDType,pIDNo,pIDFrontFilename,pIDFrontFilepath,pIDBackFilename,pIDBackFilepath,driverId"          
                        values = " '" + str(name) + "','" + str(mobileNo) + "','" + str(PIDType) + "','" + str(PIDNo) + "','" + str(PIDFrontFilename) + "','" + str(PIDFrontPicPath) + "','" + str(PIDBackFilename) + "', "            
                        values = values + " '" + str(PIDBackPicPath)+ "','" + str(driverId) + "'"
                        data = databasefile.InsertQuery("driverMaster",columns,values)
                        if data != "0":
                            column = '*'
                            WhereCondition = " mobileNo = '" + str(mobileNo) +  "'"
                            
                            data11 = databasefile.SelectQuery("driverMaster",column,WhereCondition)
                            return data11
                    
                    if key == 3:

                        columns = " name,mobileNo,driverId"          
                        values = " '" + str(name) + "','" + str(mobileNo) + "','" + str(driverId) + "'"
                        
                        data = databasefile.InsertQuery("driverMaster",columns,values)

                        columns222="driverId"
                        whereCondition2222=" "
                        data99=databasefile.SelectQuery1('driverMaster',columns222,whereCondition2222)
                        data111=data99[-1]
                        driverid=data111["driverId"]

                        columns2= "ambulanceNo,transportType,transportModel,color,ambulanceRegistrationFuel,typeNo,ambulanceFilename,ambulanceFilepath,ambulanceModeId,ambulanceTypeId,driverId"
                        values2="'" + str(AmbulanceNo) + "','" + str( TransportType)  + "','" + str(TransportModel) + "','" + str(Color) + "','" + str(AmbulanceRegistrationFuel) + "','" + str(TypeNo) + "','" + str(AIFilename) + "','" + str(AIPicPath) + "','" + str(AmbulanceModeId) + "', "            
                        values2 = values2 + " '" + str(AmbulanceId) + "','" + str(driverid) + "'"
                        data122=databasefile.InsertQuery("ambulanceMaster",columns2,values2)
                        
                        

                        if data122 != "0":
                            column = '*'
                            WhereCondition = " mobileNo = '" + str(mobileNo) +  "'"
                            whereCondition="   driverId='" + str(driverid) +  "' "
                            columns22="ambulanceId,transportType,transportModel,color,ambulanceRegistrationFuel,typeNo,ambulanceFilename,ambulanceFilepath,ambulanceModeId,ambulanceTypeId,ambulanceNo"
                            
                            data11 = databasefile.SelectQuery("driverMaster",column,WhereCondition)


                            data12=databasefile.SelectQuery("ambulanceMaster",columns22,whereCondition)

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
                
                
                else:
                    if key == 1:
                        print('A')
                        WhereCondition = " mobileNo = '" + str(mobileNo) + "'"
                        column = " name='" + str(name) + "' ,dlNo = '" + str(DlNo) + "',dlFrontFilename = '" + str(dlFrontFilename) + "',dlFrontFilepath = '" + str(DlFrontPicPath) + "',dlBackFilename = '" + str(dlBackFilename) + "',dlBackFilepath = '" + str(DlBackPicPath) + "'"
                        print(column,'column')
                        data = databasefile.UpdateQuery("driverMaster",column,WhereCondition)
                        print(data,'updatedata')
                        return data
                    if key == 2:
                        print('B')
                        WhereCondition = " mobileNo = '" + str(mobileNo) + "'"
                        column = "name='" + str(name) + "', pIDType = '" + str(PIDType) + "',pIDNo = '" + str(PIDNo) + "',pIDFrontFilename = '" + str(PIDFrontFilename) + "',pIDFrontFilepath = '" + str(PIDFrontPicPath) + "',pIDBackFilename = '" + str(PIDBackFilename) + "',pIDBackFilepath = '" + str(PIDBackPicPath) + "'"
                        print(column,'column')
                        data = databasefile.UpdateQuery("driverMaster",column,WhereCondition)
                        print(data,'updatedata')
                        return data

                    if key == 3:
                        driver_Id=data1['result']['driverId']
                        columns="ambulanceId"
                        WhereCondition = " driverId = '" + str(driver_Id) + "'"
                        data111=databasefile.SelectQuery('ambulanceMaster',columns,WhereCondition)
                        if data111['status'] == 'false':
                            
                            columns2= "ambulanceNo,transportType,transportModel,color,ambulanceRegistrationFuel,typeNo,ambulanceFilename,ambulanceFilepath,ambulanceModeId,ambulanceTypeId,driverId"

                            values2="'" + str(AmbulanceNo) + "','" + str( TransportType) + "','" + str(TransportModel) + "','" + str(Color) + "','" + str(AmbulanceRegistrationFuel) + "','" + str(TypeNo) + "','" + str(AIFilename) + "','" + str(AIPicPath) + "','" + str(AmbulanceModeId) + "', "            
                            values2 = values2 + " '" + str(AmbulanceId) + "','" + str(driver_Id) + "'"
                            data122=databasefile.InsertQuery("ambulanceMaster",columns2,values2)
                            print(data122,'+++++++++++++++++++')
                            
                            

                            if data122 != "0":
                                column = '*'
                                WhereCondition = " mobileNo = '" + str(mobileNo) +  "'"
                                whereCondition="   driverId='" + str(driver_Id) +  "' "
                                columns22="ambulanceId,transportType,transportModel,color,ambulanceRegistrationFuel,typeNo,ambulanceFilename,ambulanceFilepath,ambulanceModeId,ambulanceTypeId,ambulanceNo"
                                
                                data11 = databasefile.SelectQuery("driverMaster",column,WhereCondition)


                                data12=databasefile.SelectQuery("ambulanceMaster",columns22,whereCondition)

                                ambulanceId=data12['result']['ambulanceId']
                                columns23='ambulanceId,lat,lng'
                                values23 = " '" + str(ambulanceId) + "','" + str(lat) + "','" + str(lng) + "'"
                                data122=databasefile.InsertQuery('ambulanceRideStatus',columns23,values23)
                                whereCondition222= " ambulanceId=  '" + str(ambulanceId) +  "' "
                                columns239="lat,lng,onDuty,onTrip"
                                data12333=databasefile.SelectQuery('ambulanceRideStatus',columns239,whereCondition222)



                                data11['result'].update(data12['result'])
                                data11['result'].update(data12333['result'])

                                return data11

                            print('q')
                        else:
                            data11={"result":"","message":"Already Existed","status":"false"}
                            return data11


                        
               
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
                print('entered')
                column="ambulanceType"
                values="'"+str(ambulanceType)+"'"
                insertdata=databasefile.InsertQuery("ambulanceMode",column,values)
                column="*"
                whereCondition= "ambulanceType='"+str(ambulanceType)+ "'"
                data8= databasefile.SelectQuery1("ambulanceMode",column,whereCondition)
                print(data8,'8888888888888')
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
            if data['status']=='false':
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


@app.route('/selectproofIdentityMaster', methods=['GET'])
def proofIdentityMaster():
    try:
        msg = "1"
        if msg=="1":
            column="id ,name"
            whereCondition=""
            data=databasefile.SelectQuery1("proofIdentityMaster",column,whereCondition)
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


@app.route('/facilityMaster', methods=['GET'])
def facilityMaster():
    try:
        msg = "1"
        if msg=="1":
            column="id ,name"
            whereCondition=""
            data=databasefile.SelectQuery1("facilityMaster",column,whereCondition)
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



@app.route('/cityMaster', methods=['GET'])
def cityMaster():
    try:
        msg = "1"
        if msg=="1":
            column="id ,name"
            whereCondition=""
            data=databasefile.SelectQuery1("cityMaster",column,whereCondition)
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

@app.route('/allDrivers', methods=['POST'])
def alldrivers():
    try:
        msg = "1"
        if msg =="1":
            startlimit,endlimit="",""
            WhereCondition=" and dm.driverId = um.userId"

            inputdata =  commonfile.DecodeInputdata(request.get_data())  
            if "startlimit" in inputdata:
                if inputdata['startlimit'] != "":
                    startlimit =str(inputdata["startlimit"])
                
            if "endlimit" in inputdata:
                if inputdata['endlimit'] != "":
                    endlimit =str(inputdata["endlimit"])

            if "driverId" in inputdata:
                if inputdata['driverId'] != "":
                    driverId = str(inputdata["driverId"])
                    WhereCondition = WhereCondition + " and dm.driverId= "+str(driverId)+ " "

            column="dm.name,dm.mobileNo,dm.profilePic,am.ambulanceNo,am.ambulanceId,um.email,ars.lat,ars.lng,ars.onDuty,ars.onTrip,dm.currentLocation as address,date_format(dm.dateCreate,'%Y-%m-%d %H:%i:%s')joiningDate,dm.status as status,dm.driverId as driverId"
            whereCondition=" and dm.driverId=am.driverId  and am.ambulanceId=ars.ambulanceId  and dm.status<>'2' " + WhereCondition
            data=databasefile.SelectQuery2("driverMaster as dm,ambulanceMaster as am,ambulanceRideStatus as ars,userMaster um",column,whereCondition,"",startlimit,endlimit)
            print(data)
            
            if (data['status']!='false'):
                y2=len(data['result'])
                if y2 ==1:
                    print('111111111111111')
                    if data['result'][0]["profilePic"]==None:
                        data['result'][0]["profilePic"]=str(ConstantData.GetBaseURL())+"/profilePic/profilePic.jpg" 
                    ambulanceId1=data['result'][0]['ambulanceId']
                    d1=data['result'][0]['driverId']
                    print(ambulanceId1)
                    columns2=" am.ambulanceTypeId,concat('"+ ConstantData.GetBaseURL() + "',am.ambulanceFilepath)ambulanceFilepath,um.email,am.ambulanceModeId,am.ambulanceFilename,atm.ambulanceType  as ambulanceType,AM.ambulanceType  as category,am.ambulanceRegistrationFuel as fuelType,am.color,am.transportModel,am.transportType"
                    whereCondition222="  am.ambulanceId=ars.ambulanceId and atm.id=am.ambulanceTypeId and AM.id=am.ambulanceModeId and am.ambulanceId="+str(ambulanceId1)+ ""
                    data111=databasefile.SelectQuery('ambulanceMaster as am,ambulanceRideStatus as ars,ambulanceTypeMaster as atm,userMaster um,ambulanceMode as AM',columns2,whereCondition222)
                    y2=data111['result']
                    print(y2)
                    column2222="dlNo,dlFrontFilename,concat('"+ ConstantData.GetBaseURL() + "',dlFrontFilepath)dlFrontFilepath,dlBackFilename,concat('"+ ConstantData.GetBaseURL() + "',dlBackFilepath)dlBackFilepath,pIDType,pIDNo,pIDFrontFilename,concat('"+ ConstantData.GetBaseURL() + "',pIDFrontFilepath)pIDFrontFilepath,pIDBackFilename,concat('"+ ConstantData.GetBaseURL() + "',pIDBackFilepath)pIDBackFilepath"
                    whereCondition2222=" id = "+str(d1)+ " "
                    data11111=databasefile.SelectQuery('driverMaster',column2222,whereCondition2222)
                    y3=data11111['result']
                    data['result'][0].update(y2)
                    data['result'][0].update(y3)

                    Data = {"result":data['result'],"status":"true","message":""}
                    return Data

                else:
                    for i in data['result']:
                        if i["profilePic"]==None:
                            print('1111111111111111111')
                            i["profilePic"]=str(ConstantData.GetBaseURL())+"/profilePic/profilePic.jpg"  
                        ambulanceId2= i['ambulanceId']
                        columns99="count(*) as count"
                        whereCondition88= " ambulanceId='"+str(ambulanceId2)+ "'"
                        data122=databasefile.SelectQuery('bookAmbulance',columns99,whereCondition88)
                        if data122['status']!='false':
                            i['tripCount']=0
                        else:
                            tripcount=data122['result']['count']
                            i['tripCount']=tripcount

                    Data = {"result":data['result'],"status":"true","message":""}
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


@app.route('/addhospital', methods=['POST'])
def addhospital():
    try:
        print('A')
        inputdata =  commonfile.DecodeInputdata(request.get_data())
        startlimit,endlimit="",""
        keyarr = ['hospitalName','address','ambulanceId','lat','lng','facilityId']
        commonfile.writeLog("addhospital",inputdata,0)
        msg = commonfile.CheckKeyNameBlankValue(keyarr,inputdata)
        if msg=="1":
            hospitalName = commonfile.EscapeSpecialChar(inputdata["hospitalName"])
            address = commonfile.EscapeSpecialChar(inputdata["address"])
            ambulanceId = inputdata["ambulanceId"]
            facility=inputdata['facilityId']
            print(facility,"++++++++++++++++++++++++++++++++++++++++++")
            
            latitude=inputdata['lat']

            longitude=inputdata['lng']

            city=inputdata['cityId']
            print(city)

            column=" id "
            whereCondition= "hospitalName='"+str(hospitalName)+ "'"
            data= databasefile.SelectQuery("hospitalMaster",column,whereCondition)

            print(data['status'],'===data')

            if data['status'] =='false':
                
                print('AA')
                column="hospitalName"
                values=" '"+str(hospitalName)+"' "
                insertdata=databasefile.InsertQuery("hospitalMaster",column,values)

                column=" id as hospitalId "
                whereCondition="hospitalName= '"+str(hospitalName)+ "' "
                data= databasefile.SelectQuery1("hospitalMaster",column,whereCondition)

                print(data[-1],'data1111')
                yu=data[-1]
                mainId=yu["hospitalId"]

                
                print(mainId,'mainId')
                ambulanceId1 = ambulanceId
                facilityId1=facility

                print(ambulanceId1,'ambulance')


                column='address,lat,lng,hospitalId,cityId'
                values="'"+str(address)+"','"+str(latitude)+"','"+str(longitude)+"','"+str(mainId)+"','"+str(city)+"'"
                insertdata=databasefile.InsertQuery("hospitalLocationMaster",column,values)
                for i in ambulanceId1:

                    column=" * "
                    whereCondition2="ambulance_Id='"+str(i)+"'  and hospital_Id='"+str(mainId)+"'"
                    userHospitalMappingdata = databasefile.SelectQuery1("hospitalambulanceMapping",column,whereCondition2)
                    print(userHospitalMappingdata,'lets see')
                    if userHospitalMappingdata==0:
                        print('CC')
                        column="hospital_Id,ambulance_Id"
                        values="'"+str(mainId)+"','"+str(i)+"'"
                        insertdata=databasefile.InsertQuery("hospitalambulanceMapping",column,values)                
                        output = {"result":"data inserted successfully","status":"true"}
                        return output
                    else:
                        output = {"result":"Data already existed in mapping table","status":"true"}
                        return output

                for i in facility:

                    column=" * "
                    whereCondition="facilityId='"+str(i)+"'  and hospitalId='"+str(mainId)+"'"
                    userHospitalMappingdata = databasefile.SelectQuery1("hospitalFacilityMapping ",column,whereCondition)
                    print(userHospitalMappingdata,'lets see')
                    if userHospitalMappingdata==0:
                        print('CCcccccccccccccccccccccccccccccccccccccccc')
                        column="hospitalId,facilityId"
                        values="'"+str(mainId)+"','"+str(i)+"'"
                        insertdata=databasefile.InsertQuery("hospitalFacilityMapping",column,values)                
                        output = {"result":"data inserted successfully","status":"true"}
                        return output
                    else:
                        output = {"result":"Data already existed in mapping table","status":"true"}
                        return output        
            else:
                hospitalId=data['result']['id']
                column="*"
                whereCondition222=" hospitalId='"+str(hospitalId)+"' and address='"+str(address)+"' and lat='"+str(latitude)+"' and lng= '"+str(longitude)+"'  "
                data=databasefile.SelectQuery('hospitalLocationMaster',column,whereCondition222)
                if data['status'] == 'false':
                    column='address,lat,lng,hospitalId,city'
                    values="'"+str(address)+"','"+str(latitude)+"','"+str(longitude)+"','"+str(hospitalId)+"','"+str(city)+"'"
                    insertdata=databasefile.InsertQuery("hospitalLocationMaster",column,values)

                for i in ambulanceId:

                    column=" * "
                    whereCondition="ambulance_Id='"+str(i)+"'  and hospital_Id='"+str(hospitalId)+"'"
                    userHospitalMappingdata = databasefile.SelectQuery1("hospitalambulanceMapping",column,whereCondition)
                    print(userHospitalMappingdata,'lets see')
                    if userHospitalMappingdata==0:
                        print('CC')
                        column="hospital_Id,ambulance_Id"
                        values="'"+str(hospitalId)+"','"+str(i)+"'"
                        insertdata=databasefile.InsertQuery("hospitalambulanceMapping",column,values)                
                        output = {"result":"data inserted successfully","status":"true"}
                        return output
                    else:
                        output = {"result":"Data already existed in mapping table","status":"true"}
                        return output

                for i in facility:
                    column=" * "
                    whereCondition="facilityId='"+str(i)+"'  and hospitalId='"+str(hospitalId)+"'"
                    userHospitalMappingdata = databasefile.SelectQuery1("hospitalFacilityMapping ",column,whereCondition)
                    print(userHospitalMappingdata,'lets see')
                    if userHospitalMappingdata==0:
                        print('CC')
                        column="hospitalId,facilityId"
                        values="'"+str(hospitalId)+"','"+str(i)+"'"
                        insertdata=databasefile.InsertQuery("hospitalFacilityMapping",column,values)                
                        output = {"result":"data inserted successfully","status":"true"}
                        return output
                    else:
                        output = {"result":"Data already existed in mapping table","status":"true"}
                        return output             



                else:    
                    output = {"result":"Hospital  address Already  Existed ","status":"true"}
                    return output
        else:
            return msg 
    except Exception as e :
        print("Exception---->" + str(e))    
        output = {"result":"something went wrong","status":"false"}
        return output



@app.route('/updateHospital', methods=['POST'])
def updateStatus11():
    try:
        inputdata =  commonfile.DecodeInputdata(request.get_data())
        startlimit,endlimit="",""
        keyarr = ['id','address','ambulanceId','lat','lng','facilityId']
        print(inputdata,"B")
        commonfile.writeLog("updateHospital",inputdata,0)
        msg = commonfile.CheckKeyNameBlankValue(keyarr,inputdata)
        if msg =="1":
          
            userId = int(inputdata["id"])
            hospitalName = commonfile.EscapeSpecialChar(inputdata["hospitalName"])
            address = commonfile.EscapeSpecialChar(inputdata["address"])
            ambulanceId = inputdata["ambulanceId"]
            facilityId=inputdata['facilityId']
            print(facilityId,"++++++++++++++++++++++++++++++++++++++++++")
            
            latitude=inputdata['lat']

            longitude=inputdata['lng']

            city=inputdata['cityId']
           
            column="hospitalName"
            whereCondition= "   id = " + str(userId)+ " "
            data=databasefile.SelectQuery1("hospitalMaster",column,whereCondition)
            print(data)
            if (data !=0):
                column=" hospitalName= '"+str(hospitalName)+"' "
                whereCondition="   id = " + str(userId)+ " "
                data1=databasefile.UpdateQuery('hospitalMaster',column,whereCondition)

                column2="address='"+str(address)+"' ,lat='"+str(latitude)+"' ,lng='"+str(longitude)+"' ,cityId='"+str(city)+"' "
                whereCondition3=" hospitalId=' " + str(userId)+ " ' "
                data2=databasefile.UpdateQuery('hospitalLocationMaster',column2,whereCondition3)

                whereCondition2=" hospital_Id= ' " + str(userId)+ " ' "
                data3=databasefile.DeleteQuery('hospitalambulanceMapping',whereCondition2)

                whereCondition4= "hospitalId = ' " + str(userId)+ " ' "
                data4=databasefile.DeleteQuery('hospitalFacilityMapping',whereCondition4)


                for i in ambulanceId:
                    print('a1111111')

                    column=" * "
                    whereCondition="ambulance_Id='"+str(i)+"'  and hospital_Id='"+str(userId)+"'"
                    userHospitalMappingdata = databasefile.SelectQuery1("hospitalambulanceMapping",column,whereCondition)
                    print(userHospitalMappingdata,'lets see')
                    if userHospitalMappingdata==0:
                        print('CC')
                        column="hospital_Id,ambulance_Id"
                        values="'"+str(userId)+"','"+str(i)+"'"
                        insertdata=databasefile.InsertQuery("hospitalambulanceMapping",column,values)                
                        output = {"result":"data Updated  successfully","status":"true"}
                        return output
                    else:
                        output = {"result":"Data already existed in mapping table","status":"true"}
                        return output

                for i in facilityId:
                    print('aaaaaaaaaa')
                    column=" * "
                    whereCondition="facilityId='"+str(i)+"'  and hospitalId='"+str(userId)+"'"
                    userHospitalMappingdata = databasefile.SelectQuery1("hospitalFacilityMapping ",column,whereCondition)
                    print(userHospitalMappingdata,'lets see')
                    if userHospitalMappingdata==0:
                        print('CC')
                        column="hospitalId,facilityId"
                        values="'"+str(userId)+"','"+str(i)+"'"
                        insertdata=databasefile.InsertQuery("hospitalFacilityMapping",column,values)                
                        output = {"result":"data updated successfully","status":"true"}
                        return output
                    else:
                        output = {"result":"Data already existed in mapping table","status":"true"}
                        return output
                
                output = {"result":"data updated successfully","status":"true","message":"Updated Successfully"}
                return output                     









            else:
                data={"result":"","status":"false","message":"No Data Found"}
                return data
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
        


# @app.route('/addRiderBooking', methods=['POST'])
# def addRiderBooking():
#     try:
#         data1 = commonfile.DecodeInputdata(request.get_data())
#         pickup=str(data1["pickup"])
#         search = geocoder.get(pickup)
#         search[0].geometry.location
#         fromlatitude= search[0].geometry.location.lat
#         fromlongitude=search[0].geometry.location.lng
        
#         bookingId=uuid.uuid1()
#         bookingId=bookingId.hex
#         R = 6373.0
#         column=" * "
#         whereCondition="userId='"+str(data1["userId"])+ "' and status<>'2'"
#         data=databasefile.SelectQuery("responderBooking",column,whereCondition)
#         if data==None:
#             column="responderId,currentLocationlatlong,mobileNo,currentLocation"
#             whereCondition="drivingStatus<>'1'"
#             datavv=databasefile.SelectQuery1("responderMaster",column,whereCondition)
#             for da in datavv:
#                 da.split(",")
#                 driverlattitude=int(da[0])
#                 driverlongitude=int(da[2])
#                 distanceLongitude = driverlongitude-fromlongitude
#                 distanceLatitude = driverlattitude-fromlattitude
#                 a = sin(distanceLatitude / 2)**2 + cos(driverlattitude) * cos(fromlatitude) * sin(driverlongitude/ 2)**2
#                 c = 2 * atan2(sqrt(a), sqrt(1 - a))
#                 distanceDriver = R * c
#                 distance1=distanceDriver/100
#                 distanceD=distance2*1.85
#                 d1=round(distanceD)
#                 d9 =str(d) +' Km'
#                 if d1 <2:
#                     riderId=da['responderId']
#                     driverMobile=da['mobileNo']
           
#             column="usermobile,pickup,pickupLongitudeLatitude,userId,bookingId,finalAmount,totalDistance"
#             values="'"+str(data1["mobileNo"])+"','"+str(data1["pickup"])+"','"+str(fromlatitude,fromlongitude)+"','"+str(data1["userId"])+"','"+str(bookingId)+"','"+str(data1["finalAmount"])+"','"+str(d9)+"'"
#             insertdata=databasefile.InsertQuery("responderBooking",column,values)
#             column=" * "
#             whereCondition="userId='"+str(data1["userId"])+ "' and status<>'2'"
#             data=databasefile.SelectQuery1("responderBooking",column,whereCondition)
#             yu=data[-1]
#             mainId=yu["bookingId"]
#             pickuplocation=yu["pickup"]
#             userid=yu["userId"]
#             column="bookingId,responderId,farDistance,pickup,userId"
#             values="'"+str(mainId)+"','"+str(riderId)+"','"+str(d9)+"','"+str(pickuplocation)+"','"+str(userid)+"'"
#             insertdata=databasefile.InsertQuery("responderBookingMapping",column,values)              
#             output = {"result":"data inserted successfully","status":"true","ride Details":data[-1]}
#             return output
           
#         else:
#             output = {"result":"Hospital Already  Existed ","status":"false"}
#             return output 
#     except Exception as e :
#         print("Exception---->" + str(e))    
#         output = {"result":"something went wrong","status":"false"}
#         return output






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




@app.route('/allHospital1', methods=['POST'])
def allHospital():
    try:
        msg="1"
        if msg=="1":
            ambulanceType=""
            whereCondition=""
            whereCondition2=""
            startlimit,endlimit="",""
            inputdata =  commonfile.DecodeInputdata(request.get_data())  
            if "startLimit" in inputdata:
                if inputdata['startLimit'] != "":
                    startlimit =str(inputdata["startLimit"])
                
            if "endLimit" in inputdata:
                if inputdata['endLimit'] != "":
                    endlimit =str(inputdata["endLimit"])
            if 'ambulanceTypeId' in inputdata:
                ambulanceType=int(inputdata["ambulanceTypeId"])
                whereCondition=" and am.id   = '" + str(ambulanceType) + "'  "

            if 'hospitalId' in request.args:
                Id=request.args["hospitalId"]
                whereCondition2=" and  hosp.id  = '" + str(Id) + "'  "    

            column= "hosp.id,hosp.hospitalName,hosp.address,am.ambulanceType,hosp.longitude,hosp.latitude,am.id as ambulanceTypeId,fm.name as facility,fm.id as facilityId"   
            WhereCondition=  " hosp.id=ahm.hospital_Id and am.id=ahm.ambulance_Id and fm.id=hFm.facilityId"+whereCondition+whereCondition2
            data=databasefile.SelectQuery2("hospitalMaster as hosp,hospitalambulanceMapping as ahm,ambulanceTypeMaster as am,facilityMaster as fm,hospitalFacilityMapping as hFm",column,WhereCondition,startlimit,endlimit)
            print(data,'data')
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



@app.route('/allHospital', methods=['POST'])
def allHospital1():
    try:
        msg="1"
        if msg=="1":
            ambulanceType=""
            whereCondition=""
            whereCondition2=""
            whereCondition3=""
            whereCondition4=""
            inputdata =  commonfile.DecodeInputdata(request.get_data())  
            if "startLimit" in inputdata:
                if inputdata['startLimit'] != "":
                    startlimit =str(inputdata["startLimit"])
                
            if "endLimit" in inputdata:
                if inputdata['endLimit'] != "":
                    endlimit =str(inputdata["endLimit"])
            if 'ambulanceTypeId' in inputdata:
                ambulanceType=int(inputdata["ambulanceTypeId"])
                whereCondition=" and am.id   = '" + str(ambulanceType) + "'  "

            if 'id' in inputdata:
                Id=int(inputdata["id"])
                whereCondition2=" and  hosp.id  = '" + str(Id) + "'  "

            if 'city' in inputdata:
                city=str(inputdata["city"])
                whereCondition3=" and  cm.name  = '" + str(city) + "'  "

            if 'cityId' in inputdata:
                cityId=str(inputdata["cityId"])
                whereCondition4=" and  cm.id  = '" + str(cityId) + "'  "                   

            column= "hosp.id,hosp.hospitalName,hl.address,hl.lat,hl.lng,cm.name as city,cm.id as cityId"   
            WhereCondition=  " hl.hospitalId=hosp.id and hosp.status<>'2' and hl.cityId=cm.id "+whereCondition2+whereCondition3+whereCondition4
            data=databasefile.SelectQuery1("hospitalMaster as hosp,hospitalLocationMaster as hl,cityMaster as cm",column,WhereCondition)
            if (data!=0): 
                a=[]
                b=[]
                for i in data:
                    hospital_Id=i['id']
                    column="hma.ambulance_Id as ambulanceId,hma.hospital_Id as hospitalId,am.ambulanceType"
                    whereCondition=" hma.hospital_Id=  '" + str(hospital_Id) + "' and am.id=hma.ambulance_Id"
                    data1=databasefile.SelectQuery1('hospitalambulanceMapping as hma,ambulanceTypeMaster as am',column,whereCondition)

                    print(data1,'aaaaaaaaaaaaaaaaaaa')
                    a=[]
                    d=""

                    for j in data1:
                        
                        
                        if j['hospitalId'] == hospital_Id:
                            a_id=j['ambulanceId']
                            
                           
                            a.append(j['ambulanceId'])
                            i['ambulanceId']=a
                            y=len(a)
                            if y != 1:
                                d+=","+j['ambulanceType']
                            else:
                                d=j['ambulanceType']
                    # i['ambulanceId']=j['ambulanceId']
                    i['ambulanceType']=d


                    column=" hfm.hospitalId,hfm.facilityId as facilityId,fm.name as facilityName"
                    whereCondition21="hfm.hospitalId= '" + str(hospital_Id) + "' and fm.id=hfm.facilityId"
                    data2= databasefile.SelectQuery1('hospitalFacilityMapping as hfm,facilityMaster as fm',column,whereCondition21)
                    g=[]
                    h=""
                    for k in data2:
                        if k['hospitalId'] == hospital_Id:
                            g.append(k['facilityId'])
                            i['facilityId']=g
                            y2=len(g)
                            if y2!=1:
                                h+=","+k['facilityName']
                            else:
                                h=k['facilityName']
                    i['facilityName']= h           



                    # print(data1)

                   
                    # c=i['aId']
                    # print(c)
                    # if i['id'] not in a:
                    #     # a.append(i)
                    #     # i['ambulanceTypeId']=c
                    #     # i['ambulanceType']+=i['at'] +","


                



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
            print(data,'==data')
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
            print(data,'data')
            if (data['status'] != 'false'):
                print('A')           
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



@app.route('/nearbyHospital', methods=['POST'])
def nearbyHospital():
    try:
        whereCondition,groupby,startlimit,endlimit="","","",""
        # inputdata =  commonfile.DecodeInputdata(request.get_data())
        # startlimit,endlimit="",""
        # keyarr = ['bookingId']
        # commonfile.writeLog("trackResponder",inputdata,0)
        # msg = commonfile.CheckKeyNameBlankValue(keyarr,inputdata)
        #if msg=="1":
        #bookingId = inputdata["bookingId"]
        column="*"
        #whereCondition= "dbm.responderId=dm.responderId and dbm.bookingId='" + str(bookingId) + "'"
        nearbyHospital=databasefile.SelectQuery2(" hospitalMaster",column,whereCondition,groupby,startlimit,endlimit)
        
        if nearbyHospital:
            return nearbyHospital
        else:
            output = {"result":"No Data Found","status":"false"}
            return output
        # else:
        #     return msg

    except Exception as e :
        print("Exception---->" + str(e))    
        output = {"result":"something went wrong","status":"false"}
        return output


# @app.route('/getNearAmbulance', methods=['POST'])
# def getNearAmbulance():
#     try:
#         inputdata =  commonfile.DecodeInputdata(request.get_data())
#         startlimit,endlimit="",""
#         keyarr = ['startLocationLat','startLocationLong']
#         commonfile.writeLog("getNearAmbulance",inputdata,0)
#         msg = commonfile.CheckKeyNameBlankValue(keyarr,inputdata)
#         if msg == "1":
#             startlat ,startlng,userId= inputdata["startLocationLat"],inputdata["startLocationLong"],""#,inputdata["userId"]
#             column=  " d.name, d.mobileNo, a.ambulanceId, a.ambulanceNo, a.lat, a.lng,SQRT(POW(69.1 * (a.lat - "+str(startlat)+"), 2) +POW(69.1 * ("+str(startlng)+" - a.lng) * COS(a.lat / 57.3), 2)) AS distance "
#             whereCondition= " and d.status=1 and a.onTrip=0 and a.onDuty=1 and a.driverId=d.id HAVING distance < 25 "
#             orderby="  distance "
#             nearByAmbulance=databasefile.SelectQueryOrderbyAsc("ambulanceMaster a, driverMaster d",column,whereCondition,"",orderby,"","")
            
#             if (nearByAmbulance!=0): 
                
#                 for i in range(0,len(nearByAmbulance["result"])):
#                     topic=nearByAmbulance["result"][i]["ambulanceId"]
#                     client.publish(str(topic), "Hello world11111111111111111")
                     

#                 return nearByAmbulance
#             else:
#                 nearByAmbulance["message"]="No Ambulance Found"
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



@app.route('/getNearAmbulance', methods=['POST'])
def getNearAmbulancetest():
    try:
        inputdata =  commonfile.DecodeInputdata(request.get_data())
        startlimit,endlimit="",""
        keyarr = ['startLocationLat','startLocationLong']
        commonfile.writeLog("getNearAmbulance",inputdata,0)
        msg = commonfile.CheckKeyNameBlankValue(keyarr,inputdata)
        if msg == "1":
            startlat ,startlng,userId= inputdata["startLocationLat"],inputdata["startLocationLong"],""#,inputdata["userId"]
            column=  "d.driverId, a.ambulanceTypeId,a.ambulanceModeId,d.name, d.mobileNo, a.ambulanceId, a.ambulanceNo, b.lat, b.lng,SQRT(POW(69.1 * (b.lat - "+str(startlat)+"), 2) +POW(69.1 * ("+str(startlng)+" - b.lng) * COS(b.lat / 57.3), 2)) AS distance "
            whereCondition= " and b.onTrip=0 and b.onDuty=1 and a.driverId=d.driverId  and b.ambulanceId=a.ambulanceId HAVING distance < 25 "
            orderby="  distance "
            nearByAmbulance=databasefile.SelectQueryOrderbyAsc("ambulanceMaster a, driverMaster d,ambulanceRideStatus as b",column,whereCondition,"",orderby,"","")
            print("nearByAmbulance================================",nearByAmbulance)
            nearByAmbulance["ambulanceTypeId"]=list(set([i["ambulanceTypeId"] for i in nearByAmbulance["result"]]))
            if (nearByAmbulance!=0):   
                #for i in nearByAmbulance["result"]: 
                    # topic=str(nearByAmbulance["result"][i]["ambulanceId"])+"/booking"
                    # print(nearByAmbulance["result"][i]["ambulanceId"]) 
                    # client.publish(topic, "Hello world11111111111111111")
                    # print("2222222222222")             
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






# @app.route('/getNearAmbulance1', methods=['POST'])
# def getNearAmbulance1():
#     try:
#         inputdata =  commonfile.DecodeInputdata(request.get_data())
#         startlimit,endlimit="",""

#         keyarr = ['startLocationLat','startLocationLong',"pickupLocationAddress",'dropLocationLat','dropLocationLong',"dropLocationAddress",]
#         commonfile.writeLog("getNearAmbulance",inputdata,0)
#         msg = commonfile.CheckKeyNameBlankValue(keyarr,inputdata)
#         if msg == "1":
#             startlat ,startlng,userId= inputdata["startLocationLat"],inputdata["startLocationLong"],""#,inputdata["userId"]
#             column=  " d.name, d.mobileNo, a.ambulanceId, a.ambulanceNo, a.lat, a.lng,SQRT(POW(69.1 * (a.lat - "+str(startlat)+"), 2) +POW(69.1 * ("+str(startlng)+" - a.lng) * COS(a.lat / 57.3), 2)) AS distance "
#             whereCondition= " and a.onTrip=0 and a.onDuty=1 and a.driverId=d.id HAVING distance < 1200 "
#             orderby="  distance "
#             nearByAmbulance=databasefile.SelectQueryOrderbyAsc("ambulanceMaster a, driverMaster d",column,whereCondition,"",orderby,"","")
            
#             if (nearByAmbulance!=0): 
#                 for i in nearByAmbulance["result"]: 
#                     topic=str(nearByAmbulance["result"][i]["ambulanceId"])+"/booking"
#                     print(nearByAmbulance["result"][i]["ambulanceId"]) 
#                     client.publish(topic, "Hello world11111111111111111")
#                     print("2222222222222")             
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


@app.route('/bookRide', methods=['POST'])
def bookRide():
    try:
        print('A')
        inputdata =  commonfile.DecodeInputdata(request.get_data())
        startlimit,endlimit="",""
        #inputdata={"ambulanceId":[1,2,3,4],"driverId":[13,14,15,16,17],'startLocationLat':28.583962,'startLocationLong':77.314345,"pickupLocationAddress":" Noida se 15",'dropLocationLat':28.535517,'dropLocationLong':77.391029,"dropLocationAddress":"fortis noida","userId":"8b0e338e522a11ea93d39ebd4d0189fc"}
        # inputdata1={}
        # inputdata1["pickupLocationAddress"]=inputdata["pickupLocationAddress"]
        # inputdata1["dropLocationAddress"]=inputdata["dropLocationAddress"]
        keyarr = ["ambulanceId","id",'startLocationLat','startLocationLong',"pickupLocationAddress",'dropLocationLat','dropLocationLong',"dropLocationAddress","userId"]
        for i in inputdata["driverId"]: 
            inputdata["driverId"]=str(i)
            print(inputdata)
            
            client = mqtt.Client()
            client.connect("localhost",1883,60)
            topic=str(i)+"/booking"
            print("=================",topic)
            client.publish(topic, str(inputdata))
            print("2222222222222") 
        return  {"result":"booking send","status":"True"}
    except KeyError as e:
        print("Exception---->" +str(e))        
        output = {"result":"Input Keys are not Found","status":"false"}
        return output    
    except Exception as e :
        print("Exception---->" +str(e))           
        output = {"result":"something went wrong","status":"false"}
        return output




@app.route('/acceptRide', methods=['POST'])
def acceptRide():
    try:
        print('A')
        inputdata =  commonfile.DecodeInputdata(request.get_data())
        startlimit,endlimit="",""
        #inputdata={"ambulanceId":3,"id":17,'startLocationLat':28.583962,'startLocationLong':77.314345,"pickupLocationAddress":" Noida se 15",'dropLocationLat':28.535517,'dropLocationLong':77.391029,"dropLocationAddress":"fortis noida","userId":"7795051055a111ea93d39ebd4d0189fc"}
        #id is driverid
        print("1111")
        keyarr = ["driverId",'startLocationLat','startLocationLong',"pickupLocationAddress",'dropLocationLat','dropLocationLong',"dropLocationAddress","userId"]
        
        print("2")
        if "ambulanceId" in inputdata:
                if inputdata['ambulanceId'] != "":
                    ambulanceId =str(inputdata["ambulanceId"])
        else:
            columns=" ambulanceId "
            whereCondition22=" driverId= '"+str(inputdata["driverId"])+"'"
            ambulanceId= databasefile.SelectQuery(" ambulanceMaster ",columns,whereCondition22)
            print(ambulanceId,"ambulanceId==========================")
            ambulanceId=ambulanceId["result"]["ambulanceId"]
        if "driverId" in inputdata:
                if inputdata['driverId'] != "":
                    driverId =str(inputdata["driverId"])
        if "startLocationLat" in inputdata:
                if inputdata['startLocationLat'] != "":
                    startLocationLat =(inputdata["startLocationLat"])
        if "startLocationLong" in inputdata:
                if inputdata['startLocationLong'] != "":
                    startLocationLong =(inputdata["startLocationLong"])
        if "pickupLocationAddress" in inputdata:
                if inputdata['pickupLocationAddress'] != "":
                    pickupLocationAddress =str(inputdata["pickupLocationAddress"])
        if "dropLocationLat" in inputdata:
                if inputdata['dropLocationLat'] != "":
                    dropLocationLat =(inputdata["dropLocationLat"])
        if "dropLocationLong" in inputdata:
                if inputdata['dropLocationLong'] != "":
                    dropLocationLong =(inputdata["dropLocationLong"])
        if "dropLocationAddress" in inputdata:
                if inputdata['dropLocationAddress'] != "":
                    dropLocationAddress =str(inputdata["dropLocationAddress"])

        if "userId" in inputdata:
            if inputdata['userId'] != "":
                userId =str(inputdata["userId"])

        print("3")
        bookingId = (commonfile.CreateHashKey(driverId,userId)).hex


        commonfile.writeLog("bookRide",inputdata,0)
        msg = commonfile.CheckKeyNameBlankValue(keyarr,inputdata)
        
        if msg == "1":
            print('B')
            columns="mobileNo,name"
            whereCondition22="  userId= '"+str(userId)+"' and userTypeId='2' "
            data1= databasefile.SelectQuery("userMaster",columns,whereCondition22)
            print(data1,'data1')
            usermobile=data1['result']['mobileNo']


            whereCondition222="  driverId= '"+str(driverId)+"' "
            data11= databasefile.SelectQuery("driverMaster",columns,whereCondition222)
            print(data11,'--data')
            driverName=data11['result']['name']
            drivermobile=data11['result']['mobileNo']
            
            R = 6373.0
            print(R,'R')
            fromlongitude2= (startLocationLong)
            print(fromlongitude2,'fromlong',type(fromlongitude2))
            fromlatitude2 = startLocationLat
            # print(fromlongitude2,'fromlong')
            print('lat',fromlatitude2)
            distanceLongitude = dropLocationLong - fromlongitude2
            distanceLatitude = dropLocationLat - fromlatitude2
            a = sin(distanceLatitude / 2)**2 + cos(fromlatitude2) * cos(dropLocationLat) * sin(distanceLongitude / 2)**2
            c = 2 * atan2(sqrt(a), sqrt(1 - a))
            distance = R * c
            distance2=distance/100
            Distance=distance2*1.85
            d=round(Distance)
            d2 =str(d) +' Km'


            finalAmount= d * 11+11
            print(finalAmount,'final')




            #insertdata
            columnqq='userMobile,driverMobile,pickup,pickupLatitude,pickupLongitude,dropoff,dropOffLatitude,dropOffLongitude,ambulanceId,userId,driverId,bookingId,totalDistance,finalAmount'
            values111 = " '"+ str(usermobile) +"','" + str(drivermobile)+"','" + str(pickupLocationAddress)+"','" + str(startLocationLat) +"','" + str(startLocationLong) + "','" + str(dropLocationAddress) + "','" + str(dropLocationLat) 
            values111=values111+"','" + str(dropLocationLong)+"','" + str(ambulanceId)+"','" + str(userId) +"','" + str(driverId) + "','" + str(bookingId)+ "','" + str(d2) + "','" + str(finalAmount)+"'"
            data111=databasefile.InsertQuery('bookAmbulance',columnqq,values111)
            print(data111,'==data')
            
            columns="(ar.lat)ambulanceLat,(ar.lng)ambulanceLng, bm.ambulanceId,bm.bookingId,bm.driverId,bm.dropOff,bm.dropOffLatitude,bm.dropOffLongitude"
            columns=columns+",bm.finalAmount,bm.pickup,bm.pickupLatitude,bm.pickupLongitude,bm.totalDistance,bm.userMobile,am.ambulanceNo "
            columns=columns+",bm.driverMobile"
            whereCondition22=" am.ambulanceId=bm.ambulanceId  and bookingId= '"+str(bookingId)+"'"
            bookingDetails= databasefile.SelectQuery("bookAmbulance bm,ambulanceMaster am,ambulanceRideStatus ar",columns,whereCondition22)
            print(bookingDetails,"================")
            bookingDetails["result"]["driverName"]=driverName
            if (bookingDetails!='0'):  
                print('Entered')
                client = mqtt.Client()
                client.connect("localhost",1883,60)
                topic=str(userId)+"/booking"
                client.publish(topic, str(bookingDetails)) 
                #bookRide["message"]="ride booked Successfully" 
                return bookingDetails
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


@app.route('/driverArrive', methods=['POST'])
def driverArriver():
    try:
        inputdata =  commonfile.DecodeInputdata(request.get_data())
        startlimit,endlimit="",""
        keyarr = ["ambulanceId","bookingId","userId"]
        commonfile.writeLog("endRide",inputdata,0)
        msg = commonfile.CheckKeyNameBlankValue(keyarr,inputdata)
        if msg == "1":
            if "ambulanceId" in inputdata:
                if inputdata['ambulanceId'] != "":
                    ambulanceId =(inputdata["ambulanceId"])
            if "bookingId" in inputdata:
                    if inputdata['bookingId'] != "":
                        bookingId =str(inputdata["bookingId"])

            if "userId" in inputdata:
                if inputdata['userId'] != "":
                    userId =str(inputdata["userId"])
            
            whereCondition=" ambulanceId= '"+ str(ambulanceId)+"' and bookingId='"+ str(bookingId)+"'"
            column=" status=1 "
            bookRide=databasefile.UpdateQuery("bookAmbulance",column,whereCondition)
            whereCondition222=  " ambulanceId= '"+ str(ambulanceId)+"' "
            columns= "onTrip=1 and onDuty=1"
            bookRide1=databasefile.UpdateQuery("ambulanceRideStatus",columns,whereCondition222)
            if (bookRide!=0):   
                bookRide["message"]="Driver has arrived at your location"             
                topic=str(userId)+"/arrive"
                client.publish(topic, str(bookingDetails)) 
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


@app.route('/startRide', methods=['POST'])
def startRide():
    try:
        inputdata =  commonfile.DecodeInputdata(request.get_data())
        startlimit,endlimit="",""
        keyarr = ["ambulanceId","bookingId","userId"]
        commonfile.writeLog("endRide",inputdata,0)
        msg = commonfile.CheckKeyNameBlankValue(keyarr,inputdata)
        if msg == "1":
            if "ambulanceId" in inputdata:
                if inputdata['ambulanceId'] != "":
                    ambulanceId =(inputdata["ambulanceId"])
            if "bookingId" in inputdata:
                    if inputdata['bookingId'] != "":
                        bookingId =str(inputdata["bookingId"])

            if "userId" in inputdata:
                if inputdata['userId'] != "":
                    userId =str(inputdata["userId"])
            
            whereCondition=" ambulanceId= '"+ str(ambulanceId)+"' and bookingId='"+ str(bookingId)+"'"
            column=" status=1 "
            bookRide=databasefile.UpdateQuery("bookAmbulance",column,whereCondition)
            whereCondition222=  " ambulanceId= '"+ str(ambulanceId)+"' "
            columns= "onTrip=1 and onDuty=1"
            bookRide1=databasefile.UpdateQuery("ambulanceRideStatus",columns,whereCondition222)
            if (bookRide!=0):   
                bookRide["message"]="ride started Successfully"             
                topic=str(userId)+"/startRide"
                client.publish(topic, str(bookingDetails)) 
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



@app.route('/ActiveTrip', methods=['POST'])
def ActiveTrip():
    try:
        inputdata =  commonfile.DecodeInputdata(request.get_data())
        startlimit,endlimit="",""
       
        commonfile.writeLog("endRide",inputdata,0)
        msg="1"
        if msg == "1":
            if "startLimit" in inputdata:
                if inputdata['startLimit'] != "":
                    startlimit =str(inputdata["startLimit"])
                
            if "endLimit" in inputdata:
                if inputdata['endLimit'] != "":
                    endlimit =str(inputdata["endLimit"])

            whereCondition=" and  bm.status=1  and bm.userMobile=um.mobileNo and bm.driverId=dm.id "

            column="bm.userMobile,bm.bookingId,bm.pickup as tripFrom,bm.dropOff as tripTo,date_format(bm.ateCreate,'%Y-%m-%d %H:%i:%s')startTime,dm.name as driverName,um.name as userName"
            data=databasefile.SelectQuery2("bookAmbulance as bm,userMaster as um,driverMaster as dm",column,whereCondition,"",startlimit,endlimit)
            print(data,"______________")
           
            if (data['status']!='false'): 
                Data = {"result":data['result'],"status":"true","message":""}

                          
                return Data
            else:
                
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

@app.route('/CompeltedTrip', methods=['POST'])
def CompeltedTrip():
    try:
        inputdata =  commonfile.DecodeInputdata(request.get_data())
        startlimit,endlimit="",""
       
        commonfile.writeLog("endRide",inputdata,0)
        msg="1"
        if msg == "1":
            if "startLimit" in inputdata:
                if inputdata['startLimit'] != "":
                    startlimit =str(inputdata["startLimit"])
                
            if "endLimit" in inputdata:
                if inputdata['endLimit'] != "":
                    endlimit =str(inputdata["endLimit"])

            whereCondition=" and bm.status=2  and bm.userMobile=um.mobileNo and bm.driverId=dm.id "

            column="bm.userMobile,bm.bookingId,bm.pickup as tripFrom,bm.dropOff as tripTo,date_format(bm.ateCreate,'%Y-%m-%d %H:%i:%s')startTime,dm.name as driverName,um.name as userName"
            data=databasefile.SelectQuery2("bookAmbulance as bm,userMaster as um,driverMaster as dm",column,whereCondition,"",startlimit,endlimit)
            print(data,"---------------------------------")
           
            if (data['status']!='false'): 
                Data = {"result":data['result'],"status":"true","message":""}

                          
                return Data
            else:
                
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

@app.route('/bookedTrip', methods=['POST'])
def bookedTrip():
    try:
        inputdata =  commonfile.DecodeInputdata(request.get_data())
        print(inputdata)
        startlimit,endlimit="",""

        msg = commonfile.CheckKeyNameBlankValue("",inputdata)
        
        if msg == "1":
            if "startLimit" in inputdata:
                if inputdata['startLimit'] != "":
                    startlimit =str(inputdata["startLimit"])
                
            if "endLimit" in inputdata:
                if inputdata['endLimit'] != "":
                    endlimit =str(inputdata["endLimit"])

            whereCondition=" and bm.status=0 and bm.userMobile=um.mobileNo and bm.driverId=dm.id "

            column="bm.userMobile,bm.bookingId,bm.pickup as tripFrom,bm.dropOff as tripTo,date_format(bm.ateCreate,'%Y-%m-%d %H:%i:%s')startTime,dm.name as driverName,um.name as userName"
            data=databasefile.SelectQuery2("bookAmbulance as bm,userMaster as um,driverMaster dm",column,whereCondition,"",startlimit,endlimit)
            print(data,"-------------------------------")
           
            if (data['status']!='false'):
                print("Data",data) 
                # Data = {"result":data['result'],"status":"true","message":""}                          
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


@app.route('/cancelledTrip', methods=['POST'])
def CancelledTrip():
    try:
        inputdata =  commonfile.DecodeInputdata(request.get_data())
        startlimit,endlimit="",""
       
        commonfile.writeLog("endRide",inputdata,0)
        msg="1"
        if msg == "1":
            if "startLimit" in inputdata:
                if inputdata['startLimit'] != "":
                    startlimit =str(inputdata["startLimit"])
                
            if "endLimit" in inputdata:
                if inputdata['endLimit'] != "":
                    endlimit =str(inputdata["endLimit"])


            whereCondition="  and bm.status=3  and bm.userMobile=um.mobileNo and bm.driverId=dm.id "

            column="bm.userMobile,bm.bookingId,bm.pickup as tripFrom,bm.dropOff as tripTo,date_format(bm.ateCreate,'%Y-%m-%d %H:%i:%s')startTime,dm.name as driverName,um.name as userName"
            data=databasefile.SelectQuery2("bookAmbulance as bm,userMaster as um,driverMaster as dm",column,whereCondition,"",startlimit,endlimit)
            print(data,"--------------------------------------------------")
           
            if (data['status']!='false'): 
                Data = {"result":data['result'],"status":"true","message":""}

                          
                return Data
            else:
                
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
            columns= "onTrip=0 and onDuty=1"
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
            userId=inputdata['userId']
            whereCondition=" ambulanceId= '"+ str(ambulanceId)+"' and bookingId='"+ str(bookingId)+"' and  canceledUserId='"+ str(userId)+"'"
            column=" status=3"
            bookRide=databasefile.UpdateQuery("bookAmbulance",column,whereCondition)
            whereCondition222=  " ambulanceId= '"+ str(ambulanceId)+"' "
            columns= "onTrip=0 and onDuty=1"
            bookRide1=databasefile.UpdateQuery("ambulanceRideStatus",columns,whereCondition222)
            if (bookRide!=0):   
                bookRide["message"]="ride Cancelled Successfully"             
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
        keyarr = ["ambulanceId"]
        commonfile.writeLog("driverLeave",inputdata,0)
        msg = commonfile.CheckKeyNameBlankValue(keyarr,inputdata)
        if msg == "1":
            ambulanceId= inputdata["ambulanceId"]
            whereCondition222=  " ambulanceId= '"+ str(ambulanceId)+"'"
            columns= "onDuty=0"
            bookRide1=databasefile.UpdateQuery("ambulanceRideStatus",columns,whereCondition222)
            print(bookRide1,'bookride')
            if (bookRide1!="0"):   
                bookRide1["message"]="Leave taken Successfully"             
                return bookRide1
            else:
                
                return bookRide1
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


@app.route('/dashboard', methods=['POST'])
def dashboard():
    try:
        msg = "1"
        if msg =="1":
            startlimit,endlimit="0","5"
            WhereCondition=" and dm.driverId = um.userId"
            orderby=" driverId "

            inputdata =  commonfile.DecodeInputdata(request.get_data())  
           

            if "driverId" in inputdata:
                if inputdata['driverId'] != "":
                    driverId =str(inputdata["driverId"])
                    WhereCondition = WhereCondition + " and dm.id= "+str(driverId)+ " "

            column="dm.name,dm.mobileNo,dm.profilePic,am.ambulanceNo,am.ambulanceId,um.email,ars.lat,ars.lng,ars.onDuty,ars.onTrip,dm.currentLocation as address,date_format(dm.dateCreate,'%Y-%m-%d %H:%i:%s')joiningDate,dm.status as status,dm.driverId as driverId"
            whereCondition=" and dm.driverId=am.driverId  and am.ambulanceId=ars.ambulanceId  and dm.status<>'2' " + WhereCondition
            data=databasefile.SelectQuery2("driverMaster as dm,ambulanceMaster as am,ambulanceRideStatus as ars,userMaster um",column,whereCondition,"",startlimit,endlimit)
            print(data)

            whereCondition2392="   bm.status=3  and bm.userMobile=um.mobileNo and bm.driverId=dm.id "

            column2392="count(*) as count"
            cancelledTrip=databasefile.SelectQuery1("bookAmbulance as bm,userMaster as um,driverMaster as dm",column2392,whereCondition2392)
            if (cancelledTrip!=0):
                y=cancelledTrip[0]['count']


            else:
                y=0

            whereCondition23921="   bm.status=0  and bm.userMobile=um.mobileNo and bm.driverId=dm.id "

            column23921="count(*) as count"
            bookedTrip=databasefile.SelectQuery1("bookAmbulance as bm,userMaster as um,driverMaster as dm",column23921,whereCondition23921)
            if (bookedTrip!=0):
                y2=bookedTrip[0]['count']


            else:
                y2=0  

            

            whereCondition239212="  "
            y3=0

            column239212="finalAmount"
            bookedTrip1=databasefile.SelectQuery4("bookAmbulance ",column239212,whereCondition239212)
            if (bookedTrip1!=0):
                for i in bookedTrip1:
                    y3+=int(i['finalAmount'])
                    print(i['finalAmount'])


            else:
                y3=0  

            

            whereCondition239214="   usertypeId='2' "

            column239214="count(*) as count"
            bookedTrip2=databasefile.SelectQuery1("userMaster",column239214,whereCondition239214)
            if (bookedTrip2!=0):
                y4=bookedTrip2[0]['count']


            else:
                y4=0       

            
            
           

            
            if (data!=0):
                y2=len(data['result'])
                if y2 ==1:
                    print('111111111111111')
                    ambulanceId1=data['result'][0]['ambulanceId']

                    if data['result'][0]["profilePic"]==None:
                        data['result'][0]["profilePic"]=str(ConstantData.GetBaseURL())+"/profilePic/profilePic.jpg" 

                    d1=data['result'][0]['driverId']
                    print(ambulanceId1)
                    columns2="am.ambulanceFilepath,am.ambulanceTypeId,um.email,am.ambulanceModeId,am.ambulanceFilename,atm.ambulanceType  as ambulanceType,AM.ambulanceType  as category,am.ambulanceRegistrationFuel as fuelType,am.color,am.transportModel,am.transportType"
                    whereCondition222="  am.ambulanceId=ars.ambulanceId and atm.id=am.ambulanceTypeId and AM.id=am.ambulanceModeId and am.ambulanceId="+str(ambulanceId1)+ ""
                    data111=databasefile.SelectQuery('ambulanceMaster as am,ambulanceRideStatus as ars,ambulanceTypeMaster as atm,userMaster um,ambulanceMode as AM',columns2,whereCondition222)
                    y2=data111['result']
                    print(y2)
                    column2222="dlNo,dlFrontFilename,dlFrontFilepath,dlBackFilename,dlBackFilepath,pIDType,pIDNo,pIDFrontFilename,pIDFrontFilepath,pIDBackFilename,pIDBackFilepath"
                    whereCondition2222=" id = "+str(d1)+ " "
                    data11111=databasefile.SelectQuery('driverMaster',column2222,whereCondition2222)
                    y3=data11111['result']
                    data['result'][0].update(y2)
                    data['result'][0].update(y3)

                    Data = {"result":data['result'],"status":"true","message":""}
                    return Data

                else:
                    for i in data['result']:
                        if i["profilePic"]==None:
                            print('1111111111111111111')
                            i["profilePic"]=str(ConstantData.GetBaseURL())+"/profilePic/profilePic.jpg"  
                        
                        ambulanceId2= i['ambulanceId']
                        columns99="count(*) as count"
                        whereCondition88= " ambulanceId='"+str(ambulanceId2)+ "'"
                        data122=databasefile.SelectQuery('bookAmbulance',columns99,whereCondition88)
                        if data122['status']!='false':
                            i['tripCount']=0
                        else:
                            tripcount=data122['result']['count']
                            i['tripCount']=tripcount

                    Data = {"result":{"driverDetails":data['result'],"dashboard":{"cancelledTripCount":y,"bookedTripCount":y2,"totalEarning":y3,"newsUsers":y4},"userReviews":"No data Available"},"status":"true","message":""}
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


@app.route('/updateDriverStatus', methods=['POST'])
def updateStatus():
    try:
        inputdata =  commonfile.DecodeInputdata(request.get_data())
        startlimit,endlimit="",""
        keyarr = ['driverId']
        print(inputdata,"B")
        commonfile.writeLog("updateDriverStatus",inputdata,0)
        msg = commonfile.CheckKeyNameBlankValue(keyarr,inputdata)
        if msg =="1":
          
            userId = int(inputdata["driverId"])
           
            column="status"
            whereCondition= "   id = " + str(userId)+ " "
            data=databasefile.SelectQuery1("driverMaster",column,whereCondition)
            print(data)
            if (data !=0):
                if data[0]['status']==0:
                    print('111111111111111111')
                    column="status='1'"
                    whereCondition= "  id = " + str(userId)+ " "
                    output1=databasefile.UpdateQuery("driverMaster",column,whereCondition)
                    output=output1
                    if output!='0':
                        Data = {"status":"true","message":"","result":output["result"]}                  
                        return Data
                    else:
                        return commonfile.Errormessage() 

                else:
                    column="status='0'"
                    whereCondition= "  id = " + str(userId)+ " "
                    output1=databasefile.UpdateQuery("driverMaster",column,whereCondition)
                    output=output1    
                    if output!='0':
                        Data = {"status":"true","message":"","result":output["result"]}                  
                        return Data
                    else:
                        return commonfile.Errormessage()
            else:
                data={"result":"","status":"false","message":"No Data Found"}
                return data
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

@app.route('/updateDriver', methods=['POST'])
def updateDriver():
    try:
        print('Hello')
        inputdata=request.form.get('data')
        print(inputdata,'inputdata')
        keyarr = ['driverId']
        inputdata=json.loads(inputdata)
        # inputdata =  commonfile.DecodeInputdata(request.get_data()) 
        startlimit,endlimit="",""

        commonfile.writeLog("updateDriver",inputdata,0)
        msg = commonfile.CheckKeyNameBlankValue(keyarr,inputdata)
        print(msg,'msg')
       
        if msg == "1":
            name=inputdata['name']
            print(name,'name')
            mobileNo= inputdata["mobileNo"]
            print(mobileNo,'mobileNo')

            driverId=inputdata['driverId']
            column = " userId "
            whereCondition= " mobileNo='"+str(mobileNo)+ "' and usertypeId='3'"
            data= databasefile.SelectQuery("userMaster",column,whereCondition)

            # column2= " id as driverId,dlNo,dlFrontFilename,DlFrontPicPath,dlBackFilename,DlBackPicPath,PIDType,PIDNo,PIDFrontFilename,PIDFrontPicPath,PIDBackFilename,PIDBackPicPath"
            columns1="driverId"
            whereCondition2=" id='"+str(driverId)+ "' "

            data2=databasefile.SelectQuery('driverMaster',columns1,whereCondition2)
            address=""
            # DlNo=str(data['result']["dlNo"])


            DlNo,dlFrontFilename,DlFrontPicPath,dlBackFilename,DlBackPicPath,PIDType,PIDNo,PIDFrontFilename,PIDFrontPicPath,PIDBackFilename,PIDBackPicPath,TransportType,TransportModel,Color,AmbulanceRegistrationFuel,TypeNo,AIFilename,AIPicPath,AmbulanceModeId,AmbulanceId="","","","","","","","","","","","","","","","","","","",""

            if 'DlNo' in inputdata:
                DlNo=inputdata["DlNo"]

            if 'DlFrontImage' in request.files:
                    print("immmmmmmmmmmmmmmmm")
                    file = request.files.get('DlFrontImage')        
                    filename = file.filename or ''  
                    print(filename)               
                    dlFrontFilename= str(str(data['result']["userId"])+"Front"+".png")
                    
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
                    dlBackFilename=  str(str(data['result']["userId"])+"Back"+".png")
                  
                    DlBackFolderPath = ConstantData.GetdlImagePath(dlBackFilename)
                    DlBackfilepath = '/DLImage/' + dlBackFilename 
                    file.save(DlBackFolderPath)
                    DlBackPicPath = DlBackfilepath
                    print(DlBackPicPath)


            if 'DlFrontImage' not  in request.files:
                inputdata4 = request.form.get('DlFrontImage')
                if inputdata5==ConstantData.GetBaseURL():
                    DlFrontPicPath=""
                else : 
                    index=re.search("/DLImage", inputdata5).start()
                    DlBackPicPath=""
                    DlBackPicPath=inputdata5[index:]
                        

            

            if 'DlBackImage' not  in request.files:
                inputdata4 = request.form.get('DlBackImage')
                if inputdata4==ConstantData.GetBaseURL():
                    DlBackPicPath=""
                else : 
                    index=re.search("/DLImage", inputdata4).start()
                    DlBackPicPath=""
                    DlBackPicPath=inputdata4[index:]
                        

            if 'PIDType' in inputdata:
                PIDType=inputdata["PIDType"]

            if 'PIDNo' in inputdata:
                PIDNo=inputdata["PIDNo"]

            if 'PIDFrontImage' in request.files:
                    print("immmmmmmmmmmmmmmmm")
                    file = request.files.get('PIDFrontImage')        
                    filename = file.filename or ''  
                    print(filename)               
                    PIDFrontFilename= str(str(data['result']["userId"])+"Front"+".png")
                  
                    print(PIDFrontFilename,'Changed_filename')
                    PIDFrontFolderPath = ConstantData.GetPIDImagePath(PIDFrontFilename)
                    PIDFrontfilepath = '/PIDImage/' + PIDFrontFilename 
                    file.save(PIDFrontFolderPath)
                    PIDFrontPicPath = PIDFrontfilepath
                    print(PIDFrontPicPath)


            if 'PIDFrontImage' not  in request.files:
                inputdata3 = request.form.get('PIDFrontImage')
                if inputdata3==ConstantData.GetBaseURL():
                    PIDFrontPicPath=""
                else : 
                    index=re.search("/PIDImage", inputdata3).start()
                    PIDFrontPicPath=""
                    PIDFrontPicPath=inputdata3[index:]
                    

            if 'PIDBackImage' in request.files:
                    print("immmmmmmmmmmmmmmmm")
                    file = request.files.get('PIDBackImage')        
                    filename = file.filename or ''  
                    print(filename)               
                    PIDBackFilename= str(str(data['result']["userId"])+"Back"+".png")
                  
                    PIDBackFolderPath = ConstantData.GetPIDImagePath(PIDBackFilename)
                    PIDBackfilepath = '/PIDImage/' + PIDBackFilename 
                    file.save(PIDBackFolderPath)
                    PIDBackPicPath = PIDBackfilepath
                    print(PIDBackPicPath)

            
            if 'PIDBackImage' not  in request.files:
                inputdata2 = request.form.get('PIDBackImage')
                if inputdata2==ConstantData.GetBaseURL():
                    PIDBackPicPath=""
                else : 
                    index=re.search("/PIDImage", inputdata2).start()
                    PIDBackPicPath=""
                    PIDBackPicPath=inputdata2[index:]



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

            if 'address' in inputdata:
                address=inputdata["address"]

            if 'status' in inputdata:
                status=inputdata["status"]
            



            if 'AmbulanceImage' in request.files:
                    print("immmmmmmmmmmmmmmmm")
                    file = request.files.get('AmbulanceImage')        
                    filename = file.filename or ''  
                    print(filename)               
                    AIFilename=  str(str(data['result']["userId"])+".png")
                   
                    AIFolderPath = ConstantData.GetAmbulanceImagePath(AIFilename)
                    AIfilepath = '/AmbulanceImage/' + AIFilename 
                    file.save(AIFolderPath)
                    AIPicPath = AIfilepath
                    print(AIPicPath)

            if 'AmbulanceImage' not  in request.files:
                inputdata1 = request.form.get('AmbulanceImage')
                if inputdata1==ConstantData.GetBaseURL():
                    AIPicPath=""
                else : 
                    index=re.search("/AmbulanceImage", inputdata1).start()
                    AIPicPath=""
                    AIPicPath=inputdata1[index:]

            if data['status']!='false':
                
                
                
                
                print('A')
                WhereCondition = " id = '" + str(driverId) + "'"
                column = " name='" + str(name) + "' ,mobileNo='" + str(mobileNo) + "' ,dlNo = '" + str(DlNo) + "',dlFrontFilename = '" + str(dlFrontFilename) + "',dlFrontFilepath = '" + str(DlFrontPicPath) + "',dlBackFilename = '" + str(dlBackFilename) + "',dlBackFilepath = '" + str(DlBackPicPath) + "'"
                
                column = column + " ,pIDType = '" + str(PIDType) + "',pIDNo = '" + str(PIDNo) + "',pIDFrontFilename = '" + str(PIDFrontFilename) + "',pIDFrontFilepath = '" + str(PIDFrontPicPath) + "',pIDBackFilename = '" + str(PIDBackFilename) + "',pIDBackFilepath = '" + str(PIDBackPicPath) + "',status='" + str(status) + "'"
                print(column,'column')
                data = databasefile.UpdateQuery("driverMaster",column,WhereCondition)


                #ambulanceMaster update


               
                columns="ambulanceId"
                WhereCondition = " driverId = '" + str(driverId) + "'"
                data111=databasefile.SelectQuery('ambulanceMaster',columns,WhereCondition)
                if data111['status'] == 'false':
                    
                    columns2= "ambulanceNo='" + str(AmbulanceNo) + ",transportType='" + str(TransportType) + "',transportModel='" + str(TransportModel) + "',color='" + str(Color) + "',ambulanceRegistrationFuel='" + str(AmbulanceRegistrationFuel) + "',typeNo='" + str(TypeNo) + "',ambulanceFilename='" + str(AIFilename) + "',ambulanceFilepath='" + str(AIPicPath) + "',ambulanceModeId='" + str(AmbulanceModeId) + "',ambulanceTypeId= '" + str(AmbulanceId) + "'"

                  
                    data122=databasefile.UpdateQuery("ambulanceMaster",columns2,whereCondition)
                    print(data122,'+++++++++++++++++++')
                    
                    

                    if data122 != "0":
                        data11={"result":"","message":"Inserted successfully","status":"true"}
                        return data11

                        
                        
                    else:
                        data11={"result":"","message":"Not existed  in data","status":"false"}
                        return data11


                        
               
        else:
            return msg
    except Exception as e :
        print("Exception---->" + str(e))    
        output = {"result":"something went wrong","status":"false"}
        return output


@app.route('/updateDriver1', methods=['POST'])
def updateDriver1():
    try:
        print('Hello')
        inputdata=request.form.get('data')
        print(inputdata,'inputdata')
        keyarr = ['driverId']
        inputdata=json.loads(inputdata)
        # inputdata =  commonfile.DecodeInputdata(request.get_data()) 
        startlimit,endlimit="",""

        commonfile.writeLog("updateDriver",inputdata,0)
        msg = commonfile.CheckKeyNameBlankValue(keyarr,inputdata)
        print(msg,'msg')
       
        if msg == "1":
            name=inputdata['name']
            print(name,'name')
            mobileNo= inputdata["mobileNo"]
            print(mobileNo,'mobileNo')

            driverId=inputdata['driverId']
            column = " userId "
            whereCondition= " mobileNo='"+str(mobileNo)+ "' and usertypeId='3'"
            data= databasefile.SelectQuery("userMaster",column,whereCondition)

            # column2= " id as driverId,dlNo,dlFrontFilename,DlFrontPicPath,dlBackFilename,DlBackPicPath,PIDType,PIDNo,PIDFrontFilename,PIDFrontPicPath,PIDBackFilename,PIDBackPicPath"
            columns1="driverId"
            whereCondition2=" id='"+str(driverId)+ "' "

            data2=databasefile.SelectQuery('driverMaster',columns1,whereCondition2)
            address=""
            # DlNo=str(data['result']["dlNo"])


            DlNo,dlFrontFilename,DlFrontPicPath,dlBackFilename,DlBackPicPath,PIDType,PIDNo,PIDFrontFilename,PIDFrontPicPath,PIDBackFilename,PIDBackPicPath,TransportType,TransportModel,Color,AmbulanceRegistrationFuel,TypeNo,AIFilename,AIPicPath,AmbulanceModeId,AmbulanceId="","","","","","","","","","","","","","","","","","","",""

            if 'DlNo' in inputdata:
                DlNo=inputdata["DlNo"]

            if 'DlFrontImage' in request.files:
                    print("immmmmmmmmmmmmmmmm")
                    file = request.files.get('DlFrontImage')        
                    filename = file.filename or ''  
                    print(filename)               
                    dlFrontFilename= str(str(data['result']["userId"])+"Front"+".png")
                    
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
                    dlBackFilename=  str(str(data['result']["userId"])+"Back"+".png")
                  
                    DlBackFolderPath = ConstantData.GetdlImagePath(dlBackFilename)
                    DlBackfilepath = '/DLImage/' + dlBackFilename 
                    file.save(DlBackFolderPath)
                    DlBackPicPath = DlBackfilepath
                    print(DlBackPicPath)


            if 'DlFrontImage' not  in request.files:
                inputdata4 = request.form.get('DlFrontImage')
                if inputdata5==ConstantData.GetBaseURL():
                    DlFrontPicPath=""
                else : 
                    index=re.search("/DLImage", inputdata5).start()
                    DlBackPicPath=""
                    DlBackPicPath=inputdata5[index:]
                        

            

            if 'DlBackImage' not  in request.files:
                inputdata4 = request.form.get('DlBackImage')
                if inputdata4==ConstantData.GetBaseURL():
                    DlBackPicPath=""
                else : 
                    index=re.search("/DLImage", inputdata4).start()
                    DlBackPicPath=""
                    DlBackPicPath=inputdata4[index:]
                        

            if 'PIDType' in inputdata:
                PIDType=inputdata["PIDType"]

            if 'PIDNo' in inputdata:
                PIDNo=inputdata["PIDNo"]

            if 'PIDFrontImage' in request.files:
                    print("immmmmmmmmmmmmmmmm")
                    file = request.files.get('PIDFrontImage')        
                    filename = file.filename or ''  
                    print(filename)               
                    PIDFrontFilename= str(str(data['result']["userId"])+"Front"+".png")
                  
                    print(PIDFrontFilename,'Changed_filename')
                    PIDFrontFolderPath = ConstantData.GetPIDImagePath(PIDFrontFilename)
                    PIDFrontfilepath = '/PIDImage/' + PIDFrontFilename 
                    file.save(PIDFrontFolderPath)
                    PIDFrontPicPath = PIDFrontfilepath
                    print(PIDFrontPicPath)


            if 'PIDFrontImage' not  in request.files:
                inputdata3 = request.form.get('PIDFrontImage')
                if inputdata3==ConstantData.GetBaseURL():
                    PIDFrontPicPath=""
                else : 
                    index=re.search("/PIDImage", inputdata3).start()
                    PIDFrontPicPath=""
                    PIDFrontPicPath=inputdata3[index:]
                    

            if 'PIDBackImage' in request.files:
                    print("immmmmmmmmmmmmmmmm")
                    file = request.files.get('PIDBackImage')        
                    filename = file.filename or ''  
                    print(filename)               
                    PIDBackFilename= str(str(data['result']["userId"])+"Back"+".png")
                  
                    PIDBackFolderPath = ConstantData.GetPIDImagePath(PIDBackFilename)
                    PIDBackfilepath = '/PIDImage/' + PIDBackFilename 
                    file.save(PIDBackFolderPath)
                    PIDBackPicPath = PIDBackfilepath
                    print(PIDBackPicPath)

            
            if 'PIDBackImage' not  in request.files:
                inputdata2 = request.form.get('PIDBackImage')
                if inputdata2==ConstantData.GetBaseURL():
                    PIDBackPicPath=""
                else : 
                    index=re.search("/PIDImage", inputdata2).start()
                    PIDBackPicPath=""
                    PIDBackPicPath=inputdata2[index:]



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

            if 'address' in inputdata:
                address=inputdata["address"]

            if 'status' in inputdata:
                status=inputdata["status"]
            



            if 'AmbulanceImage' in request.files:
                    print("immmmmmmmmmmmmmmmm")
                    file = request.files.get('AmbulanceImage')        
                    filename = file.filename or ''  
                    print(filename)               
                    AIFilename=  str(str(data['result']["userId"])+".png")
                   
                    AIFolderPath = ConstantData.GetAmbulanceImagePath(AIFilename)
                    AIfilepath = '/AmbulanceImage/' + AIFilename 
                    file.save(AIFolderPath)
                    AIPicPath = AIfilepath
                    print(AIPicPath)

            if 'AmbulanceImage' not  in request.files:
                inputdata1 = request.form.get('AmbulanceImage')
                if inputdata1==ConstantData.GetBaseURL():
                    AIPicPath=""
                else : 
                    index=re.search("/AmbulanceImage", inputdata1).start()
                    AIPicPath=""
                    AIPicPath=inputdata1[index:]

            if data['status']!='false':
                
                
                
                
                print('A')
                WhereCondition = " id = '" + str(driverId) + "'"
                column = " name='" + str(name) + "' ,mobileNo='" + str(mobileNo) + "' ,dlNo = '" + str(DlNo) + "',dlFrontFilename = '" + str(dlFrontFilename) + "',dlFrontFilepath = '" + str(DlFrontPicPath) + "',dlBackFilename = '" + str(dlBackFilename) + "',dlBackFilepath = '" + str(DlBackPicPath) + "'"
                
                column = column + " ,pIDType = '" + str(PIDType) + "',pIDNo = '" + str(PIDNo) + "',pIDFrontFilename = '" + str(PIDFrontFilename) + "',pIDFrontFilepath = '" + str(PIDFrontPicPath) + "',pIDBackFilename = '" + str(PIDBackFilename) + "',pIDBackFilepath = '" + str(PIDBackPicPath) + "',status='" + str(status) + "'"
                print(column,'column')
                data = databasefile.UpdateQuery("driverMaster",column,WhereCondition)


                #ambulanceMaster update


               
                columns="ambulanceId"
                WhereCondition = " driverId = '" + str(driverId) + "'"
                data111=databasefile.SelectQuery('ambulanceMaster',columns,WhereCondition)
                if data111['status'] == 'false':
                    
                    columns2= "ambulanceNo='" + str(AmbulanceNo) + ",transportType='" + str(TransportType) + "',transportModel='" + str(TransportModel) + "',color='" + str(Color) + "',ambulanceRegistrationFuel='" + str(AmbulanceRegistrationFuel) + "',typeNo='" + str(TypeNo) + "',ambulanceFilename='" + str(AIFilename) + "',ambulanceFilepath='" + str(AIPicPath) + "',ambulanceModeId='" + str(AmbulanceModeId) + "',ambulanceTypeId= '" + str(AmbulanceId) + "'"

                  
                    data122=databasefile.UpdateQuery("ambulanceMaster",columns2,whereCondition)
                    print(data122,'+++++++++++++++++++')
                    
                    

                    if data122 != "0":
                        data11={"result":"","message":"Inserted successfully","status":"true"}
                        return data11

                        
                        
                    else:
                        data11={"result":"","message":"Not existed  in data","status":"false"}
                        return data11


                        
               
        else:
            return msg
    except Exception as e :
        print("Exception---->" + str(e))    
        output = {"result":"something went wrong","status":"false"}
        return output        





@app.route('/deleteDriver', methods=['POST'])
def deleteDriver():
    try:
        inputdata =  commonfile.DecodeInputdata(request.get_data())
        startlimit,endlimit="",""
        keyarr = ['driverId']
        print(inputdata,"B")
        commonfile.writeLog("deleteDriver",inputdata,0)
        print('C')
        msg = commonfile.CheckKeyNameBlankValue(keyarr,inputdata)
        if msg =="1":
            
            userId=inputdata["driverId"]
            column="status=2"

            WhereCondition = "  id = '" + str(userId) + "' "
            data=databasefile.UpdateQuery("driverMaster",column,WhereCondition)
           

            if data != "0":
                data= {"status":"true","message":"Deleted Successfully","result":""}
                return data
            else:
                return commonfile.Errormessage()
        else:
            return msg

    except Exception as e :
        print("Exception--->" + str(e))                                  
        return commonfile.Errormessage()




@app.route('/deleteHospital', methods=['POST'])
def deleteHospital():
    try:
        inputdata =  commonfile.DecodeInputdata(request.get_data())
        startlimit,endlimit="",""
        keyarr = ['id']
        print(inputdata,"B")
        commonfile.writeLog("deleteHospital",inputdata,0)
        print('C')
        msg = commonfile.CheckKeyNameBlankValue(keyarr,inputdata)
        if msg =="1":
            
            userId=int(inputdata["id"])
            column="status=2"

            WhereCondition = "  id = " + str(userId) + " "
            data=databasefile.UpdateQuery("hospitalMaster",column,WhereCondition)
           

            if data != "0":
                data= {"status":"true","message":"Deleted Successfully","result":""}
                return data
            else:
                return commonfile.Errormessage()
        else:
            return msg

    except Exception as e :
        print("Exception--->" + str(e))                                  
        return commonfile.Errormessage()













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






@app.route('/notification', methods=['POST'])
def notification2():
    try:
        inputdata =  commonfile.DecodeInputdata(request.get_data())
        startlimit,endlimit="",""
        keyarr = ['userId']
        userId = inputdata["userId"]
        column=  " deviceKey "
        whereCondition= " userId = '" + str(userId) + "' "
        deviceKey=databasefile.SelectQuery("userMaster",column,whereCondition)
        deviceKey=deviceKey["result"]["deviceKey"]
        a = notification.notification(deviceKey)
        return a
    except Exception as e :
        print("Exception--->" + str(e))                                  
        return commonfile.Errormessage()


if __name__ == "__main__":
    CORS(app, support_credentials=True)
    app.run(host='0.0.0.0',port=5077,debug=True)
    socketio.run(app)        
