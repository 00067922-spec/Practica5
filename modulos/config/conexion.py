import mysql.connector
from mysql.connector import Error

def obtener_conexion():
    try:
        conexion = mysql.connector.connect(
            host='bajbkalh7yvvxmv9sb7k-mysql.services.clever-cloud.com',
            user='usgfd3oz3rlvjd4k',
            password='35K9q9MbM8PKSDCGs9Zh',
            database='bajbkalh7yvvxmv9sb7k',
            port=3306
        )
        if conexion.is_connected():
            print("✅ Conexión establecida")
            return conexion
        else:
            print("❌ Conexión fallida (is_connected = False)")
            return None
    except mysql.connector.Error as e:
        print(f"❌ Error al conectar: {e}")
        return None


