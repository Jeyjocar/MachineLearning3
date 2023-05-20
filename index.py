"""03-05-2023
Array con NUMPY/bucles
Jeyfrey Calero"""



import numpy as np

primer = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(primer)
print(primer.shape)



"""primer1 = np.array([[1,2,3,4,5,],[6,7,8,9,10]])
print(primer1)
print(primer1.shape)"""

función2 = primer.reshape(2,-3,2)
print(función2)
print(función2.shape)

#recorrer ARRAY con BUCLES

funcion3 = np.array([1,2,3,4,5,6,7,8,9,10])

for i in funcion3:
    print(i)

funcion4 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[11,12,13]]])

"""for i in funcion4:
    for j in i:
        for k in j:
            print(k)"""
#Otra forma

for num in np.nditer(funcion4):
    print(num)

print()
print('/'*30)

funcion5 = np.array([5,7,3,8,4,6,2,0,1])
print(funcion5)
print(np.sort(funcion5))

print()
print('/'*30)

pares = np.array([1,2,3,4,5,6,7,8])
print(pares)

y = np.where(pares %2 == 1)
print(pares)
print(y[0])

print()
print('/'*30)

funcion6 = np.array([1,2,3,4,5,6,7,8,9,10])
vacio = []

for i in funcion6:
    if i %2 == 1:
        vacio.append(True)
    else:
        vacio.append(False)
print(funcion6)
print(vacio)
print(funcion6[vacio])

print()
print('/'*30)

#Matrices Aleatorias

variedad = np.random.randint(100, size=(2,3,4))
print(variedad)

print()
print('/'*30)

variedad = np.random.randint(50,100, size=(2,3,4))
print(variedad)

print()
print('/'*30)

variedad = np.random.randint(50,100, size=(3,3,4))
print(variedad)

print()
print('/'*30)

variedad = np.random.binomial(10, p=0.5, size=(5,10))
print(variedad)

print()
print('/'*30)

variedad = np.random.binomial(10, p=0.5, size=(5,10,2))
print(variedad)

print()
print('/'*30)

variedad = np.random.normal(loc=150, scale=15, size=(5,10))
print(variedad)

print()
print('/'*30)

variedad = np.random.choice([20,40,60,80], size=(5,10))
print(variedad)

print()
print('/'*30)