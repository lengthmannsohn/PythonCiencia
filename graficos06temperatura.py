import matplotlib.pyplot as plt

print("Grafico de barras de temperaturas")

diaSemana = ('Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo')
temperatura = []

for i in diaSemana:
    print(f"Introduzca la temperatura del {i}")
    temp = int(input())
    temperatura.append(temp)

plt.plot(diaSemana,temp)
#PERSONALIZAR EL GRAFICO
plt.title("Gráfico de barras de las temperaturas de la semana")
plt.xlabel("Dia de la semana")
plt.ylabel("Temperatura")
#PODEMOS ALMACENAR EL GRAFICO EN UNA IMAGEN
plt.savefig('images/temperaturas.png')
plt.show()