import pyodbc
import pandas as pd
# Replace Server with your PC Name
# XXX = Your PC Name

def create_connection():
    conn = None
    try:
        conn = pyodbc.connect("driver={SQL Server};"
                        "server=DFI-NB1738764;"
                        "database=Safecredit;"
                        "trusted_connection=yes;")
    except pyodbc.Error as e:
        print(f"The error '{e}' occurred")
    return conn

# for reading data
def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except pyodbc.Error as e:
        print(f"The error '{e}' occurred")

#for training model data
def execute_query_commit(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed and committed")
        print("Thank you")

    except pyodbc.Error as e:
        print(f"The error '{e}' occurred")

def get_all():
    all_select = pd.read_sql_query("SELECT * FROM Training",conn)
    return (all_select)

def rm_main():
    data = pd.DataFrame(get_all())
    return data

conn = create_connection()