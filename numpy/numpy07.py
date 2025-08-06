import numpy as np  
import matplotlib.pyplot as plt


np.random.seed(0)  # 랜덤 시드 설정
randomNumbers = np.random.randint(1, 100, size=10)  # 1부터 100 사이의 랜덤 정수 10개 생성
print("랜덤 숫자들:", randomNumbers)
randomNumbersTwoDim = np.random.randint(1, 100, size=(3, 4))  # 3x4 형태의 랜덤 정수 배열 생성
print("2차원 랜덤 숫자들:\n", randomNumbersTwoDim)
randomNumbersThreeDim = np.random.randint(1, 100, size=(2, 3, 4))  # 2x3x4 형태의 랜덤 정수 배열 생성
print("3차원 랜덤 숫자들:\n", randomNumbersThreeDim)
randomNumbersNormal = np.random.normal(0, 1, size=10)  # 평균 0, 표준편차 1인 정규 분포 랜덤 숫자 10개 생성
print("정규 분포 랜덤 숫자들:", randomNumbersNormal)

plt.figure(figsize=(12, 5)) # 그래프 전체 크기를 조절할 수 있어!

# 첫 번째 그래프: 산점도 
plt.subplot(1, 2, 1) # 1행 2열의 첫 번째 자리에 그릴 거야
plt.plot(randomNumbers, 'o-', color='salmon', markersize=8) 
plt.title('랜덤 숫자들 (1차원) - 산점도')
plt.xlabel('순서 (인덱스)')
plt.ylabel('값')
plt.grid(True, linestyle='--', alpha=0.6) 

plt.subplot(1, 2, 2) # 1행 2열의 두 번째 자리에 그릴 거야
# 히스토그램은 데이터가 어느 구간에 얼마나 많이 있는지 막대 그래프로 보여줘!
# 데이터 개수가 10개로 적어서 분포가 뚜렷하게 보이진 않을 수 있어. 😊
plt.hist(randomNumbers, bins=range(0, 101, 10), edgecolor='black', color='teal', alpha=0.7)
plt.title('랜덤 숫자들 (1차원) - 히스토그램')
plt.xlabel('값의 범위')
plt.ylabel('빈도수')
plt.grid(axis='y', alpha=0.75)
plt.suptitle('1차원 랜덤 숫자 시각화', fontsize=16, y=1.02) # 전체 제목은 맨 위에!

plt.tight_layout(rect=[0, 0.03, 1, 0.95]) # 그래프들이 겹치지 않게 예쁘게 정돈!
plt.show()