import paho.mqtt.client as mqtt
from flask import Flask, render_template



app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
client = mqtt.Client()
client.connect("localhost",1883,60)
while True:
    client.publish("outTopic", "Hello world11111111111111111")
 
# if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=5054, debug=True)