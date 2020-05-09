# https://www.hackerrank.com/challenges/30-dictionaries-and-maps/problem


def get_data(d_len):
    """
    Get name, phone number of each person and store them in dictionary
    :param d_len: Number of people (got from input)
    :return: Dictionary prepared to work with
    """
    d = {}
    for x in range(d_len):
        name, number = input().split()
        d.update({name: number})

    return d


def find_data(d, d_len):
    """
    Function to print the name and phone number if a given person is found in the dictionary
    :param d: Dictionary
    :param d_len: Number of people
    """
    for _ in range(d_len):
        name = input()
        res = d.get(name)
        if res is not None:  # if found
            print("{}={}".format(name, res))
        else:
            print("Not found")


if __name__ == '__main__':
    # Protection against incorrect input data
    try:
        dict_len = int(input())
    except TypeError:
        raise TypeError("Wrong format of input. Integer required.")

    my_dict = get_data(dict_len)
    find_data(my_dict, dict_len)
