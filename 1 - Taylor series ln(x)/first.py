import numpy as np
import pandas as pd
from tabulate import tabulate


def expand(n, x):
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

    expansion.append(calculated_sum)
    absolute_error.append(abs(np.log(x) - calculated_sum))
    relative_error.append(abs(absolute_error[-1] / np.log(x))*100)


expansion = []
absolute_error = []
relative_error = []

for i in range(11):
    expand(i, 0.5)

df = pd.DataFrame(
    {
        'n': np.arange(11),
        'Expansion': expansion,
        'Absolute error': absolute_error,
        'Relative error [%]': relative_error
    }
)
print(tabulate(df, headers='keys', tablefmt='psql', showindex=False))
