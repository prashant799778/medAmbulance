


              
data ={ 
"to":"fBA9BxUUG7A:APA91bE9iH9pqLsuLOorOGGYPobxryXJ2HqvjM1MMuzGjTeWcvxia-eMAV-oKSm7OjOyKlni_3sdZyH_CKXt4KJljiimAA1vrd78hXnZDffywk9WiFHt4rUE4K8iWc5vpU9lT3goebvo", 
"notification" : {
"body" : "your account has been verified",
"OrganizationId":"2",
"content_available" : "true",
"priority" : "high",
"subtitle":"welcome to ambulance",
"Title":" Hello ambulance driver"
}
}       

@app.route('/addResponder', methods=['POST'])
def addResponder():
    try:
        print('Hello')
        inputdata=request.form.get('data')
        print(inputdata,'inputdata')
        keyarr = ['mobileNo','key','name']
        inputdata=json.loads(inputdata)
        # inputdata =  commonfile.DecodeInputdata(request.get_data()) 
        startlimit,endlimit="",""

        commonfile.writeLog("addResponder",inputdata,0)
        msg = commonfile.CheckKeyNameBlankValue(keyarr,inputdata)
        print(msg,'msg')
       
        if msg == "1":
            mobileNo=inputdata['mobileNo']
            name=inputdata['name']
           
            key = inputdata["key"]
            column = " * "
            whereCondition= " mobileNo='"+str(mobileNo)+ "' and usertypeId='4'"
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

