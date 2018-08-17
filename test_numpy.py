import numpy as np
import matplotlib.pyplot as plt

a = np.array([2, 3, 4, 5, 6])
b = np.array([4, 5, 5, 5, 6])
c = np.arange(6)
d = np.linspace(0, 2*np.pi, 5)
print(a, b, c, d)

e = np.array([[11, 12, 13, 14, 15],
              [16, 17, 18, 19, 20],
              [21, 22, 23, 24, 25],
              [26, 27, 28, 29, 30],
              [31, 32, 33, 34, 35]])
print(e[3, 4])
print(e[0, 1:4])
print(e[1:4], 0)
print(e[::2, ::2])
print(e[:, 1])

f = np.arange(25)
print(f)
f = f.reshape((5, 5))
print(f)
g = np.array([10, 62, 1, 14, 2, 56, 79, 2, 1, 45,
              4, 92, 5, 55, 63, 43, 35, 6, 53, 24,
              56, 3, 56, 44, 78])
g = g.reshape((5, 5))
print(g)
print(f * g)

h = np.array([[1, 2], [1, 2]])
print(h)
i = np.array([[2], [4]])
print(i)
print(h * i)

# print(f + g)
# print(f - g)
# print(f * g)
# print(f / g)
# print(f ** 2)
# print(f < g)
# print(f > g)
# print(f.dot(g))

test_1 = np.array([1, 2, 3, 4])
test_1 = test_1.reshape((2, 2))
print(test_1)
print(test_1 ** 2)
print(test_1.dot(test_1))

test_2 = np.linspace(0, 2*np.pi, 50)
test_3 = np.sin(test_2)
plt.plot(test_2, test_3)

a = np.linspace(0, 2 * np.pi, 50)
b = np.sin(a)
plt.plot(a, b)
mask = b >= 0
plt.plot(a[mask], b[mask], 'bo')
mask = (b >= 0) & (a <= np.pi / 2)
plt.plot(a[mask], b[mask], 'go')
plt.show()

a = np.arange(0, 100, 10)
b = np.where(a < 50)
c = np.where(a >= 50)[0]
print(b, c)