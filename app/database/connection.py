import mysql.connector 

def execute_query(query):
    try:
        conectar = mysql.connector.connect(
            user='root',
            password='JuanEstebanRiveroRoche',
            host='localhost',
            database='customers',
            port='3306'
        )
        cursor = conectar.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        conectar.commit()
        return result
    except Exception as e:
        print("Error executing query:", e)
    finally:
        cursor.close()
        conectar.close()

# JuanEstebanRiveroRoche

