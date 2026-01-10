#Question

def reverse(str):
    pass 
str=input("Enter the String:")
print("Reversed String is",reverse(str))

#Answer

def reverse(s):
    stack = []
    for k in s:
        stack.append(k)

    r_str = ""
    while stack:
        r_str += stack.pop()

    return r_str


str = input("Enter the String: ")
print("Reversed String is", reverse(str))
