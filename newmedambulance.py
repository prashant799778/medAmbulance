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
        data= databasefile.SelectQuery("userMaster",column,whereCondition)
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

        	insertdata=databasefile.InsertQuery("userMaster",column,values)
        	
        	column = " * "
        	whereCondition= "mobile='"+str(data1["mobile"])+ "'"
        	data8= databasefile.SelectQuery1("userMaster",column,whereCondition)

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
        data= databasefile.SelectQuery("userMaster",column,whereCondition)
        if data !=None:
        	column="name,mobile,driverId,ambulanceModeId,ambulanceId,panCardNo,DlNo,currentLocation,currentLocationlatlong,vehicleNo"

        	values="'"+str(data["name"])+"','"+str(data["mobile"])"','"+str(data["userId"])+"','"+str(data1["ambulanceModeId"])+"','"
        	values=values+"'"+str(data1["ambulanceId"])+"','"+str(data1["panCardNo"])+"','"+str(data1["DlNo"])+"','"
        	values="'"+str(data["currentLocation"])+"','"+str(data["currentLocationlatlong"])+"','"+str(data1["vehicleNo"])+"'"

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
@app.route('/Login', methods=['GET'])
def login():
    try:
        password = request.args['password']
       
        mobile = request.args['mobile']
        column=  "us.mobile,us.name,um.usertype,us.userId"
        whereCondition= "us.mobile = '" + mobile + "' and us.password = '" + password + "'  and and us.usertypeId=um.Id"
        loginuser=databasefile.SelectQuery1("userMaster as us,usertypeMaster as um",column,whereCondition)
        
               
      
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
#select(resonder,driver,user,)

@app.route('/selectusertypeMaster', methods=['GET'])
def usertypeMaster():
    try:
        column="id,usertype"
        whereCondition=""
        data=databasefile.SelectQuery1("usertypeMaster",column,whereCondition)
        if data:           
            Data = {"result":data,"status":"true"}
            return Data
        else:
            output = {"result":"No Data Found","status":"false"}
            return output

    except Exception as e :
        print("Exception---->" + str(e))    
        output = {"result":"something went wrong","status":"false"}
        return output         

@app.route('/addambulanceMode', methods=['POST'])
def addambulanceMode():
    try:
        data1=commonfile.DecodeInputdata(request.get_data())  
        column = " * "
        whereCondition= "ambulanceType='"+str(data1["ambulanceType"])+ "'"
        data= databasefile.SelectQuery("ambulanceMode",column,whereCondition)
        if data==None:
            column="ambulanceType"
            values="'"+str(data1["ambulanceType"])+"'"
            insertdata=databasefile.InsertQuery("ambulanceMode",column,values)
            column="*"
            whereCondition= "ambulanceType='"+str(data1["ambulanceType"])+ "'"
            data8= databasefile.SelectQuery1("ambulanceMode",column,whereCondition)
            output= {"result":"User Added Successfully","ambulance Details":data8[-1],"status":"true"}
            return output
        
        else:
            output = {"result":"User Already Added Existed ","status":"true","ambulance Details":data}
            return output 
    except Exception as e :
        print("Exception---->" + str(e))    
        output = {"result":"something went wrong","status":"false"}
        return output         


@app.route('/selectambulanceMode', methods=['GET'])
def ambulanceMode():
    try:
        column="id ,ambulanceType"
        whereCondition=""
        data=databasefile.SelectQuery1("ambulanceMode",column,whereCondition)
        if data:           
            Data = {"result":data,"status":"true"}
            return Data
        else:
            output = {"result":"No Data Found","status":"false"}
            return output

    except Exception as e :
        print("Exception---->" + str(e))    
        output = {"result":"something went wrong","status":"false"}
        return output


@app.route('/updateambulanceMode', methods=['POST'])
def updateambulanceMode():
    try:
       data=commonfile.DecodeInputdata(request.get_data())  
       column= " ambulanceType='" + str(data["ambulanceType"]) + "'"
       whereCondition="id = '" + str(data["id"])+ "'"
       Data.UpdateQuery("ambulanceMode",column,whereCondition)
       
       
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



       


@app.route('/addambulance', methods=['POST'])
def addambulance():
    try:
        data1 = commonfile.DecodeInputdata(request.get_data())
        column="*"
        whereCondition="ambulanceType='"+str(data1["ambulanceType"])"'"
        data= databasefile.SelectQuery("ambulanceMaster",column,whereCondition)
        if data==None:
            column=ambulanceType
            values="'"+str(data1["ambulanceType"])+"'"
            insertdata=databasefile.InsertQuery("ambulanceMaster",column,values)
            column="*"
            whereCondition="ambulanceType='"+str(data1["ambulanceType"])"'"
            data1= databasefile.SelectQuery1("ambulanceMaster",column,whereCondition)
            output= {"result":"User Added Successfully","ambulance Details":data1[-1],"status":"true"}
            cursor.close()
            return output
        else:
            output = {"result":"User Already Added Existed ","status":"true","ambulance Details":data}
            return output 
    except Exception as e :
        print("Exception---->" + str(e))    
        output = {"result":"something went wrong","status":"false"}
        return output
 




@app.route('/selectambulanceMaster', methods=['GET'])
def ambulanceMaster():
    try:
        column="id ,ambulanceType"
        whereCondition=""
        data=databasefile.SelectQuery1("ambulanceMaster",column,whereCondition)
        if data:           
            Data = {"result":data,"status":"true"}
            return Data
        else:
            output = {"result":"No Data Found","status":"false"}
            return output

    except Exception as e :
        print("Exception---->" + str(e))    
        output = {"result":"something went wrong","status":"false"}
        return output  

@app.route('/updateambulanceMaster', methods=['POST'])
def updateambulanceMaster():
    try:
       data=commonfile.DecodeInputdata(request.get_data())  
       column= " ambulanceType='" + str(data["ambulanceType"]) + "'"
       whereCondition="id = '" + str(data["id"])+ "'"
       data=databasefile.UpdateQuery("ambulanceMaster",column,whereCondition)
       
       
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


@app.route('/allusers', methods=['GET'])
def allusers():
    try:
        column="*"
        whereCondition="usertypeId='2' "
        data=databasefile.SelectQuery1("userMaster",column,whereCondition)
        if data:           
            Data = {"result":data,"status":"true"}
            return Data
        else:
            output = {"result":"No Data Found","status":"false"}
            return output

    except Exception as e :
        print("Exception---->" + str(e))    
        output = {"result":"something went wrong","status":"false"}
        return output

@app.route('/alldriver', methods=['GET'])
def alldrivers():
    try:
        column="*"
        whereCondition="usertypeId='3' "
        data=databasefile.SelectQuery1("userMaster",column,whereCondition)
        if data:           
            Data = {"result":data,"status":"true"}
            return Data
        else:
            output = {"result":"No Data Found","status":"false"}
            return output

    except Exception as e :
        print("Exception---->" + str(e))    
        output = {"result":"something went wrong","status":"false"}
        return output


@app.route('/allresponder', methods=['GET'])
def alldresponder():
    try:
        column="*"
        whereCondition="usertypeId='4' "
        data=databasefile.SelectQuery1("userMaster",column,whereCondition)
        if data:           
            Data = {"result":data,"status":"true"}
            return Data
        else:
            output = {"result":"No Data Found","status":"false"}
            return output

    except Exception as e :
        print("Exception---->" + str(e))    
        output = {"result":"something went wrong","status":"false"}
        return output 


@app.route('/responderMode', methods=['GET'])
def responderMode():
    try:
        column="id ,responderType"
        whereCondition=""
        data=databasefile.SelectQuery1("responderMode",column,whereCondition)
        if data:           
            Data = {"result":data,"status":"true"}
            return Data
        else:
            output = {"result":"No Data Found","status":"false"}
            return output

    except Exception as e :
        print("Exception---->" + str(e))    
        output = {"result":"something went wrong","status":"false"}
        return output


#update riderMode(g,p,h)

@app.route('/updateresponderMode', methods=['POST'])
def updateresponderMode():
    try:
        data=commonfile.DecodeInputdata(request.get_data())  
        column= " responderType='" + str(data["responderType"]) + "'"
        whereCondition= "id = '" + str(data["id"])+ "'"
        databasefile.UpdateQuery("responderMode",column,whereCondition)
       
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


#(rider(ALs,BLS,PVT,DBT,AIR))

@app.route('/addriderType', methods=['POST'])
def addriderType():
    try:
        data1 = commonfile.DecodeInputdata(request.get_data())
        column="*"
        whereCondition="responderType='"+str(data1["ambulanceType"])"'"
        data= databasefile.SelectQuery("responderTypeMaster",column,whereCondition)
        if data==None:
            column=ambulanceType
            values="'"+str(data1["responderType"])+"'"
            insertdata=databasefile.InsertQuery("responderTypeMaster",column,values)
            column="*"
            whereCondition="responderType='"+str(data1["responderType"])"'"
            data1= databasefile.SelectQuery1("responderTypeMaster",column,whereCondition)
            output= {"result":"User Added Successfully","responder Details":data1[-1],"status":"true"}
            cursor.close()
            return output


               
            
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
        column="id ,responderType"
        whereCondition=""
        data=databasefile.SelectQuery1("responderTypeMaster",column,whereCondition)
        if data:           
            Data = {"result":data,"status":"true"}
            return Data
        else:
            output = {"result":"No Data Found","status":"false"}
            return output

    except Exception as e :
        print("Exception---->" + str(e))    
        output = {"result":"something went wrong","status":"false"}
        return output



#update rider
@app.route('/updateriderType', methods=['POST'])
def updateriderType():
    try:
        data=commonfile.DecodeInputdata(request.get_data())  
        column= " responderType='" + str(data["responderType"]) + "'"
        whereCondition= "id = '" + str(data["id"])+ "'"
        databasefile.UpdateQuery("responderTypeMaster",column,whereCondition)
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

#addOns
@app.route('/addOns', methods=['POST'])
def addOns():
    try:
        data1=commonfile.DecodeInputdata(request.get_data())  
        column="name"
        whereCondition= " name='"+str(data1["name"])+ "'"
        data=databasefile.SelectQuery("addOns",column,whereCondition)
        if data==None:
            column="name"
            values="('"+str(data1["name"])+"' "
            insertdata=databasefile.InsertQuery("addOns",column,values)
            column="*"
            whereCondition= " name='"+str(data1["name"])+ "'"
            data1=databasefile.SelectQuery1("addOns",column,whereCondition)

            output= {"result":"User Added Successfully","ambulance Details":data1[-1],"status":"true"}
            cursor.close()
            return output


               
            
        else:
            output = {"result":"User Already Added Existed ","status":"true","ambulance Details":data}
            return output 
    except Exception as e :
        print("Exception---->" + str(e))    
        output = {"result":"something went wrong","status":"false"}
        return output

#select addOns
@app.route('/addOnsSelect', methods=['GET'])
def addsOn():
    try:
        column="id ,name"
        whereCondition=""
        data=databasefile.SelectQuery1("addOns",column,whereCondition)
        if data:           
            Data = {"result":data,"status":"true"}
            return Data
        else:
            output = {"result":"No Data Found","status":"false"}
            return output

    except Exception as e :
        print("Exception---->" + str(e))    
        output = {"result":"something went wrong","status":"false"}
        return output



@app.route('/updateaddOns', methods=['POST'])
def updateaddOns():
    try:
        data=commonfile.DecodeInputdata(request.get_data())  
        column= " name='" + str(data["name"]) + "'"
        whereCondition= "id = '" + str(data["id"])+ "'"
        databasefile.UpdateQuery("addOns",column,whereCondition)
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



#finalPayment

@app.route('/finalPayment', methods=['POST'])
def finalPayment():
    try:
        data1=commonfile.DecodeInputdata(request.get_data())  
        column="userId,paymentmodeId,totalAmount"
        values=  " '"+str(data1["userId"])+"','"+str(data1["paymentmodeId"])+"','"+str(data1["totalAmount"])+ "'"
        
        insertdata=databasefile.InsertQuery("finalPayment",column,values)

        column="*"
        WhereCondition= "userId='"+str(data1["userId"])+ "' "
        data2=databasefile.SelectQuery1("finalPayment",column,values)

       


        output= {"result":"Payment Successfull","patient Details":data2[-1],"status":"true"}
        cursor.close()
        return output


               
            
        if data2 ==None:
            output = {"result":"Payment Unsuccessfull","status":"false"}
            return output 
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
       
        if data:           
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
            cursor.close()
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
        
        
        
        if data:           
            Data = {"result":data,"status":"true"}
            return Data
        else:
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
        if data:           
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
        if data:           
            Data = {"result":data,"status":"true"}
            return Data
        else:
            output = {"result":"No Data Found","status":"false"}
            return output

    except Exception as e :
        print("Exception---->" + str(e))    
        output = {"result":"something went wrong","status":"false"}
        return output 

#track Ambulance
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
        cursor.close()
        if data:           
            Data = {"result":data,"status":"true"}
            return Data
        else:
            output = {"result":"No Data Found","status":"false"}
            return output

    except Exception as e :
        print("Exception---->" + str(e))    
        output = {"result":"something went wrong","status":"false"}
        return output



#track Ambulance
@app.route('/trackAmbulance', methods=['GET'])
def trackAmbulance():
    try:
        data=commonfile.DecodeInputdata(request.get_data())
        column="dm.name,dm.mobile,dbm.farDistance,dm.currentLocation"
        whereCondition="dbm.driverId=dm.driverId and dbm.bookingId='" + str(data["bookingId"]) + "'"
        data=databasefile.SelectQuery1("driverMaster as dm ,driverBookingMapping as dbm",column,whereCondition)
        
        
        if data:           
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