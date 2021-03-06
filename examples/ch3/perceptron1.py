import numpy as np

def step(x):
  return np.where(x > 0, 1, 0)

def perceptron(X, W):
  h = np.dot(X, W)
  print("np.dot(X, W) :", h)

  return step(h)

W = np.array([0., 0., 0.])

X = np.array([[1.0, 0.0, 0.0],
              [1.0, 1.0, 0.0],
              [1.0, 0.0, 1.0],
              [1.0, 1.0, 1.0]])

Y = np.array([0,0,0,1])

print("X :", X)
output = perceptron(X, W)
print("perceptron(X) :", output)
errors = Y - output
print("errors :", errors)
sum_error = np.sum(np.absolute(errors)) / len(Y)
print("sum of errors :", sum_error)
print("W :", W)

"""
X : [[ 1.  0.  0.]
 [ 1.  1.  0.]
 [ 1.  0.  1.]
 [ 1.  1.  1.]]
np.dot(X, W) : [ 0.  0.  0.  0.]
perceptron(X) : [0 0 0 0]
errors : [0 0 0 1]
sum of errors : 1
W : [ 0.1  0.1  0.1]
"""