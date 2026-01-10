def sum(num):
    if(num==0):
        return 0
   
    return(num%10)+sum(n//10)
num=int(input("Enter the number:"))
print((sum))