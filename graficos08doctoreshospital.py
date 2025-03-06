import oracledb
import matplotlib.pyplot as plt


print("Gráfico pie de Hospitales")
connection = oracledb.connect(user='SYSTEM', password='oracle', dsn='localhost/xe')

sql = "select count(*), HOSPITAL.NOMBRE from HOSPITAL inner join DOCTOR on DOCTOR.HOSPITAL_COD = HOSPITAL.HOSPITAL_COD group  by HOSPITAL.NOMBRE"

doctores =[]
hospitales = []

cursor = connection.cursor()
cursor.execute(sql)
for numero, nombre in cursor:
    doctores.append(numero) 
    hospitales.append(nombre) 
cursor.close()
connection.close()

plt.pie(doctores, labels=hospitales)
plt.title("Grafico de numero de doctores por cada hospital")
plt.show()
