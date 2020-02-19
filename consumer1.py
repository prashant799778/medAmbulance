import paho.mqtt.client as mqtt
import json


def on_connect(client, userdata, flags, rc):
  print("-------Connected-------")
  print(client, userdata, flags, rc)
  client.subscribe("#")
  #client.publish("#", "Hello world!");

def on_message(client, userdata, msg):    
  data = msg.payload.decode('utf-8')
  # data = json.loads(data) 
  print(msg,"===============")
  print(data,"============",msg.topic)
  client.publish(str(msg.topic), "Hello world11111111111111111")
  print("qqqqqqqqqqqqqqqqqqqqqqqqqqqq")
    
client = mqtt.Client()
client.connect("localhost",1883,60)

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()