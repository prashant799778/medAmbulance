import paho.mqtt.client as mqtt
from flask import Flask, render_template



app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
client = mqtt.Client()
client.connect("localhost",1883,60)
while True:
    client.publish("ambulanceLiveLocation", '{"userId":"0726dd0e4f2911ea93d39ebd4d0189f1","driverId":["0726dd0e4f2911ea93d39ebd4d0189f1"],"startLocationLat":29.2261234,"startLocationLong":77.6294229,"pickupLocationAddress":"Unnamed Road, Uttar Pradesh, India, null","dropLocationLat":28.6185,"dropLocationLong":77.3726,"dropLocationAddress":"Fortis Hospital sec-62, Noida","lat":"29.3309517","lng":"77.6171017","ambulanceId":"1","bookingId":"61dcfbba77d911ea93d49ebd4d0189fc"}')
 