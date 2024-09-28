lista = ["Numpy",
    "Pandas",
    "Scikit-learn",
    "TensorFlow",
    "Keras"]
print (lista)
#print("Primer elemento:", mix[0])
#print("Segundo elemento:", mix[1])
#print("Ultimo elemento:", mix[-1])
string = "Numpy"
print("Pimer elemento:", string[0])
print("Segundo elemento:", string[1])
print("Ultimo elemento:", string[-1])
mix = ["uno", 2, 3.14, True, [1, 2, 3]]
print(mix)
print(len(mix))
print(mix[0:2])
print(mix[:2])
print(mix[2:])
print(mix[2:-2])
mix.append(["Romulo", "Nancy"])
mix.insert(0, "Jheyson Galvis")
print(mix)
print(mix.index("Jheyson Galvis"))
numbers = [1, 2, 3, 4]
print(numbers)
print(type(numbers))
print("Mayor:", max(numbers))
print("Menor:", min(numbers))
print(numbers)
del numbers[-1]
print(numbers)
del numbers [:2]
print(numbers)
del numbers
#print(numbers)