'''
Duplicate Number

Write a function to remove the duplicate numbers on given integer array/list.

Example

    remove_duplicates([1, 1, 2, 2, 3, 4, 5])
    Output : [1, 2, 3, 4, 5]
    
'''

def remove_duplicates(arr):
    unique_array = []
    seen_numbers = set()

    for num in arr:
        if num not in seen_numbers:
            unique_array.append(num)
            seen_numbers.add(num)
    print(unique_array)
    # return unique_array

remove_duplicates([1, 1, 2, 2, 3, 4, 5])