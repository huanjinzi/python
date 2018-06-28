# coding=utf-8
# coding 说明：
# 需要有coding=utf-8或者coding：utf-8

import numpy as np

#1. object 任何实现数组接口方法的对象或任何(嵌套)序列。
#2. dtype 数组的所需数据类型，可选。
#3. copy 可选，默认为true，对象是否被复制。
#4. order C(按行)、F(按列)或A(任意，默认)。
#5. subok 默认情况下，返回的数组被强制为基类数组。 如果为true，则返回子类。
#6. ndimin 指定返回数组的最小维数。

# ndarray的构造方法
# numpy.array(object, dtype = None, copy = True, order = None, subok = False, ndmin = 0)

# array
a = np.array([1,2,3])
print "array:"
print a

# multi degree
a = np.array([[1,2],[3,4],[5,6]])
print "multi array:"
print a

# ndmin degree
a = np.array([1,2,3,4],ndmin = 3)
print "min degree:"
print a

# dtype
a = np.array([1,2,3],dtype = complex)
print "dtype:"
print a

