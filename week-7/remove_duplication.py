# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        itr = head
        while itr.next:
            while itr.next and itr.val == itr.next.val:
                itr.next = itr.next.next
            itr = itr.next
            if itr == None:
                break
            
        return head
