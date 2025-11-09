import csv ## importar para el ejercicio 6

## Ejercicio 1
nombre_empresa="TechSolutions" ##creamos variable
año_fundacion=2010 ##otra variable
print("La empresa", nombre_empresa, "fue fundada en el año", año_fundacion) ##imprimimos por consola

## Ejercicio 2
numero_usuario=int(input("Introduce un número: ")) ##pedimo introducir un número
if numero_usuario == 0: ##comprobamos si es 0, positivo o negativo
    print("El número es cero.")
elif numero_usuario > 0:
    print("El número es positivo.")
else:
    print("El número es negativo.")
for i in range(1, 11): ## bucle indica el rango de inicio y final es 11 porque el ultimo no se imprime
    print(i)

## Ejercicio 3
def calcular_iva(precio): ##funcion para calcular IVA
    return precio * 0.21

print(calcular_iva(100)) ##llamamos a la funcion con precio 100

## Ejercicio 4
lista_empleados=["Ana", "Carlos", "María", "Luis"]##creamos lista
lista_empleados.append("Pedro")##añadimos un empleado
info_empleado = {"nombre": "Ana", "edad": 30, "departamento": "Desarrolladora"}##creamos diccionario
print("Departamento: ", info_empleado["departamento"])##indicamos la clave departamento e imprime su valor

## Ejercicio 5
class Producto:
    def __init__(self, nombre, precio, cantidad):##constructor de la clase
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def get_nombre(self):##getters
        return self.nombre
    def get_precio(self):##getters
        return self.precio
    def get_cantidad(self):##getters
        return self.cantidad

    def calcular_total(self):##metodo para calcular total
        return self.precio * self.cantidad
    def disminuir_cantidad(self, cantidad_vendida):##paracido a un setter pero solo diminuye
        self.cantidad -= cantidad_vendida
    def aumentar_cantidad(self, cantidad_recibida):##lo mismo pero aumenta
        self.cantidad += cantidad_recibida
##probamos la clase y sus funciones
portatil = Producto("Portátil", 800, 2)

print("El precio total de", portatil.get_nombre(), "es", portatil.calcular_total())

portatil.aumentar_cantidad(3)

print("El precio total de", portatil.get_nombre(), "es", portatil.calcular_total())

portatil.disminuir_cantidad(4)

print("El precio total de", portatil.get_nombre(), "es", portatil.calcular_total())

## Ejercicio 6
with open("empleados.txt", "r") as txt: ##abrimos el archio en modo lectura y los guardamos en la variable txt
    contenido = txt.read()##leemos el contenido del archivo
    print(contenido)##imprimimos el contenido

csvArchivo = open('productos.csv')##abrimos el archivo csv
productos = csv.reader(csvArchivo, delimiter=',')##leemos el archivo, con reader tenemos el parametro delimiter para indicar el separador
lista_productos=[]##lista para guardar las instancias

for f in productos:##recorremos la variable productos, creando las instancias de la clase Producto y las añadimos a la lista
    instancia = Producto(f[0], float(f[1]), int(f[2]))##creamos la instancia con los datos del csv
    lista_productos.append(instancia)##añadimos la instancia a la lista

for p in lista_productos:##recorremos la lista e imprimimos el nombre y el total
    print("Producto:", p.get_nombre(), "- precio:", p.get_precio(), "- cantidad:", p.get_cantidad(), "- total:", p.calcular_total())