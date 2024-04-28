'''
Contains Duplicate

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example :

    Input: nums = [1,2,3,1]
    Output: true
'''

def contains_duplicate(nums):
    seen_number = set()
    for num in nums:
        if num in seen_number:
            return True
        seen_number.add(num)
    return False

nums = [1,2,3,1]
print(contains_duplicate(nums))
'''
Time Complexity O(n)
Space Complexity O(1) 
'''
