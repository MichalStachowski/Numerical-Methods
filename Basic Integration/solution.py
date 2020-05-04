def get_polynomial_coef(arr):
    coef = [(element / (i+1)) for i, element in enumerate(arr)]
    return coef


def calculate_integral(arr, low, upp):
    minued, subtrahend = 0, 0
    for i, element in enumerate(arr):
        minued = minued + (element * (upp ** (i + 1)))
        subtrahend = subtrahend + (element * (low ** (i + 1)))
    diff = minued - subtrahend
    return diff


integral = list(map(float, input("Specify integral coefficients separated by space (from a0 to an): ").split()))
lower = float(input("Specify the lower boundary: "))
upper = float(input("Specify the upper boundary: "))


polynomial_coef = get_polynomial_coef(integral)


res = calculate_integral(polynomial_coef, lower, upper)
print("Result: {}".format(res))
