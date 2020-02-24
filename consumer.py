import paho.mqtt.client as mqtt
import json
from config import Connection
import time


def on_connect(client, userdata, flags, rc):
	print("-------Connected-------",rc)
	client.subscribe("#")
	#client.publish("topic1","data111111")
	

#def on_message(client, userdata, msg):    
	# data = msg.payload.decode('utf-8')
	# print(time.time()*1000)
	# data = json.loads(data) 
	# client.publish("#","data111111")  
	# print(data)


def on_message(client, userdata, msg):
	try:
		data = msg.payload.decode('utf-8')#client.publish("outTopic1","data111111")
		t=time.time()
		print(t*1000)
		data= json.loads(data)
		print(data)
		print(type(data))


		if 'text' in data:
			query2  = " insert into preiscribeMedicine(patientId,doctorId,text)"
			query2 =query2 +" values("+'"'+str(data["PatientId"])+'"'+','+'"'+str(data["doctorId"])+'"'+','+'"'+str(data["text"])+'"'+");"
			conn=Connection()
			cursor = conn.cursor()
			cursor.execute(query2)
			conn.commit()
			cursor.close()


		
		else:
			PatientId=data["PatientId"]
			heartRate=str(data["heartRate"]).replace("'",'"')
			spo2=str(data["spo2"]).replace("'",'"')
			pulseRate=str(data["pulseRate"]) .replace("'",'"')
			highPressure=str(data["highPressure"]).replace("'",'"')
			lowPressure=str(data["lowPressure"]).replace("'",'"')
			temperature=str(data["temperature"]).replace("'",'"')
			query2  = " insert into Patient_Vital_master(Patient_Id,spo2,pulseRate,highPressure,lowPressure,heartRate,temperature)"
			query2 =query2 +" values('"+str(PatientId)+"','"+str(spo2)+"','"+str(pulseRate)+"','"+str(highPressure)+"','"+str(lowPressure)+"','"+str(heartRate)+"','"+str(temperature)+"');"
			print(query2)
			conn=Connection()
			cursor = conn.cursor()
			cursor.execute(query2)
			conn.commit()
			cursor.close()
	except Exception as e :
		print("Exception---->" + str(e))    
		output = {"result":"something went wrong","status":"false"}
     
  
    
client = mqtt.Client()
client.connect("localhost",1883,60)#159.65.146.25
# while True:
    # client.publish("outTopic1", "Hello worldddddd!")
client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()
