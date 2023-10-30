class perro:
    def __init__(self, nombre, color, raza):
        self.nombre = nombre
        self.color = color
        self.raza = raza
    def dar_pata(self):
        print("El perro está dando la pata")
perro2 = perro("Luna", "Blanco", "Chihuahua")
print(perro2.nombre)
perro2.nombre = "Balto"
print("El nombre del perro ahora es:", perro2.nombre)
perro2.dar_pata()

class gato(perro):
    def __init__(self, nombre, color, raza, estatura):
        super().__init__(nombre, color, raza)
        self.estatura = estatura

    def maullar(self):
        print("El gato está maullando")

#dame un ejercicio de clase heredada incliyendo bucle while, for, diccionario, lista, funciones, clases, etc
class auto:
    def __init__(self, marca, modelo, color, precio):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.precio = precio
    def __str__(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Color: {self.color}, Precio: {self.precio}"
    def __repr__(self):
        return str(self)
auto1 = auto("Toyota", "Corolla", "Blanco", 20000)
print(auto1)
auto2 = auto("Toyota", "Corolla", "Blanco", 20000)
print(auto2)
auto3 = auto("Toyota", "Corolla", "Blanco", 20000)
print(auto3)
#hereda esa clase a una clase para autos electricos
class auto_electrico(auto):
    def __init__(self, marca, modelo, color, precio, bateria):
        super().__init__(marca, modelo, color, precio)
        self.bateria = bateria
    def __str__(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Color: {self.color}, Precio: {self.precio}, Bateria: {self.bateria}"
    def __repr__(self):
        return str(self)
auto_electrico1 = auto_electrico("Toyota", "Corolla", "Blanco", 20000, 100)
print(auto_electrico1)
auto_electrico2 = auto_electrico("Toyota", "Corolla", "Blanco", 20000, 100)

#crea una lista de autos electricos
autos_electricos = []
autos_electricos.append(auto_electrico1)
autos_electricos.append(auto_electrico2)
print(autos_electricos)
#crea una lista de autos
autos = []
autos.append(auto1)
autos.append(auto2)
autos.append(auto3)
print(autos)
#crea un diciconario de autos
autos_diccionario = {}
autos_diccionario["autos"] = autos
print(autos_diccionario)
#crea un diccionario de autos electricos
autos_electricos_diccionario = {}
autos_electricos_diccionario["autos_electricos"] = autos_electricos
#crea un bucle for para mostrar los autos
for auto in autos:
    print(auto)
#crea un bucle for para mostrar los autos electricos
for auto_electrico in autos_electricos:
    print(auto_electrico)

#clase para contar las vocales de una frase
class contar_vocales:
    def __init__(self, frase):
        self.frase = frase
    def contar_vocales(self):
        contador_vocales = 0
        vocales = ["a","e","i","o","u"]
        for caracter in self.frase:
            if caracter in vocales:
                contador_vocales += 1
        return contador_vocales
frase = contar_vocales("hola mundo")
print(frase.contar_vocales())

#clase para operaciones matematicas basicas(suma,resta,multiplicacion,division), incluyendo numeros par, impar, primos, fibonacci, y divisor para 2
class operaciones_matematicas:
    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2
    def suma(self):
        return self.numero1 + self.numero2
    def resta(self):
        return self.numero1 - self.numero2
    def multiplicacion(self):
        return self.numero1 * self.numero2
    def division(self):
        return self.numero1 / self.numero2
    def par(self):
        if self.numero1 % 2 == 0:
            return True
        else:
            return False
    def impar(self):
        if self.numero1 % 2 != 0:
            return True
        else:
            return False
    def primo(self):
        contador = 0
        for i in range(1, self.numero1 + 1):
            if self.numero1 % i == 0:
                contador += 1
        if contador == 2:
            return True
        else:
            return False
    def fibonacci(self):
        a = 0
        b = 1
        for i in range(self.numero1):
            c = a + b
            a = b
            b = c
        return a
    def divisor(self):
        if self.numero1 % 2 == 0:
            return True
        else:
            return False
numero = operaciones_matematicas(10, 2)
print(numero.suma())
print(numero.resta())
print(numero.multiplicacion())
print(numero.division())
print(numero.par())
print(numero.impar())
print(numero.primo())
print(numero.fibonacci())
print(numero.divisor())

#ordena una lista de numeros de manera manual x=[7,5,6.8.2]
x = [7,5,6,8,2]
for i in range(len(x)):
    for j in range(len(x)):
        if x[i] < x[j]:
            aux = x[i]
            x[i] = x[j]
            x[j] = aux
print(x)

#ordena la lista de numeros de manera automatica x=[7,5,6.8.2]
x = [7,5,6,8,2]
x.sort()
print(x)

#ordena la lista de numeros en forma descendente de manera automatica x=[7,5,6.8.2]
x = [7,5,6,8,2]
x.sort(reverse=True)
print(x)

#ordena la lista de numeros en forma descendente de manera manual x=[7,5,6.8.2]
x = [7,5,6,8,2]
for i in range(len(x)):
    for j in range(len(x)):
        if x[i] > x[j]:
            aux = x[i]
            x[i] = x[j]
            x[j] = aux
print(x)

#funcion para dar un saludo
def saludar(nombre):
    return f"Hola {nombre}"
print(saludar("Juan"))

#resuelveme un ejercicio complicado de examen de la universidad, con clases, funciones, bucles, en un mimso ejercicio
#clase para contar las consonantes de una frase
class contar_consonantes:
    def __init__(self, frase):
        self.frase = frase
    def contar_consonantes(self):
        contador_consonantes = 0
        consonantes = ["b","c","d","f","g","h","j","k","l","m","n","ñ","p","q","r","s","t","v","w","x","y","z"]
        for caracter in self.frase:
            if caracter in consonantes:
                contador_consonantes += 1
        return contador_consonantes
frase = contar_consonantes("hola mundo")
print(frase.contar_consonantes())

#clase para contar los caracteres de una frase
class contar_caracteres:
    def __init__(self, frase):
        self.frase = frase
    def contar_caracteres(self):
        contador_caracteres = 0
        for caracter in self.frase:
            contador_caracteres += 1
        return contador_caracteres
frase = contar_caracteres("hola mundo")
print(frase.contar_caracteres())

#clase para contar las palabras de una frase
class contar_palabras:
    def __init__(self, frase):
        self.frase = frase
    def contar_palabras(self):
        contador_palabras = 0
        for caracter in self.frase:
            if caracter == " ":
                contador_palabras += 1
        return contador_palabras + 1
frase = contar_palabras("hola mundo")
print(frase.contar_palabras())

#de una lista dada, imprime el valor que mas se repita, el primer valor de la lista, el mas alto, el mas bajo, el ultimo valor de la lista, y la suma de sus valores
lista = [1,2,3,4,5,6,7,8,9,10]
print(max(lista))
print(min(lista))
print(lista[0])
print(lista[-1])
print(sum(lista))

