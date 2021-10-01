'''
Q.No.9 Write a Python function that checks whether a passed string is palindrome or not.

Note: A palindrome is a word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.
'''


def reverse(s):
    return s[::-1]


def isPalindrome(s):
    rev = reverse(s)
    if (s == rev):
        return True
    else:
        return False


str = input("enter any string:")
ans = isPalindrome(str)

if ans == 1:
    print("palindrome")
else:
    print("Not palindrome")
