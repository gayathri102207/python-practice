def sum(num):
    s=0
    while num:
        s +=num%10
        num//=10
num=int(input("Enter the Digit:"))
    
print(sum(num))

# Recursion
def sum(num):
    if(num==0):
        return 0
    return(num%10)+sum(n//10)
print("enter the sum of digits:")
print(sum(num))