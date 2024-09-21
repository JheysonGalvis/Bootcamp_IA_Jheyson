#El primer tipo de dato compuesto que veremos será la lista

lista = ["Jheyson Galvis", "tecnotutoriales Jheyson Galvis", True, 1.69]
# En el mundo de la programación no contamos del 1 al 10, contamos del 0 al 9
print(lista[0])
lista[0] = "Jheysonsaurio"
print(lista[0])

#La tupla es una lista que no se puede modificar
tupla = ("caldo", "chocolate", "arepa", True, 8.45)
print(tupla[1])
#tupla[1] = "aguapanela"
#print(tupla[1])

#Creando un conjunto set
#El conjunto no admite elementos duplicados
conjunto = {"Jheyson Galvis", "tecnotutoriales Jheyson Galvis", True, 1.69, "Jheyson Galvis"}
print(conjunto)
#Creando un enunciado
print(f"El conjunto es: {conjunto}")

#Creando un diccionario
diccionario = {
    "nombre": "Jheyson",
    "apellidos": "Galvis",
    "estatura": 1.69,
    "está felíz": True,
    "nombre": "Jheyson",
    "edad": 24
}
print(diccionario)
print(diccionario["nombre"])
print(diccionario["apellidos"])
print(diccionario["está felíz"])
print(diccionario["estatura"] + 2) #3.69
print(diccionario["edad"])