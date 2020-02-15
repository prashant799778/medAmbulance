

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
        data = {"status":"true","message":message,"result":[]}       
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


def SelectQuery2(table,columns,whereCondition,groupby,startlimit,endlimit):
    try:
        limitCondition= ""
        
        if whereCondition != "":
            whereCondition = " where 1=1 " + whereCondition
        if startlimit != "" and endlimit != "":
            limitCondition = "limit "+startlimit+","+endlimit
            whereCondition = " where 1=1 and " + whereCondition
        
        if groupby != "":
            groupby = " group by " + groupby
                
        query = " select " + columns + " from " + table + " " + whereCondition  + " " + groupby +" "+ limitCondition +" ;"

        print(query)
        conn = Connection()      
        cursor = conn.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
        cursor.close()
      
        if data:
            data = {"status":"true","message":"","result":data}
        else:
            data = {"status":"false","message":"No Data Found","result":[]}

        return data

    except Exception as e:
        print("Error--->" + str(e))            
        return "0" 

def SelectQueryOrderbyAsc(table,columns,whereCondition,groupby,orderby,startlimit,endlimit):
    try:
        limitCondition= ""
        
        if whereCondition != "":
            whereCondition = " where 1=1 " + whereCondition
        if startlimit != "" and endlimit != "":
            limitCondition = "limit "+startlimit+","+endlimit
            whereCondition = " where 1=1  and " + whereCondition
        
        if groupby != "":
            groupby = " group by " + groupby

        if orderby != "":
            orderby = " order by " + orderby            
                
        query = " select " + columns + " from " + table + " " + whereCondition  + " " + groupby +" "+ orderby + limitCondition +" ;"

        print(query)
        conn = Connection()      
        cursor = conn.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
        cursor.close()
      
        if data:
            data = {"status":"true","message":"","result":data}
        else:
            data = {"status":"true","message":"No Data Found","result":[]}

        return data

    except Exception as e:
        print("Error--->" + str(e))            
        return "0" 

def SelectQueryOrderby(table,columns,whereCondition,groupby,startlimit,endlimit,orderby):
    try:
        limitCondition= ""
        
        if whereCondition != "":
            whereCondition = " where 1=1 " + whereCondition
        if startlimit != "" and endlimit != "":
            limitCondition = "  limit "+startlimit+","+endlimit
        if orderby != "":
            orderby = " order by " + orderby + " DESC "  
        if groupby != "":
            groupby = " group by " + groupby
        print(orderby)    
                
        query = " select " + columns + " from " + table + " " + whereCondition  + " " + groupby +" "+ orderby + limitCondition +" ;"

        print("qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq",query)
        conn = Connection()      
        cursor = conn.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
        cursor.close()
      
        if data:
            data = {"status":"true","message":"","result":data}
            return data
        else:
            data =0
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
            data = {"status":"true","message":message,"result":[]}
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
            data = {"status":"true","message":message,"result":[]}
            return data

        else :
            return "0"
                
    except Exception as e:
       print("Error--->" + str(e))            
       return "0"


def SelectCountQuery(table,whereCondition,groupby):
    try:
        groupby = ""
        if whereCondition != "":
            whereCondition = " where 1=1 " + whereCondition
        if groupby != "":
            groupby = " group by " + groupby
               
        query = " select count(1) as count from " + table + " " + whereCondition  + " " + groupby  + ";"
        print(query)
        conn = Connection()
        cursor = conn.cursor()
        cursor.execute(query)
        data = cursor.fetchall()  
        cursor.close()   

        if data:
            data = json.loads(json.dumps(data))                                 
            return str(data[0]["count"])
        else:
            return "0"

    except Exception as e:
        print("Error--->" + str(e))            
        return "0" 


