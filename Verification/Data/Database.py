import pyodbc

# Replace Server with your PC Name
# XXX = Your PC Name
# YYY = database name
conn = pyodbc.connect("driver={SQL Server};"
            "server=XXX;"
            "database=YYY;"
            "trusted_connection=yes;"
            "autocommit=True")
cursor = conn.cursor()

print("Database connected.")

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

#for inserting data
def execute_query_commit(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed and committed")
        print("Thank you")

    except pyodbc.Error as e:
        print(f"The error '{e}' occurred")