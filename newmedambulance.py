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







# client = mqtt.Client()
# client.connect("localhost",1883,60)



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
            imeiNo,country,city,deviceName,devicekey,deviceType="","","","","",""
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
            column22='userTypeId'
            
            WhereCondition = " mobileNo = '" + str(mobileNo) + "'"
            count = databasefile.SelectQuery("userMaster",column22,WhereCondition)
            
            if count['status']!='false':
                if (count['result']['userTypeId'] == '2') or (count['result']['userTypeId'] == 2)  :
                    WhereCondition = " mobileNo = '" + str(mobileNo) + "'"
                    column = " otp = '" + str(otp)  + "'"
                    updateOtp = databasefile.UpdateQuery("userMaster",column,WhereCondition)
                    print(updateOtp,'updatedata')
                    if updateOtp != "0":
                        column = '*'
                       
                        data = databasefile.SelectQuery("userMaster",column,WhereCondition)                  
                        data1={"result":data['result'],"message":"","status":"true"}
                        return data1
                if (count['result']['userTypeId'] == '3') or (count['result']['userTypeId'] == 3):
                    data={"result":"","status":"false","message":"You already signedUp as a driver"}
                    return data
                else:
                    data={"result":"","status":"false","message":"You already signedUp as a responder"}
                    return data
                   
                
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


                if 'devicekey' in inputdata:
                    deviceKey=inputdata["devicekey"]
                    column=column+" ,devicekey"
                    values=values+"','"+str(deviceKey)

                
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
                    WhereCondition = " mobileNo = '" + str(mobileNo) + "'"
                    
                    data111 = databasefile.SelectQuery("userMaster",column,WhereCondition)
                    print(data111,"@@@@@@@@@@@@@@@@@@@@@@@@")
                    Data = {"status":"true","message":"","result":data111['result']}                  
                    return Data
                else:
                    return commonfile.Errormessage()
                        
        else:
            return msg 
    except Exception as e :
        print("Exception---->" +str(e))           
        output = {"status":"false","message":"something went wrong","result":""}
        return output



@app.route('/driverSignup', methods=['POST'])
def driverSignup():
    try:
        inputdata =  commonfile.DecodeInputdata(request.get_data()) 
        startlimit,endlimit="",""
        keyarr = ['mobileNo']
        commonfile.writeLog("driverSignup",inputdata,0)
        msg = commonfile.CheckKeyNameBlankValue(keyarr,inputdata)
       
        if msg == "1":
            
            column,values="",""
            deviceKey=""

            
           
            
            mobileNo=inputdata["mobileNo"]
            email=inputdata['email']
            
            if 'deviceKey' in inputdata:
                deviceKey=inputdata["deviceKey"]
            
            usertypeId="3"
            
          
            
            digits = "0123456789"
            otp = " "
            for i in range(4):
                otp += digits[math.floor(random.random() * 10)]

           

            UserId = (commonfile.CreateHashKey(mobileNo,usertypeId)).hex
            column22='userTypeId'
            
            WhereCondition = "  mobileNo = '" + str(mobileNo) + "' "
            count = databasefile.SelectQuery("userMaster",column22,WhereCondition)
            
            if count['status']!='false':
                if (count['result']['userTypeId'] == '3') or (count['result']['userTypeId'] == 3):
                    WhereCondition = " mobileNo = '" + str(mobileNo) + "'"
                    column = " otp = '" + str(otp)  + "'"
                    updateOtp = databasefile.UpdateQuery("userMaster",column,WhereCondition)
                    print(updateOtp,'updatedata')
                    if updateOtp != "0":
                        column = '*'
                       
                        data = databasefile.SelectQuery("userMaster",column,WhereCondition)                  
                        data1={"result":data['result'],"message":"","status":"true"}
                        return data1
                
                if (count['result']['userTypeId'] == '2') or (count['result']['userTypeId'] == 2):
                    data={"result":"","status":"false","message":"You already signedUp as a user"}
                    return data
                else:
                    data={"result":"","status":"false","message":"You already signedUp as a responder"}
                    return data
                   
                
            else:
               

                if 'email' in inputdata:
                    email=inputdata["email"]
                    column=column+" ,email"
                    values=values+"','"+str(email)
                if 'password' in inputdata:
                    password=inputdata["password"]
                    column=column+" ,password"
                    values=values+"','"+str(password)
                if 'name' in inputdata:
                    name=inputdata["name"]
                    column=column+" ,name"
                    values=values+"','"+str(name)



 
                currentLocationlatlong=""

                column="mobileNo,userId,otp,userTypeId,deviceKey"+column
                
                
                values=  "'"+str(mobileNo)+"','"+str(UserId)+"','"+str(otp)+"','"+str('3')+"','"+str(deviceKey)+values+ "'"
                data=databasefile.InsertQuery("userMaster",column,values)
             

                if data != "0":
                    column = '*'
                    
                    data = databasefile.SelectQuery("userMaster",column,WhereCondition)
                    print(data)
                    Data = {"status":"true","message":"","result":data['result']}                  
                    return Data
                else:
                    return commonfile.Errormessage()
                        
        else:
            return msg 
    except Exception as e :
        print("Exception---->" +str(e))           
        output = {"status":"false","message":"something went wrong","result":""}
        return output

@app.route('/driverLogin', methods=['POST'])
def driverlogin():
    try:
        inputdata =  commonfile.DecodeInputdata(request.get_data())
        startlimit,endlimit="",""
        keyarr = ['password','mobileNo']
        commonfile.writeLog("driverLogin",inputdata,0)
        msg = commonfile.CheckKeyNameBlankValue(keyarr,inputdata)
        if msg == "1":
            mobileNo = inputdata["mobileNo"]
            password = inputdata["password"]
            column=  "us.mobileNo,us.name,um.usertype,us.userId,us.userTypeId,us.status"
            whereCondition= "us.mobileNo = '" + str(mobileNo) + "' and us.password = '" + str(password) + "'  and  us.userTypeId=um.Id"
            loginuser=databasefile.SelectQuery("userMaster as us,usertypeMaster as um",column,whereCondition)
            print(loginuser)
            if (loginuser['status']!='false'):
                if (loginuser['result']['userTypeId'] == 3) or (loginuser['result']['userTypeId']=='3'):
                    Data = {"result":loginuser['result'],"message":"","status":"true"}                  
                    return Data
                if (loginuser['result']['userTypeId'] == 2) or (loginuser['result']['userTypeId']=='2'):
                    Data = {"result":"","message":"you are not driver,Please go to user ","status":"true"}                  
                    return Data
                else:
                    Data = {"result":"","message":"you are not driver,Please go to responder ","status":"true"}                  
                    return Data

            else:
                data={"status":"false","message":"Please enter correct password & mobileNo or either you are not a driver","result":"Login Failed"}
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








@app.route('/responderSignup', methods=['POST'])
def responderSignup():
    try:
        inputdata =  commonfile.DecodeInputdata(request.get_data()) 
        startlimit,endlimit="",""
        keyarr = ['mobileNo']
        commonfile.writeLog("responderSignup",inputdata,0)
        msg = commonfile.CheckKeyNameBlankValue(keyarr,inputdata)
       
        if msg == "1":
            
            column,values="",""
            deviceKey=""

            
           
            
            mobileNo=inputdata["mobileNo"]
            
            if 'deviceKey' in inputdata:
                deviceKey=inputdata["deviceKey"]
            
            usertypeId="4"
            
          
            
            digits = "0123456789"
            otp = " "
            for i in range(4):
                otp += digits[math.floor(random.random() * 10)]

           

            UserId = (commonfile.CreateHashKey(mobileNo,usertypeId)).hex
            column22='userTypeId'
            
            WhereCondition = "  mobileNo = '" + str(mobileNo) + "'"
            count = databasefile.SelectQuery("userMaster",column22,WhereCondition)
            
            if count['status']!='false':
                if (count['result']['userTypeId'] == '4') or (count['result']['userTypeId'] == 4):
                    WhereCondition = " mobileNo = '" + str(mobileNo) + "'"
                    column = " otp = '" + str(otp)  + "'"
                    updateOtp = databasefile.UpdateQuery("userMaster",column,WhereCondition)
                    print(updateOtp,'updatedata')
                    if updateOtp != "0":
                        column = '*'
                       
                        data = databasefile.SelectQuery("userMaster",column,WhereCondition)                  
                        data1={"result":data['result'],"message":"","status":"true"}
                        return data1
                if (count['result']['userTypeId'] == '2') or (count['result']['userTypeId'] == 2):
                    data={"result":"","status":"false","message":"You already signedUp as a user"}
                    return data
                else:
                    data={"result":"","status":"false","message":"You already signedUp as a driver"}
                    return data

                   
                
            else:
               

                if 'email' in inputdata:
                    email=inputdata["email"]
                    column=column+" ,email"
                    values=values+"','"+str(email)
                if 'password' in inputdata:
                    password=inputdata["password"]
                    column=column+" ,password"
                    values=values+"','"+str(password)
                if 'name' in inputdata:
                    name=inputdata["name"]
                    column=column+" ,name"
                    values=values+"','"+str(name)



 
                currentLocationlatlong=""

                column="mobileNo,userId,otp,userTypeId,deviceKey"+column
                
                
                values=  "'"+str(mobileNo)+"','"+str(UserId)+"','"+str(otp)+"','"+str('3')+"','"+str(deviceKey)+values+ "'"
                data=databasefile.InsertQuery("userMaster",column,values)
             

                if data != "0":
                    column = '*'
                    
                    data = databasefile.SelectQuery("userMaster",column,WhereCondition)
                    print(data)
                    Data = {"status":"true","message":"","result":data['result']}                  
                    return Data
                else:
                    return commonfile.Errormessage()
                        
        else:
            return msg 
    except Exception as e :
        print("Exception---->" +str(e))           
        output = {"status":"false","message":"something went wrong","result":""}
        return output

@app.route('/responderLogin', methods=['POST'])
def responderLogin():
    try:
        inputdata =  commonfile.DecodeInputdata(request.get_data())
        startlimit,endlimit="",""
        keyarr = ['password','mobileNo']
        commonfile.writeLog("responderLogin",inputdata,0)
        msg = commonfile.CheckKeyNameBlankValue(keyarr,inputdata)
        if msg == "1":
            mobileNo = inputdata["mobileNo"]
            password = inputdata["password"]
            column=  "us.mobileNo,us.name,um.usertype,us.userId,us.userTypeId"
            whereCondition= "us.mobileNo = '" + str(mobileNo) + "' and us.password = '" + str(password) + "'  and  us.userTypeId=um.Id"
            loginuser=databasefile.SelectQuery("userMaster as us,usertypeMaster as um",column,whereCondition)
            if (loginuser['status']!='false'):
                if (loginuser['result']['userTypeId'] == 4) or (loginuser['result']['userTypeId']=='4'):
                    Data = {"result":loginuser,"message":"","status":"true"}                  
                    return Data
                if (loginuser['result']['userTypeId'] == 2) or (loginuser['result']['userTypeId']=='2'):
                    Data = {"result":"","message":"you are not driver,Please go to user ","status":"true"}                  
                    return Data
                else:
                    Data = {"result":"","message":"you are not driver,Please go to Driver ","status":"true"}                  
                    return Data

            else:
                data={"status":"false","message":"Please enter correct password & mobileNo or either you are not a responder","result":"Login Failed"}
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

            column="mobileNo,otp,userTypeId,userId,deviceKey"
            whereCondition= "  otp='" + otp+ "' and mobileNo='" + mobileNo+"'"
            verifyOtp=databasefile.SelectQuery(" userMaster ",column,whereCondition)
            print("verifyOtp======",verifyOtp)
            if  (verifyOtp["status"]!="false") or verifyOtp!=None:
                v=verifyOtp['result']['userId']
                print(v)
                v2=verifyOtp['result']['userTypeId']
                print(v2,"+++++++++++++++=")
                print(type(v2))
                if (v2 == '3' ) or ( v2== '4'):
                    print('+++++++++++++++++++===')
                    column='status'
                    whereCondition2=" driverId='"+str(v)+"'"
                    driverstatus=databasefile.SelectQuery('driverMaster',column,whereCondition2)
                    if driverstatus['status']!='false':
                        print(driverstatus['result'],"++++++++++++++++++++++")
                        y=driverstatus['result']
                        verifyOtp['result'].update(y)
                        return verifyOtp
                    else:
                        print('qqqqqqqqqqqqqqqqqqqqqqqqqqqq')
                        r={'status':0}
                        verifyOtp['result'].update(r)
                        return verifyOtp    
                else:
                    print('111')
                    r={'status':0}
                    verifyOtp['result'].update(r)

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


@app.route('/userProfile', methods=['POST'])
def userProfile():
    try:
        inputdata =  commonfile.DecodeInputdata(request.get_data()) 
        startlimit,endlimit="",""
        keyarr = ['userId']
        commonfile.writeLog("userProfile",inputdata,0)
        msg = commonfile.CheckKeyNameBlankValue(keyarr,inputdata)
       
        if msg == "1":
            
        

            
            
            if 'userId' in inputdata:
                userId=inputdata["userId"]    
                
            
            whereCondition= " userId= '"+str(userId)+"' and userTypeId='2' "
            column='userId,name,mobileNo,password,email'

            
         
            data11=databasefile.SelectQuery('userMaster',column,whereCondition)
         

            if data11['status'] != "false":
                Data = {"status":"true","message":"data Updated Successfully","result":data11['result']}                  
                return Data
            else:
                data={"status":"false","result":"","message":"Invalid User"}
                return data
                        
        else:
            return msg 
    except Exception as e :
        print("Exception---->" +str(e))           
        output = {"status":"false","message":"something went wrong","result":""}
        return output           



@app.route('/updateuserProfile', methods=['POST'])
def updateuserProfile():
    try:
        inputdata =  commonfile.DecodeInputdata(request.get_data()) 
        startlimit,endlimit="",""
        keyarr = ["name","email","password",'userId']
        commonfile.writeLog("updateuserProfile",inputdata,0)
        msg = commonfile.CheckKeyNameBlankValue(keyarr,inputdata)
       
        if msg == "1":
            name,email,password,userTypeId,mobileNo,gender="","","","","",""
            column,values="",""
            
            # UserId = (commonfile.CreateHashKey(mobileNo,userTypeId)).hex
            
            
            # WhereCondition = " and email = '" + str(email) + "'"
            # count = databasefile.SelectCountQuery("hospitalUserMaster",WhereCondition,"")

            
            if 'email' in inputdata:
                email=inputdata["email"]
                column=" email='"+str(email)+"' " 
            if 'name' in inputdata:
                name=inputdata["name"]
                column=column+" ,name='"+str(name)+"' "  
            if 'password' in inputdata:
                password=inputdata["password"]
                column=column+" ,password= '"+str(password)+"' "                
            if 'mobileNo' in inputdata:
                mobileNo=inputdata["mobileNo"]
                column=column+" ,mobileNo='"+str(mobileNo)+"' "  

            if 'userId' in inputdata:
                userId=inputdata["userId"]    
                
            
            whereCondition= " userId= '"+str(userId)+"' and userTypeId='2' "
          
            data=databasefile.UpdateQuery("userMaster",column,whereCondition)
         

            if data != "0":
                Data = {"status":"true","message":"data Updated Successfully","result":"data Updated Successfully"}                  
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


@app.route('/addDrivertest', methods=['POST'])
def addDrivertest():
    try:
        print('Hello')
        inputdata=request.form.get('data')
        print(inputdata,'inputdata')
        keyarr = ['mobileNo','key','name','driverTypeId']
        inputdata=json.loads(inputdata)
        # inputdata =  commonfile.DecodeInputdata(request.get_data()) 
        startlimit,endlimit="",""

        commonfile.writeLog("addDrivertest",inputdata,0)
        msg = commonfile.CheckKeyNameBlankValue(keyarr,inputdata)
        print(msg,'msg')
       
        if msg == "1":
            mobileNo=inputdata['mobileNo']
            name=inputdata['name']
            driverTypeId=int(inputdata['driverTypeId'])
           
            key = inputdata["key"]
            column = " * "
            whereCondition= " mobileNo='"+str(mobileNo)+ "' and usertypeId='3' "
            data= databasefile.SelectQuery("userMaster",column,whereCondition)

            column11="id,driverId"

            whereCondition1= " mobileNo='"+str(mobileNo)+ "' and driverTypeId='"+str(driverTypeId)+ "'"
            data1= databasefile.SelectQuery("driverMaster",column11,whereCondition1)

            print(data1,'data--------------------------')

           
            mobileNo= inputdata["mobileNo"]
            driverId=data['result']['userId']
            
            DlNo,dlFrontFilename,DlFrontPicPath,dlBackFilename,DlBackPicPath,PIDType,PIDNo,PIDFrontFilename,PIDFrontPicPath,PIDBackFilename,PIDBackPicPath,TransportType,TransportModel,Color,AmbulanceRegistrationFuel,TypeNo,AIFilename,AIPicPath,AmbulanceModeId,AmbulanceId="","","","","","","","","","","","","","","","","","","0","0"
            lat,lng="",""

            
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
                    if (key == 1) or (key =='1'):
                        columns = "name,mobileNo,dlNo,dlFrontFilename,dlFrontFilepath,dlBackFilename,dlBackFilepath,driverId,driverTypeId"          
                        values = " '" + str(name) + "','" + str(mobileNo) + "','" + str(DlNo) + "','" + str( dlFrontFilename) + "','" + str(DlFrontPicPath) + "','" + str(dlBackFilename) + "', "            
                        values = values + " '" + str(DlBackPicPath) + "','" + str(driverId) + "','" + str(driverTypeId) + "'"
                        data = databasefile.InsertQuery("driverMaster",columns,values)
                        if data != "0":
                            column = '*'
                            WhereCondition = " mobileNo = '" + str(mobileNo) +  "'"

                            
                            data11 = databasefile.SelectQuery("driverMaster",column,WhereCondition)
                            print(data11,"+++++++++++++++++++")

                            if data11['result']['pIDType'] == None:
                                columns='ambulanceNo'
                                whereCondition=" driverId= '"+str(driverId)+"'"
                                data1111=databasefile.SelectQuery('ambulanceMaster',columns,whereCondition)
                                print(data1111,"++++++++++++++")
                                if data1111['status']=='false':
                                    y={'documentStatus':"false"}
                                    data11.update(y)
                                   
                            return data11

                    if (key == 2) or (key =='2'):
                        
                        columns = " name,mobileNo,pIDType,pIDNo,pIDFrontFilename,pIDFrontFilepath,pIDBackFilename,pIDBackFilepath,driverId,driverTypeId"          
                        values = " '" + str(name) + "','" + str(mobileNo) + "','" + str(PIDType) + "','" + str(PIDNo) + "','" + str(PIDFrontFilename) + "','" + str(PIDFrontPicPath) + "','" + str(PIDBackFilename) + "', "            
                        values = values + " '" + str(PIDBackPicPath)+ "','" + str(driverId) + "','" + str(driverTypeId) + "'"
                        data = databasefile.InsertQuery("driverMaster",columns,values)
                        if data != "0":
                            column = '*'
                            WhereCondition = " mobileNo = '" + str(mobileNo) +  "'"
                            
                            data11 = databasefile.SelectQuery("driverMaster",column,WhereCondition)
                            if data11['result']['dlNo'] == None:
                                columns='ambulanceNo'
                                whereCondition=" driverId='"+str(driverId)+"'"
                                data1111=databasefile.SelectQuery('ambulanceMaster',columns,whereCondition)
                                if data1111['status']=='false':
                                    y={'documentStatus':"false"}
                                    data11.update(y)
                                   
                            return data11
                    
                    if (key == 3) or (key =='3'):

                        columns = " name,mobileNo,driverId,driverTypeId"          
                        values = " '" + str(name) + "','" + str(mobileNo) + "','" + str(driverId) + "','" + str(driverTypeId) + "'"
                        
                        data = databasefile.InsertQuery("driverMaster",columns,values)

                        columns222="driverId"
                        whereCondition2222=" mobileNo = '" + str(mobileNo) +  "' "
                        data99=databasefile.SelectQuery1('driverMaster',columns222,whereCondition2222)
                        data111=data99[-1]
                        driverid=data111["driverId"]

                        columns2= "ambulanceNo,transportType,transportModel,color,ambulanceRegistrationFuel,typeNo,ambulanceFilename,ambulanceFilepath,ambulanceModeId,ambulanceTypeId,driverId,driverTypeId"
                        values2="'" + str(AmbulanceNo) + "','" + str( TransportType)  + "','" + str(TransportModel) + "','" + str(Color) + "','" + str(AmbulanceRegistrationFuel) + "','" + str(TypeNo) + "','" + str(AIFilename) + "','" + str(AIPicPath) + "','" + str(AmbulanceModeId) + "', "            
                        values2 = values2 + " '" + str(AmbulanceId) + "','" + str(driverid) + "','" + str(driverTypeId) + "'"
                        data122=databasefile.InsertQuery("ambulanceMaster",columns2,values2)
                        
                        

                        if data122 != "0":

                            column = '*'
                            WhereCondition = " mobileNo = '" + str(mobileNo) +  "'"
                            whereCondition="   driverId='" + str(driverid) +  "' "
                            columns22="ambulanceId,transportType,transportModel,color,ambulanceRegistrationFuel,typeNo,ambulanceFilename,ambulanceFilepath,ambulanceModeId,ambulanceTypeId,ambulanceNo,driverTypeId"
                            
                            data11 = databasefile.SelectQuery("driverMaster",column,WhereCondition)
                            print(data11['result'],"______--")
                            print(data11['result']['dlNo'],"+++++++++")


                            data12=databasefile.SelectQuery("ambulanceMaster",columns22,whereCondition)

                            ambulanceId=data12['result']['ambulanceId']
                            columns23='ambulanceId,lat,lng'
                            values23 = " '" + str(ambulanceId) + "','" + str(lat) + "','" + str(lng) + "'"
                            data122=databasefile.InsertQuery('ambulanceRideStatus',columns23,values23)
                            whereCondition222= " ambulanceId=  '" + str(ambulanceId) +  "' "
                            columns239="lat,lng,onDuty,onTrip"
                            data12333=databasefile.SelectQuery('ambulanceRideStatus',columns239,whereCondition222)



                            data11.update(data12)
                            data11.update(data12333)
                            if data11['result']['dlNo'] == None:
                                if data11['result']['pIDNo'] == None:
                                    y={'documentStatus':"false"}
                                    data11.update(y)

                                


                            return data11
                
                
                else:
                    if (key == 1) or (key =='1'):
                        print('A')
                        columns="dlNo"
                        WhereCondition = " mobileNo = '" + str(mobileNo) + "'"
                        data19 = databasefile.SelectQuery("driverMaster",columns,WhereCondition)
                        if data19['result']['dlNo'] == None:

                            column = " name='" + str(name) + "' ,dlNo = '" + str(DlNo) + "',dlFrontFilename = '" + str(dlFrontFilename) + "',dlFrontFilepath = '" + str(DlFrontPicPath) + "',dlBackFilename = '" + str(dlBackFilename) + "',dlBackFilepath = '" + str(DlBackPicPath) + "',driverTypeId='" + str(driverTypeId) + "'"
                            print(column,'column')
                            data = databasefile.UpdateQuery("driverMaster",column,WhereCondition)
                            print(data,'updatedata')
                            column = '*'
                            WhereCondition = " mobileNo = '" + str(mobileNo) +  "'"

                            
                            data11 = databasefile.SelectQuery("driverMaster",column,WhereCondition)
                            if data11['result']['pIDType'] == None:
                               
                                    y={'documentStatus':"false"}
                                    data11.update(y)
                                
                            else:
                                columns='ambulanceNo'
                                whereCondition=" driverId='"+str(driverId)+"'"
                                data1111=databasefile.SelectQuery('ambulanceMaster',columns,whereCondition)
                                if data1111['status']=='false':
                                    y={'documentStatus':"false"}
                                    data11.update(y)
                                else:
                                    y={'documentStatus':"true"}
                                    data11.update(y)

                            return data11
                        else:
                            data={"result":"","message":"Already Uploaded","status":"false"}
                            return data

                    if (key == 2) or (key =='2'):
                        print('B')
                        columns='pIDType,pIDNo'
                        WhereCondition = " mobileNo = '" + str(mobileNo) + "'"
                        data19 = databasefile.SelectQuery("driverMaster",columns,WhereCondition)
                        if data19['result']['pIDType'] == None:
                            column = "name='" + str(name) + "', pIDType = '" + str(PIDType) + "',pIDNo = '" + str(PIDNo) + "',pIDFrontFilename = '" + str(PIDFrontFilename) + "',pIDFrontFilepath = '" + str(PIDFrontPicPath) + "',pIDBackFilename = '" + str(PIDBackFilename) + "',pIDBackFilepath = '" + str(PIDBackPicPath) + "',driverTypeId='" + str(driverTypeId) + "'"
                            print(column,'column')
                            data = databasefile.UpdateQuery("driverMaster",column,WhereCondition)
                            print(data,'updatedata')
                            column = '*'
                            WhereCondition = " mobileNo = '" + str(mobileNo) +  "'"
                            
                            data11 = databasefile.SelectQuery("driverMaster",column,WhereCondition)
                            if data11['result']['dlNo'] == None:
                                y={'documentStatus':"false"}
                                data11.update(y)
                            else:
                                columns='ambulanceNo'
                                whereCondition=" driverId= '"+str(driverId)+"'"
                                data1111=databasefile.SelectQuery('ambulanceMaster',columns,whereCondition)
                                if data1111['status']=='false':
                                    y={'documentStatus':"false"}
                                    data11.update(y)
                                else:
                                    y={'documentStatus':"true"}
                                    data11.update(y)

                            
                            return data11
                        
                        else:
                            data={"result":"","message":"Already Uploaded","status":"false"}
                            return data



                    if (key == 3) or (key =='3'):
                        driver_Id=data1['result']['driverId']
                        columns="ambulanceId"
                        WhereCondition = " driverId = '" + str(driver_Id) + "'"
                        data111=databasefile.SelectQuery('ambulanceMaster',columns,WhereCondition)
                        if data111['status'] == 'false':
                            
                            columns2= "ambulanceNo,transportType,transportModel,color,ambulanceRegistrationFuel,typeNo,ambulanceFilename,ambulanceFilepath,ambulanceModeId,ambulanceTypeId,driverId,driverTypeId"

                            values2="'" + str(AmbulanceNo) + "','" + str( TransportType) + "','" + str(TransportModel) + "','" + str(Color) + "','" + str(AmbulanceRegistrationFuel) + "','" + str(TypeNo) + "','" + str(AIFilename) + "','" + str(AIPicPath) + "','" + str(AmbulanceModeId) + "', "            
                            values2 = values2 + " '" + str(AmbulanceId) + "','" + str(driver_Id) + "','" + str(driverTypeId) + "'"
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
                                if data11['result']['dlNo'] == None:
                                    y={'documentStatus':"false"}
                                    data11.update(y)
                                   

                                
                                if data11['result']['pIDNo'] == None:
                                    y={'documentStatus':"false"}
                                    data11.update(y)
                                else:
                                    y={'documentStatus':"true"}
                                    data11.update(y)

                                        


                                return data11

                            print('q')
                        else:
                            data11={"result":"","message":"Already Uploaded","status":"false"}
                            return data11

            else:
                data={"result":"","message":"Invalid mobileNo","status":"false"}
                return data
                        
               
        else:
            return msg
    except Exception as e :
        print("Exception---->" + str(e))    
        output = {"result":"something went wrong","status":"false"}
        return output




@app.route('/addResponder', methods=['POST'])
def addDrivertest1():
    try:
        print('Hello')
        inputdata=request.form.get('data')
        print(inputdata,'inputdata')
        keyarr = ['mobileNo','key','name','userTypeId']
        inputdata=json.loads(inputdata)
        # inputdata =  commonfile.DecodeInputdata(request.get_data()) 
        startlimit,endlimit="",""

        commonfile.writeLog("addResponder",inputdata,0)
        msg = commonfile.CheckKeyNameBlankValue(keyarr,inputdata)
        print(msg,'msg')
       
        if msg == "1":
            mobileNo=inputdata['mobileNo']
            name=inputdata['name']
            driverTypeId=int(inputdata['userTypeId'])
           
            key = inputdata["key"]
            column = " * "
            whereCondition= " mobileNo='"+str(mobileNo)+ "' and usertypeId='4'"
            data= databasefile.SelectQuery("userMaster",column,whereCondition)

            column11="id,driverId"

            whereCondition1= " mobileNo='"+str(mobileNo)+ "' and driverTypeId='"+str(driverTypeId)+ "'"
            data1= databasefile.SelectQuery("driverMaster",column11,whereCondition1)

            print(data1,'data--------------------------')

           
            mobileNo= inputdata["mobileNo"]
            driverId=data['result']['userId']
            
            DlNo,dlFrontFilename,DlFrontPicPath,dlBackFilename,DlBackPicPath,PIDType,PIDNo,PIDFrontFilename,PIDFrontPicPath,PIDBackFilename,PIDBackPicPath,TransportType,TransportModel,Color,AmbulanceRegistrationFuel,TypeNo,AIFilename,AIPicPath,AmbulanceModeId,AmbulanceId="","","","","","","","","","","","","","","","","","","0","0"

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
                        columns = "name,mobileNo,dlNo,dlFrontFilename,dlFrontFilepath,dlBackFilename,dlBackFilepath,driverId,driverTypeId"          
                        values = " '" + str(name) + "','" + str(mobileNo) + "','" + str(DlNo) + "','" + str( dlFrontFilename) + "','" + str(DlFrontPicPath) + "','" + str(dlBackFilename) + "', "            
                        values = values + " '" + str(DlBackPicPath) + "','" + str(driverId) + "','" + str(driverTypeId) + "'"
                        data = databasefile.InsertQuery("driverMaster",columns,values)
                        if data != "0":
                            column = '*'
                            WhereCondition = " mobileNo = '" + str(mobileNo) +  "'"
                            
                            data11 = databasefile.SelectQuery("driverMaster",column,WhereCondition)
                            return data11
                    if key == 2:
                        columns = " name,mobileNo,pIDType,pIDNo,pIDFrontFilename,pIDFrontFilepath,pIDBackFilename,pIDBackFilepath,driverId,driverTypeId"          
                        values = " '" + str(name) + "','" + str(mobileNo) + "','" + str(PIDType) + "','" + str(PIDNo) + "','" + str(PIDFrontFilename) + "','" + str(PIDFrontPicPath) + "','" + str(PIDBackFilename) + "', "            
                        values = values + " '" + str(PIDBackPicPath)+ "','" + str(driverId) + "','" + str(driverTypeId) + "'"
                        data = databasefile.InsertQuery("driverMaster",columns,values)
                        if data != "0":
                            column = '*'
                            WhereCondition = " mobileNo = '" + str(mobileNo) +  "'"
                            
                            data11 = databasefile.SelectQuery("driverMaster",column,WhereCondition)
                            return data11
                    
                    if key == 3:

                        columns = " name,mobileNo,driverId,driverTypeId"          
                        values = " '" + str(name) + "','" + str(mobileNo) + "','" + str(driverId) + "','" + str(driverTypeId) + "'"
                        
                        data = databasefile.InsertQuery("driverMaster",columns,values)

                        columns222="driverId"
                        whereCondition2222=" "
                        data99=databasefile.SelectQuery1('driverMaster',columns222,whereCondition2222)
                        data111=data99[-1]
                        driverid=data111["driverId"]

                        columns2= "ambulanceNo,transportType,transportModel,color,ambulanceRegistrationFuel,typeNo,ambulanceFilename,ambulanceFilepath,ambulanceModeId,ambulanceTypeId,driverId,driverTypeId"
                        values2="'" + str(AmbulanceNo) + "','" + str( TransportType)  + "','" + str(TransportModel) + "','" + str(Color) + "','" + str(AmbulanceRegistrationFuel) + "','" + str(TypeNo) + "','" + str(AIFilename) + "','" + str(AIPicPath) + "','" + str(AmbulanceModeId) + "', "            
                        values2 = values2 + " '" + str(AmbulanceId) + "','" + str(driverid) + "','" + str(driverTypeId) + "'"
                        data122=databasefile.InsertQuery("ambulanceMaster",columns2,values2)
                        
                        

                        if data122 != "0":
                            column = '*'
                            WhereCondition = " mobileNo = '" + str(mobileNo) +  "'"
                            whereCondition="   driverId='" + str(driverid) +  "' "
                            columns22="ambulanceId,transportType,transportModel,color,ambulanceRegistrationFuel,typeNo,ambulanceFilename,ambulanceFilepath,ambulanceModeId,ambulanceTypeId,ambulanceNo,driverTypeId"
                            
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
                        column = " name='" + str(name) + "' ,dlNo = '" + str(DlNo) + "',dlFrontFilename = '" + str(dlFrontFilename) + "',dlFrontFilepath = '" + str(DlFrontPicPath) + "',dlBackFilename = '" + str(dlBackFilename) + "',dlBackFilepath = '" + str(DlBackPicPath) + "',driverTypeId='" + str(driverTypeId) + "'"
                        print(column,'column')
                        data = databasefile.UpdateQuery("driverMaster",column,WhereCondition)
                        print(data,'updatedata')
                        return data
                    if key == 2:
                        print('B')
                        WhereCondition = " mobileNo = '" + str(mobileNo) + "'"
                        column = "name='" + str(name) + "', pIDType = '" + str(PIDType) + "',pIDNo = '" + str(PIDNo) + "',pIDFrontFilename = '" + str(PIDFrontFilename) + "',pIDFrontFilepath = '" + str(PIDFrontPicPath) + "',pIDBackFilename = '" + str(PIDBackFilename) + "',pIDBackFilepath = '" + str(PIDBackPicPath) + "',driverTypeId='" + str(driverTypeId) + "'"
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
                            
                            columns2= "ambulanceNo,transportType,transportModel,color,ambulanceRegistrationFuel,typeNo,ambulanceFilename,ambulanceFilepath,ambulanceModeId,ambulanceTypeId,driverId,driverTypeId"

                            values2="'" + str(AmbulanceNo) + "','" + str( TransportType) + "','" + str(TransportModel) + "','" + str(Color) + "','" + str(AmbulanceRegistrationFuel) + "','" + str(TypeNo) + "','" + str(AIFilename) + "','" + str(AIPicPath) + "','" + str(AmbulanceModeId) + "', "            
                            values2 = values2 + " '" + str(AmbulanceId) + "','" + str(driver_Id) + "','" + str(driverTypeId) + "'"
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

@app.route('/responderProfile', methods=['POST'])
def resProfile():
    try:
        inputdata =  commonfile.DecodeInputdata(request.get_data()) 
        startlimit,endlimit="",""
        keyarr = ['userId']
        commonfile.writeLog("responderProfile",inputdata,0)
        msg = commonfile.CheckKeyNameBlankValue(keyarr,inputdata)
       
        if msg == "1":
            
        

            
            
            if 'userId' in inputdata:
                driverId=inputdata["userId"]    
                
            
            whereCondition= " userId= '"+str(driverId)+"' and userTypeId='4' "
            column='userId,name,mobileNo,password,email'

            
         
            data11=databasefile.SelectQuery('userMaster',column,whereCondition)
            print(data11,"+++")
         

            if data11['status'] != "false":
                Data = {"status":"true","message":"","result":data11['result']}                  
                return Data
            else:
                data={"status":"false","result":"","message":"Invalid userId"}
                return data
                        
        else:
            return msg 
    except Exception as e :
        print("Exception---->" +str(e))           
        output = {"status":"false","message":"something went wrong","result":""}
        return output             

@app.route('/updateresponderProfile', methods=['POST'])
def updateresponderProfile():
    try:
        inputdata =  commonfile.DecodeInputdata(request.get_data()) 
        startlimit,endlimit="",""
        keyarr = ["name","email","password",'userId']
        commonfile.writeLog("updateresponderProfile",inputdata,0)
        msg = commonfile.CheckKeyNameBlankValue(keyarr,inputdata)
       
        if msg == "1":
            name,email,password,userTypeId,mobileNo,gender="","","","","",""
            column,values="",""
            columns2,values2="",""
        

            
            if 'email' in inputdata:
                email=inputdata["email"]
                column=" email='"+str(email)+"' " 
            if 'name' in inputdata:
                name=inputdata["name"]
                column=column+" ,name='"+str(name)+"' "  
                column2= " name='"+str(name)+"' " 
            if 'password' in inputdata:
                password=inputdata["password"]
                column=column+" ,password= '"+str(password)+"' "                
            if 'mobileNo' in inputdata:
                mobileNo=inputdata["mobileNo"]
                column=column+" ,mobileNo='"+str(mobileNo)+"' "
                column2=column2+" ,mobileNo='"+str(mobileNo)+"' "  

            if 'userId' in inputdata:
                driverId=inputdata["userId"]    
                
            
            whereCondition= " driverId= '"+str(driverId)+"' "
            whereCondition2= " userId ='"+str(driverId)+"' "
          
            data=databasefile.UpdateQuery("driverMaster",column2,whereCondition)
            data11=databasefile.UpdateQuery('userMaster',column,whereCondition2)
         

            if data != "0":
                Data = {"status":"true","message":"data Updated Successfully","result":"data Updated Successfully"}                  
                return Data
            else:
                return commonfile.Errormessage()
                        
        else:
            return msg 
    except Exception as e :
        print("Exception---->" +str(e))           
        output = {"status":"false","message":"something went wrong","result":""}
        return output                 

@app.route('/driverProfile', methods=['POST'])
def DriverProfile():
    try:
        inputdata =  commonfile.DecodeInputdata(request.get_data()) 
        startlimit,endlimit="",""
        keyarr = ['userId']
        commonfile.writeLog("driverProfile",inputdata,0)
        msg = commonfile.CheckKeyNameBlankValue(keyarr,inputdata)
       
        if msg == "1":
            
        

            
            
            if 'userId' in inputdata:
                driverId=inputdata["userId"]    
                
            
            whereCondition= " userId= '"+str(driverId)+"' and userTypeId='3' "
            column='userId,name,mobileNo,password,email'

            
         
            data11=databasefile.SelectQuery('userMaster',column,whereCondition)
         

            if data11['status'] != "false":
                Data = {"status":"true","message":"data Updated Successfully","result":data11['result']}                  
                return Data
            else:
                data={"status":"false","result":"","message":"Invalid userID"}
                return data
                        
        else:
            return msg 
    except Exception as e :
        print("Exception---->" +str(e))           
        output = {"status":"false","message":"something went wrong","result":""}
        return output             

@app.route('/updateDriverProfile', methods=['POST'])
def updateDriverProfile():
    try:
        inputdata =  commonfile.DecodeInputdata(request.get_data()) 
        startlimit,endlimit="",""
        keyarr = ["name","email","password",'userId']
        commonfile.writeLog("updateDriverProfile",inputdata,0)
        msg = commonfile.CheckKeyNameBlankValue(keyarr,inputdata)
       
        if msg == "1":
            name,email,password,userTypeId,mobileNo,gender="","","","","",""
            column,values="",""
            columns2,values2="",""
        

            
            if 'email' in inputdata:
                email=inputdata["email"]
                column=" email='"+str(email)+"' " 
            if 'name' in inputdata:
                name=inputdata["name"]
                column=column+" ,name='"+str(name)+"' "  
                column2= " name='"+str(name)+"' " 
            if 'password' in inputdata:
                password=inputdata["password"]
                column=column+" ,password= '"+str(password)+"' "                
            if 'mobileNo' in inputdata:
                mobileNo=inputdata["mobileNo"]
                column=column+" ,mobileNo='"+str(mobileNo)+"' "
                column2=column2+" ,mobileNo='"+str(mobileNo)+"' "  

            if 'userId' in inputdata:
                driverId=inputdata["userId"]    
                
            
            whereCondition= " driverId= '"+str(driverId)+"' "
            whereCondition2= " userId ='"+str(driverId)+"' "
          
            data=databasefile.UpdateQuery("driverMaster",column2,whereCondition)
            data11=databasefile.UpdateQuery('userMaster',column,whereCondition2)
         

            if data != "0":
                Data = {"status":"true","message":"data Updated Successfully","result":"data Updated Successfully"}                  
                return Data
            else:
                return commonfile.Errormessage()
                        
        else:
            return msg 
    except Exception as e :
        print("Exception---->" +str(e))           
        output = {"status":"false","message":"something went wrong","result":""}
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



@app.route('/hospitalMaster', methods=['GET'])
def hospitalMaster():
    try:
        msg = "1"
        if msg=="1":
            column="id  as hospitalId,hospitalName"
            whereCondition=""
            data=databasefile.SelectQuery1("hospitalMaster",column,whereCondition)
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
            if "startLimit" in inputdata:
                if inputdata['startLimit'] != "":
                    startlimit =str(inputdata["startLimit"])
                
            if "endLimit" in inputdata:
                if inputdata['endLimit'] != "":
                    endlimit =str(inputdata["endLimit"])
            orderby="AM.ambulanceId"

            column=" AM.ambulanceId,AM.ambulanceNo,atm.ambulanceType,dm.name as driverName,am.ambulanceType as category,AM.transportType,AM.transportModel,AM.color,AM.ambulanceRegistrationFuel as fueltype,AM.typeNo,AM.ambulanceFilename,concat('"+ ConstantData.GetBaseURL() + "',AM.ambulanceFilepath)ambulanceFilepath,AM.ambulanceModeId,AM.ambulanceTypeId "
           
            whereCondition=" and  AM.ambulanceTypeId=atm.id and AM.ambulanceModeId=am.id and AM.driverId=dm.driverId and AM.driverTypeId='1'"
            data=databasefile.SelectQueryOrderby("ambulanceMaster as AM, ambulanceTypeMaster  as atm,ambulanceMode as am,driverMaster as dm",column,whereCondition,"",startlimit,endlimit,orderby)
            print(data)
            whereCondition9=" AM.ambulanceTypeId=atm.id and AM.ambulanceModeId=am.id and AM.driverId=dm.driverId  and AM.driverTypeId='1' "
            countdata =databasefile.SelectQuery1("ambulanceMaster as AM, ambulanceTypeMaster  as atm,ambulanceMode as am,driverMaster as dm",column,whereCondition9)
            if (data['status']!='false'):
                count=len(countdata)
                Data = {"result":data['result'],'message':"","status":"true","totalCount":count}
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


@app.route('/allBikes', methods=['POST'])
def allBikes():
    try:
        msg = "1"
        if msg=="1":
            startlimit,endlimit="",""

            inputdata =  commonfile.DecodeInputdata(request.get_data())  
            if "startLimit" in inputdata:
                if inputdata['startLimit'] != "":
                    startlimit =str(inputdata["startLimit"])
                
            if "endLimit" in inputdata:
                if inputdata['endLimit'] != "":
                    endlimit =str(inputdata["endLimit"])
            orderby="AM.ambulanceId"

            column=" AM.ambulanceId,AM.ambulanceNo,ars.lat,ars.lng,atm.ambulanceType,dm.name as driverName,am.ambulanceType as category,AM.transportType,AM.transportModel,AM.color,AM.ambulanceRegistrationFuel as fueltype,AM.typeNo,AM.ambulanceFilename,concat('"+ ConstantData.GetBaseURL() + "',AM.ambulanceFilepath)ambulanceFilepath,AM.ambulanceModeId,AM.ambulanceTypeId "
           
            whereCondition="  and AM.driverId=dm.driverId  and AM.driverTypeId='2' and AM.ambulanceId=ars.ambulanceId"
            data=databasefile.SelectQueryOrderby("ambulanceMaster as AM,driverMaster as dm,ambulanceRideStatus as ars",column,whereCondition,"",startlimit,endlimit,orderby)
            print(data)
            whereCondition9=" AM.driverId=dm.driverId and  and AM.driverTypeId='2'"
            countdata =databasefile.SelectQuery1("ambulanceMaster as AM,driverMaster as dm",column,whereCondition9)
            if (data['status']!='false'):
                count=len(countdata)
                Data = {"result":data['result'],'message':"","status":"true","totalCount":count}
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
            WhereCondition=" and dm.driverId = um.userId and dm.driverTypeId='1'"

            inputdata =  commonfile.DecodeInputdata(request.get_data())  
            if "startLimit" in inputdata:
                if inputdata['startLimit'] != "":
                    startlimit =str(inputdata["startLimit"])
                
            if "endLimit" in inputdata:
                if inputdata['endLimit'] != "":
                    endlimit =str(inputdata["endLimit"])

            if "driverId" in inputdata:
                if inputdata['driverId'] != "":
                    driverId = str(inputdata["driverId"])
                    WhereCondition = WhereCondition + " and dm.driverId='"+str(driverId)+"'"

            orderby="dm.id"        

            column="dm.name,dm.id,dm.mobileNo,dm.profilePic,am.ambulanceNo,am.ambulanceId,um.email,ars.lat,ars.lng,ars.onDuty,ars.onTrip,dm.currentLocation as address,date_format(dm.dateCreate,'%Y-%m-%d %H:%i:%s')joiningDate,dm.status as status,dm.driverId as driverId"
            whereCondition=" and dm.driverId=am.driverId  and am.ambulanceId=ars.ambulanceId  and dm.status<>'2' " + WhereCondition
            data=databasefile.SelectQueryOrderby("driverMaster as dm,ambulanceMaster as am,ambulanceRideStatus as ars,userMaster um",column,whereCondition,"",startlimit,endlimit,orderby)
            print(data)
            WhereCondition999="  dm.driverId=am.driverId  and am.ambulanceId=ars.ambulanceId  and dm.status<>'2' " + WhereCondition
            countdata=databasefile.SelectQuery1("driverMaster as dm,ambulanceMaster as am,ambulanceRideStatus as ars,userMaster um",column, WhereCondition999)

            
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
                    whereCondition2222=" driverId = '"+str(d1)+"' "
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
                        print(ambulanceId2)
                        columns99="count(*) as count"
                        whereCondition88= " ambulanceId='"+str(ambulanceId2)+ "'"
                        data122=databasefile.SelectQuery('bookAmbulance',columns99,whereCondition88)
                        if data122['status']=='false':
                            i['tripCount']=0
                        else:
                            tripcount=data122['result']['count']
                            i['tripCount']=tripcount

                    count=len(countdata)        

                    Data = {"result":data['result'],"status":"true","message":"","totalCount":count}
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


@app.route('/allResponder', methods=['POST'])
def allResponder():
    try:
        msg = "1"
        if msg =="1":
            startlimit,endlimit="",""
            WhereCondition=" and dm.driverId = um.userId and dm.driverTypeId='2'"

            inputdata =  commonfile.DecodeInputdata(request.get_data())  
            if "startLimit" in inputdata:
                if inputdata['startLimit'] != "":
                    startlimit =str(inputdata["startLimit"])
                
            if "endLimit" in inputdata:
                if inputdata['endLimit'] != "":
                    endlimit =str(inputdata["endLimit"])

            if "driverId" in inputdata:
                if inputdata['driverId'] != "":
                    driverId = str(inputdata["driverId"])
                    WhereCondition = WhereCondition + " and dm.driverId='"+str(driverId)+"'"

            orderby="dm.id"        

            column="dm.name,dm.id,dm.mobileNo,dm.profilePic,am.ambulanceNo,am.ambulanceId,um.email,ars.lat,ars.lng,ars.onDuty,ars.onTrip,dm.currentLocation as address,date_format(dm.dateCreate,'%Y-%m-%d %H:%i:%s')joiningDate,dm.status as status,dm.driverId as driverId"
            whereCondition=" and dm.driverId=am.driverId  and am.ambulanceId=ars.ambulanceId  and dm.status<>'2' " + WhereCondition
            data=databasefile.SelectQueryOrderby("driverMaster as dm,ambulanceMaster as am,ambulanceRideStatus as ars,userMaster um",column,whereCondition,"",startlimit,endlimit,orderby)
            print(data,"+++++++++++++++++==")

            WhereCondition999="  dm.driverId=am.driverId  and am.ambulanceId=ars.ambulanceId  and dm.status<>'2' " 
            countdata=databasefile.SelectQuery1("driverMaster as dm,ambulanceMaster as am,ambulanceRideStatus as ars,userMaster um",column,WhereCondition999)
            
            if (data['status']!='false'):
                y2=len(data['result'])
                if y2 ==1:
                    print('111111111111111')
                    if data['result'][0]["profilePic"]==None:
                        data['result'][0]["profilePic"]=str(ConstantData.GetBaseURL())+"/profilePic/profilePic.jpg"

                    ambulanceId1=data['result'][0]['ambulanceId']     
                   
                    d1=data['result'][0]['driverId']
                    print(ambulanceId1)
                    columns2=" concat('"+ ConstantData.GetBaseURL() + "',am.ambulanceFilepath)ambulanceFilepath,um.email,am.ambulanceFilename,am.ambulanceRegistrationFuel as fuelType,am.color,am.transportModel,am.transportType"
                    whereCondition222="  am.ambulanceId=ars.ambulanceId  and am.ambulanceId="+str(ambulanceId1)+ ""
                    data111=databasefile.SelectQuery('ambulanceMaster as am,ambulanceRideStatus as ars,userMaster um',columns2,whereCondition222)
                    y2=data111['result']
                    print(y2)
                    column2222="dlNo,dlFrontFilename,concat('"+ ConstantData.GetBaseURL() + "',dlFrontFilepath)dlFrontFilepath,dlBackFilename,concat('"+ ConstantData.GetBaseURL() + "',dlBackFilepath)dlBackFilepath,pIDType,pIDNo,pIDFrontFilename,concat('"+ ConstantData.GetBaseURL() + "',pIDFrontFilepath)pIDFrontFilepath,pIDBackFilename,concat('"+ ConstantData.GetBaseURL() + "',pIDBackFilepath)pIDBackFilepath"
                    whereCondition2222=" driverId = '"+str(d1)+"' "
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
                        data122=databasefile.SelectQuery('bookResponder',columns99,whereCondition88)
                        if data122['status']!='false':
                            i['tripCount']=0
                        else:
                            tripcount=data122['result']['count']
                            i['tripCount']=tripcount

                    count=len(countdata)        

                    Data = {"result":data['result'],"status":"true","message":"","totalCount":count}
                    return Data
            else:
                output = {"message":"No Data Found","status":"true","result":""}
                return output
        else:
            return msg
    except Exception as e :
        print("Exception---->" + str(e))    
        output = {"result":"something went wrong","status":"false"}
        return output


#previous form
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
                       
                    else:
                        output = {"result":"Data already existed in mapping table","status":"true"}
                        return output

                for j in facility:
                    print('qqqqqqqqqqqqqqqqqqq')

                    column=" * "
                    whereCondition="facilityId='"+str(j)+"'  and hospitalId='"+str(mainId)+"'"
                    userHospitalMappingdata = databasefile.SelectQuery1("hospitalFacilityMapping ",column,whereCondition)
                    print(userHospitalMappingdata,'lets see')
                    if userHospitalMappingdata==0:
                        print('CCcccccccccccccccccccccccccccccccccccccccc')
                        column="hospitalId,facilityId"
                        values="'"+str(mainId)+"','"+str(j)+"'"
                        insertdata=databasefile.InsertQuery("hospitalFacilityMapping",column,values)                
                       
                    else:
                        output = {"result":"Data already existed in mapping table","status":"true"}
                        return output
                output = {"result":"Data Inserted Successfully","status":"true"}
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
                       
                    else:
                        output = {"result":"Data already existed in mapping table","status":"true"}
                        return output             



                else:    
                    output = {"result":"Hospital  address Already  Existed ","status":"true"}
                    return output
                    
                output = {"result":"Data Inserted Successfully","status":"true"}
                return output      
        else:
            return msg 
    except Exception as e :
        print("Exception---->" + str(e))    
        output = {"result":"something went wrong","status":"false"}
        return output

#according to new form


@app.route('/addhospital1', methods=['POST'])
def addhospital1():
    try:
        print('A')
        inputdata =  commonfile.DecodeInputdata(request.get_data())
        startlimit,endlimit="",""
        keyarr = ['hospitalName','address','ambulanceId','laboratary','empanelmentanyOther','emergencyBed','paraMedicalStaff','operationTheatre','inHouseSpecialist','ICUBed','generalBed','inHouseDoctor','lat','lng','keyPersonName','keyPersonEmail','keyPersonMobileNo','keyPersonTelephone','keyPersonFax','accreditaionA','accreditaionB','accreditaionC','facilityId','hospTypeId','empanelment','serviceTypeId','beds','specialities','fixedHours','emergencyKeyName','emergencyKeyMobileNo','emergencyKeyDesignation']
        commonfile.writeLog("addhospital",inputdata,0)
        msg = commonfile.CheckKeyNameBlankValue(keyarr,inputdata)
        if msg=="1":
            hospitalName = commonfile.EscapeSpecialChar(inputdata["hospitalName"])
            address = commonfile.EscapeSpecialChar(inputdata["address"])
            ambulanceId = inputdata["ambulanceId"]
            facility=inputdata['facilityId']
            empanelment= inputdata['empanelment']

            empanelmentanyOther= inputdata['empanelmentanyOther']
            anyo=[]
            mm=len(empanelmentanyOther)
            if mm>0:
                for i in empanelmentanyOther:
                    column="id"
                    whereCondition111=" empanelmentType='"+str(i)+"'"
                    data=databasefile.SelectQuery('empanelmentTypeMaster',column,whereCondition111)
                    if data['status'] == 'false':
                        column1='empanelmentType'
                        values="'"+str(i)+"'"
                        insertdata=databasefile.insertdata('empanelmentTypeMaster',column1,values)
                        data99911=databasefile.SelectQuery1('empanelmentTypeMaster',column,whereCondition111)
                        Id=data99911[-1]['id']
                        anyo.append(Id)
                        for j in anyo:
                            empanelment.append(j)



            laboratary = inputdata['laboratary']

            laborataryanyOther=inputdata['laborataryanyOther']
            anyo1=[]
            mm1=len(laborataryanyOther)
            if mm1>0:
                for i in laborataryanyOther:
                    column="id"
                    whereCondition111=" labotary  ='"+str(i)+"'"
                    data=databasefile.SelectQuery('hospitalLabotaryMaster',column,whereCondition111)
                    if data['status'] == 'false':
                        column1='labotary '
                        values="'"+str(i)+"'"
                        insertdata=databasefile.insertdata('hospitalLabotaryMaster',column1,values)
                        data99911=databasefile.SelectQuery1('hospitalLabotaryMaster',column,whereCondition111)
                        Id=data99911[-1]['id']
                        anyo1.append(Id)
                        for j in anyo1:
                            laboratary.append(j)



            print(facility,"++++++++++++++++++++++++++++++++++++++++++")
            
            latitude=inputdata['lat']

            longitude=inputdata['lng']

            city=inputdata['cityId']

            hospTypeId=inputdata['hospTypeId']
            serviceTypeId=inputdata['serviceTypeId'] 
            
            keyPersonName=inputdata['keyPersonName']
            keyPersonEmail=inputdata['keyPersonEmail']

            keyPersonMobileNo=inputdata['keyPersonMobileNo']
            keyPersonTelephone=inputdata['keyPersonTelephone']
            keyPersonFax=inputdata['keyPersonFax']

            accreditaionA=inputdata['accreditaionA']
            accreditaionB=inputdata['accreditaionB']
            accreditaionC=inputdata['accreditaionC']

            emergencyKeyName=inputdata['emergencyKeyName']
            emergencyKeyMobileNo=inputdata['emergencyKeyMobileNo']
            emergencyKeyDesignation=inputdata['emergencyKeyDesignation']

            
            emergencyBed= inputdata['emergencyBed']
            ICUBed=inputdata['ICUBed']
            generalBed=inputdata['generalBed']

            inHouseDoctor=inputdata ['inHouseDoctor']
            inHouseSpecialist=inputdata['inHouseSpecialist']

            paraMedicalStaff=inputdata['paraMedicalStaff']
            operationTheatre=inputdata['operationTheatre']
            specialities=inputdata['specialities']
            fixedHours=inputdata['fixedHours']
            beds=inputdata['beds']







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

                column='hospitalId,hospTypeId'
                values="'"+str(mainId)+"','"+str(hospTypeId)+"'"
                insertdata=databasefile.InsertQuery(" hospitalTypeMapping ",column,values)

                column='hospitalId,serviceTypeId'
                values="'"+str(mainId)+"','"+str(serviceTypeId)+"'"
                insertdata=databasefile.InsertQuery("hospitalServiceMapping",column,values)


                column='name,email,mobileNo,landlineTelephoneNo,fax,hospitalId'
                values="'"+str(keyPersonName)+"','"+str(keyPersonEmail)+"','"+str(keyPersonMobileNo)+"','"+str(keyPersonTelephone)+"','"+str(keyPersonFax)+"','"+str(mainId)+"'"
                insertdata=databasefile.InsertQuery("hospitalKeyPersonMaster",column,values)

                y1=len(accreditaionA)
                y2=len(accreditaionB)
                y3=len(accreditaionC)

                if y1 !=0:
                    column='hospitalId,accreditationsId'
                    values="'"+str(mainId)+"','"+str(accreditaionA)+"'"
                    insertdata=databasefile.InsertQuery("hospitalAccreditationsMapping",column,values)

                if y2 !=0:
                    column='hospitalId,accreditationsId'
                    values="'"+str(mainId)+"','"+str(accreditaionA)+"'"
                    insertdata=databasefile.InsertQuery("hospitalAccreditationsMapping",column,values)

                if y3 !=0:
                    column='hospitalId,accreditationsId'
                    values="'"+str(mainId)+"','"+str(accreditaionA)+"'"
                    insertdata=databasefile.InsertQuery("hospitalAccreditationsMapping",column,values)

                
                column='emergencyKeyName,emergencyKeyDesignation,emergencyKeyMobileNo,hospitalId'
                values="'"+str(emergencyKeyName)+"','"+str(emergencyKeyDesignation)+"','"+str(emergencyKeyMobileNo)+"','"+str(mainId)+"'"
                insertdata=databasefile.InsertQuery("hospitalemergencyKeyContactMaster",column,values)

                
                column='casuality,icu,generalBed,hospitalId'
                values="'"+str(emergencyBed)+"','"+str(ICUBed)+"','"+str(generalBed)+"','"+str(mainId)+"'"
                insertdata=databasefile.InsertQuery("hospitalBedMaster",column,values)

                column='hospitalId, inhouseDoctors, inhouseSpecialists'
                values="'"+str(mainId)+"','"+str(inHouseDoctor)+"','"+str(inHouseSpecialist)+"'"
                insertdata=databasefile.InsertQuery("hospitalDoctorMaster",column,values)


                column='hospitalId, paramedicalStaff, operationTheatre'
                values="'"+str(mainId)+"','"+str(paraMedicalStaff)+"','"+str(operationTheatre)+"'"
                insertdata=databasefile.InsertQuery("hospitaloperationparamedicalStaffMaster",column,values)

                column='hospitalId,  fixedHours , beds'
                values="'"+str(mainId)+"','"+str(fixedHours )+"','"+str(beds)+"'"
                insertdata=databasefile.InsertQuery(" emergencyDepartMentMaster ",column,values)














                








                
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
                       
                    else:
                        output = {"result":"Data already existed in mapping table","status":"true"}
                        return output

                for j in facility:
                    print('qqqqqqqqqqqqqqqqqqq')

                    column=" * "
                    whereCondition="facilityId='"+str(j)+"'  and hospitalId='"+str(mainId)+"'"
                    userHospitalMappingdata = databasefile.SelectQuery1("hospitalFacilityMapping ",column,whereCondition)
                    print(userHospitalMappingdata,'lets see')
                    if userHospitalMappingdata==0:
                        print('CCcccccccccccccccccccccccccccccccccccccccc')
                        column="hospitalId,facilityId"
                        values="'"+str(mainId)+"','"+str(j)+"'"
                        insertdata=databasefile.InsertQuery("hospitalFacilityMapping",column,values)                
                       
                    else:
                        output = {"result":"Data already existed in mapping table","status":"true"}
                        return output
                output = {"result":"Data Inserted Successfully","status":"true"}
                return output

                for k in empanelment:
                    print('qqqqqqqqqqqqqqqqqqq')

                    column=" * "
                    whereCondition=" empanelmentTypeId ='"+str(k)+"'  and hospitalId='"+str(mainId)+"'"
                    userHospitalMappingdata = databasefile.SelectQuery1("empanelmentTypeMapping ",column,whereCondition)
                    print(userHospitalMappingdata,'lets see')
                    if userHospitalMappingdata==0:
                        print('CCcccccccccccccccccccccccccccccccccccccccc')
                        column="hospitalId,empanelmentTypeId"
                        values="'"+str(mainId)+"','"+str(k)+"'"
                        insertdata=databasefile.InsertQuery("empanelmentTypeMapping",column,values)                
                       
                    else:
                        output = {"result":"Data already existed in mapping table","status":"true"}
                        return output
                output = {"result":"Data Inserted Successfully","status":"true"}
                return output

                for m in laboratary:
                    print('qqqqqqqqqqqqqqqqqqq')

                    column=" * "
                    whereCondition=" hlmId   ='"+str(m)+"'  and hospitalId='"+str(mainId)+"'"
                    userHospitalMappingdata = databasefile.SelectQuery1("hospitalLabotaryMapping ",column,whereCondition)
                    print(userHospitalMappingdata,'lets see')
                    if userHospitalMappingdata==0:
                        print('CCcccccccccccccccccccccccccccccccccccccccc')
                        column="hospitalId,hlmId   "
                        values="'"+str(mainId)+"','"+str(m)+"'"
                        insertdata=databasefile.InsertQuery("hospitalLabotaryMapping",column,values)                
                       
                    else:
                        output = {"result":"Data already existed in mapping table","status":"true"}
                        return output

                for j in specialities:
                    print('qqqqqqqqqqqqqqqqqqq')

                    column=" * "
                    whereCondition="hospitalId='"+str(mainId)+"'  and spId ='"+str(j)+"'"
                    userHospitalMappingdata = databasefile.SelectQuery1("emergencySpecialistMapping ",column,whereCondition)
                    print(userHospitalMappingdata,'lets see')
                    if userHospitalMappingdata==0:
                        print('CCcccccccccccccccccccccccccccccccccccccccc')
                        column="hospitalId,spId "
                        values="'"+str(mainId)+"','"+str(j)+"'"
                        insertdata=databasefile.InsertQuery("emergencySpecialistMapping",column,values)                
                       
                    else:
                        output = {"result":"Data already existed in mapping table","status":"true"}
                        return output
                output = {"result":"Data Inserted Successfully","status":"true"}
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
                       
                    else:
                        output = {"result":"Data already existed in mapping table","status":"true"}
                        return output  

                for k in empanelment:
                    print('qqqqqqqqqqqqqqqqqqq')

                    column=" * "
                    whereCondition=" empanelmentTypeId ='"+str(k)+"'  and hospitalId='"+str(mainId)+"'"
                    userHospitalMappingdata = databasefile.SelectQuery1("empanelmentTypeMapping ",column,whereCondition)
                    print(userHospitalMappingdata,'lets see')
                    if userHospitalMappingdata==0:
                        print('CCcccccccccccccccccccccccccccccccccccccccc')
                        column="hospitalId,empanelmentTypeId"
                        values="'"+str(mainId)+"','"+str(k)+"'"
                        insertdata=databasefile.InsertQuery("empanelmentTypeMapping",column,values)                
                       
                    else:
                        output = {"result":"Data already existed in mapping table","status":"true"}
                        return output

                for m in laboratary:
                    print('qqqqqqqqqqqqqqqqqqq')

                    column=" * "
                    whereCondition=" hlmId   ='"+str(m)+"'  and hospitalId='"+str(mainId)+"'"
                    userHospitalMappingdata = databasefile.SelectQuery1("hospitalLabotaryMapping ",column,whereCondition)
                    print(userHospitalMappingdata,'lets see')
                    if userHospitalMappingdata==0:
                        print('CCcccccccccccccccccccccccccccccccccccccccc')
                        column="hospitalId,hlmId   "
                        values="'"+str(mainId)+"','"+str(m)+"'"
                        insertdata=databasefile.InsertQuery("hospitalLabotaryMapping",column,values)                
                       
                    else:
                        output = {"result":"Data already existed in mapping table","status":"true"}
                        return output

                for j in specialities:
                    print('qqqqqqqqqqqqqqqqqqq')

                    column=" * "
                    whereCondition="hospitalId='"+str(mainId)+"'  and spId ='"+str(j)+"'"
                    userHospitalMappingdata = databasefile.SelectQuery1("emergencySpecialistMapping ",column,whereCondition)
                    print(userHospitalMappingdata,'lets see')
                    if userHospitalMappingdata==0:
                        print('CCcccccccccccccccccccccccccccccccccccccccc')
                        column="hospitalId,spId "
                        values="'"+str(mainId)+"','"+str(j)+"'"
                        insertdata=databasefile.InsertQuery("emergencySpecialistMapping",column,values)                
                       
                    else:
                        output = {"result":"Data already existed in mapping table","status":"true"}
                        return output

                else:    
                    output = {"result":"Hospital  address Already  Existed ","status":"true"}
                    return output
                    
                output = {"result":"Data Inserted Successfully","status":"true"}
                return output      
        else:
            return msg 
    except Exception as e :
        print("Exception---->" + str(e))    
        output = {"result":"something went wrong","status":"false"}
        return output





@app.route('/updateHospital1', methods=['POST'])
def updateStatus11():
    try:
        inputdata =  commonfile.DecodeInputdata(request.get_data())
        startlimit,endlimit="",""
        keyarr = ['id','address','ambulanceId','empanelmentanyOther','laboratary','specialities','emergencyBed','paraMedicalStaff','operationTheatre','inHouseSpecialist','ICUBed','generalBed','inHouseDoctor','lat','lng','keyPersonName','keyPersonEmail','keyPersonMobileNo','keyPersonTelephone','keyPersonFax','accreditaionA','accreditaionB','accreditaionC','facilityId','hospTypeId','empanelment','serviceTypeId','beds','fixedHours','emergencyKeyName','emergencyKeyMobileNo','emergencyKeyDesignation']
        print(inputdata,"B")
        commonfile.writeLog("updateHospital1",inputdata,0)
        msg = commonfile.CheckKeyNameBlankValue(keyarr,inputdata)
        if msg =="1":
          
            hospitalId = int(inputdata["id"])
            hospitalName = commonfile.EscapeSpecialChar(inputdata["hospitalName"])
            address = commonfile.EscapeSpecialChar(inputdata["address"])
            ambulanceId = inputdata["ambulanceId"]
            facilityId=inputdata['facilityId']
            empanelment= inputdata['empanelment']
            print(facilityId,"++++++++++++++++++++++++++++++++++++++++++")
            
            latitude=inputdata['lat']

            longitude=inputdata['lng']

            city=inputdata['cityId']
           
            empanelmentanyOther= inputdata['empanelmentanyOther']
            anyo=[]
            mm=len(empanelmentanyOther)
            if mm>0:
                for i in empanelmentanyOther:
                    column="id"
                    whereCondition111=" empanelmentType='"+str(i)+"'"
                    data=databasefile.SelectQuery('empanelmentTypeMaster',column,whereCondition111)
                    if data['status'] == 'false':
                        column1='empanelmentType'
                        values="'"+str(i)+"'"
                        insertdata=databasefile.insertdata('empanelmentTypeMaster',column1,values)
                        data99911=databasefile.SelectQuery1('empanelmentTypeMaster',column,whereCondition111)
                        Id=data99911[-1]['id']
                        anyo.append(Id)
                        for j in anyo:
                            empanelment.append(j)



            laboratary = inputdata['laboratary']

            laborataryanyOther=inputdata['laborataryanyOther']
            anyo1=[]
            mm1=len(laborataryanyOther)
            if mm1>0:
                for i in laborataryanyOther:
                    column="id"
                    whereCondition111=" labotary  ='"+str(i)+"'"
                    data=databasefile.SelectQuery('hospitalLabotaryMaster',column,whereCondition111)
                    if data['status'] == 'false':
                        column1='labotary '
                        values="'"+str(i)+"'"
                        insertdata=databasefile.insertdata('hospitalLabotaryMaster',column1,values)
                        data99911=databasefile.SelectQuery1('hospitalLabotaryMaster',column,whereCondition111)
                        Id=data99911[-1]['id']
                        anyo1.append(Id)
                        for j in anyo1:
                            laboratary.append(j)



            hospTypeId=inputdata['hospTypeId']
            serviceTypeId=inputdata['serviceTypeId'] 
            keyPersonName=inputdata['keyPersonName']
            keyPersonEmail=inputdata['keyPersonEmail']

            keyPersonMobileNo=inputdata['keyPersonMobileNo']
            keyPersonMobileNo=inputdata['keyPersonTelephone']
            keyPersonFax=inputdata['keyPersonFax']

            accreditaionA=inputdata['accreditaionA']
            accreditaionB=inputdata['accreditaionB']
            accreditaionC=inputdata['accreditaionC']

            emergencyKeyName=inputdata['emergencyKeyName']
            emergencyKeyMobileNo=inputdata['emergencyKeyMobileNo']
            emergencyKeyDesignation=inputdata['emergencyKeyDesignation']

            
            emergencyBed= inputdata['emergencyBed']
            ICUBed=inputdata['ICUBed']
            generalBed=inputdata['generalBed']

            inHouseDoctor=inputdata ['inHouseDoctor']
            inHouseSpecialist=inputdata['inHouseSpecialist']

            paraMedicalStaff=inputdata['paraMedicalStaff']
            operationTheatre=inputdata['operationTheatre']
            specialities=inputdata['specialities']
            fixedHours=inputdata['fixedHours']
            beds=inputdata['beds']

            column="hospitalName"
            whereCondition= "   id = " + str(userId)+ " "
            data=databasefile.SelectQuery1("hospitalMaster",column,whereCondition)
            print(data)
            if (data !=0):
                print(facilityId,"+++11+++++++++++++++++++++++++++++++++++++++")

                column=" hospitalName= '"+str(hospitalName)+"' "
                whereCondition="   id = " + str(hospitalId)+ " "
                data1=databasefile.UpdateQuery('hospitalMaster',column,whereCondition)

                column2="address='"+str(address)+"' ,lat='"+str(latitude)+"' ,lng='"+str(longitude)+"' ,cityId='"+str(city)+"' "
                whereCondition3=" hospitalId=' " + str(hospitalId)+ " ' "
                data2=databasefile.UpdateQuery('hospitalLocationMaster',column2,whereCondition3)









                whereCondition2=" hospital_Id= ' " + str(hospitalId)+ " ' "
                data3=databasefile.DeleteQuery('hospitalambulanceMapping',whereCondition2)

                whereCondition4= "hospitalId = ' " + str(hospitalId)+ " ' "
                data4=databasefile.DeleteQuery('hospitalFacilityMapping',whereCondition4)

                whereCondition5= "hospitalId = ' " + str(hospitalId)+ " ' "
                data5=databasefile.DeleteQuery('empanelmentTypeMapping',whereCondition5)

                whereCondition6= "hospitalId = ' " + str(hospitalId)+ " ' "
                data6=databasefile.DeleteQuery('hospitalLabotaryMapping',whereCondition6)

                whereCondition7= "hospitalId = ' " + str(hospitalId)+ " ' "
                data7=databasefile.DeleteQuery('emergencySpecialistMapping',whereCondition7)

                column77="hospTypeId='"+str(serviceTypeId)+"'"
                
                insertdata=databasefile.UpdateQuery(" hospitalTypeMapping ",column77,whereCondition7)




                column4="serviceTypeId='"+str(serviceTypeId)+"'"
               
                insertdata=databasefile.UpdateQuery("hospitalServiceMapping",column4,whereCondition7)


                column="name='"+str(keyPersonName)+"',email='"+str(keyPersonEmail)+"',mobileNo='"+str(keyPersonMobileNo)+"',landlineTelephoneNo='"+str(keyPersonTelephone)+"',fax='"+str(keyPersonFax)+"'"
                
                insertdata=databasefile.UpdateQuery("hospitalKeyPersonMaster",column,whereCondition7)

                y1=len(accreditaionA)
                y2=len(accreditaionB)
                y3=len(accreditaionC)

                if y1 !=0:
                    column="accreditationsId='"+str(accreditaionA)+"'"
                   
                    insertdata=databasefile.UpdateQuery("hospitalAccreditationsMapping",column,whereCondition7)

                if y2 !=0:
                    column="accreditationsId='"+str(accreditaionB)+"'"
                    insertdata=databasefile.UpdateQuery("hospitalAccreditationsMapping",column,whereCondition7)

                if y3 !=0:
                    column="accreditationsId='"+str(accreditaionC)+"'"
                    insertdata=databasefile.UpdateQuery("hospitalAccreditationsMapping",column,whereCondition7)

                
                column="emergencyKeyName= '"+str(emergencyKeyName)+"',emergencyKeyDesignation='"+str(emergencyKeyDesignation)+"',emergencyKeyMobileNo='"+str(emergencyKeyMobileNo)+"'"
                
                insertdata=databasefile.UpdateQuery("hospitalemergencyKeyContactMaster",column,whereCondition7)

                column="casuality='"+str(emergencyBed)+"',icu='"+str(ICUBed)+"',generalBed='"+str(generalBed)+"'"

                insertdata=databasefile.UpdateQuery("hospitalemergencyKeyContactMaster",column,whereCondition7)

                column=" inhouseDoctors='"+str(inHouseDoctor)+"', inhouseSpecialists='"+str(inHouseSpecialist)+"'"
                
                insertdata=databasefile.UpdateQuery("hospitalDoctorMaster",column,whereCondition7)


                column="paramedicalStaff='"+str(paraMedicalStaff)+"', operationTheatre='"+str(operationTheatre)+"'"
                values="'"+str(paraMedicalStaff)+"','"+str(operationTheatre)+"'"
                insertdata=databasefile.UpdateQuery("hospitaloperationparamedicalStaffMaster",column,whereCondition7)

                column=" fixedHours='"+str(fixedHours)+"' , beds='"+str(beds)+"' "
                insertdata=databasefile.UpdateQuery(" emergencyDepartMentMaster ",column,whereCondition7)








                print("aaaa1111111111111111111111111111")

                print(facilityId,"+++2222222222222++++++++++++++++++++++++++++++++++++++")   
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
                       
                    else:
                        output = {"result":"Data already existed in mapping table","status":"true"}
                        return output

                print(facilityId,"+++555++++++++++++++++++++++++++++++++++++++") 
                print(facilityId,"11111111111111111++++++++++++++++++++++++++++++++++++++++++")        

                for j in facilityId:
                    print('aaaaaaaaaa')
                    column=" * "
                    whereCondition="facilityId='"+str(j)+"'  and hospitalId='"+str(userId)+"'"
                    userHospitalMappingdata = databasefile.SelectQuery1("hospitalFacilityMapping ",column,whereCondition)
                    print(userHospitalMappingdata,'lets see')
                    if userHospitalMappingdata==0:
                        print('CC')
                        column="hospitalId,facilityId"
                        values="'"+str(userId)+"','"+str(j)+"'"
                        insertdata=databasefile.InsertQuery("hospitalFacilityMapping",column,values)                
                       
                    else:
                        output = {"result":"Data already existed in mapping table","status":"true"}
                        return output

                for k in empanelment:
                    print('qqqqqqqqqqqqqqqqqqq')

                    column=" * "
                    whereCondition=" empanelmentTypeId ='"+str(k)+"'  and hospitalId='"+str(mainId)+"'"
                    userHospitalMappingdata = databasefile.SelectQuery1("empanelmentTypeMapping ",column,whereCondition)
                    print(userHospitalMappingdata,'lets see')
                    if userHospitalMappingdata==0:
                        print('CCcccccccccccccccccccccccccccccccccccccccc')
                        column="hospitalId,empanelmentTypeId"
                        values="'"+str(mainId)+"','"+str(k)+"'"
                        insertdata=databasefile.InsertQuery("empanelmentTypeMapping",column,values)                
                       
                    else:
                        output = {"result":"Data already existed in mapping table","status":"true"}
                        return output

                for m in laboratary:
                    print('qqqqqqqqqqqqqqqqqqq')

                    column=" * "
                    whereCondition=" hlmId   ='"+str(m)+"'  and hospitalId='"+str(mainId)+"'"
                    userHospitalMappingdata = databasefile.SelectQuery1("hospitalLabotaryMapping ",column,whereCondition)
                    print(userHospitalMappingdata,'lets see')
                    if userHospitalMappingdata==0:
                        print('CCcccccccccccccccccccccccccccccccccccccccc')
                        column="hospitalId,hlmId   "
                        values="'"+str(mainId)+"','"+str(m)+"'"
                        insertdata=databasefile.InsertQuery("hospitalLabotaryMapping",column,values)                
                       
                    else:
                        output = {"result":"Data already existed in mapping table","status":"true"}
                        return output

                for j in specialities:
                    print('qqqqqqqqqqqqqqqqqqq')

                    column=" * "
                    whereCondition="hospitalId='"+str(mainId)+"'  and spId ='"+str(j)+"'"
                    userHospitalMappingdata = databasefile.SelectQuery1("emergencySpecialistMapping ",column,whereCondition)
                    print(userHospitalMappingdata,'lets see')
                    if userHospitalMappingdata==0:
                        print('CCcccccccccccccccccccccccccccccccccccccccc')
                        column="hospitalId,spId "
                        values="'"+str(mainId)+"','"+str(j)+"'"
                        insertdata=databasefile.InsertQuery("emergencySpecialistMapping",column,values)                
                       
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



@app.route('/updateHospital', methods=['POST'])
def updateStatus11111():
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
                print(facilityId,"+++11+++++++++++++++++++++++++++++++++++++++")

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
                print("aaaa1111111111111111111111111111")

                print(facilityId,"+++2222222222222++++++++++++++++++++++++++++++++++++++")   
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
                       
                    else:
                        output = {"result":"Data already existed in mapping table","status":"true"}
                        return output

                print(facilityId,"+++555++++++++++++++++++++++++++++++++++++++") 
                print(facilityId,"11111111111111111++++++++++++++++++++++++++++++++++++++++++")        

                for j in facilityId:
                    print('aaaaaaaaaa')
                    column=" * "
                    whereCondition="facilityId='"+str(j)+"'  and hospitalId='"+str(userId)+"'"
                    userHospitalMappingdata = databasefile.SelectQuery1("hospitalFacilityMapping ",column,whereCondition)
                    print(userHospitalMappingdata,'lets see')
                    if userHospitalMappingdata==0:
                        print('CC')
                        column="hospitalId,facilityId"
                        values="'"+str(userId)+"','"+str(j)+"'"
                        insertdata=databasefile.InsertQuery("hospitalFacilityMapping",column,values)                
                       
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
            startlimit,endlimit="",""
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
            orderby="hosp.id"                       

            column= "hosp.id,hosp.hospitalName,hl.address,hl.lat,hl.lng,cm.name as city,cm.id as cityId"   
            WhereCondition=  " and  hl.hospitalId=hosp.id and hosp.status<>'2' and hl.cityId=cm.id "+whereCondition2+whereCondition3+whereCondition4
            WhereCondition999=  " hl.hospitalId=hosp.id and hosp.status<>'2' and hl.cityId=cm.id "+whereCondition2+whereCondition3+whereCondition4
            data=databasefile.SelectQueryOrderby("hospitalMaster as hosp,hospitalLocationMaster as hl,cityMaster as cm",column,WhereCondition,"",startlimit,endlimit,orderby)
            countdata=databasefile.SelectQuery1('hospitalMaster as hosp,hospitalLocationMaster as hl,cityMaster as cm',column,WhereCondition999)
            print(countdata) 
            if (data!=0): 
                a=[]
                b=[]
                for i in data['result']:
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
                    count=len(countdata)          



                    # print(data1)

                   
                    # c=i['aId']
                    # print(c)
                    # if i['id'] not in a:
                    #     # a.append(i)
                    #     # i['ambulanceTypeId']=c
                    #     # i['ambulanceType']+=i['at'] +","


                



                Data = {"result":data['result'],"status":"true","totalCount":count}
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
        keyarr = ['startLocationLat','startLocationLong','driverTypeId']
        commonfile.writeLog("getNearAmbulance",inputdata,0)
        msg = commonfile.CheckKeyNameBlankValue(keyarr,inputdata)
        if msg == "1":
            startlat ,startlng,userId= inputdata["startLocationLat"],inputdata["startLocationLong"],""#,inputdata["userId"]
            driverTypeId=inputdata['driverTypeId']
            ambulanceTypeId=inputdata['ambulanceTypeId']

            print(ambulanceTypeId)
            ambulanceModeId=inputdata['ambulanceModeId']
            print(ambulanceModeId)
            column=  "d.driverId, a.ambulanceTypeId,a.ambulanceModeId,d.name, d.mobileNo, a.ambulanceId, a.ambulanceNo, b.lat, b.lng,SQRT(POW(69.1 * (b.lat - "+str(startlat)+"), 2) +POW(69.1 * ("+str(startlng)+" - b.lng) * COS(b.lat / 57.3), 2)) AS distance "
            whereCondition= " and  a.driverTypeId='"+str(driverTypeId)+"'" + " and a.ambulanceModeId='"+str(ambulanceModeId)+"'  and a.ambulanceTypeId='"+str(ambulanceTypeId)+"' and d.status=1 and b.onTrip=0 and b.onDuty=1 and a.driverId=d.driverId  and b.ambulanceId=a.ambulanceId HAVING distance < 25 "
            orderby="  distance "
            nearByAmbulance=databasefile.SelectQueryOrderbyAsc("ambulanceMaster a, driverMaster d,ambulanceRideStatus as b",column,whereCondition,"",orderby,"","")
            #print("nearByAmbulance================================",nearByAmbulance)
            nearByAmbulance["ambulanceTypeId"]=list(set([i["ambulanceTypeId"] for i in nearByAmbulance["result"]]))
            nearByAmbulance["ambulanceModeId"]=list(set([i["ambulanceModeId"] for i in nearByAmbulance["result"]]))
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
        client = mqtt.Client()
        client.connect("localhost",1883,60)

        for i in inputdata["driverId"]:

            #inputdata["driverId"]=str(i)
            #print(inputdata)
            
            
            topic=str(i)+"/booking"
            print(topic)
            print("1")
            #print("=================",topic)
            client.publish(topic, str(inputdata))
            print("2")
        client.disconnect()    
             
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
        print(inputdata)
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
                    print(driverId)
        if "startLocationLat" in inputdata:
                if inputdata['startLocationLat'] != "":
                    startLocationLat =inputdata["startLocationLat"]
        if "startLocationLong" in inputdata:
                if inputdata['startLocationLong'] != "":
                    startLocationLong =inputdata["startLocationLong"]
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
            userName=data1['result']['name']


            whereCondition222="  driverId= '"+str(driverId)+"' "
            data11= databasefile.SelectQuery("driverMaster",columns,whereCondition222)
            print(data11,'--data')
            driverName=data11['result']['name']
            drivermobile=data11['result']['mobileNo']
            
            R = 6373.0
            print(R,'R')
            fromlongitude2= startLocationLong
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
            bookingDetails['result']['userName']=userName
            if (bookingDetails!='0'):  
                print('Entered')
                client = mqtt.Client()
                client.connect("localhost",1883,60)
                topic=str(userId)+"/booking"
                client.publish(topic, str(bookingDetails)) 
                #bookRide["message"]="ride booked Successfully" 
                client.disconnect()
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
        commonfile.writeLog("driverArrive",inputdata,0)
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
            column=" status=0 "
            bookRide=databasefile.UpdateQuery("bookAmbulance",column,whereCondition)
            print(bookRide)
            whereCondition222=  " ambulanceId= '"+ str(ambulanceId)+"' "
            columns= "onTrip=0 and onDuty=1"
            bookRide1=databasefile.UpdateQuery("ambulanceRideStatus",columns,whereCondition222)
            if (bookRide!=0):   
                bookRide["message"]="Driver has arrived at your location" 
                columns="(ar.lat)ambulanceLat,(ar.lng)ambulanceLng, bm.ambulanceId,bm.bookingId,bm.driverId,bm.dropOff,bm.dropOffLatitude,bm.dropOffLongitude"
                columns=columns+",bm.finalAmount,bm.status,bm.pickup,bm.pickupLatitude,bm.pickupLongitude,bm.totalDistance,bm.userMobile,am.ambulanceNo "
                columns=columns+",bm.driverMobile"
                whereCondition22=" am.ambulanceId=bm.ambulanceId  and bookingId= '"+str(bookingId)+"'"
                bookingDetails= databasefile.SelectQuery("bookAmbulance bm,ambulanceMaster am,ambulanceRideStatus ar",columns,whereCondition22)
                bookingDetails["message"]="Driver has arrived at your location" 
                client = mqtt.Client()
                client.connect("localhost",1883,60)            
                topic=str(userId)+"/arrive"
                print(topic,"+driverArrive")
                client.publish(topic, str(bookingDetails))
                print(bookingDetails,"@@") 

                return bookingDetails
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


@app.route('/startRide1', methods=['POST'])
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
                client = mqtt.Client()
                client.connect("localhost",1883,60)            
                topic=str(userId)+"/startRide"
                client.publish(topic, str(bookRide1)) 
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

            whereCondition=" and  bm.status=1  and bm.userMobile=um.mobileNo and bm.driverId=dm.driverId "

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

            whereCondition=" and bm.status=2  and bm.userMobile=um.mobileNo and bm.driverId=dm.driverId "

            column="bm.userMobile,bm.totalDistance,bm.finalAmount,bm.bookingId,bm.pickup as tripFrom,bm.dropOff as tripTo,date_format(bm.ateCreate,'%Y-%m-%d %H:%i:%s')startTime,dm.name as driverName,um.name as userName"
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

            whereCondition=" and bm.status=0 and bm.userMobile=um.mobileNo and bm.driverId=dm.driverId "

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


@app.route('/myrides', methods=['POST'])
def myrides():
    try:
        inputdata =  commonfile.DecodeInputdata(request.get_data())
        startlimit,endlimit="",""
        whereCondition2=""
       
        commonfile.writeLog("myrides",inputdata,0)
        print('aa')
        msg="1"
        if msg == "1":
            if "startLimit" in inputdata:
                if inputdata['startLimit'] != "":
                    startlimit =str(inputdata["startLimit"])
                
            if "endLimit" in inputdata:
                if inputdata['endLimit'] != "":
                    endlimit =str(inputdata["endLimit"])

                 
            if "userId" in inputdata:
                if inputdata['userId'] != "":
                    userId =str(inputdata["userId"])

            if "bookingId" in inputdata:
                if inputdata['bookingId'] != "":
                    bookingId =str(inputdata["bookingId"])
                    whereCondition2=" and bm.bookingId= '"+ str(bookingId)+"'"

            orderby="bm.id"                

                    



            whereCondition="  and  bm.userId=um.userId and bm.driverId=dm.driverId and um.userId='"+str(userId)+"' "+whereCondition2

            column="bm.id,bm.userMobile,bm.drivermobile,bm.bookingId,bm.pickup as tripFrom,bm.dropOff as tripTo,date_format(bm.ateCreate,'%Y-%m-%d %H:%i:%s')startTime,dm.name as driverName,um.name as userName,bm.status,bm.finalAmount,bm.totalDistance"
            data=databasefile.SelectQueryOrderby("bookAmbulance as bm,userMaster as um,driverMaster as dm",column,whereCondition,"",startlimit,endlimit,orderby)
            print(data,"--------------------------------------------------")
            countdata=databasefile.SelectQuery4("bookAmbulance as bm,userMaster as um,driverMaster as dm",column,whereCondition)

            whereCondition3="  and  bm.userId=um.userId and bm.driverId=dm.driverId and um.userId='"+str(userId)+"' "+whereCondition2

            column2="bm.id,bm.userMobile,bm.drivermobile,bm.bookingId,bm.pickup as tripFrom,bm.dropOff as tripTo,date_format(bm.dateCreate,'%Y-%m-%d %H:%i:%s')startTime,dm.name as driverName,um.name as userName,bm.status,bm.finalAmount,bm.totalDistance"
            data2=databasefile.SelectQueryOrderby("bookResponder as bm,userMaster as um,driverMaster as dm",column2,whereCondition3,"",startlimit,endlimit,orderby)
            print(data,"--------------------------------------------------")
            countdata2=databasefile.SelectQuery4("bookResponder as bm,userMaster as um,driverMaster as dm",column2,whereCondition3)
            
            if (data2['status']=='false'):
                data2['result']=[]
                
           

            if (data['status']!='false'): 
                Data = {"result":{"ambulance":data['result'],"responder":data2['result']},"status":"true","message":"","ambulanceCount":len(countdata),"respondercount":len(countdata2)}

                          
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





@app.route('/myResponder', methods=['POST'])
def myrides1():
    try:
        inputdata =  commonfile.DecodeInputdata(request.get_data())
        startlimit,endlimit="",""
        whereCondition2=""
       
        commonfile.writeLog("myResponder",inputdata,0)
        msg="1"
        if msg == "1":
            if "startLimit" in inputdata:
                if inputdata['startLimit'] != "":
                    startlimit =str(inputdata["startLimit"])
                
            if "endLimit" in inputdata:
                if inputdata['endLimit'] != "":
                    endlimit =str(inputdata["endLimit"])

                 
            if "userId" in inputdata:
                if inputdata['userId'] != "":
                    userId =str(inputdata["userId"])

            if "bookingId" in inputdata:
                if inputdata['bookingId'] != "":
                    bookingId =str(inputdata["bookingId"])
                    whereCondition2=" and bm.bookingId= '"+ str(bookingId)+"'"

            orderby="bm.id"                

                    



            whereCondition="  and  bm.userId=um.userId and bm.driverId=dm.driverId and um.userId='"+str(userId)+"' "+whereCondition2

            column="bm.id,bm.userMobile,bm.drivermobile,bm.bookingId,bm.pickup as tripFrom,bm.dropOff as tripTo,date_format(bm.dateCreate,'%Y-%m-%d %H:%i:%s')startTime,dm.name as driverName,um.name as userName,bm.status,bm.finalAmount,bm.totalDistance"
            data=databasefile.SelectQueryOrderby("bookResponder as bm,userMaster as um,driverMaster as dm",column,whereCondition,"",startlimit,endlimit,orderby)
            print(data,"--------------------------------------------------")
            countdata=databasefile.SelectQuery4("bookResponder as bm,userMaster as um,driverMaster as dm",column,whereCondition)
           
            if (data['status']!='false'): 
                Data = {"result":data['result'],"status":"true","message":"","totalCount":len(countdata)}

                          
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

@app.route('/myTrip', methods=['POST'])
def myTrip():
    try:
        inputdata =  commonfile.DecodeInputdata(request.get_data())
        startlimit,endlimit="",""
        whereCondition2=""
       
        commonfile.writeLog("myTrip",inputdata,0)
        msg="1"
        if msg == "1":
            if "startLimit" in inputdata:
                if inputdata['startLimit'] != "":
                    startlimit =str(inputdata["startLimit"])
                
            if "endLimit" in inputdata:
                if inputdata['endLimit'] != "":
                    endlimit =str(inputdata["endLimit"])

                 
            if "userId" in inputdata:
                if inputdata['userId'] != "":
                    userId =str(inputdata["userId"])
            if "bookingId" in inputdata:
                if inputdata['bookingId'] != "":
                    bookingId =str(inputdata["bookingId"])
                    whereCondition2=" and bm.bookingId= '"+ str(bookingId)+"'"

            orderby="bm.id"                

                    



            whereCondition="  and  bm.userId=um.userId and bm.driverId=dm.driverId and dm.driverId='"+str(userId)+"' "+whereCondition2

            column="bm.id,bm.userMobile,bm.drivermobile,bm.bookingId,bm.pickup as tripFrom,bm.dropOff as tripTo,date_format(bm.ateCreate,'%Y-%m-%d %H:%i:%s')startTime,dm.name as driverName,um.name as userName,bm.status,bm.finalAmount,bm.totalDistance"
            data=databasefile.SelectQueryOrderby("bookAmbulance as bm,userMaster as um,driverMaster as dm",column,whereCondition,"",startlimit,endlimit,orderby)
            print(data,"--------------------------------------------------")
            countdata=databasefile.SelectQuery4("bookAmbulance as bm,userMaster as um,driverMaster as dm",column,whereCondition)
           
            if (data['status']!='false'): 
                Data = {"result":data['result'],"status":"true","message":"","totalCount":len(countdata)}

                          
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

@app.route('/endRide1', methods=['POST'])
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





@app.route('/cancelRide1', methods=['POST'])
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
            inputdata =  commonfile.DecodeInputdata(request.get_data())  
           

            if "driverId" in inputdata:
                if inputdata['driverId'] != "":
                    driverId =str(inputdata["driverId"])
                    WhereCondition = WhereCondition + " and dm.driverId= '"+str(driverId)+ "' "

            orderby="dm.id"        

            column="dm.name,dm.id,dm.mobileNo,dm.profilePic,am.ambulanceNo,am.ambulanceId,um.email,ars.lat,ars.lng,ars.onDuty,ars.onTrip,dm.currentLocation as address,date_format(dm.dateCreate,'%Y-%m-%d %H:%i:%s')joiningDate,dm.status as status,dm.driverId as driverId"
            whereCondition=" and dm.driverId=am.driverId  and am.ambulanceId=ars.ambulanceId  and dm.status<>'2' " + WhereCondition
            data=databasefile.SelectQueryOrderby("driverMaster as dm,ambulanceMaster as am,ambulanceRideStatus as ars,userMaster um",column,whereCondition,"",startlimit,endlimit,orderby)
            
            print(data)
            whereCondition2=" dm.driverId=am.driverId  and am.ambulanceId=ars.ambulanceId  and dm.status<>'2' " +WhereCondition
            countdata=databasefile.SelectQuery1("driverMaster as dm,ambulanceMaster as am,ambulanceRideStatus as ars,userMaster um",column,whereCondition2)


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
                    whereCondition2222=" driverId = '"+str(d1)+ "' "
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
                        if data122['status']=='false':
                            i['tripCount']=0
                        else:
                            tripcount=data122['result']['count']
                            i['tripCount']=tripcount
                    count=len(countdata)        

                    Data = {"result":{"driverDetails":data['result'],"totaldriverCount":count,"dashboard":{"cancelledTripCount":y,"bookedTripCount":y2,"totalEarning":y3,"newsUsers":y4},"userReviews":"No data Available"},"status":"true","message":""}
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
          
            driverId = str(inputdata["driverId"])
           
            # column="status"
            # whereCondition= "   driverId = " + str(userId)+ " "
            # data=databasefile.SelectQuery1("driverMaster",column,whereCondition)
            # print(data)
            # if (data !=0):
            #     if data[0]['status']==0:
            #         print('111111111111111111')


            column="status='1'"
            whereCondition= "  driverId = '" + str(driverId)+ "' "
            output1=databasefile.UpdateQuery("driverMaster",column,whereCondition)
            output=output1
            if output!='0':
                column=  " deviceKey "
                whereCondition= " userId = '" + str(driverId) + "'"
                deviceKey=databasefile.SelectQuery("userMaster",column,whereCondition)
                deviceKey=deviceKey["result"]["deviceKey"]




                a = notification.notification1(deviceKey)
                Data = {"status":"true","message":"","result":output["result"]}                  
                return Data
            else:
                return commonfile.Errormessage() 

                # else:
                #     column="status='0'"
                #     whereCondition= "  driverId = " + str(userId)+ " "
                #     output1=databasefile.UpdateQuery("driverMaster",column,whereCondition)
                #     output=output1    
                #     if output!='0':
                #         Data = {"status":"true","message":"","result":output["result"]}                  
                #         return Data
                #     else:
                #         return commonfile.Errormessage()
            #
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

@app.route('/updateDriverLatLong', methods=['POST'])
def updateDriverLatLong():
    try:
        #print('Hello')
        inputdata=commonfile.DecodeInputdata(request.get_data())
        #print(inputdata,'inputdata')
        keyarr = ['driverId']
       
        # inputdata =  commonfile.DecodeInputdata(request.get_data()) 
        startlimit,endlimit="",""

        commonfile.writeLog("updateDriverLatLong",inputdata,0)
        msg = commonfile.CheckKeyNameBlankValue(keyarr,inputdata)
        #print(msg,'msg')
       
        if msg == "1":

            if 'lat' in inputdata:
                lat=inputdata["lat"]

            if 'lng' in inputdata:
                lng=inputdata["lng"]

            if 'driverId' in inputdata:
                driverId=inputdata["driverId"]

            columns="ambulanceId"
            WhereCondition = " driverId = '" + str(driverId) + "'"
            data111=databasefile.SelectQuery('ambulanceMaster',columns,WhereCondition)
            print("1111111111")
            if data111['status'] != 'false':
                print("222222222222")
                
                ambulanceId=data111['result']['ambulanceId']
                WhereCondition2=" ambulanceId= '" + str(ambulanceId) + "'"
                columns23="lat='" + str(lat) + "',lng='" + str(lng) + "'"
                data122=databasefile.UpdateQuery('ambulanceRideStatus',columns23,WhereCondition2)
                print("333333333333")
                if data122 != "0":
                    data11={"result":"","message":"Updated successfully","status":"true"}
                    return data11

                else:
                    print("4444444444")
                    data11={"result":"","message":"Not existed  in data","status":"false"}
            
                    return data11
            else:
                data={"result":"","message":"please enter keys lat,lng & driverId","status":"false"}
                return data


                        
               
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

            WhereCondition = "  driverId = '" + str(userId) + "' "
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


@app.route('/deleteAmbulance', methods=['POST'])
def deleteAmbulance():
    try:
        inputdata =  commonfile.DecodeInputdata(request.get_data())
        startlimit,endlimit="",""
        keyarr = ['driverId']
        print(inputdata,"B")
        commonfile.writeLog("deleteAmbulance",inputdata,0)
        print('C')
        msg = commonfile.CheckKeyNameBlankValue(keyarr,inputdata)
        if msg =="1":
            
            userId=inputdata["driverId"]
            column="status=1"

            WhereCondition = "  driverId = '" + str(userId) + "' "
            data=databasefile.UpdateQuery("ambulanceMaster",column,WhereCondition)
           

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








#==================================hospitaladmins==========================

@app.route('/addHospitalAdmin', methods=['POST'])
def addHospitalAdmin():
    try:
        inputdata =  commonfile.DecodeInputdata(request.get_data()) 
        startlimit,endlimit="",""
        keyarr = ["name","email","password","userTypeId","gender"]
        commonfile.writeLog("hospitalAdminSignup",inputdata,0)
        msg = commonfile.CheckKeyNameBlankValue(keyarr,inputdata)
       
        if msg == "1":
            name,email,password,userTypeId,mobileNo,gender="","","","","",""
            column,values="",""
            
            UserId = (commonfile.CreateHashKey(mobileNo,userTypeId)).hex
            
           
            
            if 'email' in inputdata:
                email=inputdata["email"]
                column=column+" ,email"
                values=values+"','"+str(email)
            if 'name' in inputdata:
                name=inputdata["name"]
                column=column+" ,name"
                values=values+"','"+str(name)
            if 'password' in inputdata:
                password=inputdata["password"]
                column=column+" ,password"
                values=values+"','"+str(password)
            if 'mobileNo' in inputdata:
                mobileNo=inputdata["mobileNo"]
                column=column+" ,mobileNo"
                values=values+"','"+str(mobileNo)
            if 'userTypeId' in inputdata:
                userTypeId=inputdata["userTypeId"]
                column=column+" ,userTypeId"
                values=values+"','"+str(userTypeId)
            
            if 'hospitalId' in inputdata:
                hospitalId=inputdata["hospitalId"]
                column=column+" ,hospitalId"
                values=values+"','"+str(hospitalId)
            if 'gender' in inputdata:
                gender=inputdata["gender"]
                column=column+" ,gender"
                values=values+"','"+str(gender)
            
            WhereCondition = " and email = '" + str(email) + "'"
            count = int(databasefile.SelectCountQuery("hospitalUserMaster",WhereCondition,""))
            if count>0:
                return {"status":"true","message":"Record Already Exist","result":[]}

            else:
                print("1111111111111")
                column=" userId "+column
                values="'"+str(UserId)+values+"'"
                data=databasefile.InsertQuery("hospitalUserMaster",column,values)
             

                if data != "0":
                    Data = {"status":"true","message":"","result":data}                  
                    return Data
                else:
                    return commonfile.Errormessage()
                        
        else:
            return msg 
    except Exception as e :
        print("Exception---->" +str(e))           
        output = {"status":"false","message":"something went wrong","result":""}
        return output


@app.route('/updateHospitalAdmin', methods=['POST'])
def updateHospitalAdmin():
    try:
        inputdata =  commonfile.DecodeInputdata(request.get_data()) 
        startlimit,endlimit="",""
        keyarr = ["name","email","password",'userTypeId','hospitalId']
        commonfile.writeLog("hospitalAdminSignup",inputdata,0)
        msg = commonfile.CheckKeyNameBlankValue(keyarr,inputdata)
       
        if msg == "1":
            name,email,password,userTypeId,mobileNo,gender="","","","","",""
            column,values="",""
            
            # UserId = (commonfile.CreateHashKey(mobileNo,userTypeId)).hex
            
            
            # WhereCondition = " and email = '" + str(email) + "'"
            # count = databasefile.SelectCountQuery("hospitalUserMaster",WhereCondition,"")

            
            if 'email' in inputdata:
                email=inputdata["email"]
                column=" email='"+str(email)+"' " 
            if 'name' in inputdata:
                name=inputdata["name"]
                column=column+" ,name='"+str(name)+"' "  
            if 'password' in inputdata:
                password=inputdata["password"]
                column=column+" ,password= '"+str(password)+"' "                
            if 'mobileNo' in inputdata:
                mobileNo=inputdata["mobileNo"]
                column=column+" ,mobileNo='"+str(mobileNo)+"' "  
               
            if 'userTypeId' in inputdata:
                userTypeId=inputdata["userTypeId"]
                column=column+" ,usertypeId= '"+str(userTypeId) +"' " 
               
            
            if 'hospitalId' in inputdata:
                hospitalId=inputdata["hospitalId"]
                column=column+" ,hospitalId= '"+str(hospitalId) +"' " 

            if 'gender' in inputdata:
                gender=inputdata["gender"] 
                column=column+" ,gender= '"+str(gender) +"' " 


              
            if 'Id' in inputdata:
                userId=inputdata["Id"]    
                
            
            whereCondition= " id= '"+str(userId)+"' "
          
            data=databasefile.UpdateQuery("hospitalUserMaster",column,whereCondition)
         

            if data != "0":
                Data = {"status":"true","message":"data Updated Successfully","result":"data Updated Successfully"}                  
                return Data
            else:
                return commonfile.Errormessage()
                        
        else:
            return msg 
    except Exception as e :
        print("Exception---->" +str(e))           
        output = {"status":"false","message":"something went wrong","result":""}
        return output        
   

@app.route('/deletehospitalAdmin', methods=['POST'])
def deleteHospital1():
    try:
        inputdata =  commonfile.DecodeInputdata(request.get_data())
        startlimit,endlimit="",""
        keyarr = ['Id']
        print(inputdata,"B")
        commonfile.writeLog("deletehospitalAdmin",inputdata,0)
        print('C')
        msg = commonfile.CheckKeyNameBlankValue(keyarr,inputdata)
        if msg =="1":
            
            userId=int(inputdata["Id"])
            column="status=2"

            WhereCondition = "  id= " + str(userId) + " "
            data=databasefile.UpdateQuery("hospitalUserMaster",column,WhereCondition)
           

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


@app.route('/updateHospitalAdminStatus', methods=['POST'])
def updateHospitalAdminStatus():
    try:
        inputdata =  commonfile.DecodeInputdata(request.get_data())
        startlimit,endlimit="",""
        keyarr = ['Id']
        print(inputdata,"B")
        commonfile.writeLog("updateHospitalAdminStatus",inputdata,0)
        msg = commonfile.CheckKeyNameBlankValue(keyarr,inputdata)
        if msg =="1":
          
            driverId = int(inputdata["Id"])
           
           
            column="status"
            whereCondition= "   id = " + str(driverId)+ " "
            data=databasefile.SelectQuery1("hospitalUserMaster",column,whereCondition)
            print(data)
            if (data !=0):
                if data[0]['status']==0:
            #         print('111111111111111111')
                    column="status='1'"
                    whereCondition= "  id = '" + str(driverId)+ "' "
                    output1=databasefile.UpdateQuery("hospitalUserMaster",column,whereCondition)
                    output=output1
                    if output!='0':
                        Data = {"status":"true","message":"","result":output["result"]}                  
                        return Data
                    else:
                        return commonfile.Errormessage() 

                else:
                    column="status='0'"
                    whereCondition= "  id = " + str(driverId)+ " "
                    output1=databasefile.UpdateQuery("hospitalUserMaster",column,whereCondition)
                    output=output1    
                    if output!='0':
                        Data = {"status":"true","message":"","result":output["result"]}                  
                        return Data
                    else:
                        return commonfile.Errormessage()
            
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




@app.route('/allhospitalUserMaster', methods=['post'])
def allhospitalUserMaster():
    try:
        msg = "1"
        if msg=="1":
            inputdata =  commonfile.DecodeInputdata(request.get_data())
            startlimit,endlimit="",""
            whereCondition3=""
            if "startLimit" in inputdata:
                if inputdata['startLimit'] != "":
                    startlimit =str(inputdata["startLimit"])
                
            if "endLimit" in inputdata:
                if inputdata['endLimit'] != "":
                    endlimit =str(inputdata["endLimit"])


            if "Id" in inputdata:
                if inputdata['Id'] != "":
                    Id =int(inputdata["Id"])
                    whereCondition3=" and hum.id = '"+str(Id)+"' " 


            orderby="hum.id"



            column="hum.name,hum.userId,hum.status,hum.hospitalId,hum.mobileNo,hum.password,hum.gender,hum.email,hum.usertypeId,hum.id as Id,hm.hospitalName as hospitalName"
            whereCondition="  and hum.status<>'2'  and hum.hospitalId=hm.id"+whereCondition3
            data=databasefile.SelectQueryOrderby("hospitalUserMaster as hum,hospitalMaster as hm",column,whereCondition,"",startlimit,endlimit,orderby)
            
            totalCount= databasefile.SelectQuery4("hospitalUserMaster as hum,hospitalMaster as hm",column,whereCondition)
            if (data['status']!='false'):   
                count=len(totalCount)

                Data = {"result":data['result'],"status":"true","totalCount":count}
                return Data
            else:
                output = {"result":"No Data Found","status":"true","message":"No Data Found"}
                return output
        else:
            return msg
    except Exception as e :
        print("Exception---->" + str(e))    
        output = {"result":"something went wrong","status":"false"}
        return output


@app.route('/hospitalAdminLogin', methods=['POST'])
def hospitalAdminLogin():
    try:
        inputdata =  commonfile.DecodeInputdata(request.get_data())
        startlimit,endlimit="",""
        keyarr = ['email','password']
        commonfile.writeLog("hospitalAdminLogin",inputdata,0)
        msg = commonfile.CheckKeyNameBlankValue(keyarr,inputdata)
        if msg == "1":
            email = inputdata["email"]
            password = inputdata["password"]
            column=  "us.mobileNo,us.name,us.userTypeId,um.usertype,us.userId,us.email,us.hospitalId"
            whereCondition= " us.email = '" + str(email) + "' and us.password = '" + str(password) + "'  and  us.userTypeId=um.id"
            loginuser=databasefile.SelectQuery("hospitalUserMaster as us,usertypeMaster as um",column,whereCondition)
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







@app.route('/currentBooking', methods=['post'])
def allhospitalUserMaster12():
    try:
        msg = "1"
        if msg=="1":
            inputdata =  commonfile.DecodeInputdata(request.get_data())
            startlimit,endlimit="",""
            whereCondition3=""
            if "startLimit" in inputdata:
                if inputdata['startLimit'] != "":
                    startlimit =str(inputdata["startLimit"])
                
            if "endLimit" in inputdata:
                if inputdata['endLimit'] != "":
                    endlimit =str(inputdata["endLimit"])


            if "hospitalId" in inputdata:
                if inputdata['hospitalId'] != "":
                    hospitalId =int(inputdata["hospitalId"])
                    whereCondition3=" and hum.hospitalId = '"+str(hospitalId)+"' " 

            if ("bookingId" in inputdata) and ("hospitalId" in inputdata):
                if (inputdata['hospitalId'] != "") and (inputdata['bookingId'] != ""):
                    hospitalId =int(inputdata["hospitalId"])
                    bookingId =int(inputdata["bookingId"])
                    whereCondition3=" and hum.hospitalId = '"+str(hospitalId)+"' and  hum.bookingId = '"+str(bookingId)+"'  " 


            orderby="hum.id"



            column="hum.userMobile,um.name as userName,dm.name as driverName,hum.hospitalId,hum.driverMobile,hum.userId,hum.driverId,hum.pickup,hum.dropOff,hum.bookingId,hum.totalDistance,hum.finalAmount,date_format(hum.ateCreate,'%Y-%m-%d %H:%i:%s')rideDate,hum.ambulanceId"
            whereCondition="  and  hum.status='1' and  um.userId=hum.userId and dm.driverId=hum.driverId "+whereCondition3
            data=databasefile.SelectQueryOrderby("bookAmbulance as hum,userMaster as um,driverMaster as dm",column,whereCondition,"",startlimit,endlimit,orderby)
            
            totalCount= databasefile.SelectQuery4("bookAmbulance as hum,userMaster as um,driverMaster as dm",column,whereCondition)
            if (data['status']!='false'):   
                count=len(totalCount)

                Data = {"result":data['result'],"status":"true","totalCount":count}
                return Data
            else:
                output = {"result":"No Data Found","status":"true","message":"No Data Found"}
                return output
        else:
            return msg
    except Exception as e :
        print("Exception---->" + str(e))    
        output = {"result":"something went wrong","status":"false"}
        return output

@app.route('/pastBooking', methods=['post'])
def allhospitalUserMaster1():
    try:
        msg = "1"
        if msg=="1":
            inputdata =  commonfile.DecodeInputdata(request.get_data())
            startlimit,endlimit="",""
            whereCondition3=""
            if "startLimit" in inputdata:
                if inputdata['startLimit'] != "":
                    startlimit =str(inputdata["startLimit"])
                
            if "endLimit" in inputdata:
                if inputdata['endLimit'] != "":
                    endlimit =str(inputdata["endLimit"])


            if "hospitalId" in inputdata:
                if inputdata['hospitalId'] != "":
                    hospitalId =int(inputdata["hospitalId"])
                    whereCondition3=" and hum.hospitalId = '"+str(hospitalId)+"' " 

            if ("bookingId" in inputdata) and ("hospitalId" in inputdata):
                if (inputdata['hospitalId'] != "") and (inputdata['bookingId'] != ""):
                    hospitalId =int(inputdata["hospitalId"])
                    bookingId =int(inputdata["bookingId"])
                    whereCondition3=" and hum.hospitalId = '"+str(hospitalId)+"' and  hum.bookingId = '"+str(bookingId)+"'  " 


            orderby="hum.id"



            column="hum.userMobile,um.name as userName,dm.name as driverName,hum.hospitalId,hum.driverMobile,hum.userId,hum.driverId,hum.pickup,hum.dropOff,hum.bookingId,hum.totalDistance,hum.finalAmount,date_format(hum.ateCreate,'%Y-%m-%d %H:%i:%s')rideDate,hum.ambulanceId"
            whereCondition="  and  hum.status='2' and um.userId=hum.userId and dm.driverId=hum.driverId "+whereCondition3
            data=databasefile.SelectQueryOrderby("bookAmbulance as hum,userMaster as um,driverMaster as dm",column,whereCondition,"",startlimit,endlimit,orderby)
            
            totalCount= databasefile.SelectQuery4("bookAmbulance as hum,userMaster as um,driverMaster as dm",column,whereCondition)
            if (data['status']!='false'):   
                count=len(totalCount)

                Data = {"result":data['result'],"status":"true","totalCount":count}
                return Data
            else:
                output = {"result":"No Data Found","status":"true","message":"No Data Found"}
                return output
        else:
            return msg
    except Exception as e :
        print("Exception---->" + str(e))    
        output = {"result":"something went wrong","status":"false"}
        return output





#==================================hospitaladmins==========================



@app.route('/getFareManagement', methods=['POST'])
def getFareManagement():

    try:
        msg = "1"
        if msg=="1":
            inputdata =  commonfile.DecodeInputdata(request.get_data())
            startlimit,endlimit="",""
            whereCondition3="  "

            if "startLimit" in inputdata:
                if inputdata['startLimit'] != "":
                    startlimit =str(inputdata["startLimit"])
                
            if "endLimit" in inputdata:
                if inputdata['endLimit'] != "":
                    endlimit =str(inputdata["endLimit"])


            if "id" in inputdata:
                if inputdata['id'] != "":
                    Id =int(inputdata["id"])
                    whereCondition3=" and Fm.id = '"+str(Id)+"' "

            if "categoryId" in inputdata:
                if inputdata['categoryId'] != "":
                    categoryId =int(inputdata["categoryId"])
                    whereCondition3=" and Fm.categoryId= '"+str(categoryId)+"' "

            column="Fm.id,Fm.fare as farePerKM,am.ambulanceType as category,Fm.categoryId as ambType,Fm.minimumFare as minFare,Fm.minimumDistance as minDistance,Fm.waitingFare as waitFare"
            whereCondition="Fm.categoryId=am.id"+whereCondition3
            data=databasefile.SelectQuery1("fareManagement as Fm,ambulanceMode as am",column,whereCondition)
        
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


@app.route('/addFare', methods=['POST'])
def addFare():
    try:
        inputdata =  commonfile.DecodeInputdata(request.get_data())
        startlimit,endlimit="",""
        keyarr = ['farePerKM','ambType','minFare','minDistance','waitFare']
        commonfile.writeLog("addFare",inputdata,0)
        msg = commonfile.CheckKeyNameBlankValue(keyarr,inputdata)
        if msg=="1":
            fare= inputdata["farePerKM"]
            categoryId= inputdata["ambType"]
            minimumFare= inputdata["minFare"]
            minimumDistance= inputdata["minDistance"]
            waitingFare= inputdata["waitFare"]

            column="*"
            whereCondition= "categoryId='"+str(categoryId)+ "'"
            data=databasefile.SelectQuery("fareManagement",column,whereCondition)
            print(data,'data')
            if data['status']=='false':
                column="fare,categoryId,minimumFare,minimumDistance,waitingFare"
                values="'"+str(fare)+"', '"+str(categoryId)+"','"+str(minimumFare)+"','"+str(minimumDistance)+"','"+str(waitingFare)+"'"
                insertdata=databasefile.InsertQuery("fareManagement",column,values)
               

                output= {"result":"User Added Successfully","message":"Inserted Successfully","status":"true"}
                return output
            else:
                whereCondition= "categoryId='"+str(categoryId)+ "'"
                data2=databasefile.DeleteQuery("fareManagement",whereCondition)

                column="fare,categoryId,minimumFare,minimumDistance,waitingFare"
                values="'"+str(fare)+"', '"+str(categoryId)+"','"+str(minimumFare)+"','"+str(minimumDistance)+"','"+str(waitingFare)+"'"
                insertdata=databasefile.InsertQuery("fareManagement",column,values)

                output= {"result":"User Added Successfully","message":"Inserted Successfully","status":"true"}
                return output

            
               
        else:

            return msg 
    except Exception as e :
        print("Exception---->" + str(e))    
        output = {"result":"something went wrong","status":"false"}
        return output



@app.route('/deletefareManagement', methods=['POST'])
def fareManagement():
    try: 

        inputdata =  commonfile.DecodeInputdata(request.get_data()) 
        WhereCondition=""
  
        if len(inputdata) > 0:           
            commonfile.writeLog("deletefareManagement",inputdata,0)
        
        keyarr = ['id']
        msg = commonfile.CheckKeyNameBlankValue(keyarr,inputdata)
        if "id" in inputdata:
            if inputdata['id'] != "":
                Id =inputdata["id"] 
                WhereCondition=WhereCondition+" and id='"+str(Id)+"'" 
        if msg == "1":                        
            
            data = databasefile.DeleteQuery("fareManagement",WhereCondition)

            if data != "0":
                return data
            else:
                return commonfile.Errormessage()
        else:
            return msg

    except Exception as e :
        print("Exception--->" + str(e))                                  
        return commonfile.Errormessage() 

########################################START########################################################


@app.route('/startRide', methods=['POST'])
def startRide1():
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
                
               
            
            
            
                columns="(ar.lat)ambulanceLat,(ar.lng)ambulanceLng, bm.ambulanceId,bm.bookingId,bm.driverId,bm.dropOff,bm.dropOffLatitude,bm.dropOffLongitude"
                columns=columns+",bm.finalAmount,bm.pickup,bm.status,bm.pickupLatitude,bm.pickupLongitude,bm.totalDistance,bm.userMobile,am.ambulanceNo "
                columns=columns+",bm.driverMobile"
                whereCondition22=" am.ambulanceId=bm.ambulanceId  and bookingId= '"+str(bookingId)+"'"
                bookingDetails= databasefile.SelectQuery("bookAmbulance bm,ambulanceMaster am,ambulanceRideStatus ar",columns,whereCondition22)
                print(bookingDetails,"================")
                
                bookingDetails["message"]="ride started Successfully"  
                if (bookingDetails!='0'):  
                    print('Entered')
                    client = mqtt.Client()
                    client.connect("localhost",1883,60)
                    topic=str(userId)+"/startRide"
                    client.publish(topic, str(bookingDetails)) 
                    #bookRide["message"]="ride started Successfully" 
                    client.disconnect()
                    return bookingDetails
                else:
                    data={"result":"","message":"No data Found","status":"false"}
                    
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

@app.route('/endRide', methods=['POST'])
def endRide1():
    try:
        inputdata =  commonfile.DecodeInputdata(request.get_data())
        startlimit,endlimit="",""
        keyarr = ["ambulanceId","bookingId"]
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
            column=" status=2 "
            bookRide=databasefile.UpdateQuery("bookAmbulance",column,whereCondition)
            whereCondition222=  " ambulanceId= '"+ str(ambulanceId)+"' "
            columns= "onTrip=0 and onDuty=1"
            bookRide1=databasefile.UpdateQuery("ambulanceRideStatus",columns,whereCondition222)
            if (bookRide!=0):   
                bookRide["message"]="ride Ended Successfully"             
               
            
            
                
                columns="(ar.lat)ambulanceLat,(ar.lng)ambulanceLng, bm.ambulanceId,bm.bookingId,bm.driverId,bm.dropOff,bm.dropOffLatitude,bm.dropOffLongitude"
                columns=columns+",bm.finalAmount,bm.pickup,bm.status,bm.pickupLatitude,bm.pickupLongitude,bm.totalDistance,bm.userMobile,am.ambulanceNo "
                columns=columns+",bm.driverMobile"
                whereCondition22=" am.ambulanceId=bm.ambulanceId  and bookingId= '"+str(bookingId)+"'"
                bookingDetails= databasefile.SelectQuery("bookAmbulance bm,ambulanceMaster am,ambulanceRideStatus ar",columns,whereCondition22)
                print(bookingDetails,"================")
                bookingDetails["message"]="ride Ended Successfully"
               
                if (bookingDetails!='0'):  
                    print('Entered')
                    client = mqtt.Client()
                    client.connect("localhost",1883,60)
                    topic=str(userId)+"/endRide"
                    client.publish(topic, str(bookingDetails)) 
                    #bookRide["message"]="ride ended Successfully" 
                    client.disconnect()
                    return bookingDetails
                else:
                    data={"result":"","message":"No data Found","status":"false"}
                    
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





@app.route('/cancelRide', methods=['POST'])
def cancelRide1():
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
            column=" status=3  , canceledUserId='"+str(userId)+"'"
            bookRide=databasefile.UpdateQuery("bookAmbulance",column,whereCondition)
            whereCondition222=  " ambulanceId= '"+ str(ambulanceId)+"' "
            columns= "onTrip=0 and onDuty=1"
            bookRide1=databasefile.UpdateQuery("ambulanceRideStatus",columns,whereCondition222)
            if (bookRide!=0):   
                bookRide["message"]="ride Cancelled Successfully"             
                

           
                
                columns="(ar.lat)ambulanceLat,(ar.lng)ambulanceLng, bm.ambulanceId,bm.bookingId,bm.driverId,bm.dropOff,bm.dropOffLatitude,bm.dropOffLongitude"
                columns=columns+",bm.finalAmount,bm.status,bm.pickup,bm.pickupLatitude,bm.pickupLongitude,bm.totalDistance,bm.userMobile,am.ambulanceNo "
                columns=columns+",bm.driverMobile"
                whereCondition22=" am.ambulanceId=bm.ambulanceId  and bookingId= '"+str(bookingId)+"'"
                bookingDetails= databasefile.SelectQuery("bookAmbulance bm,ambulanceMaster am,ambulanceRideStatus ar",columns,whereCondition22)
                print(bookingDetails,"================")
                bookingDetails["message"]="ride Cancelled Successfully" 

               
                if (bookingDetails!='0'):  
                    print('Entered')
                    client = mqtt.Client()
                    client.connect("localhost",1883,60)
                    topic=str(userId)+"/cancelRide"
                    client.publish(topic, str(bookingDetails)) 
                    #bookRide["message"]="ride Cancelled" 
                    client.disconnect()
                    return bookingDetails
                else:
                    data={"result":"","message":"No data Found","status":"false"}
                    
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



########################################END##########################################################


@app.route('/empanelmentTypeMaster', methods=['GET'])
def empanelmentTypeMaster():
    try:
        msg = "1"
        if msg=="1":
            column="*"
            whereCondition=""
            data=databasefile.SelectQuery1("empanelmentTypeMaster",column,whereCondition)
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



@app.route('/hospitalLabotaryMaster', methods=['GET'])
def hospitalLabotaryMaster():
    try:
        msg = "1"
        if msg=="1":
            column="*"
            whereCondition=""
            data=databasefile.SelectQuery1("hospitalLabotaryMaster",column,whereCondition)
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



@app.route('/accreditationMaster', methods=['GET'])
def accreditationMaster():
    try:
        msg = "1"
        if msg=="1":
            column="*"
            whereCondition=""
            data=databasefile.SelectQuery1("accreditationMaster",column,whereCondition)
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



@app.route('/hospitalServiceMaster', methods=['GET'])
def hospitalServiceMaster():
    try:
        msg = "1"
        if msg=="1":
            column="*"
            whereCondition=""
            data=databasefile.SelectQuery1("hospitalServiceMaster",column,whereCondition)
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



@app.route('/hospitalTypeMaster', methods=['GET'])
def hospitalTypeMaster():
    try:
        msg = "1"
        if msg=="1":
            column="*"
            whereCondition=""
            data=databasefile.SelectQuery1("hospitalTypeMaster",column,whereCondition)
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



@app.route('/emergencyDepartMentSpecialitiesMaster', methods=['GET'])
def emergencyDepartMentSpecialitiesMaster():
    try:
        msg = "1"
        if msg=="1":
            column="*"
            whereCondition=""
            data=databasefile.SelectQuery1("emergencyDepartMentSpecialitiesMaster",column,whereCondition)
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

#____________

@app.route('/aboutUs', methods=['POST'])
def aboutUs(): 
    try: 
        startlimit,endlimit="",""   
        inputdata =  commonfile.DecodeInputdata(request.get_data())
        aboutId = '1'
        keyarr = ['description','flag']
        commonfile.writeLog("aboutUs",inputdata,0)
        msg = commonfile.CheckKeyNameBlankValue(keyarr,inputdata)
       
        if msg == "1":      
            description = commonfile.EscapeSpecialChar(inputdata["description"])
            flag = inputdata["flag"]
            print('====',flag)
        
            WhereCondition = " "
            count = databasefile.SelectCountQuery("aboutUs",WhereCondition,"")
            
            if int(count) > 0 and flag == 'n':
                print('F')         
                return commonfile.aboutUsDescriptionAlreadyExistMsg()
            else:
                if flag == 'n':
                    columns = " description"          
                    values = " '" + str(description) + "'"       
                    data = databasefile.InsertQuery("aboutUs",columns,values)
                    if data != "0":
                        column = '*'
                        WhereCondition = " and description = '" + str(description) + "'"
                        
                        data11 = databasefile.SelectQuery("aboutUs",column,WhereCondition,"",startlimit,endlimit)
                        return data11
                if flag == 'u':
                    WhereCondition = " and id='" + str(aboutId) + "'"
                    column = " description = '" + str(description) + "'"
                    data = databasefile.UpdateQuery("aboutUs",column,WhereCondition)
                    return data
                else:
                    return commonfile.Errormessage()
        else:
            return msg

    except Exception as e:
        print("Exception--->" + str(e))                                  
        return commonfile.Errormessage() 


@app.route('/deleteAboutUs', methods=['POST'])
def deleteAboutUs():
    try:


        inputdata =  commonfile.DecodeInputdata(request.get_data()) 

        WhereCondition=""
  
        if len(inputdata) > 0:           
            commonfile.writeLog("deleteAboutUs",inputdata,0)
        
        keyarr = ['id']
        msg = commonfile.CheckKeyNameBlankValue(keyarr,inputdata)
        if "id" in inputdata:
            if inputdata['id'] != "":
                Id =inputdata["id"] 
                WhereCondition=WhereCondition+" and id='"+str(Id)+"'" 
        if msg == "1":                        
            
            data = databasefile.DeleteQuery("aboutUs",WhereCondition)

            if data != "0":
                return data
            else:
                return commonfile.Errormessage()
        else:
            return msg

    except Exception as e :
        print("Exception--->" + str(e))                                  
        return commonfile.Errormessage()


@app.route('/allaboutUs', methods=['POST'])
def allaboutUs():
    try:
        columns=" * "
        
        data = databasefile.SelectQueryMaxId("aboutUs",columns)
       

        if data:           
            Data = {"status":"true","message":"","result":data["result"]}
            return Data
        else:
            output = {"status":"false","message":"No Data Found","result":""}
            return output

    except Exception as e :
        print("Exception---->" + str(e))    
        output = {"status":"false","message":"something went wrong","result":""}
        return output


@app.route('/support', methods=['POST'])
def support():
    try:
        inputdata =  commonfile.DecodeInputdata(request.get_data())
        startlimit,endlimit="",""
       
        commonfile.writeLog("support",inputdata,0)
        msg="1"
        if msg == "1":
            if "startLimit" in inputdata:
                if inputdata['startLimit'] != "":
                    startlimit =str(inputdata["startLimit"])
                
            if "endLimit" in inputdata:
                if inputdata['endLimit'] != "":
                    endlimit =str(inputdata["endLimit"])

                 
            if "userId" in inputdata:
                if inputdata['userId'] != "":
                    userId =str(inputdata["userId"])

            orderby="bm.id"                

                    



            whereCondition="  and  bm.userId=um.userId and bm.driverId=dm.driverId and um.userId='"+str(userId)+"' and bm.status='3' "

            column="bm.id,bm.userMobile,bm.userId,bm.driverId,bm.bookingId,bm.pickup as tripFrom,bm.dropOff as tripTo,bm.canceledUserId,date_format(bm.ateCreate,'%Y-%m-%d %H:%i:%s')startTime,dm.name as driverName,um.name as userName,bm.status"
            data=databasefile.SelectQueryOrderby("bookAmbulance as bm,userMaster as um,driverMaster as dm",column,whereCondition,"",startlimit,endlimit,orderby)
            print(data,"--------------------------------------------------")
            countdata=databasefile.SelectQuery4("bookAmbulance as bm,userMaster as um,driverMaster as dm",column,whereCondition)
           
            if (data['status']!='false'): 
                for i in data['result']:
                    if i['canceledUserId'] == i['userId']:
                        i['canceledBy']=i['userName']
                    if i['canceledUserId'] == i['driverId']:
                        i['canceledBy']=i['driverName']

                Data = {"result":data['result'],"status":"true","message":"","totalCount":len(countdata)}

                          
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


#responder______________





@app.route('/getNearByResponder', methods=['POST'])
def getNearByResponder():
    try:
        inputdata =  commonfile.DecodeInputdata(request.get_data())
        startlimit,endlimit="",""
        keyarr = ['startLocationLat','startLocationLong']
        commonfile.writeLog("getNearByResponder",inputdata,0)
        msg = commonfile.CheckKeyNameBlankValue(keyarr,inputdata)
        if msg == "1":
            
           

            
            #============NearByResponder========
            startlat ,startlng,userId= inputdata["startLocationLat"],inputdata["startLocationLong"],""#,inputdata["userId"]
            column=  "d.driverId,d.name, d.mobileNo, a.ambulanceId, a.ambulanceNo, b.lat, b.lng,SQRT(POW(69.1 * (b.lat - "+str(startlat)+"), 2) +POW(69.1 * ("+str(startlng)+" - b.lng) * COS(b.lat / 57.3), 2)) AS distance "
            whereCondition= "and a.driverTypeId=2 and  d.status=1 and b.onTrip=0 and b.onDuty=1 and a.driverId=d.driverId  and b.ambulanceId=a.ambulanceId HAVING distance < 25 "
            orderby="  distance "
            nearByAmbulance=databasefile.SelectQueryOrderbyAsc("ambulanceMaster a, driverMaster d,ambulanceRideStatus as b",column,whereCondition,"",orderby,"","")
            print("nearByAmbulance================================",nearByAmbulance)
            #============NearByResponder========

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


@app.route('/bookResponder', methods=['POST'])
def bookResponder():
    try:
        print('A')
        inputdata =  commonfile.DecodeInputdata(request.get_data())
        startlimit,endlimit="",""
        #inputdata={"ambulanceId":[1,2,3,4],"driverId":[13,14,15,16,17],'startLocationLat':28.583962,'startLocationLong':77.314345,"pickupLocationAddress":" Noida se 15",'dropLocationLat':28.535517,'dropLocationLong':77.391029,"dropLocationAddress":"fortis noida","userId":"8b0e338e522a11ea93d39ebd4d0189fc"}
        # inputdata1={}
        # inputdata1["pickupLocationAddress"]=inputdata["pickupLocationAddress"]
        # inputdata1["dropLocationAddress"]=inputdata["dropLocationAddress"]
        keyarr = ["ambulanceId","id",'startLocationLat','startLocationLong',"pickupLocationAddress",'dropLocationLat','dropLocationLong',"dropLocationAddress","userId"]
        client = mqtt.Client()
        client.connect("localhost",1883,60)

        for i in inputdata["driverId"]:

            #inputdata["driverId"]=str(i)
            #print(inputdata)
            
            
            topic=str(i)+"/booking"
            print(topic)
            print("1")
            #print("=================",topic)
            client.publish(topic, str(inputdata))
            print("2")
        client.disconnect()    
             
        return  {"result":"booking send","status":"True"}
    except KeyError as e:
        print("Exception---->" +str(e))        
        output = {"result":"Input Keys are not Found","status":"false"}
        return output    
    except Exception as e :
        print("Exception---->" +str(e))           
        output = {"result":"something went wrong","status":"false"}
        return output




@app.route('/acceptResponder', methods=['POST'])
def acceptResponder():
    try:
        print('A')
        inputdata =  commonfile.DecodeInputdata(request.get_data())
        print(inputdata)
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
                    print(driverId)
        if "startLocationLat" in inputdata:
                if inputdata['startLocationLat'] != "":
                    startLocationLat =inputdata["startLocationLat"]
        if "startLocationLong" in inputdata:
                if inputdata['startLocationLong'] != "":
                    startLocationLong =inputdata["startLocationLong"]
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


        commonfile.writeLog("bookResponder",inputdata,0)
        msg = commonfile.CheckKeyNameBlankValue(keyarr,inputdata)
        
        if msg == "1":
            print('B')
            columns="mobileNo,name"
            whereCondition22="  userId= '"+str(userId)+"' and userTypeId='2' "
            data1= databasefile.SelectQuery("userMaster",columns,whereCondition22)
            print(data1,'data1')
            usermobile=data1['result']['mobileNo']
            userName=data1['result']['name']


            whereCondition222="  driverId= '"+str(driverId)+"' "
            data11= databasefile.SelectQuery("driverMaster",columns,whereCondition222)
            print(data11,'--data')
            driverName=data11['result']['name']
            drivermobile=data11['result']['mobileNo']
            
            R = 6373.0
            print(R,'R')
            fromlongitude2= startLocationLong
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
            data111=databasefile.InsertQuery('bookResponder',columnqq,values111)
            print(data111,'==data')
            
            columns="(ar.lat)ambulanceLat,(ar.lng)ambulanceLng, bm.ambulanceId,bm.bookingId,bm.driverId,bm.dropOff,bm.dropOffLatitude,bm.dropOffLongitude"
            columns=columns+",bm.finalAmount,bm.pickup,bm.pickupLatitude,bm.pickupLongitude,bm.totalDistance,bm.userMobile,am.ambulanceNo "
            columns=columns+",bm.driverMobile"
            whereCondition22=" am.ambulanceId=bm.ambulanceId  and bookingId= '"+str(bookingId)+"'"
            bookingDetails= databasefile.SelectQuery("bookResponder bm,ambulanceMaster am,ambulanceRideStatus ar",columns,whereCondition22)
            print(bookingDetails,"================")
            bookingDetails["result"]["driverName"]=driverName
            bookingDetails['result']['userName']=userName
            if (bookingDetails!='0'):  
                print('Entered')
                client = mqtt.Client()
                client.connect("localhost",1883,60)
                topic=str(userId)+"/booking"
                client.publish(topic, str(bookingDetails)) 
                #bookRide["message"]="ride booked Successfully" 
                client.disconnect()
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




@app.route('/startResponder', methods=['POST'])
def startResponder():
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
            bookRide=databasefile.UpdateQuery("bookResponder",column,whereCondition)
            whereCondition222=  " ambulanceId= '"+ str(ambulanceId)+"' "
            columns= "onTrip=1 and onDuty=1"
            bookRide1=databasefile.UpdateQuery("ambulanceRideStatus",columns,whereCondition222)
            if (bookRide!=0):   
                bookRide["message"]="ride started Successfully"             
                topic=str(userId)+"/startRide"
                
               
            
            
            
                columns="(ar.lat)ambulanceLat,(ar.lng)ambulanceLng, bm.ambulanceId,bm.bookingId,bm.driverId,bm.dropOff,bm.dropOffLatitude,bm.dropOffLongitude"
                columns=columns+",bm.finalAmount,bm.pickup,bm.status,bm.pickupLatitude,bm.pickupLongitude,bm.totalDistance,bm.userMobile,am.ambulanceNo "
                columns=columns+",bm.driverMobile"
                whereCondition22=" am.ambulanceId=bm.ambulanceId  and bookingId= '"+str(bookingId)+"'"
                bookingDetails= databasefile.SelectQuery("bookResponder bm,ambulanceMaster am,ambulanceRideStatus ar",columns,whereCondition22)
                print(bookingDetails,"================")
                
                bookingDetails["message"]="ride started Successfully"  
                if (bookingDetails!='0'):  
                    print('Entered')
                    client = mqtt.Client()
                    client.connect("localhost",1883,60)
                    topic=str(userId)+"/startRide"
                    client.publish(topic, str(bookingDetails)) 
                    #bookRide["message"]="ride started Successfully" 
                    client.disconnect()
                    return bookingDetails
                else:
                    data={"result":"","message":"No data Found","status":"false"}
                    
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

@app.route('/endResponder', methods=['POST'])
def endResponder():
    try:
        inputdata =  commonfile.DecodeInputdata(request.get_data())
        startlimit,endlimit="",""
        keyarr = ["ambulanceId","bookingId"]
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
            column=" status=2 "
            bookRide=databasefile.UpdateQuery("bookResponder",column,whereCondition)
            whereCondition222=  " ambulanceId= '"+ str(ambulanceId)+"' "
            columns= "onTrip=0 and onDuty=1"
            bookRide1=databasefile.UpdateQuery("ambulanceRideStatus",columns,whereCondition222)
            if (bookRide!=0):   
                bookRide["message"]="ride Ended Successfully"             
               
            
            
                
                columns="(ar.lat)ambulanceLat,(ar.lng)ambulanceLng, bm.ambulanceId,bm.bookingId,bm.driverId,bm.dropOff,bm.dropOffLatitude,bm.dropOffLongitude"
                columns=columns+",bm.finalAmount,bm.pickup,bm.status,bm.pickupLatitude,bm.pickupLongitude,bm.totalDistance,bm.userMobile,am.ambulanceNo "
                columns=columns+",bm.driverMobile"
                whereCondition22=" am.ambulanceId=bm.ambulanceId  and bookingId= '"+str(bookingId)+"'"
                bookingDetails= databasefile.SelectQuery("bookResponder bm,ambulanceMaster am,ambulanceRideStatus ar",columns,whereCondition22)
                print(bookingDetails,"================")
                bookingDetails["message"]="ride Ended Successfully"
               
                if (bookingDetails!='0'):  
                    print('Entered')
                    client = mqtt.Client()
                    client.connect("localhost",1883,60)
                    topic=str(userId)+"/endRide"
                    client.publish(topic, str(bookingDetails)) 
                    #bookRide["message"]="ride ended Successfully" 
                    client.disconnect()
                    return bookingDetails
                else:
                    data={"result":"","message":"No data Found","status":"false"}
                    
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





@app.route('/cancelResponder', methods=['POST'])
def cancelResponder():
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
            column=" status='3' , canceledUserId='"+str(userId)+"' "
            bookRide=databasefile.UpdateQuery("bookResponder",column,whereCondition)
            whereCondition222=  " ambulanceId= '"+ str(ambulanceId)+"' "
            columns= "onTrip=0 and onDuty=1"
            bookRide1=databasefile.UpdateQuery("ambulanceRideStatus",columns,whereCondition222)
            if (bookRide!=0):   
                bookRide["message"]="ride Cancelled Successfully"             
                

           
                
                columns="(ar.lat)ambulanceLat,(ar.lng)ambulanceLng, bm.ambulanceId,bm.bookingId,bm.driverId,bm.dropOff,bm.dropOffLatitude,bm.dropOffLongitude"
                columns=columns+",bm.finalAmount,bm.status,bm.pickup,bm.pickupLatitude,bm.pickupLongitude,bm.totalDistance,bm.userMobile,am.ambulanceNo "
                columns=columns+",bm.driverMobile"
                whereCondition22=" am.ambulanceId=bm.ambulanceId  and bookingId= '"+str(bookingId)+"'"
                bookingDetails= databasefile.SelectQuery("bookResponder bm,ambulanceMaster am,ambulanceRideStatus ar",columns,whereCondition22)
                print(bookingDetails,"================")
                bookingDetails["message"]="ride Cancelled Successfully" 

               
                if (bookingDetails!='0'):  
                    print('Entered')
                    client = mqtt.Client()
                    client.connect("localhost",1883,60)
                    topic=str(userId)+"/cancelRide"
                    client.publish(topic, str(bookingDetails)) 
                    #bookRide["message"]="ride Cancelled" 
                    client.disconnect()
                    return bookingDetails
                else:
                    data={"result":"","message":"No data Found","status":"false"}
                    
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





@app.route('/responderTrip', methods=['POST'])
def responderTrip():
    try:
        inputdata =  commonfile.DecodeInputdata(request.get_data())
        startlimit,endlimit="",""
        whereCondition2=""
       
        commonfile.writeLog("responderTrip",inputdata,0)
        msg="1"
        if msg == "1":
            if "startLimit" in inputdata:
                if inputdata['startLimit'] != "":
                    startlimit =str(inputdata["startLimit"])
                
            if "endLimit" in inputdata:
                if inputdata['endLimit'] != "":
                    endlimit =str(inputdata["endLimit"])

            if "startLocationLong" in inputdata:
                if inputdata['endLimit'] != "":
                   startlat =str(inputdata["endLimit"])

            if "startLocationLat" in inputdata:
                if inputdata['startLocationLat'] != "":
                    startlng=str(inputdata["startLocationLat"])


                 
            if "userId" in inputdata:
                if inputdata['userId'] != "":
                    userId =str(inputdata["userId"])
            if "bookingId" in inputdata:
                if inputdata['bookingId'] != "":
                    bookingId =str(inputdata["bookingId"])
                    whereCondition2=" and bm.bookingId= '"+ str(bookingId)+"'"

            orderby="bm.id"                

                    



            whereCondition=" and bm.userId=um.userId and bm.driverId=dm.driverId   and dm.driverId='"+str(userId)+"' "+whereCondition2

            column="bm.id,bm.userMobile,bm.driverMobile,bm.bookingId,bm.pickup as tripFrom,bm.dropOff as tripTo,date_format(bm.dateCreate,'%Y-%m-%d %H:%i:%s')startTime,dm.name as driverName,um.name as userName,bm.status,bm.finalAmount,bm.totalDistance"
            data=databasefile.SelectQueryOrderby("bookResponder as bm,userMaster as um,driverMaster as dm",column,whereCondition,"",startlimit,endlimit,orderby)
            print(data,"--------------------------------------------------")
            countdata=databasefile.SelectQuery4("bookResponder as bm,userMaster as um,driverMaster as dm",column,whereCondition)
           
            if (data['status']!='false'):
               

                Data = {"result":data['result'],"status":"true","message":"","totalCount":len(countdata)}

                          
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


#________________________________________







@app.route('/responderArrive', methods=['POST'])
def driverArriver1():
    try:
        inputdata =  commonfile.DecodeInputdata(request.get_data())
        startlimit,endlimit="",""
        keyarr = ["ambulanceId","bookingId","userId"]
        commonfile.writeLog("responderArrive",inputdata,0)
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
            column=" status=0 "
            bookRide=databasefile.UpdateQuery("bookAmbulance",column,whereCondition)
            print(bookRide)
            whereCondition222=  " ambulanceId= '"+ str(ambulanceId)+"' "
            columns= "onTrip=0 and onDuty=1"
            bookRide1=databasefile.UpdateQuery("ambulanceRideStatus",columns,whereCondition222)
            if (bookRide!=0):   
                bookRide["message"]="Responder has arrived at your location" 
                columns="(ar.lat)ambulanceLat,(ar.lng)ambulanceLng, bm.ambulanceId,bm.bookingId,bm.driverId,bm.dropOff,bm.dropOffLatitude,bm.dropOffLongitude"
                columns=columns+",bm.finalAmount,bm.status,bm.pickup,bm.pickupLatitude,bm.pickupLongitude,bm.totalDistance,bm.userMobile,am.ambulanceNo "
                columns=columns+",bm.driverMobile"
                whereCondition22=" am.ambulanceId=bm.ambulanceId  and bookingId= '"+str(bookingId)+"'"
                bookingDetails= databasefile.SelectQuery("bookResponder bm,ambulanceMaster am,ambulanceRideStatus ar",columns,whereCondition22)
                bookingDetails["message"]="Responder has arrived at your location" 
                client = mqtt.Client()
                client.connect("localhost",1883,60)            
                topic=str(userId)+"/arrive"
                print(topic,"+driverArrive")
                client.publish(topic, str(bookingDetails))
                print(bookingDetails,"@@") 

                return bookingDetails
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



















if __name__ == "__main__":
    CORS(app, support_credentials=True)
    app.run(host='0.0.0.0',port=5077,debug=True)
    socketio.run(app)        
