# coding=utf-8
import numpy as np

# 数值类型
# 1.bool_存储为一个字节的布尔值(真或假)
# 2.int_默认整数，相当于 C 的long，通常为int32或int64
# 3.intc相当于 C 的int，通常为int32或int64
# 4.intp用于索引的整数，相当于 C 的size_t，通常为int32或int64
# 5.int8 单字节(-128 ~ 127)
# 6.int16 16 位整数(-32768 ~ 32767)
# 7.int32 32 位整数(-2147483648 ~ 2147483647)
# 8.int64 64 位整数(-9223372036854775808 ~ 9223372036854775807)
# 9.uint8 8 位无符号整数(0 ~ 255)
# 10.uint16 16 位无符号整数(0 ~ 65535)
# 11.uint32 32 位无符号整数(0 ~ 4294967295)
# 12.uint64 64 位无符号整数(0 ~ 18446744073709551615)
# 13.float _float64的简写
# 14.float16 半精度浮点：符号位，5 位指数，10 位尾数
# 15.float32 单精度浮点：符号位，8 位指数，23 位尾数
# 16.float64 双精度浮点：符号位，11 位指数，52 位尾数
# 17.complex _complex128的简写
# 18.complex64复数，由两个 32 位浮点表示(实部和虚部)
# 19.complex128复数，由两个 64 位浮点表示(实部和虚部)

# dtype的构造方法
# numpy.dtype(object, align, copy)

# int dtype
dt = np.dtype(np.int32)
print dt

# 'i2'表示2个字节
dt = np.dtype('i2')
print dt

# 使用端记号
dt = np.dtype('>i4')
print dt

# 创建结构化数据
dt = np.dtype([('age',np.int8)])
print dt

# 将结构化dtype应用于ndarray
a = np.array([23,30],dtype = dt)
print a

# 文件名称可用于访问 age 列的内容
print a['age']

# 定义 student 的结构化数据类型，字符串字段name，整数字段age和浮点字段marks
dt = np.dtype([('name','S20'), ('age','i1'), ('marks','f4')])
a = np.array([('a',12,1.0), ('b',34,2.3), ('c',45,9.0)],dtype = dt)
print a['name']
