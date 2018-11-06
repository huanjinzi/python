# encoding=utf-8
import numpy as np
from numpy.linalg import inv

# inv 函数用来计算矩阵的逆矩阵
a = np.array([ [1,2,6],[1,6,3],[1,2,3] ])

print(a)

ret = inv(a)

print(ret)