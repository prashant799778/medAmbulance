
from datetime import datetime,timedelta
import pytz 
import json
import config
import hashlib
import random
import uuid
 
#current datetime time zone india
def CurrentDatetime():
    ist = pytz.timezone('Asia/Kolkata')
    ist_time = datetime.now(tz=ist)
    ist_f_time = str(ist_time.strftime("%Y-%m-%d %H:%M:%S"))
    return  ist_f_time 



#success message for crud operation
def Successmessage(type):
    if type == "insert":
        output ="Record Inserted Successfully"
    elif type == "update":
        output ="Record Updated Successfully"
    elif type == "delete":
        output ="Record Deleted Successfully"

    return output

def DecodeInputdata(data):
    data = json.loads(data.decode("utf-8"))                 
    return data




