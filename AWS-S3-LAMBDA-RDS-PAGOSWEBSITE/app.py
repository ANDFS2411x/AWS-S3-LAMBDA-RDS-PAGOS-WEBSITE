import boto3
from flask import Flask, render_template, request, redirect, url_for
import pymysql
from botocore.exceptions import NoCredentialsError

# Configuración de la base de datos
DB_CONFIG = {
    'host': 'endpoint',
    'user': 'admin',
    'password': 'tucontraseña',
    'database': 'tabladesql'
}

# Configuración de S3
S3_BUCKET = 'reporte-pagos-bucket'
s3_client = boto3.client('s3')

# Inicializar la app Flask
app = Flask(__name__)

# Función para generar una URL firmada para un archivo en S3
def generar_url_firmada(bucket_name, archivo_nombre):
    try:
        url = s3_client.generate_presigned_url('get_object',
                                              Params={'Bucket': bucket_name, 'Key': archivo_nombre},
                                              ExpiresIn=3600)  # La URL expira en 1 hora
        return url
    except NoCredentialsError:
        print("Credenciales no válidas")
        return None

# Ruta para ver los datos de la tabla pagos
@app.route('/')
def mostrar_datos():
    connection = pymysql.connect(**DB_CONFIG)
    try:
        with connection.cursor() as cursor:
            sql = "SELECT Nombre, Apellido, Cedula, Valor_PagosPagado, Fecha_Consignacion FROM pagos"
            cursor.execute(sql)
            pagos = cursor.fetchall()
    except Exception as e:
        print(f"Error al conectar con la base de datos: {str(e)}")
        pagos = []
    finally:
        connection.close()
    
    return render_template('tabla.html', pagos=pagos)

# Ruta para mostrar el formulario y procesar nuevos pagos
@app.route('/agregar', methods=['GET', 'POST'])
def agregar_pago():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        cedula = request.form['cedula']
        valor = request.form['valor']
        fecha = request.form['fecha']
        
        connection = pymysql.connect(**DB_CONFIG)
        try:
            with connection.cursor() as cursor:
                sql = """
                INSERT INTO pagos (Nombre, Apellido, Cedula, Valor_PagosPagado, Fecha_Consignacion)
                VALUES (%s, %s, %s, %s, %s)
                """
                cursor.execute(sql, (nombre, apellido, cedula, valor, fecha))
                connection.commit()
        except Exception as e:
            print(f"Error al insertar datos: {str(e)}")
        finally:
            connection.close()
        
        return redirect(url_for('mostrar_datos'))
    
    return render_template('formulario.html')

# Ruta para eliminar un pago
@app.route('/eliminar_pago/<cedula>', methods=['GET'])
def eliminar_pago(cedula):
    connection = pymysql.connect(**DB_CONFIG)
    try:
        with connection.cursor() as cursor:
            # Eliminar el pago basado en la cédula
            sql = "DELETE FROM pagos WHERE Cedula = %s"
            cursor.execute(sql, (cedula,))
            connection.commit()
        print(f"Pago con cédula {cedula} eliminado exitosamente.")
    except Exception as e:
        print(f"Error al eliminar el pago: {str(e)}")
    finally:
        connection.close()

    # Después de eliminar el pago, redirigimos a la página de listado de pagos
    return redirect(url_for('mostrar_datos'))

# Ruta para listar los archivos del bucket S3 y generar URLs firmadas
@app.route('/reportes')
def listar_reportes():
    try:
        # Obtener la lista de objetos del bucket
        objetos = s3_client.list_objects_v2(Bucket=S3_BUCKET)
        archivos = [obj['Key'] for obj in objetos.get('Contents', [])]
        
        # Generar las URLs firmadas para cada archivo
        archivos_con_urls = []
        for archivo in archivos:
            url_firmada = generar_url_firmada(S3_BUCKET, archivo)
            if url_firmada:
                archivos_con_urls.append({'nombre': archivo, 'url': url_firmada})
    
    except Exception as e:
        print(f"Error al conectar con S3: {str(e)}")
        archivos_con_urls = []
    
    return render_template('reportes.html', archivos=archivos_con_urls)

if __name__ == '__main__':
    app.run(debug=True)
