def pair_sum(myList, sum):
    output_array = []
    for i in range(len(myList)):
        for j in range(i+1, len(myList)):
            if myList[i] + myList[j] == sum:
                output_array.append(f"{myList[i]} + {myList[j]}")
 
    print(output_array)

arr = [2, 4, 3, 5, 6, -2, 4, 7, 8, 9]
target_sum = 7
pair_sum(arr, target_sum)