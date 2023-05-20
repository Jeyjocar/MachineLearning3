"""03-05-2023
Array con NUMPY
Jeyfrey Calero"""

import numpy as np

"""a = np.array([[1,2,3,4,5,6],
             [7,8,9,10,11,12],
             [13,14,15,16,17,18],
             [19,20,21,22,23,24]]
             )

np.save('mi_matriz.npy',a)""" #* MODULANDO #para guardar archivos npy guardar sin extensión CSV y para guardar archivos CSV se debe usar el DELIMITER =","

"""prueba = np.load('mi_matriz.npy')
print(prueba)"""

#*Para guardar varias matrices o archivos se usa SAVEZ y NPY, a,b,c,d,e según sea le nombre del archivo

"""a = np.array([[1,2,3,4,5,6],
             [7,8,9,10,11,12],
             [13,14,15,16,17,18],
             [19,20,21,22,23,24]]
             )

b = np.array([[-1,-2,-3,-4,-5,-6],
             [-7,-8,-9,-10,-11,-12],
             [-13,-14,-15,-16,-17,-18],
             [-19,-20,-21,-22,-23,-24]]
             )

np.savez('matriz2.npz',a,b)"""

prueba = np.load("matriz2.npz") 
print(prueba)
             