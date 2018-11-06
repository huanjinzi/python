# encoding=utf-8
import numpy as np
from numpy.linalg import inv

# det 函数用来计算矩阵的乘法
a = np.array([ [1,2,6],[1,6,3],[1,2,3] ])

print(a)

b = inv(a)

print(b)

print(np.dot(a,b))