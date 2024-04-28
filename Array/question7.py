data = [[[1,2], [3,4]], [[5,6], [7,8]]]
def fun(m):
    v = m[0][0]

    for row in m:
        for element in row:
            if v < element: v = element

    return v
print(fun(data[0]))



'''
Explanation

In the given code block, the function fun takes a 2D list (matrix) as an argument and iterates through its elements to find the largest value. The code block calls the function fun with the first element of the data list, which is [[1, 2], [3, 4]].

Here's a step-by-step explanation of the code execution:

    The function fun is called with the argument [[1, 2], [3, 4]].

    The variable v is assigned the value of the first element in the first row of the matrix, which is 1.

    The function iterates through each row of the matrix and each element in each row using nested loops.

    If the current element is greater than the current value of v, v is updated with the new larger value.

    After iterating through all the elements, v holds the largest value in the matrix.

    The function returns the largest value found, which is 4.

So, the output of the code block will be:

    4

'''