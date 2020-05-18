import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


# System of differential equations
def dx_dt(x, y):
    return (-10 * x) + (10 * y)


def dy_dt(x, y, z):
    return 28*x - y - x*z


def dz_dt(x, y, z):
    return ((-8/3) * z) + (x*y)


# Assumptions
t0 = 0
tk = 25
h = 0.03125
n = int((tk - t0) / h)

# Initial condition for all variables
x_list = [5]
y_list = [5]
z_list = [5]

# Using the Runge Kutta 4th order method
for i in range(n):
    k1_x = dx_dt(x_list[-1], y_list[-1])
    k1_y = dy_dt(x_list[-1], y_list[-1], z_list[-1])
    k1_z = dz_dt(x_list[-1], y_list[-1], z_list[-1])
    x_new = x_list[-1] + (k1_x * h/2)
    y_new = y_list[-1] + (k1_y * h/2)
    z_new = z_list[-1] + (k1_z * h/2)

    k2_x = dx_dt(x_new, y_new)
    k2_y = dy_dt(x_new, y_new, z_new)
    k2_z = dz_dt(x_new, y_new, z_new)
    x_new = x_list[-1] + (k2_x * h/2)
    y_new = y_list[-1] + (k2_y * h/2)
    z_new = z_list[-1] + (k2_z * h/2)

    k3_x = dx_dt(x_new, y_new)
    k3_y = dy_dt(x_new, y_new, z_new)
    k3_z = dz_dt(x_new, y_new, z_new)
    x_new = x_list[-1] + (k3_x * h)
    y_new = y_list[-1] + (k3_y * h)
    z_new = z_list[-1] + (k3_z * h)

    k4_x = dx_dt(x_new, y_new)
    k4_y = dy_dt(x_new, y_new, z_new)
    k4_z = dz_dt(x_new, y_new, z_new)

    temp_x = (1/6) * (k1_x + 2*k2_x + 2*k3_x + k4_x) * h
    temp_y = (1/6) * (k1_y + 2*k2_y + 2*k3_y + k4_y) * h
    temp_z = (1/6) * (k1_z + 2*k2_z + 2*k3_z + k4_z) * h
    x_new = x_list[-1] + temp_x
    y_new = y_list[-1] + temp_y
    z_new = z_list[-1] + temp_z

    x_list.append(x_new)
    y_list.append(y_new)
    z_list.append(z_new)


# Use matplotlib to show results
plot_range = np.linspace(t0, tk, n+1)

fig = plt.figure(figsize=(10, 7))
ax1 = fig.add_subplot(2, 2, 1)
ax1.plot(plot_range, x_list, 'tab:orange')
ax1.set_title('Variable x')

ax2 = fig.add_subplot(2, 2, 2)
ax2.plot(plot_range, y_list, 'tab:green')
ax2.set_title('Variable y')

ax3 = fig.add_subplot(2, 2, 3)
ax3.plot(plot_range, z_list, 'tab:red')
ax3.set_title('Variable z')

ax4 = fig.add_subplot(2, 2, 4, projection='3d')
ax4.plot(x_list, y_list, z_list, 'k-')
ax4.set_title('Three-dimensional space')
plt.show()
