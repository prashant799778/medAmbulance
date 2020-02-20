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


# def makeVoteNotification(FDP,FDT,UserName):
#     try:
#         config.data['subtitle'] = "Congratulation "+str(UserName)+" - You Earned "+str(FDP)+" FandomPoints and "+str(FDT)+" FandomTokens"
#         print(config.data)
#         r=requests.post(config.URL, headers=config.headers, data=json.dumps(config.data))
#         response=json.loads(r.text) 
#         if response:
#             return response
#         else:
#             return commonfile.Errormessage()
#     except Exception as e :
#         print("Exception--->" + str(e))                                  
#         return commonfile.Errormessage()

# def makeRewardNotification(FDP,FDT,UserName):
#     try:
#         config.data['subtitle'] = "Congratulation "+str(UserName)+" - You Earned "+str(FDP)+" FandomPoints and "+str(FDT)+" FandomTokens"
#         print(config.data)        
#         r=requests.post(config.URL, headers=config.headers, data=json.dumps(config.data))
#         response=json.loads(r.text) 
#         if response:
#             return response
#         else:
#             return commonfile.Errormessage()
#     except Exception as e :
#         print("Exception--->" + str(e))                                  
#         return commonfile.Errormessage()

# def makeSecurityCampaignNotification(FDP,FDT,UserName):
#     try:
#         config.data['subtitle'] = "Congratulation "+str(UserName)+" - You Earned "+str(FDP)+" FandomPoints and "+str(FDT)+" FandomTokens"
#         print(config.data)        
#         r=requests.post(config.URL, headers=config.headers, data=json.dumps(config.data))
#         response=json.loads(r.text) 
#         if response:
#             return response
#         else:
#             return commonfile.Errormessage()
#     except Exception as e :
#         print("Exception--->" + str(e))                                  
#         return commonfile.Errormessage()

# def loginNotification(FDP,FDT,UserName):
#     try:
#         config.data['subtitle'] = "Congratulation "+str(UserName)+" - You Earned "+str(FDP)+" FandomPoints and "+str(FDT)+" FandomTokens"
#         print(config.data)        
#         r=requests.post(config.URL, headers=config.headers, data=json.dumps(config.data))
#         response=json.loads(r.text) 
#         if response:
#             return response
#         else:
#             return commonfile.Errormessage()
#     except Exception as e :
#         print("Exception--->" + str(e))                                  
#         return commonfile.Errormessage()


# def signupReferralNotification():
#     try:
#         r=requests.post(config.URL, headers=config.headers, data=json.dumps(config.data))
#         response=json.loads(r.text) 
#         if response:
#             return response
#         else:
#             return commonfile.Errormessage()
#     except Exception as e :
#         print("Exception--->" + str(e))                                  
#         return commonfile.Errormessage()

# def commentNotification(FDP,FDT,UserName):
#     try:
#         config.data['subtitle'] = "Congratulation "+str(UserName)+" - You Earned "+str(FDP)+" FandomPoints and "+str(FDT)+" FandomTokens"
#         print(config.data)        
#         r=requests.post(config.URL, headers=config.headers, data=json.dumps(config.data))
#         response=json.loads(r.text) 
#         if response:
#             return response
#         else:
#             return commonfile.Errormessage()
#     except Exception as e :
#         print("Exception--->" + str(e))                                  
#         return commonfile.Errormessage()


# def forumLikeNotification(FDP,FDT,UserName):
#     try:
#         config.data['subtitle'] = "Congratulation "+str(UserName)+" - You Earned "+str(FDP)+" FandomPoints and "+str(FDT)+" FandomTokens"
#         print(config.data)        
#         r=requests.post(config.URL, headers=config.headers, data=json.dumps(config.data))
#         response=json.loads(r.text) 
#         if response:
#             return response
#         else:
#             return commonfile.Errormessage()
#     except Exception as e :
#         print("Exception--->" + str(e))                                  
#         return commonfile.Errormessage()

def notification(deviceKey):
    try:
        r=requests.post(config.URL, headers=config.headers, data=json.dumps(config.data))
        response=json.loads(r.text) 
        if response:
            return response
        else:
            return commonfile.Errormessage()
    except Exception as e :
        print("Exception--->" + str(e))                                  
        return commonfile.Errormessage()

