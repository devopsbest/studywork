import matplotlib.pyplot as plt
import numpy as np
fig = plt.figure() # 定义区域
ax1 = fig.add_subplot(2,2,1) # 添加子图，参数2,2,1代表区域划分为2行2列共4个区域，顺序为1开始从左到右，从上到下。1为在1区域添加子图。即前两个参数代表布局，第三个参数代表位置。
ax2 = fig.add_subplot(2,2,2) # 2为在2区域添加子图
# ax3 = fig.add_subplot(2,2,3) # 3为在3区域添加子图
# plt.show() # 这里不给图填充数据，我们画一下看效果

# from numpy.random import randn
# plt.plot(randn(50).cumsum(),'k--')   # 随机选取50个正态分布数进行虚线绘图
# plt.show()

ax1.hist(np.random.randn(100),bins=20,color='k',alpha=0.3) # 20个直方图,alpha透明度
ax2.scatter(np.arange(30),np.arange(30)+3*np.random.randn(30)) # 绘制散点图
plt.show()