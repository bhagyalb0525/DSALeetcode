# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        seen=set()
        curr=head
        temp=head
        while curr:
            if curr.val not in seen:
                temp=curr
                seen.add(curr.val)
                curr=curr.next
                
            else:
                temp.next=curr.next
                curr=curr.next
        return head
