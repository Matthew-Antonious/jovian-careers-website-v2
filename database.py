import mysql.connector
from dotenv import load_dotenv
import os

# Load the env variables
load_dotenv()

# Replace the placeholders with your actual values os.environ uses a default value if the key is not found
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST")
dbname = os.getenv("DB_NAME")
# table_name = "jobs"

connection = mysql.connector.connect(
    user=user,
    password=password,
    host=host,
    database=dbname
)

# Create a cursor
cursor = connection.cursor(dictionary=True)

def load_jobs_from_db():
    #connection.reconnect()
    cursor.execute("SELECT * FROM jobs")
    #cursor = connection.cursor(dictionary=True)   
    result_dicts = []
    for row in cursor.fetchall():
        result_dicts.append(dict(row))
    return result_dicts

def load_job_from_db(job_id):
    # connection.reconnect()
    query = "SELECT * FROM jobs WHERE id = %s"
    cursor.execute(query, (job_id,))
    row = cursor.fetchone()
    if row:
        return dict(row)
    return None

