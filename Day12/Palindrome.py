def palindrome(s):
    s = s.lower().replace(" ", "")
    stack = []

    for ch in s:
        stack.append(ch)

    rev = " "
    while stack:
        rev += stack.pop()

    return s == rev


str = input("Enter the String: ")
print("Palindrome String" if palindrome(str) else "Not a Palindrome String")

#One line
string = input("Enter a string: ")

print("Palindrome" if string == string[::-1] else "Not a palindrome")
