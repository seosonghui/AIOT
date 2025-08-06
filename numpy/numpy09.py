import matplotlib.pyplot as plt
import numpy as np  

numbers = np.random.normal(size=10000)
plt.hist(numbers, bins=50, density=True)
plt.title('Histogram of Normal Distribution')
plt.xlabel('value')
plt.ylabel('Density')
plt.show()

a = np.array([[3, 1], [1, 2]])
b = np.array([9, 8])
x = np.linalg.solve(a, b)   # 선형 방정식의 해를 구함
print(x)
