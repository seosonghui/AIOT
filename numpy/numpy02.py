import numpy as np      

A = np.array([1, 2, 3, 4, 5])
B = np.array([6, 7, 8, 9, 10])
C = A + B
print("A:", A)
print("B:", B)  
print("C:", C)
D = A < 3
print("D:", D)
print("3보다 작은 원소들", A[A < 3])