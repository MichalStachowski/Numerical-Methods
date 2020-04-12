from first import expand
import numpy as np
import matplotlib.pyplot as plt
np.seterr(divide='ignore', invalid='ignore')


x_range = np.linspace(0, 1, 1000)

expansion_n3 = []
expansion_n6 = []
expansion_n9 = []

for i in x_range:
    exp, _, _ = expand(3, i)
    expansion_n3.append(exp)
    exp, _, _ = expand(6, i)
    expansion_n6.append(exp)
    exp, _, _ = expand(9, i)
    expansion_n9.append(exp)

plt.plot(x_range, expansion_n3, label='n=3')
plt.plot(x_range, expansion_n6, label='n=6')
plt.plot(x_range, expansion_n9, label='n=9')
plt.plot(x_range, np.log(x_range), label='ln(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
