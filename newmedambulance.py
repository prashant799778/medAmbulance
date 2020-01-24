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
        	values= values++ " '" +"','"+str(data1["mobile"])+"','"+str(UserID)+"','"+str(data1["imeiNo"])+"','"+str(data1["deviceName"])+"','"
        	values= values+ " '"+str(data1["currentLocation"])+"','"+str(data1["currentLocationLatlong"])+"','"+str(data1["usertypeId"])+ "'"
        	values= values+ " '"+str(data1["email"])+"','"+str(data1["country"])+"','"+str(data1["city"])+ "'"
        	values= values+ " '"+str(data1["ipAddress"])+"','"+str(data1["userAgent"])+"','"+str(data1["deviceId"])+ "'"
        	values= values+ " '"+str(data1["os"])+"','"+str(data1["deviceType"])+"','"+str(data1["appVersion"])+ "','"+str(data1["notificationToken"])+ "'"
        	


        	
        	insertdata=InsertQuery("userMaster",column,values)
        	
        	column = " * "
        	whereCondition= "mobile='"+str(data1["mobile"])+ "'"
        	data= SelectQuery1("userMaster",column,whereCondition)

        	output= {"result":"User Added Successfully","patient Details":data1[-1],"status":"true"}
            cursor.close()
            return output


               
            
        else:
            output = {"result":"User Already Added Existed ","status":"true","patient Details":data}
            return output 
    except Exception as e :
        print("Exception---->" + str(e))    
        output = {"result":"something went wrong","status":"false"}
        return output