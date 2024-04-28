'''
Elementwise Sum

Create a function that takes two tuples and returns a tuple containing the element-wise sum of the input tuples.

Example

    tuple1 = (1, 2, 3)
    tuple2 = (4, 5, 6)
    output_tuple = tuple_elementwise_sum(tuple1, tuple2)
    print(output_tuple)  # Expected output: (5, 7, 9)
'''

#solution1
def tuple_elementwise_sum(tuple1, tuple2):
    if len(tuple1) != len(tuple2):
        raise ValueError("Input tuples must have the same length.")
    result = tuple(a + b for a,b in zip(tuple1, tuple2))
    return result

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

print(tuple_elementwise_sum(tuple1, tuple2))

#solution 2
def tuple_elementwise_sum(tuple1, tuple2):
    return tuple(map(sum, zip(tuple1, tuple2)))