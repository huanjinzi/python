# encoding=utf-8
import numpy as np
from numpy.linalg import det

# det 函数用来计算行列式的值
a = np.array([ [1,2,6],[1,6,3],[1,2,3] ])

print(a)

ret = det(a)

print(ret)