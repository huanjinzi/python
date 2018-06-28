# coding=utf-8
import numpy as np

# shape row x column
a = np.array([ [(1),(2),(3)], [(4),(5),(6)] ])
print a.shape

# 修改数组的shape,size不能改变
a.shape = (3,2)
print a

a.shape = (1,6)
print a

# reshape生成新的数组
b = a.reshape(2,3,1)
print b

# ndarray.ndim,获取数组维度
dim = b.ndim
print dim

# 生成等间距数组
a = np.arange(24,dtype = 'i1')
a.shape = (4,6)
b = a.reshape(3,8)
print a
print b

# itemsize,数组元素的字节长度
print a.itemsize

# flags
print a.flags

# 1.C_CONTIGUOUS (C) 数组位于单一的、C 风格的连续区段内
# 2.F_CONTIGUOUS (F) 数组位于单一的、Fortran 风格的连续区段内
# 3.OWNDATA (O) 数组的内存从其它对象处借用
# 4.WRITEABLE (W) 数据区域可写入。 将它设置为flase会锁定数据，使其只读
# 5.ALIGNED (A) 数据和任何元素会为硬件适当对齐
# 6.UPDATEIFCOPY (U) 这个数组是另一数组的副本。当这个数组释放时，源数组会由这个数组中的元素更新

