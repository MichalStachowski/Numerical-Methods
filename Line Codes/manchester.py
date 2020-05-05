import numpy as np
import matplotlib.pyplot as plt


def get_manchester_arr(arr):
    """
    Manchester code (IEEE 802.3): 1 -> [-1, 1], 0 -> [1, -1]
    :param arr: Random data array. Array must contain only 0 or 1 integer type.
    :return: Manchester coded array.
    """
    res_arr = [0, 0]
    for x in arr:
        if x == 0:
            res_arr.append(1)
            res_arr.append(-1)
        elif x == 1:
            res_arr.append(-1)
            res_arr.append(1)
        else:
            raise TypeError("Wrong format of array.")

    return res_arr


if __name__ == '__main__':
    num_of_bits = 10

    # Generate array in range (0,1)
    random_data = np.random.random(num_of_bits)

    # change array to binary form
    random_data = np.where(random_data > 0.5, 1, 0)

    manchester_arr = get_manchester_arr(random_data)

    # to double random_data
    random_data = np.repeat(random_data, 2)  # [0, 1, 0] -> [0, 0, 1, 1, 0, 0]
    # insert "0" in the beginning to better see result of Manchester coding
    random_data = np.insert(random_data, 0, 0)
    random_data = np.insert(random_data, 0, 0)

    # Use matplotlib to show result
    plot_range = np.arange(2 * (num_of_bits+1))
    fig = plt.figure(figsize=(10, 6))
    ax1 = fig.add_subplot(2, 1, 1)
    ax1.step(plot_range, random_data, 'r')
    ax1.plot([0, 0.5, 1], [0, 0, 0], 'x')  # part of 'x' to ignore
    ax1.set_title("Data")

    ax2 = fig.add_subplot(2, 1, 2)
    ax2.step(plot_range, manchester_arr, 'k')
    ax2.plot([0, 0.5, 1], [0, 0, 0], 'x')  # part of 'x' to ignore
    ax2.set_title("Manchester (IEEE 802.3)")

    plt.show()
