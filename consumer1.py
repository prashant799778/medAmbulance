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

    column=" ambulanceId, onTrip,onDuty "
    whereCondition=" ambulanceId='"+str(data["ambulanceId"])+"'"
    ambulanceTripDetails = databasefile.SelectQuery1("ambulanceRideStatus",column,whereCondition)
    print(ambulanceTripDetails["result"])
    return {"status":"ok"}



    # whereCondition="ambulance_Id='"+str(ambulanceId1)+"'  and hospital_Id='"+str(mainId)+"'"
    # column=""
    # values="'"+str(mainId)+"','"+str(ambulanceId1)+"'"
    # insertdata=databasefile.InsertQuery("hospitalambulanceMapping",column,values)
  except Exception as e :
    print("Exception---->" + str(e))    
    output = {"result":"something went wrong","status":"false"}
     
  




client = mqtt.Client()
client.connect("localhost",1883,60)

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()