from collections import deque
dq=deque()
print(dq)
dq=deque()
dq.append(10)
print(dq)
dq.appendleft(1)
dq.insert(1,7)
print(dq)
print(dq.pop())#used to pop last element in the list
print(dq.popleft())#used to pop leftside first element
dq=deque()
dq.append(10)
print(dq)
dq.appendleft(1)
dq.insert(1,7)
print(dq)
dq.rotate(2)
print(dq)