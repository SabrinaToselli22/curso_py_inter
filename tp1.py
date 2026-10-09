# Trabajo Practico 1 #

# Ejercicio 1

A = {1, 2, 3}  
B = {3, 4, 5}
print (A | B)

# Ejercicio 2

print (A & B)

# Ejercicio 3

print(A.symmetric_difference(B))

# Ejercicio 4

A = {1, 2}
B = {1,2,3,4}
print (A.issubset(B))

# Ejercicio 5

A= {10,20,30,40,50}
print(len(A))

# Trabajo Practico 2 #

# Ejercicio 1

a = 10
b = 0
try:
    print(a/b)
except ZeroDivisionError:
    print("no se puede dividir por cero")

# Ejercicio 2

numero = 5
texto = "hola"
try:
        print(numero + texto)
except TypeError:
        print("No se puede sumar un numero con un texto")

# Ejercicio 3

edades = {"Melina":30,"Diego":80}
try:
      print(edades["Gisela"])
except KeyError:
        print("Esa persona no esta en la lista")

# Ejercicio 4

def abrir_o_crear_archivo(nombre_archivo):
    try:
      with open(nombre_archivo, "r") as f:
            contenido= f.read()
            print("contenido del archivo:")
            print(contenido)
    except FileNotFoundError:
      print(F"Error:El archivo '{nombre_archivo}' no existe.Creando uno nuevo...")

      with open(nombre_archivo,"w") as f:
            f.write("este archivo fue creado automaticamente.")
            print("Archivo creado exitosamente.")

abrir_o_crear_archivo("prueba.txt")

# Ejercicio 5

def dividir_numeros(num1,num2): 
     try:
          num1 = float(num1)
          num2= float(num2)

          resultado = num1 / num2
          print("El resultado de la division es:",resultado)
          
     except ZeroDivisionError:
         print("Error:No se puede dividir por cero.")
     except ValueError:
        print("Error: Debe ingresar un numero valido.")

dividir_numeros(10,2)
dividir_numeros(20,5)
dividir_numeros(10,0)
dividir_numeros("hola",2)

# trabajo practico 3 

# Ejercicio 1 - calcular el mayor de dos numeros ingresados por teclado usando el operador ternario.

num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))

mayor = num1 if num1 > num2 else num2

print("El numero mayor es:", mayor)

# Ejercicio 2 buscar una palabra en una lista por teclado usando args y un operador ternario


def buscar(palabra, *args):
    return "Está en la lista" if palabra in args else "No está en la lista"

entrada = input("Ingrese la lista de palabras separadas por espacios: ")
lista = entrada.split()

palabra_buscada = input("Ingrese la palabra a buscar: ")

resultado = buscar(palabra_buscada, *lista)
print(resultado)


# EJERCICIO 3  Determinar si un numero es par o impar


numero = int(input("Ingrese un numero entero: "))

if numero % 2 == 0:
    print(f"El numero {numero} es PAR.")
else:
    print(f"El numero {numero} es IMPAR.")


# EJERCICIO 4 Calcular el promedio de una lista de numeros usando args y un operador ternario


def calcular_promedio(*args):
    return sum(args) / len(args) if args else "No se ingresaron números."

entrada_numeros = input("Ingrese numeros separados por espacios: ")
numeros = [float(n) for n in entrada_numeros.split()] if entrada_numeros.strip() else []

promedio = calcular_promedio(*numeros)
print("El promedio es:", promedio)



# EJERCICIO 5 Imprimir un mensaje de error si no se pasan suficientes argumentos


def validar_argumentos(*args, cantidad_minima=2):
    return "Argumentos procesados correctamente." if len(args) >= cantidad_minima else "Error: No se ingresaron suficientes argumentos."

print(validar_argumentos("azul"))
print(validar_argumentos("azul", "rojo", "negro"))

