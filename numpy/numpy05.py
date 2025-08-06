import numpy as np

# np.arange(start, stop, step)
arr1 = np.arange(5)  # 0부터 5 미만까지 1씩 증가
print("arr1:", arr1)

arr2 = np.arange(2, 10)  # 2부터 10 미만까지 1씩 증가
print("arr2:", arr2)

arr3 = np.arange(1, 10, 2)  # 1부터 10 미만까지 2씩 증가
print("arr3:", arr3)

arr4 = np.arange(10, 1, -2)  # 10부터 1 초과까지 -2씩 감소
print("arr4:", arr4)

# 실수 범위도 가능
arr5 = np.arange(0, 1, 0.2)
print("arr5:", arr5)