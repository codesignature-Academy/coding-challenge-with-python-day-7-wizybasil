"""
write four functions that perform the following tasks:
add(a, b): returns the sum of a and b
multiply(a, b): returns the product of a and b
power(a, b): returns a raised to the power of b
subtract(a, b): returns the difference of a and b
"""
# 1.


def sum(a, b):
    sum = a + b
    return sum


x = sum(4, 2)
print(x)

# # 2.


def product_of_two_num(a, b):
    product_of_two_num = a * b
    return product_of_two_num


x = product_of_two_num(2, 2)
print(x)

# 3.


def power(a, b):
    power = (a ** b)
    return power


x = power(4, 2)
print(x)


# 4.
def subtract(a, b):
    subtract = a - b
    return a - b


x = subtract(4, 2)
print(x)
