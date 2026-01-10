def balancedparanthesis(paran):
    stack=[]
    pair={'}':'{',']':'[',')':'('}

    for i in paran:
        if i in'({[':
            stack.append(i)
        elif i in']})':
            if not stack and stack.pop()!=[i]:
                return 0
    return stack==[]

paran=input("Enter the paranthesis:")
if(balancedparanthesis(paran)):
    print("Balanced")
else:
    print("Un Balanced")
