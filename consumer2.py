import paho.mqtt.client as mqtt
import json
import databasefile


def on_connect(client, userdata, flags, rc):
  print("-------Connected-------")
  print(client, userdata, flags, rc)
  client.subscribe("#")
  #client.publish("#", "Hello world!");

def on_message(client, userdata, msg):    
  data = msg.payload.decode('utf-8')
  #print(data,"===============",type(data))
  data = json.loads(data)
  # print(msg,"===============")
  # print(data,"============",msg.topic)
  #topic=str(msg.topic)#+"/ambulanceLiveLocation"
 
  #print("2")
  #print("qqqqqqqqqqqqqqqqqqqqqqqqqqqq")
  
  try:
    ambulanceId=data["ambulanceId"]
    lat=data["lat"]
    lng=data["lng"]
    userId=data['userId']
    bookingId=data['bookingId']
    columns="(ar.lat)driverLat,(ar.lng)driverLng, bm.ambulanceId,bm.bookingId,bm.driverId,bm.dropOff,bm.dropOffLatitude,bm.dropOffLongitude"
    columns=columns+",bm.finalAmount,bm.pickup,bm.status,bm.pickupLatitude,bm.pickupLongitude,bm.totalDistance,bm.userMobile,am.ambulanceNo "
    columns=columns+",bm.driverMobile"
    whereCondition22=" am.ambulanceId=bm.ambulanceId  and bm.arrivingstatus='1' and bookingId= '"+str(bookingId)+"' "
    bookingDetails= databasefile.SelectQuery("bookAmbulance bm,ambulanceMaster am,ambulanceRideStatus ar",columns,whereCondition22)
    print(bookingDetails,"================")
    userLat=bookingDetails['result']['pickupLatitude']
    userLng==bookingDetails['result']['pickupLongitude']
    fromlongitude2= lng
    print(fromlongitude2,'fromlong',type(fromlongitude2))
    fromlatitude2 = lat
    print('lat',fromlatitude2)
    distanceLongitude = userLng- fromlongitude2
    distanceLatitude = userLat - fromlatitude2
    a = sin(distanceLatitude / 2)**2 + cos(fromlatitude2) * cos(userLat) * sin(distanceLongitude / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c
    distance2=distance/100
    Distance=distance2*1.85
    if Distance < 0.0012:
        bookingDetails["message"]="driver Arrived"  
        if (bookingDetails['status']!='false'):
            column=" arrivingstatus = '0' "
            whereCondition=" bookingId ='"+str(bookingId)+"'"
            a=databasefile.UpdateQuery('bookAmbulance',column,whereCondition)
            topic=str(userId)+"/notifyRide"
            #print(topic,"topic==================")
            data1 = json.dumps(data)
            #print("11111111111111")
            #print(data)
            client = mqtt.Client()
            client.connect("localhost",1883,60)
            client.publish(topic, data1)
            client.disconnect()
            return bookingDetails
        else:
            data={"result":"","message":"Already Reached to driver","status":"false"}
            return data


    else:
        pass
  except Exception as e :
  #print("Exception---->" + str(e))    
  output = {"result":"something went wrong","status":"false"}
     
  



          

    
  