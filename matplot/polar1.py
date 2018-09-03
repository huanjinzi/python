# encoding=utf-8
import numpy as np
import matplotlib.pyplot as plt

N=20
theta  =np.linspace(0.0,2*np.pi,N,endpoint=False)
radii = 10*np.random.rand(N)
width = np.pi/4*np.random.rand(N)
ax = plt.subplot(111,projection = 'polar')
bars = ax.bar(theta,radii,width=width,bottom=0.0)  
  #前三个参数分别对应left,height,width,left表示从哪开始，表示开始  位置，height表示从中心点向边缘绘制的长度
for r,bar in zip(radii,bars):
    bar.set_facecolor(plt.cm.viridis(r/10.))
    bar.set_alpha(0.5)
plt.show()