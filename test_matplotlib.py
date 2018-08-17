# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# # 简单Demo
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# X = [1, 1, 2, 2]
# Y = [3, 4, 4, 3]
# Z = [1, 2, 1, 1]
#
# # 绘面
# ax.plot_trisurf(X, Y, Z)
# # 绘点
#
# # ax.scatter(X, Y, Z)
# plt.show()

# 绘制曲线图
# fig = plt.figure()
# ax = Axes3D(fig)
# X = np.arange(-4, 4, 0.25)
# Y = np.arange(-4, 4, 0.25)
# X, Y = np.meshgrid(X, Y)
# R = np.sqrt(X**2 + Y**2)
# Z = np.sin(R)
# # 具体函数方法可用 help(function) 查看，如：help(ax.plot_surface)
# ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='rainbow')
# print(X)
#
# plt.show()
#
# 绘制三维三点图
data = np.random.randint(0, 255, size=[40, 40, 40])

x, y, z = data[0], data[1], data[2]
ax = plt.subplot(111, projection='3d')  # 创建一个三维的绘图工程
#  将数据点分成三部分画，在颜色上有区分度
ax.scatter(x[:10], y[:10], z[:10], c='y')  # 绘制数据点
ax.scatter(x[10:20], y[10:20], z[10:20], c='r')
ax.scatter(x[30:40], y[30:40], z[30:40], c='g')

ax.set_zlabel('Z')  # 坐标轴
ax.set_ylabel('Y')
ax.set_xlabel('X')
plt.show()

#绘制函数
# fig = plt.figure()
# ax = Axes3D(fig)
# x = np.arange(-1, 1, 0.001)
# y = np.arange(-1, 1, 0.001)
# # z = np(x**2) + np(y**2) + np(x*y) + np(x) + np(y) + np(1)
# z = np.sqrt(x**2 + y**2 + x*y + x + y + 1)
# # y = [1/(1 + np.exp(-i)) for i in x]
#
# ax.plot_surface(x, y, z,rstride=1, cstride=1, cmap='rainbow')
# ax.set_zlabel('Z')  # 坐标轴
# ax.set_ylabel('Y')
# ax.set_xlabel('X')
# plt.show()

fig = plt.figure()
ax = Axes3D(fig)
X = np.arange(-10, 10, 0.04)
Y = np.arange(-10, 10, 0.04)
X, Y = np.meshgrid(X, Y)
Z = (X**2 + Y**2 + X*Y + X + Y + 1)
# X, Y = np.meshgrid(X, Y)
# R = np.sqrt(X**2 + Y**2)
# Z = np.sin(R)
# 具体函数方法可用 help(function) 查看，如：help(ax.plot_surface)
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='rainbow')

plt.show()




