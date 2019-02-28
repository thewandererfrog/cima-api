from playhouse.postgres_ext import PostgresqlExtDatabase
import time

# Connect to a Postgres database.
def getDB():
    try:
        return PostgresqlExtDatabase(
            'cima', 
            user='cima', 
            password='cima',
            host='127.0.0.1', 
            port=5432
        )
    except Exception as e:
        print(e)
    else:
        time.sleep(5)
        getDB()        
