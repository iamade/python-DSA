'''
List is mutable
tuple is immutable but can be reassigned
'''

list1 =[0,1,2,3,4,5,6,7]
del list1[0]

print(list1)

tuple1 = 0,1,2,3,4,5,6,7
tuple1[1] = 3
print(tuple1)

'''
storing tuple in list 

storing list in tuple

storing tuple inside a tuple
'''

list1 = [(1,2), (9,0), (3,4)]
tuple1 = ([1,2], [3,4], [5,6])
tuple2 = ((1,2), (3,4), (5,6))
print(list1)
print(tuple1)

'''
there are certain advantages of implementing a tuple over a list.

We generally use tuples for heterogeneous data types and list for homogeneous data types.

Since tuples are immutable,

Iterating through a tuple is faster than with list.

So this is slide performance boost.

So when you do iteration, it's better to use tuples.

Tuples that contain immutable elements can be used as a key for a dictionary, while with list this is

not possible.

So in these cases we can use tuples.

So as I mentioned before, if you have the data that does not change, implementing it as a tuple will
'''
