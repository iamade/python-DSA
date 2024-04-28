#using dictionary
def findPairs(nums, target):
    seen = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            return [seen[complement], i]
            
        
        seen[num] = 1

#using array
# def findPairs(nums, target):
#     for i in range(len(nums)):
#         for j in range(i+ 1, len(nums)):
#             if nums[i] == nums[j]:
#                 continue
#             elif nums[i] + nums[j] == target:
#                 print[i,j]

            