#ejemplo
#Ax = B la idea es buscar la matriz x
# A = 2 1 -2
#     3 0 1
#     1 1 -1
#============
# B = -3
#      5
#     -2

import numpy as np 

A = np.array([[2,1,-2],[3,0,1],[1,1,-1]])
print(A)
print("")
B = np.array([[-3],[5],[-2]])
#cambiamos la direccion de la matriz
print(np.transpose(B))
print("")

#lo resolvemos de esta manera
x = np.linalg.solve(A,B)
print(x)
#verificamos si la resolucion es correcta
print(np.allclose(np.dot(A,x),B))
