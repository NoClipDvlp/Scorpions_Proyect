import sqlite3

# Conexión a la base de datos SQLite
conexion_db = sqlite3.connect("bloqueos.db")

# Crear tabla de bloqueos
cursor = conexion_db.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS bloqueos
                  (numero_tarjeta TEXT, motivo_bloqueo TEXT, fecha_bloqueo TEXT,
                   hora_bloqueo TEXT, correo_electronico TEXT)''')
conexion_db.commit()
cursor.close()

# Cerrar la conexión a la base de datos
conexion_db.close()

