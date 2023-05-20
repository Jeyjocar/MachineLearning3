"""03-05-2023
Array con NUMPY/algebra lineal
Jeyfrey Calero"""

import numpy as np

algebra = np.array([[2,1,-2],[3,0,1],[1,1,1]])
print(algebra)

lineal = np.array([[-3],[5],[-2]])
print(np.transpose(lineal))

resultado = np.linalg.solve(algebra, lineal)
print(resultado)
print(np.allclose(np.dot(algebra, resultado, lineal)))

#*página donde se validan las ecuaciones matemáticas https://dm.udc.es/elearning/Applets/Resolucion_Stmas/