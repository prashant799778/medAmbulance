import paho.mqtt.client as mqtt
from flask import Flask, render_template



app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
client = mqtt.Client()
client.connect("localhost",1883,60)
while True:
    client.publish("outTopic", '{"userId":"91dbe288564e11ea93d39ebd4d0189fc","ambulanceId":1,"RideId":"cca056e84f1311ea93d39ebd4d0189fc","driverId":1,"lat":28.456788,"lng":77.072472}')


              
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