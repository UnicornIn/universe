import mysql.connector

def authenticate_user(username: str, password: str) -> bool:

    conn = mysql.connector.connect(
        host="tu_host",
        user="tu_usuario",
        password="tu_contraseña",
        database="tu_base_de_datos"
    )

    cursor = conn.cursor()

    query = "SELECT password FROM users WHERE username = %s"
    cursor.execute(query, (username,))
    result = cursor.fetchone()

    if result and result[0] == password:
        return True
    else:
        return False

    cursor.close()
    conn.close()