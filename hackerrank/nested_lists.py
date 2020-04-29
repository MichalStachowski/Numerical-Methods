# https://www.hackerrank.com/challenges/nested-list/problem
def sort_by_score(arr):
    """
    Function used to sort [student, grade] list by grade
    """
    return arr[1]


def del_lowest(arr):
    """
    :param arr: [student, grade] list
    :return: list without student(s) with lowest score using list comprehension
    """
    lowest = arr[0][1]
    new = [x for x in arr if x[1] != lowest]
    return new


def get_names_of_second_lowest_score(arr):
    """
    :param arr: [student, grade] list without lowest score
    :return: list of name(s) with second lowest score using list comprehension
    """
    second_lowest = arr[0][1]
    new = [x[0] for x in arr if x[1] == second_lowest]
    return new


def print_output(arr):
    for x in arr:
        print(x)


if __name__ == '__main__':
    sg_list = []  # [student, grade] list
    for _ in range(int(input())):
        name = input()
        score = float(input())
        sg_list.append([name, score])

    sorted_by_score = sorted(sg_list, key=sort_by_score)
    without_lowest = del_lowest(sorted_by_score)
    names = get_names_of_second_lowest_score(without_lowest)
    names_sorted_alphabetically = sorted(names)

    print_output(names_sorted_alphabetically)
