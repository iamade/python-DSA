newTuple = 'a','b','c','d','e'
newTupleFunction = tuple()
newTupleFuncWithContent = tuple('abcde')
print(newTuple[-2])
print(newTuple[1:4])
print(newTuple)
print(newTupleFunction)
print(newTupleFuncWithContent)

#Traversing a tuple



#Search for an element in Tuple



#Tuple operations / functions
# operator + it concatinates the element
mytuple =(1,4,3,4,5)
mytuple1 = (1,2,3,4,5,6)

print(mytuple + mytuple1)

# operator * it repeats the element
print(mytuple * 4 )

#in operator
print( 4 in mytuple ) 

#count function
print(mytuple.count(2))

#index function
print(mytuple.index(4 ))

#lenght function
print(len(mytuple))

#max function
print(max(mytuple))

#min function
print(min(mytuple))

#tuple function to convert list to tuple
print(tuple([1,2,3,4,5]))

init_tuple_a = 1, 2
init_tuple_b = (3, 4)

[print(sum(x)) for x in [init_tuple_a + init_tuple_b]]