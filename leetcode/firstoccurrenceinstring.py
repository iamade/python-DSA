
def strStr(haystack, needle):
    for i in range(0, len(haystack)):
        if haystack[i:i+len(needle)] == needle:
            return i
    return -1

haystack = "hello"
needle = "ll"

print(strStr(haystack, needle))


''''
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
 

Constraints:

1 <= haystack.length, needle.length <= 104


'''

'''

Approach
1. Use a loop to iterate through the haystack string. The loop starts at index i = 0 and goes up to i = haystack.length() - needle.length(). This is done to ensure that there are enough characters left in the haystack for the needle to fit.

2. Within the loop, check substrings of length equal to the length of the needle starting from the current index i up to i + needle.length(). If any of these substrings matches the needle, return the current index i.

3. If the loop completes without finding a match, return -1.
'''