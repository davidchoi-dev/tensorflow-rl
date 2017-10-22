# Chapter2. Linear Algebra in numpy

선형대수학을 힘들어하시는 개발자분들을 위해 numpy만으로 선형대수학을 배울 수 있는 글을 작성해보았습니다. 

## 2-1. 스칼라, 벡터, 행렬, 텐서

* 스칼라 : 스칼라는 하나의 숫자입니다. 

```python
s = 1.5
n = 1
print("s :", s)
print("n :", n)
print("type(s) :", type(s))
print("type(n) :", type(n))
"""
s : 1.5
n : 1
type(s) : <class 'float'>
type(n) : <class 'int'>
"""
``` 

* 벡터 : 벡터는 숫자의 배열입니다. 

```python
import numpy as np
A = np.array([1,2,3])
print("A :")
print(A)
"""
A :
[1 2 3]
"""
```

* 행렬 : 행렬은 2차원 배열입니다.

```python
import numpy as np
A = np.array([[1,2,3],
             [4,5,6]])
print("A :")
print(A)
"""
A :
 [[1 2 3]
 [4 5 6]]
"""
```


* 텐서 : 텐서는 3차원 이상의 배열입니다.

```python
import numpy as np
A = np.array(
  [[[1,2,3],
    [4,5,6]],

   [[11,12,13],
    [14,15,16]]])

print("A :")
print(A)
"""
A :
[[[ 1  2  3]
  [ 4  5  6]]

 [[11 12 13]
  [14 15 16]]]
"""
```

## 2-2. 행렬 원소 선택


행렬에서 i번째 행에 j번째 열에 있는 원소를 조회하는 표현은 다음과 같습니다.

$$A_{i,j}$$

파이썬에서는 다음과 같이 표현됩니다.

```python
A[i-1][j-1]
```

행렬에서 i번째 행을 선택하는 기호는 다음과 같습니다.

$$A_{i,:}$$

Python에서도 비슷하지만, 약간 다릅니다. Python의 배열은 0부터 시작하기 때문에, 선형대수학에서 행렬의 첫번째 행을 선택하는 기호 $$A_{1,:}$$ 가 파이썬에서는 `A[0][:]`으로 표현합니다.

```
# i 번째 행을 선택
A[i-1][:]
```

행렬에서 j번째 열을 선택하는 법

$$A_{:,j}$$

Python에서도 비슷하지만, 약간 다릅니다. Python의 배열은 0부터 시작하기 때문에, 선형대수학에서 행렬의 첫번째 행을 선택하는 기호 $$A_{1,:}$$ 가 파이썬에서는 `A[0][:]`으로 표현합니다.

```
# i 번째 행을 선택
A[i-1][:]
```


행렬 연산 중 주목할만한 연산이 있습니다. 바로 Transpose 입니다. 선형대수학에서는 아래와 같이 표현합니다.

$$A^T$$

```python
import numpy as np

A = np.array([[1,2,3],
              [4,5,6]])
print("A :")
print(A)

B = A.transpose()
print("B = A.transpose()")
print("B :")
print(B)
"""
A :
[[1 2 3]
 [4 5 6]]
B = A.transpose()
B :
[[1 4]
 [2 5]
 [3 6]]
"""
```

## 2-3. 행렬 연산

* 행렬 곱(Matrix product)

행렬 연산에서 가장 중요하다고 볼 수 있는 행렬곱을 설명드리겠습니다.

행렬 곱은 아래와 같이 정의됩니다. 

$$C_{i,j} = \sum_k A_{i,k}B_{k,j}$$

여기서 주의해야할 점은 같은 자리에 있는 행렬 성분의 곱이 아니라는 점입니다.

파이썬에서는 행렬 곱을 이렇게 표현합니다.

```python
import numpy as np

# add arrays
A = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])

B = np.array([[2,3,4],
              [5,6,7],
              [8,9,10]])
              
C = np.dot(A, B)
print("np.dot(A, B) :\n", C)
"""
np.dot(A, B) :
 [[ 36  42  48]
 [ 81  96 111]
 [126 150 174]]
"""
```

* 행렬 성분곱(Element-wise product)

```python
import numpy as np

# add arrays
A = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])

B = np.array([[2,3,4],
              [5,6,7],
              [8,9,10]])
              
C = np.multiply(A, B)
print("np.multiply(A, B) :\n", C)
"""
np.multiply(A, B) :
 [[ 2  6 12]
 [20 30 42]
 [56 72 90]]
"""

C = A * B
print("A * B :\n", C)
"""
A * B :
 [[ 2  6 12]
 [20 30 42]
 [56 72 90]]
"""
```