# https://www.hackerrank.com/challenges/find-a-string/problem
def count_substring_recursive(substring, string, counted, where_to_start):
    """
    The function counts occurrences of a given phrase using recursion. Using the find() function, the first occurrence of
    the phrase is found. If a phrase is found, the function is called again and the search starts with where_found + 1.
    If a phrase is not found, it means that the end of the text has been reached and the number of occurrences of the
    phrase in the whole text is returned.
    :param substring: The fragment whose number of occurrences we want to count
    :param string: The text in which the fragment is searched
    :param counted: Number of occurrences of searched phrase in the text
    :param where_to_start: Index from which the search in the text begins
    :return: Number of occurrences of searched phrase in the text
    """
    where_found = string.find(substring, where_to_start)  # finds the first occurrence
    if where_found != -1:  # method returns -1 if the value is not found
        counted += 1
        return count_substring_recursive(substring, string, counted, where_found + 1)
    else:  # if the value is not found return value of counted occurences
        return counted


if __name__ == '__main__':
    text = input()
    sub_string = input()
    result = count_substring_recursive(sub_string, text, 0, 0)
    print(result)
