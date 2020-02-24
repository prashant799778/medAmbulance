import paho.mqtt.client as mqtt
from flask import Flask, render_template



app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
client = mqtt.Client()
client.connect("localhost",1883,60)
while True:
    client.publish("outTopic", '{"ambulanceId":1,"RideId":"cca056e84f1311ea93d39ebd4d0189fc","driverId":1,"lat":28.456789,"lng":77.072472}')
 
# if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=5054, debug=True)