def isPalindrome(s):
    return s == s[::-1]
 
 
#code
s = "abba"
a = isPalindrome(s)
 
if a:
    print("Yes")
else:
    print("No")
