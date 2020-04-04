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
  topic=data["userId"]+"/notifyRide"
  #print(topic,"topic==================")
  data1 = json.dumps(data)
  #print("11111111111111")
  #print("1")
  #print(data)
  client.publish(topic, data1)
  client.disconnect()
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
    whereCondition22=" am.ambulanceId=bm.ambulanceId  and bookingId= '"+str(bookingId)+"'"
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
      bookingDetails["message"]="driver Arrived Successfully near user"  
      if (bookingDetails!='0'):  
        return bookingDetails
    else:
      y=str(Distance) +'Km'
      y1={"distanceFromLocation":y}
      bookingDetails['result'].update(y1)
      data={"result":bookingDetails['result'],"message":" driver has stil not Arrived ","status":"true"}
      return data
  except Exception as e :
  #print("Exception---->" + str(e))    
  output = {"result":"something went wrong","status":"false"}
     
  




client = mqtt.Client()
client.connect("localhost",1883,60)
client.on_connect = on_connect
client.on_message = on_message
client.loop_forever()
          

    
  