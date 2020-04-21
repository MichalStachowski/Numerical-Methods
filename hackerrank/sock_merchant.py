# https://www.hackerrank.com/challenges/sock-merchant/problem


def sockMerchant(n, ar):
    unique = list(set(ar))
    list_of_pairs = [(ar.count(unique_value) // 2) for unique_value in unique]
    num_of_pair = sum(list_of_pairs)
    
    return num_of_pair
