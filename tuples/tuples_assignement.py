
'''
Elementwise Sum

Create a function that takes two tuples and returns a tuple containing the element-wise sum of the input tuples.
'''


def tuple_elementwise_sum(t1, t2):
        if len(t1) != len(t2):
            raise ValueError("Input tuples must have the same length.")
     
        result = tuple(a + b for a, b in zip(t1, t2))
        return result

def tuple_elementwise_sum(tuple1, tuple2):
    return tuple(map(sum, zip(tuple1, tuple2)))
