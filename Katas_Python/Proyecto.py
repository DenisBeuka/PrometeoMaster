from functools import reduce
### 1. Frecuencia de letras en una cadena

# Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias
# de cada letra en la cadena. Los espacios no deben ser considerados.

def frecuencia_letras(cadena):
    cadena = cadena.replace(" ", "").lower() #sustituimos los espacios y lo pongo en minusculas para que no haga distinciones
    frecuencias= {} 
    
    for letra in cadena: # recorremos la cadena con un bucle for
        if letra in frecuencias: # si la letra ya está en el diccionario
            frecuencias[letra] += 1 # sumamos 1 a su frecuencia
        else: # si la letra no está en el diccionario
            frecuencias[letra]=1 # la agregamos con una frecuencia de 1

    return frecuencias

print("Ejercicio 1",  frecuencia_letras("HOLA THE POWER"))


### 2. Doble de cada valor en una lista

# Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map().

def doble_valor(lista):
    return list(map(lambda x:x * 2 , lista)) #aplicamos la función lambda a cada elemento de la lista y la convertimos a lista

print ("Ejercicio 2",doble_valor([1, 2, 3, 4, 5]))  

### 3. Filtrar palabras que contienen una palabra objetivo

# Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe
# devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.


def buscar_palabra (lista, objetivo):
    return [palabra for palabra in lista if objetivo in palabra] #filtramos la lista con un bucle for y una condición 

print("Ejercicio 3" , buscar_palabra(["hola", "mundo", "hola mundo" , "adios"], "hola")) # buscamos la palabra "hola" en la lista




### 4. Diferencia entre valores de dos listas

# Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map().


def diferencia_listas(lista1, lista2):
    return list(map(lambda x,y: x-y , lista1 , lista2)) # lambda donde definimos dos variables y las restamos , esas variables son las dos listas.
lista1=[4 , 10 , 73]
lista2=[1 , 3 , 36]  
resultado= diferencia_listas(lista1, lista2)  
print("Ejercicio 4" , resultado)



### 5. Media y estado de aprobación

# Escribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por
# defecto es 5. La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual
# que nota_aprobado. Si es así, el estado será "aprobado", de lo contrario, será "suspenso". La función debe devolver
# una tupla que contenga la media y el estado.



def media_aprobado(lista, nota_aprobado=5):
    media=sum(lista) / len(lista) #calculamos la media de la lista que es la suma de todos los elementos dividida por la cantidad de elementos
    estado = "aprobado" if media>=nota_aprobado else "suspenso" # si la media es mayor o igual a la nota aprobada el estado es aprobado , si no es suspenso
    return (media, estado) #retornamos una tupla con la media y el estado

notas=[4, 5 , 10 , 7 , 0 ]
resultado= media_aprobado(notas)
print("Ejercicio 5" , resultado)



### 6. Factorial recursivo

# Escribe una función que calcule el factorial de un número de manera recursiva.

def factorial(num):
    return 1 if num== 0 else num*factorial(num-1) #el factorial de 0 es 1 , si no es el número multiplicado por el factorial del número menos

print("Ejercicio 6" , factorial(8))




### 7. Convertir lista de tuplas a lista de strings

# Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map().


def tupla_a_string(lista_tupla):
    return list(map(lambda tupla : str(tupla) , lista_tupla)) #usamos la funcion str que convierte la tupla a String
lista_tupla=[(1,7) , (0,2) , (2,4)]
resultado= tupla_a_string(lista_tupla)
print("Ejercicio 7" , resultado)






### 8. Manejo de excepciones en división

# Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico
# o intenta dividir por cero, maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje
# indicando si la división fue exitosa o no.

def division():
    try:
        num1=float(input("Ingresa el primer número: ")) 
        num2=float(input("Ingresa el segundo número: "))
        resultado = num1 / num2
        print(f"EJERCICIO 8 División exitosa: {num1} / {num2} = {resultado}")
        return resultado
    except ValueError:
        print("Error: El valor ingresado no es un número.")
    except ZeroDivisionError: # manejo de la excepción de división por cero
        print("Error: No se puede dividir por cero.")

division()






### 9. Filtrar mascotas prohibidas

# Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista
# excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre",
# "Serpiente Pitón", "Cocodrilo", "Oso"]. Usa la función filter().

def filtro_mascotas(lista_mascotas):
    mascotas_prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo" , "Oso"]
    return list(filter(lambda mascota : mascota not in mascotas_prohibidas , lista_mascotas)) #filtramos las mascotas prohibidas , es decir que unicamente devolvera , los animales que no esten en la lista de prohibidos
    
mascotas = ["Perro", "Gato", "Mapache", "Tigre", "Conejo", "Oso"]
resultado = filtro_mascotas(mascotas)
print("Ejercicio 9" , resultado)



### 10. Promedio de una lista con manejo de excepciones

# Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una
# excepción personalizada y maneja el error adecuadamente.

def promedio(lista_numeros):
    if not lista_numeros: # si la lista está vacía
        raise ValueError("La lista está vacía.") # lanzamos una excepción personalizada
    return sum(lista_numeros) / len(lista_numeros) # calculamos el promedio
try:
    print("Ejercicio 10", promedio([1, 2, 3, 4, 5]))
except ValueError as e: # es un numero irracional 
    print(e)



### 11. Validación de edad

# Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un
# valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones
# adecuadamente.

### 11. Validación de edad

# Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un
# valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones
# adecuadamente.

def valida_edad():
    try:
        edad = int(input("Introduzca su edad: "))
        if edad < 0 or edad > 120:
            raise ValueError("La edad debe estar entre 0 y 120.")
        print(f"EJERCICIO 11 " , " La edad es válida. {edad}")
    except ValueError as e: # es un numero irracional que el usuario puede introducir en el inpunt int
        print(f"error: {e}")
valida_edad()







### 12. Longitud de cada palabra en una frase

# Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función map().

def longitud_palabras(frase):
    return list(map(len, frase.replace(",", "").split())) # Divide la frase en palabras y no cuenta las comas como palabras
print("Ejercicio 12", longitud_palabras("Hola the power, dadme el master"))






### 13. Letras en mayúsculas y minúsculas

# Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en
# mayúsculas y minúsculas. Las letras no pueden estar repetidas. Usa la función map().


def letras_mayus_minus(caract):
    caract_unicos= set(caract) # elimina las repeticiones
    return list(map(lambda letra: (letra.upper(), letra.lower()), caract_unicos))

caract="HolaHola"
resultado= letras_mayus_minus(caract)
print("Ejercicio 13", resultado) # imprime una lista de tuplas con cada letra en mayúsculas y minúsculas pero de forma desordenada




### 14. Filtrar palabras que comienzan con una letra específica

# Crea una función que retorne las palabras de una lista de palabras que comience con una letra en específico. Usa la
# función filter().


def filtro_letras(lista_palabras , letra):
    return list(filter(lambda palabra: palabra[0].lower() == letra.lower(), lista_palabras)) #iguala la palabra con la letra , las pongo en minuscula para evitar errores

palabras = ["hola", "mundo" , "adios" , "blablabla" , "Denis"]
letra = "D"
resultado = filtro_letras(palabras, letra)
print("Ejercicio 14", resultado)





### 15. Sumar 3 a cada número en una lista

# Crea una función lambda que sume 3 a cada número de una lista dada.


def sumar_tres(lista_numeros):
    return list(map(lambda numero: numero + 3, lista_numeros))
lista_numeros = [1, 2, 3, 4, 5]
resultado = sumar_tres(lista_numeros)
print("Ejercicio 15", resultado)



### 16. Palabras más largas que n

# Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de
# todas las palabras que sean más largas que n. Usa la función filter().

def palabras_largas(cadena, n):
    return list(filter(lambda palabra: len(palabra) > n, cadena.split()))
cadena = "Texto de prueba blablabla si , no"
n = 3
resultado = palabras_largas(cadena, n)
print("Ejercicio 16", resultado)





### 17. Convertir lista de dígitos a número

# Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5, 7, 2]
# corresponde al número quinientos setenta y dos (572). Usa la función reduce().

# arriba he importado la tool (para buena practica)

from functools import reduce
def lista_a_numero(lista_digitos):
    if not lista_digitos:
        raise ValueError("La lista está vacía.")
    return reduce(lambda x, y: x * 10 + y, lista_digitos)
lista_digitos = [5, 7, 2]
try:
    resultado = lista_a_numero(lista_digitos)
    print("Ejercicio 17", resultado)  # 1º 5*10 +7 , 2º 57 *10 +2
except ValueError as e:
    print(e)





### 18. Filtrar estudiantes con calificación alta

# Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes
# (nombre, edad, calificación) y use la función filter para extraer a los estudiantes con una calificación mayor o igual a
# 90. Usa la función filter().

def filtrar_estudiantes(estudiantes):
    return list(filter(lambda estudiante: estudiante['calificacion'] >= 90, estudiantes))
estudiantes = [
    {'nombre': 'Juan', 'edad': 20, 'calificacion': 85},
    {'nombre': 'Pedro', 'edad': 22, 'calificacion': 73},
    {'nombre': 'Denis', 'edad': 19, 'calificacion': 100},
]
resultado = filtrar_estudiantes(estudiantes)
print("Ejercicio 18", resultado)





### 19. Filtrar números impares

# Crea una función lambda que filtre los números impares de una lista dada.

def filtrar_impares(lista_numeros):
    return list(filter(lambda x : x%2 !=0 , lista_numeros))
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = filtrar_impares(lista_numeros)
print("Ejercicio 19", resultado)




### 20. Filtrar valores enteros de una lista mixta

# Para una lista con elementos tipo integer y string, obtén una nueva lista sólo con los valores int. Usa la función filter().



def filtar_enteros(lista_mixta):
    return list(filter(lambda x: isinstance(x,int) , lista_mixta))
lista_mixta = [1, 2, 3, 4, 5, 'a' , '/' , '@']
resultado = filtar_enteros(lista_mixta)
print("Ejercicio 20", resultado)



### 21. Calcular el cubo de un número

# Crea una función que calcule el cubo de un número dado mediante una función lambda.

def calcular_cubo():
    return list(map(lambda x: x**3, range(1, 11)))
resultado = calcular_cubo()
print("Ejercicio 21", resultado)





### 22. Producto total de una lista

# Dada una lista numérica, obtén el producto total de los valores de dicha lista. Usa la función reduce().

from functools import reduce
def producto_total(lista_numeros):
    return reduce(lambda x, y: x*y, lista_numeros)
lista_numeros = [1, 2, 3, 4, 5] 
resultado = producto_total(lista_numeros)
print("Ejercicio 22", resultado)
    





### 23. Concatenar lista de palabras

# Concatena una lista de palabras. Usa la función reduce().

from functools import reduce

def concatenar_palabras(lista_palabras):
    return reduce(lambda x,y: x + " " + y , lista_palabras)
lista_palabras = ['Hola', 'mundo', 'buenos', 'dias']
resultado = concatenar_palabras(lista_palabras)
print("Ejercicio 23", resultado)




### 24. Diferencia total en los valores de una lista

# Calcula la diferencia total en los valores de una lista. Usa la función reduce().



from functools import reduce

def diferencia_total(lista_numeros):
    return reduce(lambda x,y: x-y , lista_numeros)
lista_numeros = [10, 20, 30, 40, 50]
resultado = diferencia_total(lista_numeros)
print("Ejercicio 24", resultado)



### 25. Contar caracteres en una cadena

# Crea una función que cuente el número de caracteres en una cadena de texto dada.

def contar_num_de_caracteres(cadena_carac):
    return len(cadena_carac.replace(" ", "")) #asi no cuenta los espacios como caracteres
cadena_carac = "Hola mundo"
resultado = contar_num_de_caracteres(cadena_carac)
print("Ejercicio 25", resultado)
    




### 26. Resto de la división con lambda

# Crea una función lambda que calcule el resto de la división entre dos números dados.

def resto_division(a, b):
    return lambda x,y: x%y
a = 20
b = 5
resultado = resto_division(a, b)
print("Ejercicio 26", resultado(a, b))



### 27. Promedio de una lista de números

# Crea una función que calcule el promedio de una lista de números.

def promedio_lista(lisst_num):
    return sum(lisst_num)/len(lisst_num)

lisst_num=(3.5,1.5,7,8)
resultado = promedio_lista(lisst_num)
print("Ejercicio 27", resultado)





### 28. Primer elemento duplicado en una lista

# Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.

def primer_elemento_duplicado(lista):
    for i in range(len(lista)):
        if lista.count(lista[i]) > 1:
            return lista[i]
    return None

lisst_num=(3,1,7,8,3)
resultado = primer_elemento_duplicado(lisst_num)
print("Ejercicio 28", resultado)




### 29. Enmascarar cadena de texto

# Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el
# carácter '#', excepto los últimos cuatro.

def enmascarar(cadena):
    return "#" * (len(cadena)-4 ) + cadena[-4:] #se devuelve # hasta la longitud de la cadena -4 y se agrega los últimos 4 caracteres

cadena = "contraseña"
resultado = enmascarar(cadena)
print("Ejercicio 29", resultado)





### 30. Verificar si dos palabras son anagramas

# Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras
# pero en diferente orden.

def anagramas(p1 , p2):
     return sorted(p1) == sorted(p2) #se ordenan las palabras y se comparan
p1="amor"
p2="roma"
f2="odio"
resultado = anagramas(p1, p2)
resultado2 = anagramas(p1,f2)

print("Ejercicio 30", resultado , resultado2)  # se devuelve true o false dependiendo si son anagramas o no


### 31. Buscar nombre en una lista

# Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en
# esa lista. Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se
# lanza una excepción.
def buscar_nombre(lista):
    try:
        nombre = input("Ingrese un nombre a buscar: ")
        if nombre in lista:
            print("El nombre fue encontrado en la lista.")
        else:
            print("No se encontro el nombre en la lista")
    except Exception as e:
        print(f"Error: {e}")
        return lista
    
lista = []
num_nombres = int(input("Ingrese el número de nombres que desea agregar a la lista: ")) #se solicita el número de nombres
for i in range(num_nombres): #va pidiendo nombres hasta que llegue al numero indicado
    nombre = input(f"Ingrese el nombre {i+1}: ")
    lista.append(nombre) #se agregan los nombres a la lista



### 32. Buscar puesto de empleado

# Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y
# devuelva el puesto del empleado si está en la lista, de lo contrario, devuelva un mensaje indicando que la persona
# no trabaja aquí.

def buscar_puesto(nombre_completo, empleados): #se solicitan el nombre completo y el diccionario de empleados con claves y sus valores
    return empleados.get(nombre_completo, "La persona no trabaja aquí.") #.get() busca el valor asociado a la clave nombre_completo en el diccionario. Si no se encuentra el nombre, devuelve el mensaje "La persona no trabaja aquí." como valor por defecto.

# Ejemplo de uso
empleados = {"Juan Alberto": "Gerente", "Anastasia Kolesnikova": "Ingeniera"}
print("Ejercicio 32 " " Puesto:", buscar_puesto("Juan Alberto", empleados))


 
### 33. Sumar elementos correspondientes de dos listas

# Crea una función lambda que sume elementos correspondientes de dos listas dadas.


def sumar_elementos(lista1 , lista2):
    return list(map(lambda x, y: x + y, lista1, lista2)) 

lista1=[4, 2, 3]
lista2=[3, 5, 0]
print("EJERCICIO 33" , sumar_elementos(lista1, lista2))






### 34. Clase Árbol

# Crea la clase Arbol, define un árbol genérico con un tronco y ramas como atributos. Los métodos disponibles son:
# crecer_tronco, nueva_rama, crecer_ramas, quitar_rama e info_arbol. El objetivo es implementar estos métodos para
# manipular la estructura del árbol.

# Código a seguir:
#  1. Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas.
#  2. Implementar el método 
# crecer_tronco para aumentar la longitud del tronco en una unidad.
#  3. Implementar el método 
# nueva_rama para agregar una nueva rama de longitud 1 a la lista de ramas.
#  4. Implementar el método 
# crecer_ramas para aumentar en una unidad la longitud de todas las ramas existentes.
#  5. Implementar el método 
# quitar_rama para eliminar una rama en una posición específica
# 6. Implementar el método 
# info_arbol para devolver información sobre la longitud del tronco, el número de ramas y las longitudes de las 
# mismas.

class Arbol:
    def __init__(self): #constructor de los atributos
        self.tronco = 1
        self.ramas = []
    
    def crecer_tronco(self): #metodos
        self.tronco += 1 # para sumarle 1 a la longitud pre-existente
        
    def nueva_rama(self):
        self.ramas.append(1) # para agregar una rama de longitud 1 a la lista
    
    def crecer_ramas(self):
        self.ramas=[rama + 1 for rama in self.ramas]  # Aumenta en una unidad la longitud de todas las ramas existentes
    
    def quitar_rama(self , posicion):
        if 0<=posicion <len(self.ramas):
            self.ramas.pop(posicion)
        else:
            print("posicion no valida")
            
    def info_arbol(self):
          return (f"Tronco: {self.tronco}, Número de ramas: {len(self.ramas)}, Longitudes de las ramas: {self.ramas}")
      
#1
arbol = Arbol()

#2
arbol.crecer_tronco()

#3
arbol.nueva_rama()

#4
arbol.crecer_ramas()

#5
arbol.nueva_rama()
arbol.nueva_rama()

# 6. Retirar la rama situada en la posición 2
arbol.quitar_rama(2)
#7
print(arbol.info_arbol()) #resultado , crece el tronco a 2 , crea 3 ramas , la primera aumenta a 2 y la tercera es cortada.

        


### 36. Clase UsuarioBanco

# Crea la clase UsuarioBanco, representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta
# corriente. Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario y
# agregar dinero al saldo.

# Código a seguir:
# Inicializar un usuario con su nombre, saldo y si tiene o no cuenta corriente mediante 
# Implementar el método 
# True y 
# False .
#  retirar_dinero para retirar dinero del saldo del usuario. Lanzará un error en caso de no 
# poder hacerse.
#  Implementar el método 
# transferir_dinero para realizar una transferencia desde otro usuario al usuario actual. 
# Lanzará un error en caso de no poder hacerse.
# Implementar el método 
# agregar_dinero para agregar dinero al saldo del usuario.
#  Caso de uso:
#  crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente.  
# Agregar 20 unidades de saldo de "Bob".
#  Hacer una transferencia de 80 unidades desde "Bob" a "Alicia".
#  Retirar 50 unidades de saldo a "Alicia"


class UsuarioBanco:
    def __init__(self, nombre, saldo, cuenta_corriente):
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente

    def retirar_dinero(self, cantidad):
        if cantidad > self.saldo:
            raise ValueError(f"{self.nombre} no tiene suficiente saldo para retirar {cantidad} unidades.")
        self.saldo -= cantidad

    def transferir_dinero(self, otro_usuario, cantidad):
        if cantidad > self.saldo:
            raise ValueError(f"{self.nombre} no tiene suficiente saldo para transferir {cantidad} unidades.")
        self.saldo -= cantidad
        otro_usuario.saldo += cantidad

    def agregar_dinero(self, cantidad):
        self.saldo += cantidad

    def __str__(self):
        return f"{self.nombre} - Saldo: {self.saldo}, Cuenta corriente: {self.cuenta_corriente}"

# Caso de uso corregido:
Alicia = UsuarioBanco("Alicia", 100, True)
Bob = UsuarioBanco("Bob", 60, True)  # Ajustamos el saldo inicial a 60 para cumplir con el enunciado.

Bob.agregar_dinero(20)  # Nuevo saldo de Bob: 80
Bob.transferir_dinero(Alicia, 80)  # Ahora sí puede transferir los 80 sin errores
Alicia.retirar_dinero(50)  # Alicia retira 50 unidades

print(Alicia) 
print(Bob)   


### 37. Función procesar_texto

# Crea una función llamada procesar_texto que procesa un texto según la opción especificada: contar_palabras,
# reemplazar_palabras, eliminar_palabra. Estas opciones son otras funciones que tenemos que definir primero y llamar dentro
# de la función procesar_texto.

from collections import Counter

# Función para contar palabras en el texto
def contar_palabras(texto):
    palabras = texto.split()
    return dict(Counter(palabras))

# Función para reemplazar palabras en el texto
def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    return texto.replace(palabra_original, palabra_nueva)

# Función para eliminar una palabra del texto
def eliminar_palabra(texto, palabra_a_eliminar):
    palabras = texto.split()
    palabras_filtradas = [palabra for palabra in palabras if palabra != palabra_a_eliminar]
    return " ".join(palabras_filtradas)

# Función principal para procesar el texto
from collections import Counter

# Definir funciones antes de llamarlas en procesar_texto
def contar_palabras(texto):
    """Cuenta cuántas veces aparece cada palabra en el texto y devuelve un diccionario."""
    palabras = texto.split()
    return dict(Counter(palabras))

def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    """Reemplaza todas las ocurrencias de una palabra por otra en el texto."""
    return texto.replace(palabra_original, palabra_nueva)

def eliminar_palabra(texto, palabra_a_eliminar):
    """Elimina todas las ocurrencias de una palabra en el texto."""
    palabras = texto.split()
    palabras_filtradas = [palabra for palabra in palabras if palabra != palabra_a_eliminar]
    return " ".join(palabras_filtradas)

# Función principal para procesar el texto
def procesar_texto(texto):
    opciones = {
        "1": contar_palabras,
        "2": reemplazar_palabras,
        "3": eliminar_palabra
    }

    opcion = input("¿Qué acción quieres realizar? 1 (contar palabras), 2 (reemplazar palabras), 3 (eliminar palabra): ")

    if opcion == "1":
        print(opciones["1"](texto))

    elif opcion == "2":
        palabra = input("Introduce la palabra que quieres reemplazar: ")
        reemplazo = input("Introduce la palabra por la que quieres reemplazarla: ")
        print(opciones["2"](texto, palabra, reemplazo))

    elif opcion == "3":
        palabra = input("Introduce la palabra que quieres eliminar: ")
        print(opciones["3"](texto, palabra))

    else:
        print("Introduce una opción válida (1, 2 o 3).")

# Ejemplo de uso
texto_ejemplo = "No se que poner aqui , bla bla cosas."
procesar_texto(texto_ejemplo)




### 38. Determinar si es de noche, día o tarde

# Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario.

def noche_dia(hora):
    if hora >= 18 or hora <= 6:
        return "Es de noche"
    elif 7 <= hora <= 17:  # Corregido: Se usa `elif` en lugar de `else`
        return "Es de día"
    else:
        return "Hora no válida"

try:
    hora = int(input("Introduce la hora (0-23): "))
    print(noche_dia(hora))
except ValueError:
    print("Error: introduce un número entero válido.")


### 39. Calificación en texto

# Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica.
# Las reglas de calificación son:
# - 0 - 69: insuficiente
# - 70 - 79: bien
# - 80 - 89: muy bien
# - 90 - 100: excelente

def calificacion_en_texto(calificacion):
    if 0 <= calificacion <= 69:
        return "Insuficiente"
    elif 70 <= calificacion <= 79:
        return "Bien"
    elif 80 <=calificacion<=89:
        return "Muy bien"
    elif 90 <= calificacion <= 100:
        return "Excelente"
    else:
        return "Calificación no válida"

try:
    calificacion = int(input("Introduce la calificación (0-100): "))
    print("Ejercicio 39  " , calificacion_en_texto(calificacion))
except ValueError:
    print("Error: introduce un número entero válido.")


### 40. Calcular área de una figura
# Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangular", "circulo" o
# "triangular") y datos (una tupla con los datos necesarios para calcular el área de la figura).


def calcular_figura(figura, datos):
    if figura == "rectangular":
        largo, ancho = datos
        return largo * ancho
    elif figura == "circulo":
        radio = datos[0]
        return 3.14 * radio ** 2
    elif figura == "triangular":
        base, altura = datos
        return 0.5 * base * altura
    else:
        return "Figura no válida"

figura = input("Introduce la figura (rectangular, circulo, triangular): ")
datos = input("Introduce los datos (separados por comas): ")
datos = tuple(map(float, datos.split(',')))
print("Ejercicio 40  " , calcular_figura(figura, datos))

###  41 (el 35 no existe en el pdf btw). Aplicar descuento a una compra

# Escribe un programa en Python que utilice condicionales para determinar el monto final de una compra en una tienda en línea,
# después de aplicar un descuento. El programa debe hacer lo siguiente:
# 1. Solicita al usuario que ingrese el precio original de un artículo.
# 2. Pregunta al usuario si tiene un cupón de descuento (respuesta sí o no).
# 3. Si el usuario responde que sí, solicita que ingrese el valor del cupón de descuento.
# 4. Aplica el descuento al precio original del artículo, siempre y cuando el valor del cupón sea válido (es decir, mayor a cero).
# 5. Muestra el precio final de la compra, teniendo en cuenta el descuento aplicado o sin él.



def aplicar_descuento(precio_original, descuento):
    # Aplica el descuento al precio original si el descuento es válido
    if descuento > 0:
        precio_final = precio_original - descuento
    else:
        precio_final = precio_original
    return precio_final

# Solicitar el precio original del artículo
try:
    precio_original = float(input("Introduce el precio original del artículo: "))
    
    # Preguntar si tiene un cupón de descuento
    tiene_cupon = input("¿Tienes un cupón de descuento? (sí/no): ").strip().lower()
    
    if tiene_cupon == "sí":
        # Solicitar el valor del cupón de descuento
        descuento = float(input("Introduce el valor del cupón de descuento: "))
        
        # Aplicar descuento y mostrar el precio final
        precio_final = aplicar_descuento(precio_original, descuento)
        print(f"El precio final con descuento es: {precio_final} euros.")
    else:
        # Mostrar el precio original si no hay descuento
        print(f"El precio final es: {precio_original} euros.")
except ValueError:
    print("Error: Introduce un valor numérico válido.")
