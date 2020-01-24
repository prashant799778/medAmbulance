
from config import connection
import commonfile
import json
import smtplib 
import config
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def InsertQuery(table,columns,values):
    try:
        
        query = " insert into " + table + " (" + columns + ") values(" + values + ");" 
        print(query)
        conn = Connection()
        cursor = conn.cursor()
        cursor.execute(query)            
        conn.commit()        
        cursor.close()   

        message = commonfile.Successmessage('insert')
        data = {"status":"true","message":message,"result":""}       
        return data

    except Exception as e:
        print("Error--->" + str(e))            
        return "0" 


def SelectQuery(table,columns,whereCondition):
    try:
       
        
        if whereCondition != "":
            whereCondition = " where 1=1 " + whereCondition
        
        
       
                
        query = " select " + columns + " from " + table + " " + whereCondition  + "  ;"

        print(query)
        conn = Connection()      
        cursor = conn.cursor()
        cursor.execute(query)
        data = cursor.fetchone()
        cursor.close()
      
        if data:
            data = {"status":"true","message":"","result":data}
        else:
            data = {"status":"true","message":"No Data Found","result":""}

        return data

    except Exception as e:
        print("Error--->" + str(e))            
        return "0" 



def SelectQuery1(table,columns,whereCondition):
    try:
       
        
        if whereCondition != "":
            whereCondition = " where 1=1 " + whereCondition
        
        
       
                
        query = " select " + columns + " from " + table + " " + whereCondition  + "  ;"

        print(query)
        conn = Connection()      
        cursor = conn.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
        cursor.close()
      
        if data:
            data = {"status":"true","message":"","result":data}
        else:
            data = {"status":"true","message":"No Data Found","result":""}

        return data

    except Exception as e:
        print("Error--->" + str(e))            
        return "0"         



def UpdateQuery(table,columns,whereCondition):
    try:

        if whereCondition != "":
            whereCondition = " where 1=1 " + whereCondition  

        if columns != "":   
            query = " update " + table + " set " + columns  + " " + whereCondition  + ";"             
            print(query)
            conn = Connection()
            cursor = conn.cursor()         
            cursor.execute(query)
            conn.commit()
            cursor.close()
              
            message = commonfile.Successmessage('update')
            data = {"status":"true","message":message,"result":""}
            return data
        else:
            return "0"

    except Exception as e:
        print("Error--->" + str(e))            
        return "0"

def DeleteQuery(table,whereCondition):
    try:

        if whereCondition != "":
            whereCondition = " where 1=1 " + whereCondition        

            query = " delete from " + table + " " + whereCondition + ";" 
            print(query)
            con = DBconnection()
            cursor = con.cursor()
            cursor.execute(query)
            con.commit()
            cursor.close()

            message = commonfile.Successmessage('delete')
            data = {"status":"true","message":message,"result":""}
            return data

        else :
            return "0"
                
    except Exception as e:
       print("Error--->" + str(e))            
       return "0"

def SendEmail(emailto,subject,message):
       
    message = Mail(
    from_email = config.EmailFrom,
    to_emails = emailto,
    subject = "Fandom email Varification",
    html_content = '<strong>Thank you for visiting FandomLive </strong> <br> . <br> Thanks, FandomLive Team')
    print(message)

    try:
        sg = SendGridAPIClient('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')
        response = sg.send(message)
       
        return "1" 
            
    except Exception as e:
        print("Error--->" + str(e))            
        return "0"



def SendSMS(SMSTo,message):
    try:   
            
        return commonfile.GetRandomNo()
            
        #return "1" 
                
    except Exception as e:
       print("Error--->" + str(e))            
       return "0"
