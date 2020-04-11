import numpy as np
import pandas as pd
from tabulate import tabulate


def expand(n, x):
    """
    ln(x) = 2 * [((x-1)/(x+1)) + ((x-1)^3 / 3(x+1)^3) + ((x-1)^5 / 5(x+1)^5) + ...]
    :param n: n-th expansion in the power series
    :param x: at the given point we determine the value
    :return:
        calculated_sum: value of n-th expansion at the given x
        absolute_error: ln(x) - calculated_sum
        relative_error: absolute_error / ln(x)
    """
    index = np.arange(1, 2 * n + 1, 2)  # [1, 3, 5, 7, 9 ...]

    numerator = np.ones(n)
    numerator = numerator * (x - 1)
    numerator = numerator ** index  # [(x-1)^1, (x-1)^3, (x-1)^5 ...]

    denominator = np.ones(n)
    denominator = denominator * (x + 1)
    denominator = denominator ** index  # [(x+1)^1, (x+1)^3, (x+1)^5 ...]
    denominator = denominator * index  # [(x-1)^1, 3(x-1)^3, 5(x-1)^5 ...]

    fraction = numerator / denominator

    calculated_sum = 2 * np.sum(fraction)
    absolute_error = abs(np.log(x) - calculated_sum)
    relative_error = abs(absolute_error / np.log(x))*100

    return calculated_sum, absolute_error, relative_error


def main():
    exp_arr = []
    abs_arr = []
    rel_arr = []

    for i in range(11):
        exp, abs_error, rel_error = expand(i, 0.5)
        exp_arr.append(exp)
        abs_arr.append(abs_error)
        rel_arr.append(rel_error)

    df = pd.DataFrame(
        {
            'n': np.arange(11),
            'Expansion': exp_arr,
            'Absolute error': abs_arr,
            'Relative error [%]': rel_arr
        }
    )
    print(tabulate(df, headers='keys', tablefmt='psql', showindex=False))


if __name__ == "__main__":
    main()
