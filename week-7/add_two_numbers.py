# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans1 = ans2 = ''
        while l1:
            ans1 += str(l1.val)
            l1 = l1.next
        while l2:
            ans2 += str(l2.val)
            l2 = l2.next
        ans1 = ans1[::-1]
        ans2 = ans2[::-1]
        res = str(int(ans1) + int(ans2))
        head = ListNode(0)
        curr = head
        i = len(res) - 1
        print(head)
        while i >=0:
            curr.next = ListNode(int(res[i]))
            curr = curr.next
            i -= 1
        return head.next
        
