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









 








