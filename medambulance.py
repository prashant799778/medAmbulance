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
        json1=request.get_data() 
        data1=json.loads(json1.decode("utf-8"))  
        
        query = "select * from userMaster where   mobile='"+str(data1["mobile"])+ "';"
        conn=Connection()
        cursor = conn.cursor()
        cursor.execute(query)
        data = cursor.fetchone()
        UserId=uuid.uuid1()
        UserID=UserId.hex
        if data==None:
        	if data1["password"]==data1["confirm_password"]:
                query="insert into userMaster(name,password,mobile,userid,imeiNo,deviceName,currentLocation,currentLocationlatlong,usertypeId)values "
                query = query+"('"+str(data1["name"])+"','"+str(data1["password"])
                query= query+"','"+str(data1["mobile"])+"','"+str(UserID)+"','"+str(data1["imeiNo"])+"','"+str(data1["deviceName"])+"','"+str(data1["currentLocation"])+"','"+str(data1["currentLocationLatlong"])+"','"+str(data1["usertypeId"])+"');"
                conn=Connection()
                cursor = conn.cursor()
                cursor.execute(query)
                conn.commit()
                query = "select * from userMaster where   mobile='"+str(data1["mobile"])+ "';"
                conn=Connection()
                cursor = conn.cursor()
                cursor.execute(query)
                data1 = cursor.fetchall()

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


#driver signup
@app.route('/addDriver', methods=['POST'])
def addDriver():
    try:
        json1=request.get_data() 
        data1=json.loads(json1.decode("utf-8"))  
        
        query = "select * from userMaster where   mobile='"+str(data1["mobile"])+ "' and usertypeId='3';"
        conn=Connection()
        cursor = conn.cursor()
        cursor.execute(query)
        data = cursor.fetchone()
        UserId=uuid.uuid1()
        UserID=UserId.hex
        if data !=None:
            query="insert into driverMaster(name,mobile,driverId,ambulanceModeId,ambulanceId,panCardNo,DlNo,currentLocation,currentLocationlatlong,vehicleNo)values"
            query = query+"('"+str(data["name"])+"','"+str(data["mobile"])
            query= query+"','"+str(data["userId"])+"','"+str(data1["ambulanceModeId"])+"','"+str(data1["ambulanceId"])+"','"+str(data1["panCardNo"])+"','"+str(data1["DlNo"])+"','"+str(data["currentLocation"])+"','"+str(data["currentLocationlatlong"])+"','"+str(data1["vehicleNo"])+"');"
            conn=Connection()
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()
            query = "select * from driverMaster where   mobile='"+str(data1["mobile"])+ "';"
            conn=Connection()
            cursor = conn.cursor()
            cursor.execute(query)
            data1 = cursor.fetchall()
            cursor.close()
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
        
               
       
        query ="select us.mobile,us.name,um.usertype,us.userId  from userMaster as us,usertypeMaster as um where us.mobile = '" + mobile + "' and us.password = '" + password + "'  and and us.usertypeId=um.Id ;"   
        conn=Connection()
        cursor = conn.cursor()
        cursor.execute(query)
        loginuser = cursor.fetchone()
        cursor.close()
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






#ambulance(goverment,private,Hospital)
@app.route('/addambulanceMode', methods=['POST'])
def addambulanceMode():
    try:
        json1=request.get_data() 
        data1=json.loads(json1.decode("utf-8"))  
        
        query = "select * from ambulanceMode where   ambulanceType='"+str(data1["ambulanceType"])+ "';"
        conn=Connection()
        cursor = conn.cursor()
        cursor.execute(query)
        data = cursor.fetchone()
       
        if data==None:
           
            query="insert into ambulanceMode(ambulanceType)values"
            query = query+"('"+str(data1["ambulanceType"])+"');"
            conn=Connection()
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()
            query = "select * from ambulanceMode where   ambulanceType='"+str(data1["ambulanceType"])+ "';"
            conn=Connection()
            cursor = conn.cursor()
            cursor.execute(query)
            data1 = cursor.fetchall()
            cursor.close()
            output= {"result":"User Added Successfully","ambulance Details":data1[-1],"status":"true"}
            return output
        
        else:
            output = {"result":"User Already Added Existed ","status":"true","ambulance Details":data}
            return output 
    except Exception as e :
        print("Exception---->" + str(e))    
        output = {"result":"something went wrong","status":"false"}
        return output

#select ambulance(goverment,private,Hospiatl)        
 
@app.route('/ambulanceMode', methods=['GET'])
def ambulanceMode():
    try:
        query = "select * from ambulanceMode "
        conn=Connection()
        cursor = conn.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
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


@app.route('/usertypeMaster', methods=['GET'])
def usertypeMaster():
    try:
        query = "select * from usertypeMaster "
        conn=Connection()
        cursor = conn.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
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


#update aM(g,p,h)

@app.route('/updateambulanceMode', methods=['POST'])
def updateambulanceMode():
    try:
       
        json1=request.get_data() 
        data=json.loads(json1.decode("utf-8")) 
       
        query1 = " update ambulanceMode set   ambulanceType='" + str(data["ambulanceType"]) + "'  where   id = '" + str(data["id"])+ "' ;"
        print(query1)
        conn=Connection()
        cursor = conn.cursor()
        cursor.execute(query1)
        conn.commit()
        cursor.close()
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


#(ambulance(ALs,BLS,PVT,DBT,AIR))

@app.route('/addambulance', methods=['POST'])
def addambulance():
    try:
        json1=request.get_data() 
        data1=json.loads(json1.decode("utf-8"))  
        
        query = "select * from ambulanceMaster where   ambulanceType='"+str(data1["ambulanceType"])+ "';"
        conn=Connection()
        cursor = conn.cursor()
        cursor.execute(query)
        data = cursor.fetchone()
       
        if data==None:
           
            query="insert into ambulanceMaster(ambulanceType)values"
            query = query+"('"+str(data1["ambulanceType"])+"');"
            conn=Connection()
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()
            query = "select * from ambulanceMaster where   ambulanceType='"+str(data1["ambulanceType"])+ "';"
            conn=Connection()
            cursor = conn.cursor()
            cursor.execute(query)
            data1 = cursor.fetchall()

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
 
#(select ambulance)
@app.route('/ambulanceType', methods=['GET'])
def ambulanceType():
    try:
        query = "select * from ambulanceMaster "
        conn=Connection()
        cursor = conn.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
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



#update ambulance
@app.route('/updateambulanceType', methods=['POST'])
def updateambulanceType():
    try:
       
        json1=request.get_data() 
        data=json.loads(json1.decode("utf-8")) 
       
        query1 = " update ambulanceMaster set   ambulanceType='" + str(data["ambulanceType"]) + "'  where   id = '" + str(data["id"])+ "' ;"
        print(query1)
        conn=Connection()
        cursor = conn.cursor()
        cursor.execute(query1)
        conn.commit()
        cursor.close()
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


#all users
@app.route('/allusers', methods=['GET'])
def allusers():
    try:
        query = "select * from userMaster where usertypeId='2' "
        conn=Connection()
        cursor = conn.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
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

@app.route('/alldriver', methods=['GET'])
def alldrivers():
    try:
        query = "select * from userMaster where usertypeId='3' "
        conn=Connection()
        cursor = conn.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
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

#add hospitals
@app.route('/addhospital', methods=['POST'])
def addhospital():
    try:
        json1=request.get_data() 
        data1=json.loads(json1.decode("utf-8"))  
        
        query = "select * from hospitalMaster where   hospitalName='"+str(data1["hospitalName"])+ "';"
        conn=Connection()
        cursor = conn.cursor()
        cursor.execute(query)
        data = cursor.fetchone()
        print(data)
        if data==None:
        	
        	query2  = " insert into hospitalMaster (hospitalName,address)"
        	query2 = query2 +" values('"+str(data1["hospitalName"])+"','"+str(data1["address"])+"');"
        	print(query2)
        	cursor.execute(query2)
        	conn.commit()

        	query = "select id as hospitalId from hospitalMaster where hospitalName= '"+str(data1["hospitalName"])+ "' and  address='"+str(data1["address"])+ "';"
        	cursor.execute(query)
        	data=cursor.fetchall()
        	yu=data[-1]
        	mainId=yu["hospitalId"]
        	ambulanceId = data1["ambulanceId"]
        	for i in ambulanceId:
        		query = "select * from ambulanceHospitalMapping where ambulance_Id='"+str(i)+"'  and hospital_Id='"+str(mainId)+"' ;"
        		cursor.execute(query)
        		userHospitalMappingdata = cursor.fetchall()
        		if userHospitalMappingdata==():
        			query2  = " insert into ambulanceHospitalMapping(hospital_Id,ambulance_Id)"
        			query2 = query2 +" values('"+str(mainId)+"','"+str(i)+"');"
        			conn=Connection()
        			cursor = conn.cursor()
        			cursor.execute(query2)
        			conn.commit()

        	# query = "select * from hospitalMaster where   hospitalName='"+str(data1["hospitalName"])+ "';"
        	# cursor.execute(query)
        	# data = cursor.fetchone()
        	# if data!=None:
        	# 	mainId=data["hospitalId"]
        	# 	ambulanceId = data1["ambulanceId"]
        	# 	for i in ambulanceId:
        	# 		query = "select * from ambulanceHospitalMapping where ambulance_Id='"+str(i)+"'  and hospital_Id='"+str(mainId)+"' ;"
        	# 		conn=Connection()
        	# 		cursor = conn.cursor()
        	# 		cursor.execute(query)
        	# 		userHospitalMappingdata = cursor.fetchall()
        	# 		if userHospitalMappingdata==():
        	# 			query2  = " insert into ambulanceHospitalMapping(hospital_Id,ambulance_Id)"
        	# 			query2 = query2 +" values('"+str(mainId)+"','"+str(i)+"');"
        	# 			conn=Connection()
        	# 			cursor = conn.cursor()
        	# 			cursor.execute(query2)
        	# 			conn.commit()
            cursor.close()                
            output = {"result":"data inserted successfully","status":"true"}
            return output
           
        else:
            output = {"result":"Hospital Already  Existed ","status":"true"}
            return output 
    except Exception as e :
        print("Exception---->" + str(e))    
        output = {"result":"something went wrong","status":"false"}
        return output




#addbooking

@app.route('/addbookingambulance', methods=['POST'])
def addbooking():
    try:
        json1=request.get_data() 
        data1=json.loads(json1.decode("utf-8"))  
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

        




        
        query = "select * from bookAmbulance where   userId='"+str(data1["userId"])+ "' and status<>'2';"
        conn=Connection()
        cursor = conn.cursor()
        cursor.execute(query)
        data = cursor.fetchone()
        print(data)
        if data==None:
            query = "select driverId,currentLocationlatlong,mobile from driverMaster  where   drivingstatus<>'F';"
            conn=Connection()
            cursor = conn.cursor()
            cursor.execute(query)
            datavv = cursor.fetchall()
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
           
            
            query2  = " insert into bookAmbulance (usermobile,pickup,pickupLongitudeLatitude,dropoff,dropoffLongitudeLatitude,selectBookingDate,bookingType,patientMedicalCondition,ambulanceId,userId,bookingId,finalAmount,totalDistance)"
            query2 = query2 +" values('"+str(data1["mobile"])+"','"+str(data1["pickup"])+"','"+str(fromlatitude,fromlongitude)+"','"+str(data1["dropoff"])+"','"+str(tolatitude,tolongitude)+"','"+str(data1["selectBookingDate"])+"','"+str(data1["patientMedicalCondition"])+"','"+str(data1["userId"])+"','"+str(bookingId)+"','"+str(data1["finalAmount"])+"','"+str(d3)+"');"
            print(query2)
            cursor.execute(query2)
            conn.commit()

            query = "select * from bookAmbulance  where userId='"+str(data1["userId"])+ "' and status<>'2';"
            cursor.execute(query)
            data=cursor.fetchall()
            yu=data[-1]
            mainId=yu["bookingId"]
            pickuplocation=yu["pickup"]
            userid=yu["userId"]

            query2  = " insert into driverBookingMapping(bookingId,driverId,farDistance,pickup,userId) values ('"+str(mainId)+"','"+str(driverId)+"','"+str(d9)+"','"+str(pickuplocation)+"','"+str(userid)+"');"
            cursor.execute(query2)
            conn.commit()

            ambulanceId = data1["addsOnId"]
            for i in ambulanceId:
                query = "select * from  addsOnbookambulanceMapping  where addsOnId='"+str(i)+"'  and bookingId='"+str(mainId)+"' ;"
                cursor.execute(query)
                userHospitalMappingdata = cursor.fetchall()
                if userHospitalMappingdata==():
                    query2  = " insert into addsOnbookambulanceMapping(addsOnId,bookingId)"
                    query2 = query2 +" values('"+str(mainId)+"','"+str(i)+"');"
                    conn=Connection()
                    cursor = conn.cursor()
                    cursor.execute(query2)
                    conn.commit()


            # cursor.execute(query)
            # data = cursor.fetchone()
            # if data!=None:
            #     mainId=data["bookingId"]
            #     ambulanceId = data1["addsOnId"]
            #     for i in ambulanceId:
            #         query = "select * from  addsOnbookambulanceMapping  where addsOnId='"+str(i)+"'  and bookingId='"+str(mainId)+"' ;"
            #         cursor.execute(query)
            #         userHospitalMappingdata = cursor.fetchall()
            #         if userHospitalMappingdata==():
            #             query2  = " insert into addsOnbookambulanceMapping(addsOnId,bookingId)"
            #             query2 = query2 +" values('"+str(mainId)+"','"+str(i)+"');"
            #             conn=Connection()
            #             cursor = conn.cursor()
            #             cursor.execute(query2)
            #             conn.commit()
            cursor.close()                
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
@app.route('/trackAmbulance', methods=['GET'])
def trackAmbulance():
    try:
        json1=request.get_data() 
        data1=json.loads(json1.decode("utf-8"))  
        
        query = "select dm.name,dm.mobile,dbm.farDistance,dm.currentLocation from driverMaster as dm ,driverBookingMapping as dbm where dbm.driverId=dm.driverId and dbm.bookingId='" + str(data["bookingId"]) + "'"
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





#book Rider




@app.route('/addRiderBooking', methods=['POST'])
def addRiderBooking():
    try:
        json1=request.get_data() 
        data1=json.loads(json1.decode("utf-8"))  
        pickup=str(data1["pickup"])
        search = geocoder.get(pickup)
        search[0].geometry.location
        fromlatitude= search[0].geometry.location.lat
        fromlongitude=search[0].geometry.location.lng
        
        bookingId=uuid.uuid1()
        bookingId=bookingId.hex
        R = 6373.0
        query = "select * from responderBooking where   userId='"+str(data1["userId"])+ "' and status<>'2';"
        conn=Connection()
        cursor = conn.cursor()
        cursor.execute(query)
        data = cursor.fetchone()
        print(data)
        if data==None:
            query = "select responderId,currentLocationlatlong,mobile from responderMaster  where   ridingstatus<>'F';"
            conn=Connection()
            cursor = conn.cursor()
            cursor.execute(query)
            datavv = cursor.fetchall()
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
           
            
            query2  = " insert into responderBooking (usermobile,pickup,pickupLongitudeLatitude,selectBookingDate,bookingType,patientMedicalCondition,ambulanceId,userId,bookingId,finalAmount,totalDistance)"
            query2 = query2 +" values('"+str(data1["mobile"])+"','"+str(data1["pickup"])+"','"+str(fromlatitude,fromlongitude)+"','"+str(data1["selectBookingDate"])+"','"+str(data1["patientMedicalCondition"])+"','"+str(data1["userId"])+"','"+str(bookingId)+"','"+str(data1["finalAmount"])+"','"+str(d9)+"');"
            print(query2)
            cursor.execute(query2)
            conn.commit()

            query = "select * from responderBooking  where userId='"+str(data1["userId"])+ "' and status<>'2';"
            cursor.execute(query)
            data=cursor.fetchall()
            yu=data[-1]
            mainId=yu["bookingId"]
            pickuplocation=yu["pickup"]
            userid=yu["userId"]

            query2  = " insert into responderBookingMapping(bookingId,responderId,farDistance,pickup,userId) values ('"+str(mainId)+"','"+str(riderId)+"','"+str(d9)+"','"+str(pickuplocation)+"','"+str(userid)++"');"
            cursor.execute(query2)
            conn.commit()
            cursor.close()                
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
@app.route('/trackResponder', methods=['GET'])
def trackRider():
    try:
        json1=request.get_data() 
        data1=json.loads(json1.decode("utf-8"))  
        
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

@app.route('/ResponderTraceUser', methods=['GET'])
def ResponderTraceUser():
    try:
        json1=request.get_data() 
        data1=json.loads(json1.decode("utf-8"))  
        
        query = "select um.name,um.mobile,dbm.farDistance,dbm.pickup,dbm.bookingId from responderbookingMapping as dbm,userMaster as  um where dbm.userId=dm.userId and dbm.responderId='" + str(data["responderId"]) + "'"
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

@app.route('/DriverTraceUser', methods=['GET'])
def DriverTraceUser():
    try:
        json1=request.get_data() 
        data1=json.loads(json1.decode("utf-8"))  
        
        query = "select um.name,um.mobile,dbm.farDistance,dbm.pickup,dbm.bookingId from driverBookingMapping as dbm,userMaster as  um where dbm.userId=dm.userId and dbm.driverId='" + str(data["driverId"]) + "'"
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




#driver location update

@app.route('/updateDriverMasterlocation', methods=['POST'])
def updateDriverMasterlocation():
    try:
       
        json1=request.get_data() 
        data=json.loads(json1.decode("utf-8")) 
       
        query1 = " update driverMaster set   currentLocation ='" + str(data["currentLocation"]) + "',currentLocationlatlong='" + str(data["currentLocationlatlong"]) + "'  where   driverId = '" + str(data["driverId"])+ "' and ambulanceId='" + str(data["ambulanceId"]) + "' ;"
        print(query1)
        conn=Connection()
        cursor = conn.cursor()
        cursor.execute(query1)
        conn.commit()
        cursor.close()
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
 





#all hospital
 
@app.route('/allHospital', methods=['GET'])
def allHospital():
    try:
        ambulanceType=""

        if 'ambulanceType' in request.args:
            ambulanceType=request.args["ambulanceType"]


        if ambulanceType !="":
            
            WhereCondition1 =  " and  ambulanceType   = '" + ambulanceType + "'  "
        
        
        query = "select hosp.id,hosp.hospitalName,hosp.address,am.ambulanceType from hospitalMaster as hosp,hospitalambulanceMapping as ahm,ambulanceMaster as am where hosp.id=ahm.hospital_Id and am.id=ahm.ambulance_Id" + WhereCondition1
        conn=Connection()
        cursor = conn.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
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

#paymenttypeMaster(debit,credit,paypal)

@app.route('/addpaymentType', methods=['POST'])
def addpaymentType():
    try:
        json1=request.get_data() 
        data1=json.loads(json1.decode("utf-8"))  
        
        query = "select * from paymentTypeMaster where   paymentType='"+str(data1["paymentType"])+ "';"
        conn=Connection()
        cursor = conn.cursor()
        cursor.execute(query)
        data = cursor.fetchone()
       
        if data==None:
           
            query="insert into paymentTypeMaster(paymentType)values"
            query = query+"('"+str(data1["paymentType"])+"');"
            conn=Connection()
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()
            query = "select * from paymentTypeMaster where   paymentType='"+str(data1["paymentType"])+ "';"
            conn=Connection()
            cursor = conn.cursor()
            cursor.execute(query)
            data1 = cursor.fetchall()

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





 
@app.route('/paymentTypeMaster', methods=['GET'])
def paymentTypeMaster():
    try:
        query = "select * from paymentTypeMaster"
        conn=Connection()
        cursor = conn.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
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



@app.route('/updatepaymentType', methods=['POST'])
def updatepaymentType():
    try:
       
        json1=request.get_data() 
        data=json.loads(json1.decode("utf-8")) 
       
        query1 = " update paymentTypeMaster set   paymentType='" + str(data["paymentType"]) + "'  where   id = '" + str(data["id"])+ "' ;"
        print(query1)
        conn=Connection()
        cursor = conn.cursor()
        cursor.execute(query1)
        conn.commit()
        cursor.close()
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
        json1=request.get_data() 
        data1=json.loads(json1.decode("utf-8"))  
        
        query = "select * from addOns where   name='"+str(data1["name"])+ "';"
        conn=Connection()
        cursor = conn.cursor()
        cursor.execute(query)
        data = cursor.fetchone()
       
        if data==None:
           
            query="insert into addOns(name)values"
            query = query+"('"+str(data1["name"])+"');"
            conn=Connection()
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()
            query = "select * from addOns where   name='"+str(data1["name"])+ "';"
            conn=Connection()
            cursor = conn.cursor()
            cursor.execute(query)
            data1 = cursor.fetchall()

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
        query = "select * from addOns"
        conn=Connection()
        cursor = conn.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
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



@app.route('/updateaddOns', methods=['POST'])
def updateaddOns():
    try:
       
        json1=request.get_data() 
        data=json.loads(json1.decode("utf-8")) 
       
        query1 = " update addOns set   name='" + str(data["name"]) + "'  where   id = '" + str(data["id"])+ "' ;"
        print(query1)
        conn=Connection()
        cursor = conn.cursor()
        cursor.execute(query1)
        conn.commit()
        cursor.close()
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
        json1=request.get_data() 
        data1=json.loads(json1.decode("utf-8"))  
        query="insert into finalPayment(userId,paymentmodeId,totalAmount)values"
        query = query+"('"+str(data1["userId"])+"','"+str(data1["paymentmodeId"])
        query= query+"','"+str(data1["totalAmount"])+"');"
        conn=Connection()
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        query = "select * from finalPayment where   userId='"+str(data1["bookingId"])+ "';"
        conn=Connection()
        cursor = conn.cursor()
        cursor.execute(query)
        data2 = cursor.fetchall()


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


#driver add Rider
@app.route('/addRider', methods=['POST'])
def addrider():
    try:
        json1=request.get_data() 
        data1=json.loads(json1.decode("utf-8"))  
        
        query = "select * from userMaster where   mobile='"+str(data1["mobile"])+ "' and usertypeId='4';"
        conn=Connection()
        cursor = conn.cursor()
        cursor.execute(query)
        data = cursor.fetchone()
        UserId=uuid.uuid1()
        UserID=UserId.hex
        if data != None:
            query="insert into responderMaster(name,mobile,responderId,responderModeId,responderTypeId,panCardNo,DlNo,currentLocation,currentLocationlatlong,vehicleNo)values"
            query = query+"('"+str(data["name"])+"','"+str(data["mobile"])
            query= query+"','"+str(data["userId"])+"','"+str(data1["responderModeId"])+"','"+str(data1["responderTypeId"])+"','"+str(data1["panCardNo"])+"','"+str(data1["DlNo"])+"','"+str(data["currentLocation"])+"','"+str(data["currentLocationlatlong"])+"','"+str(data["vehicleNo"])+"');"
            conn=Connection()
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()
            query = "select * from responderMaster where   mobile='"+str(data1["mobile"])+ "';"
            conn=Connection()
            cursor = conn.cursor()
            cursor.execute(query)
            data1 = cursor.fetchall()
            cursor.close()
            output= {"result":"Revert You Soon,After Verification ","status":"true"}
            return output
        else:
            output = {"result":"User Not Existed ","status":"false"}
            return output 
    except Exception as e :
        print("Exception---->" + str(e))    
        output = {"result":"something went wrong","status":"false"}
        return output        

#rider(goverment,private,Hospital)
@app.route('/addresponderMode', methods=['POST'])
def responderMode():
    try:
        json1=request.get_data() 
        data1=json.loads(json1.decode("utf-8"))  
        
        query = "select * from responderMode where   responderType='"+str(data1["responderType"])+ "';"
        conn=Connection()
        cursor = conn.cursor()
        cursor.execute(query)
        data = cursor.fetchone()
       
        if data==None:
           
            query="insert into responderMode(responderType)values"
            query = query+"('"+str(data1["responderType"])+"');"
            conn=Connection()
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()
            query = "select * from responderMode where   responderType='"+str(data1["responderType"])+ "';"
            conn=Connection()
            cursor = conn.cursor()
            cursor.execute(query)
            data1 = cursor.fetchall()
            cursor.close()
            output= {"result":"User Added Successfully","rider Details":data1[-1],"status":"true"}
            return output
        
        else:
            output = {"result":"User Already Added Existed ","status":"true","ambulance Details":data}
            return output 
    except Exception as e :
        print("Exception---->" + str(e))    
        output = {"result":"something went wrong","status":"false"}
        return output

#select rider(goverment,private,Hospiatl)        
 
@app.route('/responderMode', methods=['GET'])
def responderMode():
    try:
        query = "select * from responderMode "
        conn=Connection()
        cursor = conn.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
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


#update riderMode(g,p,h)

@app.route('/updateresponderMode', methods=['POST'])
def updateresponderMode():
    try:
       
        json1=request.get_data() 
        data=json.loads(json1.decode("utf-8")) 
       
        query1 = " update responderMode set   responderType='" + str(data["responderType"]) + "'  where   id = '" + str(data["id"])+ "' ;"
        print(query1)
        conn=Connection()
        cursor = conn.cursor()
        cursor.execute(query1)
        conn.commit()
        cursor.close()
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
        json1=request.get_data() 
        data1=json.loads(json1.decode("utf-8"))  
        
        query = "select * from responderMaster where   responderType='"+str(data1["responderType"])+ "';"
        conn=Connection()
        cursor = conn.cursor()
        cursor.execute(query)
        data = cursor.fetchone()
       
        if data==None:
           
            query="insert into responderMaster(responderType)values"
            query = query+"('"+str(data1["responderType"])+"');"
            conn=Connection()
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()
            query = "select * from responderMaster where   responderType='"+str(data1["responderType"])+ "';"
            conn=Connection()
            cursor = conn.cursor()
            cursor.execute(query)
            data1 = cursor.fetchall()

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
        query = "select * from responderMaster "
        conn=Connection()
        cursor = conn.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
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



#update rider
@app.route('/updateriderType', methods=['POST'])
def updateriderType():
    try:
       
        json1=request.get_data() 
        data=json.loads(json1.decode("utf-8")) 
       
        query1 = " update responderMaster set   responderType='" + str(data["responderType"]) + "'  where   id = '" + str(data["id"])+ "' ;"
        print(query1)
        conn=Connection()
        cursor = conn.cursor()
        cursor.execute(query1)
        conn.commit()
        cursor.close()
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

@app.route('/allresponders', methods=['GET'])
def allresponders():
    try:
        query = "select * from userMaster where usertypeId='4' "
        conn=Connection()
        cursor = conn.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
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



if __name__ == "__main__":
    CORS(app, support_credentials=True)
    app.run(host='0.0.0.0',port=5078,debug=True)
    