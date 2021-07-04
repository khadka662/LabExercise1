'''
Q.No.9 Write a Python function that checks whether a passed string is palindrome or not.

Note: A palindrome is a word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.
'''

def isPalindrome(s):
     return s == s[::-1]

s = "madam"
ans = isPalindrome(s)

if ans:
    print("Yes")
else:
    print("No")