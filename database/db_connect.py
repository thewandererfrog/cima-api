from playhouse.postgres_ext import PostgresqlExtDatabase
import os
import time

# Connect to a Postgres database.
class Database:
    __instance = None

    def getInstance():
        """ Static access method. """
        if Database.__instance == None:
            Database()
        return Database.__instance
    def __init__(self):
        """ Virtually private constructor. """
        if Database.__instance != None:
            raise Exception("This class is a Database!")
        else:
            try:
                Database.__instance = PostgresqlExtDatabase(
                    os.getenv('DATABASE_DB'), 
                    user=os.getenv('DATABASE_USER'), 
                    password=os.getenv('DATABASE_PASS'),
                    host=os.getenv('DATABASE_URL'), 
                    port=5432
                )
            except Exception as e:
                print(e)                    

