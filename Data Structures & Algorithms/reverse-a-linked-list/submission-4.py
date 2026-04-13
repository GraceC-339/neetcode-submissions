# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # Recursive

        if not head:
            return None
        
        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head # reverse the link between next node and head
        head.next = None

        return newHead
    

    # 1 -> 2 -> 3 -> None
    # ^
    # H

    # head = [1,2,3]
    # reverseList(head)

    # head = 1
    # newHead = 1
    # newHead = self.reverseList(2)
    # head.next.next = 1 => 2.next -> 1

    # reverseList(2)
    # newHead = 2
    # newHead = self.reverseList(3)
    # head.next.next = 2 => 3.next -> 2

    # reverseList(3)
    # newHead = 3
    # head.next = None
    # return newHead

