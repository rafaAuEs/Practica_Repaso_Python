import csv ## importar para el ejercicio 6

nombre_empresa="TechSolutions"
año_fundacion=2010
print("La empresa", nombre_empresa, "fue fundada en el año", año_fundacion)

numero_usuario=int(input("Introduce un número: "))
if numero_usuario == 0:
    print("El número es cero.")
elif numero_usuario > 0:
    print("El número es positivo.")
else:
    print("El número es negativo.")

def calcular_iva(precio):
    return precio * 0.21

print(calcular_iva(100))

lista_empleados=["Ana", "Carlos", "María", "Luis"]
lista_empleados.append("Pedro")
info_empleado = {"nombre": "Ana", "edad": 30, "departamento": "Desarrolladora"}
print("Departamento: ", info_empleado["departamento"])

class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def get_nombre(self):
        return self.nombre

    def calcular_total(self):
        return self.precio * self.cantidad
    def disminuir_cantidad(self, cantidad_vendida):
        self.cantidad -= cantidad_vendida
    def aumentar_cantidad(self, cantidad_recibida):
        self.cantidad += cantidad_recibida
    def __str__(self):## esto es del ejercicio 6
        return f"{self.nombre} - Precio: ${self.precio:.2f}, Cantidad: {self.cantidad}"

portatil = Producto("Portátil", 800, 2)

print("El precio totoal de", portatil.get_nombre(), "es", portatil.calcular_total())

portatil.aumentar_cantidad(3)

print("El precio totoal de", portatil.get_nombre(), "es", portatil.calcular_total())

portatil.disminuir_cantidad(4)

print("El precio totoal de", portatil.get_nombre(), "es", portatil.calcular_total())

with open("empleados.txt", "r") as txt:
    contenido = txt.read()
    print(contenido)

productos = []

with open("productos.csv", newline='', encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)  # Usa la primera línea como encabezado
    for fila in lector:
        producto = Producto(fila["nombre"], float(fila["precio"]), int(fila["cantidad"]))
        productos.append(producto)

for p in productos:
    print(p)
