import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import *

my_font = FontProperties(fname='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc')

keys = []
values = []
with open('/home/huanjinzi/PycharmProjects/sym/category.txt', 'r') as f:
    dic = {}
    for line in f.readlines():
        for key in line.split(','):
            key = key.strip()

            if key == '':
                continue

            if key in dic:
                value = dic[key]
                value = value + 1
                dic[key] = value
            else:
                dic[key] = 1

index = np.arange(dic.keys().__len__())

for key, value in dic.items():
    keys.append(key)
    values.append(value)

plt.bar(index, values, width=0.6, facecolor='lightskyblue', edgecolor='black', lw=1)

plt.xlabel('Category')
plt.ylabel('Numbers')
# plt.grid(True)

plt.xticks(index, keys, fontproperties=my_font)

plt.show()
