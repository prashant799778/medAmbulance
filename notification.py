from flask import Flask
from flask import request
import json
import pymysql
#from flask_cors import CORS
from datetime import datetime
import pytz 
import hashlib
import databasefile
import commonfile
import requests
import config
import leftoverapi



def notification(deviceKey):
    try:
        # config.data["to"]=str(deviceKey)
        # print(config.data)
        r=requests.post(config.URL, headers=config.headers, data=json.dumps(config.data))
        response=json.loads(r.text) 
        if response:
            return response
        else:
            return commonfile.Errormessage()
    except Exception as e :
        print("Exception--->" + str(e))                                  
        return commonfile.Errormessage()




def notification1(deviceKey):
    try:
        # config.data["to"]=str(deviceKey)
        # print(config.data)
        r=requests.post(config.URL, headers=config.headers, data=json.dumps(leftoverapi.data))
        response=json.loads(r.text) 
        if response:
            return response
        else:
            return commonfile.Errormessage()
    except Exception as e :
        print("Exception--->" + str(e))                                  
        return commonfile.Errormessage()        



