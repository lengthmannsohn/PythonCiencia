import matplotlib.pyplot as plt

productos = []
ventas = []

print ("Nombre del comercial:")
comercial = input()

for i in range(5):
    print("Nombre del producto producto:")
    prod = input()
    print("Numero de ventas:")
    num = int(input())
    productos.append(prod)
    ventas.append(num)

print(productos)
print(ventas)

plt.pie(ventas, labels=productos)
plt.title(f"Comercial: {comercial}")
plt.savefig('images/productos.png')
plt.show()