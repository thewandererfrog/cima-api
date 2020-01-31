from playhouse.postgres_ext import PostgresqlExtDatabase
import os
import time

# Connect to a Postgres database.
def getDB():
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
    else:
        time.sleep(5)
        getDB()        
