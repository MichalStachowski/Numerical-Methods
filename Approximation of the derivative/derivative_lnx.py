import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from tabulate import tabulate


def derivative(x_d, h_d):
    numerator_of_derivative = np.log(x_d + h_d) - np.log(x_d - h_d)
    denominator_of_derivative = 2 * h_d
    fraction_of_derivative = numerator_of_derivative / denominator_of_derivative
    return fraction_of_derivative


# Prepare the h array
x = 0.5
numerator = np.ones(20)                             # [1 1 1 1 ...]
vector_of_fives = 5 * np.ones(20)                   # [5 5 5 5 ...]
denominator = vector_of_fives ** np.arange(20)      # [1 5 25 125 ...]
fraction = numerator / denominator                  # [1 1/5 1/25 1/125 ...]
h = 0.4 * np.ones(20)                               # [0.4 0.4 0.4 ...]
h = h * fraction                                    # [0.4 0.08 0.016 ...]

# Calculate the derivative and absolute error
calculated_derivative = np.array([])
calculated_derivative = np.append(calculated_derivative, derivative(x, h))
true_derivative = 1/x                                                       # f'(x) = [ln(x)]' = 1/x
absolute_error = abs(calculated_derivative - true_derivative)

# Use pandas to show data in form of table
df = pd.DataFrame(
    {
        'h': h,
        'Calculated derivative': calculated_derivative,
        'Absolute error': absolute_error
    }
)
print(tabulate(df, headers='keys', tablefmt='psql', showindex=False))

# Find the smallest absolute error
index_of_min_h = absolute_error.argmin()
print(f"The smallest error occurs for h={h[index_of_min_h]} and it is {absolute_error[index_of_min_h]}")

# Use matplotlib to show results on graph
fig = plt.figure()
plt.loglog(h, absolute_error, 'ob')
plt.loglog(h[index_of_min_h], absolute_error[index_of_min_h], "ro")
plt.loglog(h, absolute_error, '-k')
plt.ylabel('Absolute error')
plt.xlabel('h')
plt.show()
