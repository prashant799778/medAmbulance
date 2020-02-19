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
   
  print(msg,"===============")
  print(data,"============",msg.topic)
  client.publish(str(msg.topic), "Hello world11111111111111111")
  print("qqqqqqqqqqqqqqqqqqqqqqqqqqqq")
  
  try:
    data = json.loads(data)
    print(data)
    ambulanceId=data["ambulanceId"]
    driverId=data["driverId"]
    lat=data["lat"]
    lng=data["lng"]

    column=" ambulanceId, onTrip,onDuty "
    whereCondition=" ambulanceId='"+str(ambulanceId)+"'"
    ambulanceTripDetails = databasefile.SelectQuery1("ambulanceRideStatus",column,whereCondition)
    

    #if ambulanceRideId!=0:
    if (ambulanceTripDetails[0]["onTrip"]==1) and (ambulanceTripDetails[0]["onDuty"]==1):

      column1=" id,bookingId "
      whereCondition1=" and  ambulanceId='"+str(ambulanceId)+"'"
      orderby=" id "
      ambulanceRideId = databasefile.SelectQueryOrderby("bookAmbulance",column1,whereCondition1,"","0","1",orderby)



      column=" rideId,ambulanceId,driverId,lat,lng "
      values="'"+str(ambulanceRideId["result"][0]["bookingId"])+"','"+str(ambulanceId)+"','"+str(driverId)+"','"+str(lat)+"','"+str(lng)+"'"
      insertdata=databasefile.InsertQuery("ambulanceRideTracking",column,values)
      
    
    elif  (ambulanceTripDetails[0]["onTrip"]==0) and (ambulanceTripDetails[0]["onDuty"]==1):
      print("2222222222222222222")
      column= " lat='" + str(lat) ++"',lng='"+ str(lng) + "'"
      whereCondition=" and ambulanceId='" + str(ambulanceId)+   "' "
      data = databasefile.UpdateQuery("ambulanceRideStatus",column,whereCondition)

    
  except Exception as e :
    print("Exception---->" + str(e))    
    output = {"result":"something went wrong","status":"false"}
     
  




client = mqtt.Client()
client.connect("localhost",1883,60)

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()