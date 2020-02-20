from flask import request
from datetime import datetime
import json
import uuid
import pymysql
from flask import Flask, send_from_directory, abort                
from flask_cors import CORS


def Connection():
    connection = pymysql.connect(host='localhost',
                                user='root',
                                password='OHAvgawzUw##32',
                                db='medambulance',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)

    #cursor = connection.cursor()
    return connection





URL = "https://fcm.googleapis.com/fcm/send"  # request url

headers = {  
"Content-Type": "application/json",
"Authorization":"key=AAAAaJ2SOao:APA91bFTSnFiNs_zmEcIVdC1TOiLXY0mjAwDtI59WpG93hFkXmy8VSb-AK5C0ktRP39tRB2OUEGT2Eu8_61WmenfMi6RW_eFu6NYDCmII-h88Vabon4L1QicTtynf07gaLItU-0RwaQ7"}
data ={ 
"to":"fBA9BxUUG7A:APA91bE9iH9pqLsuLOorOGGYPobxryXJ2HqvjM1MMuzGjTeWcvxia-eMAV-oKSm7OjOyKlni_3sdZyH_CKXt4KJljiimAA1vrd78hXnZDffywk9WiFHt4rUE4K8iWc5vpU9lT3goebvo", 
"notification" : {
"body" : " driver has arrived at your location",
"OrganizationId":"2",
"content_available" : "true",
"priority" : "high",
"subtitle":"welcome to ambulance User",
"Title":" Hello ambulance User "
}
}