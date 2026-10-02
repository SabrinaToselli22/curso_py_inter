#Trabajo Practico 1#

#Ejercicio 1

A = {1, 2, 3}  
B = {3, 4, 5}
print (A | B)

#Ejercicio 2

print (A & B)

#Ejercicio 3

print(A.symmetric_difference(B))

#Ejercicio 4

A = {1, 2}
B = {1,2,3,4}
print (A.issubset(B))

#Ejercicio 5

A= {10,20,30,40,50}
print(len(A))

#Trabajo Practico 2#

#Ejercicio 1

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

#Ejercicio 5

def dividir_numeros(num1,num2): 
     try:
          resultado = num1 / num2
          print("El resultado de la division es:",resultado)
     except ZeroDivisionError:
         print("Error:No se puede dividir por cero.")

dividir_numeros(10,2)
dividir_numeros(20,5)
dividir_numeros(10,0)
    
