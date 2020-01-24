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
import databasefile
import commonfile
import json
import pymysql
from flask_cors import CORS
from datetime import datetime
import pytz 
import pytz
from config import Connection


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

geocoder = GoogleGeocoder("AIzaSyB0Pz6VjrQmWPCCbDbWDuyjo79GhDJPOlI")




#user signup
@app.route('/addUser', methods=['POST'])
def addUser():
    try:
        data1 = commonfile.DecodeInputdata(request.get_data())
        column = " * "
        whereCondition= "mobile='"+str(data1["mobile"])+ "'"
        data= SelectQuery("userMaster",column,whereCondition)
        UserId=uuid.uuid1()
        UserID=UserId.hex
        if data==None:
        	
        	column="name,password,mobile,userid,imeiNo,deviceName,currentLocation,currentLocationlatlong,usertypeId,email,country,city, "
        	column=column+ "ipAddress,userAgent,deviceId,os,deviceType,appVersion,notificationToken"
        	
        	values =  "'"+str(data1["name"])+"','"+str(data1["password"])
        	values= values+ " '" +"','"+str(data1["mobile"])+"','"+str(UserID)+"','"+str(data1["imeiNo"])+"','"+str(data1["deviceName"])+"','"
        	values= values+ " '"+str(data1["currentLocation"])+"','"+str(data1["currentLocationLatlong"])+"','"+str(data1["usertypeId"])+ "'"
        	values= values+ " '"+str(data1["email"])+"','"+str(data1["country"])+"','"+str(data1["city"])+ "'"
        	values= values+ " '"+str(data1["ipAddress"])+"','"+str(data1["userAgent"])+"','"+str(data1["deviceId"])+ "'"
        	values= values+ " '"+str(data1["os"])+"','"+str(data1["deviceType"])+"','"+str(data1["appVersion"])+ "','"+str(data1["notificationToken"])+ "'"

        	insertdata=InsertQuery("userMaster",column,values)
        	
        	column = " * "
        	whereCondition= "mobile='"+str(data1["mobile"])+ "'"
        	data8= SelectQuery1("userMaster",column,whereCondition)

        	output= {"result":"User Added Successfully","patient Details":data8[-1],"status":"true"}
            cursor.close()
            return output


               
            
        else:
            output = {"result":"User Already Added Existed ","status":"true","patient Details":data}
            return output 
    except Exception as e :
        print("Exception---->" + str(e))    
        output = {"result":"something went wrong","status":"false"}
        return output

@app.route('/addDriver', methods=['POST'])
def addDriver():
    try:
    	data1 = commonfile.DecodeInputdata(request.get_data())
        column = " * "
        whereCondition= "mobile='"+str(data1["mobile"])+ "' and usertypeId='3'"
        data= SelectQuery("userMaster",column,whereCondition)
        if data !=None:
        	column="name,mobile,driverId,ambulanceModeId,ambulanceId,panCardNo,DlNo,currentLocation,currentLocationlatlong,vehicleNo"

        	values="'"+str(data["name"])+"','"+str(data["mobile"])"','"+str(data["userId"])+"','"+str(data1["ambulanceModeId"])+"','"
        	values=values+"'"+str(data1["ambulanceId"])+"','"+str(data1["panCardNo"])+"','"+str(data1["DlNo"])+"','"
        	values="'"+str(data["currentLocation"])+"','"+str(data["currentLocationlatlong"])+"','"+str(data1["vehicleNo"])+"'"

        	insertdata=InsertQuery("driverMaster",column,values)
           

            column = " * "
        	whereCondition= "mobile='"+str(data1["mobile"])+ "'"
        	data17= SelectQuery1("driverMaster",column,whereCondition)
            
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
@app.route('/Login', methods=['GET'])
def login():
    try:
        password = request.args['password']
       
        mobile = request.args['mobile']
        column=  "us.mobile,us.name,um.usertype,us.userId"
        whereCondition= "us.mobile = '" + mobile + "' and us.password = '" + password + "'  and and us.usertypeId=um.Id"
        loginuser=SelectQuery("userMaster as us,usertypeMaster as um",column,whereCondition)
        
               
      
        if loginuser:   
            Data = {"result":loginuser,"status":"true"}                  
            return Data
        else:
            data={"status":"Failed","result":"Login Failed"}
            return data

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