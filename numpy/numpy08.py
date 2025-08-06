import numpy as np

scores = np.array([[99, 93, 60], [98, 82, 93], [93, 65, 81], [78, 82, 81]])

print(scores.sum())
print(scores.sum(axis=0))  # 각 열의 합
print(scores.sum(axis=1))  # 각 행의 합
print(scores.mean())
print(scores.mean(axis=0))  # 각 열의 평균
print(scores.mean(axis=1))  # 각 행의 평균  
print(scores.std())
print(scores.std(axis=0))  # 각 열의 표준편차
print(scores.std(axis=1))  # 각 행의 표준편차
print(scores.var())
print(scores.var(axis=0))  # 각 열의 분산
print(scores.var(axis=1))  # 각 행의 분산   
print(scores.max())
print(scores.max(axis=0))  # 각 열의 최대값
print(scores.max(axis=1))  # 각 행의 최대값
print(scores.min())
print(scores.min(axis=0))  # 각 열의 최소값
print(scores.min(axis=1))  # 각 행의 최소값
print(scores.argmax())  # 전체 배열에서 최대값의 인덱스
print(scores.argmax(axis=0))  # 각 열에서 최대값의 인덱스
print(scores.argmax(axis=1))  # 각 행에서 최대값의 인덱스