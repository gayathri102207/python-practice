def postfix(exp):
    stack=[]
    
    for i in exp:
        if i.isdigit():
            stack.append(int(i))
        else:
            b=stack.pop()
            a=stack.pop()
            
            if i=='+':
                stack.append(a+b)
            elif i=='-':
                stack.append(a-b)
            elif i=='*':
                stack.append(a*b)
            elif i=='//':
                stack.append(a//b)
    return stack.pop()
            

exp='23*54*+9-'
print(postfix(exp))
            

