import numpy as np
import matplotlib.pyplot as plt

heights = [1.83, 1.75, 1.68, 1.80, 1.90]
weights = [70, 65, 60, 75, 80]

np_heights = np.array(heights)
np_weights = np.array(weights)          

bmi = np_weights / (np_heights ** 2)
print("BMI:", bmi)

plt.plot(bmi, marker='o')
plt.show()