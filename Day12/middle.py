class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        count=0
        while temp:
            count+=1
            temp=temp.next
        n=count//2

        temp = head
        for i in range(n):
            temp=temp.next
        return temp
    # 🔹 Create linked list: 1 → 2 → 3 → 4 → 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

# 🔹 Call function
sol = Solution()
middle = sol.middleNode(head)

print(middle.val)   # ✅ Output: 3
