# 📊 NumPy 소개
NumPy(Numerical Python)는 파이썬에서 수치 계산을 위한 핵심 라이브러리입니다. 특히 다차원 배열 객체인 ndarray를 효율적으로 다룰 수 있도록 강력한 기능을 제공합니다. 과학 계산, 데이터 분석, 머신러닝 등 다양한 분야에서 광범위하게 사용되며, 파이썬에서 고성능 수치 연산을 가능하게 합니다.

# ✨ 주요 특징
- ndarray 객체: 효율적인 다차원 배열 객체를 제공하여 대규모 데이터셋을 빠르게 처리할 수 있습니다.

- 브로드캐스팅 기능: 서로 다른 크기의 배열 간에도 연산을 수행할 수 있게 해주는 강력한 기능입니다.

- 수학 함수: 선형 대수, 푸리에 변환, 난수 생성 등 다양한 수학 함수를 제공합니다.

- C/C++ 및 Fortran 통합: C, C++, Fortran과 같은 언어로 작성된 코드를 파이썬에서 쉽게 통합하여 사용할 수 있습니다.

- 성능: 파이썬 리스트에 비해 훨씬 빠른 연산 속도를 자랑합니다. 이는 내부적으로 C 언어로 구현되어 있기 때문입니다.

# 🚀 설치 방법
NumPy는 pip를 사용하여 간단하게 설치할 수 있습니다.

pip install numpy

# 🧱 NumPy의 핵심: ndarray
NumPy의 가장 중요한 데이터 구조는 바로 ndarray (N-dimensional array) 예요. 이건 숫자들이 규칙적으로 쌓여있는 상자라고 생각하면 돼요!

- 다차원: 1차원 (벡터), 2차원 (행렬), 3차원 이상 (텐서) 등 여러 차원의 배열을 만들 수 있어요.
- 단일 자료형: 하나의 배열 안에는 반드시 같은 종류의 데이터(예: 모든 정수, 모든 실수)만 담을 수 있다는 특징이 있어요. 

# 💻 기본 사용법
NumPy를 사용하기 위한 기본적인 예시입니다.

## 1. 배열 생성
```
import numpy as np

# 1차원 배열 생성
arr1 = np.array([1, 2, 3, 4, 5])
print("1차원 배열:", arr1)
print("배열의 타입:", type(arr1))
print("배열의 형태 (shape):", arr1.shape)

# 2차원 배열 생성
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("\n2차원 배열:\n", arr2)
print("배열의 형태 (shape):", arr2.shape)

# 0으로 채워진 배열
zeros_arr = np.zeros((2, 3))
print("\n0으로 채워진 배열:\n", zeros_arr)

# 1로 채워진 배열
ones_arr = np.ones((3, 2))
print("\n1로 채워진 배열:\n", ones_arr)

# 특정 범위의 배열
range_arr = np.arange(0, 10, 2) # 0부터 10 미만까지 2씩 증가
print("\n범위 배열:", range_arr)

# 무작위 값 배열
random_arr = np.random.rand(2, 2) # 0과 1 사이의 무작위 값
print("\n무작위 배열:\n", random_arr)
```

## 2. 배열 연산
```
import numpy as np

arr1 = np.array([10, 20, 30, 40])
arr2 = np.array([1, 2, 3, 4])

# 배열 간 덧셈
add_result = arr1 + arr2
print("덧셈 결과:", add_result)

# 배열 간 곱셈
mul_result = arr1 * arr2
print("곱셈 결과:", mul_result)

# 스칼라 연산
scalar_mul = arr1 * 2
print("스칼라 곱셈:", scalar_mul)

# 조건부 연산
greater_than_20 = arr1 > 20
print("20보다 큰 요소:", greater_than_20)
print("20보다 큰 값만:", arr1[greater_than_20])
```

## 3. 인덱싱 및 슬라이싱
```
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("원본 배열:\n", arr)

# 단일 요소 접근
print("arr[0, 0]:", arr[0, 0]) # 첫 번째 행, 첫 번째 열

# 행 슬라이싱
print("arr[0, :]:", arr[0, :]) # 첫 번째 행 전체

# 열 슬라이싱
print("arr[:, 1]:", arr[:, 1]) # 두 번째 열 전체

# 부분 배열 슬라이싱
print("arr[0:2, 1:3]:\n", arr[0:2, 1:3]) # 0,1행과 1,2열
```
# 🌍 NumPy는 어디에 사용될까요?
데이터 과학 및 분석 📊: 수많은 데이터를 빠르게 처리하고 분석하는 데 필수적이에요.
머신러닝 및 인공지능 🤖: 딥러닝 모델의 기본인 행렬 연산과 벡터 계산을 효율적으로 수행해요. TensorFlow, PyTorch 같은 라이브러리들도 내부적으로 NumPy를 많이 사용한답니다.
과학 및 공학 계산 🔬: 물리학, 화학, 생물학, 재무, 공학 등 복잡한 수치 모델링과 시뮬레이션에 폭넓게 활용돼요.

# 📚 더 알아보기
NumPy는 파이썬에서 수치 계산을 위한 필수 도구이며, 이 문서에서 다룬 내용은 기본적인 시작점일 뿐입니다. 더 깊이 있는 학습을 위해서는 NumPy 공식 문서를 참고하시거나, 데이터 과학 및 머신러닝 관련 학습 자료를 찾아보시는 것을 추천합니다
