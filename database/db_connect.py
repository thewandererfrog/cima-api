from playhouse.postgres_ext import PostgresqlExtDatabase
import os
import time

# Connect to a Postgres database.
class Database:
    __instance = None

    def getInstance(a):
        print(a)
        """ Static access method. """
        if Database.__instance == None:
            print("No instance!")
            Database()
        return Database.__instance
    def __init__(self):
        print("Constructing!")
        """ Virtually private constructor. """
        if Database.__instance != None:
            raise Exception("This class is a Database!")
        else:
            print("Try to initi DB")
            try:
                Database.__instance = PostgresqlExtDatabase(
                    os.getenv('DATABASE_DB'), 
                    user=os.getenv('DATABASE_USER'), 
                    password=os.getenv('DATABASE_PASS'),
                    host=os.getenv('DATABASE_URL'), 
                    port=5432
                )
                print(Database.__instance)
            except Exception as e:
                print(e)                    
