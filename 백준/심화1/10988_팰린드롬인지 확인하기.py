x = input()
palindrome = x
nonpalindrome = (x[::-1])
if palindrome == nonpalindrome:
    print("1")
else:
    print("0")