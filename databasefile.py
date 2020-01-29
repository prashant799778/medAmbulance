

from config import Connection
import commonfile
import json
import smtplib 
import config


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
            whereCondition = " where 1=1  and " + whereCondition
        
        
       
                
        query = " select " + columns + " from " + table + " " + whereCondition  + "  ;"

        print(query)
        conn = Connection()      
        cursor = conn.cursor()
        cursor.execute(query)
        data = cursor.fetchone()
        cursor.close()
      
        if data:
            return data
        else:
            data=0
            return data

    except Exception as e:
        print("Error--->" + str(e))            
        return "0" 



def SelectQuery1(table,columns,whereCondition):
    try:
       
        
        if whereCondition != "":
            whereCondition = " where 1=1 and " + whereCondition
        
        
       
                
        query = " select " + columns + " from " + table + " " + whereCondition  + "  ;"

        print(query)
        conn = Connection()      
        cursor = conn.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
        cursor.close()
      
        if data:
            return data
        else:
            data=0
            return data

    except Exception as e:
        print("Error--->" + str(e))            
        return "0"         



def UpdateQuery(table,columns,whereCondition):
    try:

        if whereCondition != "":
            whereCondition = " where 1=1 and " + whereCondition  

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
            whereCondition = " where 1=1 and " + whereCondition        

            query = " delete from " + table + " " + whereCondition + ";" 
            print(query)
            conn = Connection()
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()
            cursor.close()

            message = commonfile.Successmessage('delete')
            data = {"status":"true","message":message,"result":""}
            return data

        else :
            return "0"
                
    except Exception as e:
       print("Error--->" + str(e))            
       return "0"

