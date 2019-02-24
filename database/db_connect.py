from playhouse.postgres_ext import PostgresqlExtDatabase

# Connect to a Postgres database.
def getDB():
    return PostgresqlExtDatabase(
        'cima', 
        user='cima', 
        password='cima',
        host='127.0.0.1', 
        port=5432
    )
