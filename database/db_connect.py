from playhouse.postgres_ext import PostgresqlExtDatabase
import os
import time

global count
count= 0
# Connect to a Postgres database.
def getDB():
    global count    
    print(count)
    
    count = count+1
    try:
        return PostgresqlExtDatabase(
            'cima', 
            user=os.getenv('DATABASE_USER'), 
            password=os.getenv('DATABASE_PASS'),
            host=os.getenv('DATABASE_URL'), 
            port=5432
        )
    except Exception as e:
        print(e)
        time.sleep(5)
        #getDB()   
             
