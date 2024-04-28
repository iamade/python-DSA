
def longestpalindrome(self, s):
    



'''
5. Longest Palindromic Substring
Medium
Topics
Companies
Hint
Given a string s, return the longest 
palindromic
 
substring
 in s.

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
'''

'''
Algorithm

We need to shift a start point one by one to check longest palindromic substring.

What is the start point?
Since palindromic substring is like a mirror from some character, it's good idea to consider current index as a center of palindromic substring and expand left and right at the same time.

For example,

Input = "abcba"
If we start from c, then

"ab" "c" "ba"
      i

i = curerent index
"ab" and "ba" is a mirror when "c" is center.

Let's see one by one.

Input = "abcba"
We use left and right pointers. The both pointers start from index i but let me start from next to index i to make my explanation short. A single character is definitely a palindrome which is length of 1.

i = 0

"abcba"
lir
 
Check left(= out of bounds) and right(= "b")
max_length = 1 (= "a")
i = 1

"abcba"
 lir

Check left(= "a") and right(= "c")
max_length = 1 (= "a" or "b")
i = 2

"abcba"
  lir

l = 1
r = 3
Check left(= "b") and right(= "b") → "bcb" is a palindrome.😆

Let's expand the range!

"abcba"
 l i r

l = 0
r = 4
Check left(= "a") and right(= "a") → "abcba" is a palindrome.😆
max_length = 5 (= "abcba")

 "abcba"
 l  i  r

l = -1
r = 5
Now left and right are out of bounds, so we finish iteration.
Let me skip the cases where we start from later "b" and "a". We already found the max length. (of course solution code will check the later part)

How do you calculate length of palindrome we found?
From the example above, we found 5 as a max length. how do you calculate it? Simply

right - left
Right? So,

right - left
5 - (-1)
= 6
Wait? It's longer than max length we found. The reason why this happens is because the two pointers stop at the next position of max length of palindrome.

"abcba"
 l i r
When i = 2 left = 0 and right = 4, we found 5 as a max length, but we don't know 5 is the max length in the current iteration, so we try to move to the next place to find longer palindrome, even if we don't find it in the end.

That's why, left and right pointer always overrun and stop at max length in current iteration + 1, so we need to subtract -1 from right - left.

❌ right - left
🔴 right - left - 1
But still you don't get it because we have two pointers expanding at the same time? you think we should subtract -2?

This is calculation of index number, so index number usually starts from 0 not 1, so right - left includes -1 already. For example,

"aba"
 l r
Actual length is 3, but if we calculate the length with index number, that should be 2(index 2 - index 0), so it's already including -1 compared with actual length. That's why when we have two pointers and calculate actual length, right - left - 1 works well.

Now you understand main idea of my solution, but I'm sure you will not pass all cases. Can you geuss why?

The answer is I explain the case where we have odd length of input string.

⭐️ Points

We have to care about both odd length of input string and even length of input string

Input: "abbc"
Let's see one by one. we can use the same idea. Let me write briefly.

"abbc"
lir

max length = 1
"abbc"
 lir

max length = 1
"abbc"
  lir

max length = 1
"abbc"
   lir

max length = 1
❌ Output: "a" or "b" or "c"  
Output should be

🔴 Output: "bb"  
Why this happens?
Regarding odd length of input array, center position of palindrome is definitely on some charcter.

"abcba", center is "c"
How about even length of input string

"abbc"
Center of palindrome is "b | b" 
| is center of palindrome. Not on some character.

So how can you avoid this?
My idea to avoid this is we start left with current index and right with current index + 1, so we start interation as if we are coming from between the characters. Let me write only when index = 1.

current index = 1

  lr
"abbc"
  i

We found palindrome "bb"

 l  r
"abbc"
  i

Finish iteration.
Then

right - left - 1
3 - 0 - 1
= 2(= length of "bb")
We can use the same idea for both cases but start position is different, that's why we call the same function twice in one iteration.

Let's see a real algorithm!

Algorithm Overview:
Initialize start and end variables to keep track of the starting and ending indices of the longest palindromic substring.
Iterate through each character of the input string s.
For each character, expand around it by calling the expand_around_center function with two different center possibilities: (i) the current character as the center (odd length palindrome), and (ii) the current character and the next character as the center (even length palindrome).
Compare the lengths of the two expanded palindromes and update start and end if a longer palindrome is found.
Finally, return the longest palindromic substring by slicing the input string s based on the start and end indices.
Detailed Explanation:
Check if the input string s is empty. If it is, return an empty string, as there can be no palindromic substring in an empty string.

Define a helper function expand_around_center that takes three arguments: the input string s, and two indices left and right. This function is responsible for expanding the palindrome around the center indices and returns the length of the palindrome.

Initialize start and end variables to 0. These variables will be used to keep track of the indices of the longest palindromic substring found so far.

Iterate through each character of the input string s using a for loop.

Inside the loop, call the expand_around_center function twice: once with i as the center for an odd length palindrome and once with i and i + 1 as the center for an even length palindrome.

Calculate the length of the palindrome for both cases (odd and even) and store them in the odd and even variables.

Calculate the maximum of the lengths of the two palindromes and store it in the max_len variable.

Check if the max_len is greater than the length of the current longest palindromic substring (end - start). If it is, update the start and end variables to include the new longest palindromic substring. The new start is set to i - (max_len - 1) // 2, and the new end is set to i + max_len // 2.

Continue the loop until all characters in the input string have been processed.

After the loop, return the longest palindromic substring by slicing the input string s using the start and end indices. This substring is inclusive of the characters at the start and end indices.

Complexity
Time complexity: O(n2)O(n^2)O(n 
2
 )
"n" is the length of the input string "s." This is because the code uses nested loops. The outer loop runs for each character in the string, and the inner loop, expand_around_center, can potentially run for the entire length of the string in the worst case, leading to a quadratic time complexity.

Space complexity: O(1)O(1)O(1)
the code uses a constant amount of extra space for variables like "start," "end," "left," "right," and function parameters. The space used does not depend on the size of the input string.





'''

