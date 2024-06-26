'''
Sum and Product

Write a function that calculates the sum and product of all elements in a tuple of numbers.

Example

    input_tuple = (1, 2, 3, 4)
    sum_result, product_result = sum_product(input_tuple)
    print(sum_result, product_result)  # Expected output: 10, 24
'''

def sum_product(input_tuple):
    sum_result = 0
    sum_product = 1

    for num in input_tuple:
        sum_result += num
        sum_product *= num
    return sum_result, sum_product

input_tuple = (1, 2, 3, 4)
print(sum_product(input_tuple))