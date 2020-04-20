import numpy as np
from tabulate import tabulate
import pandas as pd

# Operation on txt file
elements = np.array([])
f = open("lottery_data.txt", "r")
file = f.readlines()
for actual_line in range(len(file)):
    char_number = 0
    how_many_char_in_single_line = len(file[actual_line])
    how_many_numbers_in_single_line = int(how_many_char_in_single_line / 3)
    for x in range(how_many_numbers_in_single_line):
        var = file[actual_line][char_number] + file[actual_line][char_number+1]     # ignore '-' char
        var_int = int(var)
        elements = np.append(elements, var_int)
        char_number += 3

# operation to sort two list with sync between them
(unique_elements, occurrence_count) = np.unique(elements, return_counts=True)
occurrence_count, unique_elements = zip(*sorted(zip(occurrence_count, unique_elements), reverse=True))
unique_elements = list(map(int, unique_elements))
occurrence_count = list(map(int, occurrence_count))

# prepare numpy array to use them in pandas
indices = np.arange(6)  # [0 1 2 3 4 5]
top_6_numbers = np.take(unique_elements, indices)
top_6_occurrence = np.take(occurrence_count, indices)

# operations in pandas to make pretty table
df = pd.DataFrame(
    {
        'number': top_6_numbers,
        'frequency': top_6_occurrence
    }
)
print("6 most common occurences:")
print(tabulate(df, headers='keys', tablefmt='psql', showindex=False))
