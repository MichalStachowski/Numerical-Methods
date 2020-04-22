import numpy as np
import matplotlib.pyplot as plt


def newton_interpolation_4_points(x_arr, y_arr):
    x = []
    y = []
    b1 = y_arr[0]
    b2 = (y_arr[1] - y_arr[0]) / (x_arr[1] - x_arr[0])
    b3 = (((y_arr[2] - y_arr[0]) / (x_arr[2] - x_arr[0])) - b2) / (x_arr[2] - x_arr[1])
    temp_b4_nom = (((y_arr[3] - y_arr[0]) / (x_arr[3] - x_arr[0])) - ((y_arr[1] - y_arr[0]) / (x_arr[1] - x_arr[0])))
    temp_b4_denominator = (x_arr[3] - x_arr[1])
    temp_b4 = temp_b4_nom / temp_b4_denominator
    b4 = (temp_b4 - b3) / (x_arr[3] - x_arr[2])
    x_range = np.linspace(min(x_arr), max(x_arr), 100)
    for _ in x_range:
        x.append(x_range)
        res = b1 + (b2 * (x_range - x_arr[0])) + (b3 * (x_range - x_arr[0]) * (x_range - x_arr[1]))
        res = res + (b4 * (x_range - x_arr[0]) * (x_range - x_arr[1]) * (x_range - x_arr[2]))
        y.append(res)
    return x, y


if __name__ == '__main__':
    px = np.random.rand(4) * 10
    py = np.random.rand(4) * 10

    i_x, i_y = newton_interpolation_4_points(px, py)
    plt.plot(px, py, 'o', label='points')
    plt.plot(i_x[0], i_y[0], label='interpolated trajectory')
    plt.legend()
    plt.show()
