import matplotlib.pyplot as plt

print("Grafico de barras de temperaturas")

semana = ('Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo')
temperaturas = []

for i in semana:
    print(f"Introduzca la temperatura del {i}")
    temp = int(input())
    temperaturas.append(temp)

plt.plot(semana,temperaturas, label="Semana 1")
#PODEMOS INCLUIR MAS DATOS DENTRO DEL GRAFICO LINEAL
#SIEMPRE QUE PONGAMOS UNA LABEL A CADA plot()
temperaturas2 = [5, 20, 8, 12, 19, 22, 30]
plt.plot(semana, temperaturas2, label="Semana 2")
plt.legend()
plt.title("Gráfico de barras de las temperaturas de la semana")
plt.xlabel("Dia de la semana")
plt.ylabel("Temperatura")
#PODEMOS ALMACENAR EL GRAFICO EN UNA IMAGEN
plt.savefig('images/temperaturas.png')
plt.show()