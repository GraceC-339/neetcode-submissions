class ListNode:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node

class LinkedList:
    
    def __init__(self):
        # init the list with a dummy head node
        self.dummy_head = ListNode(-1)
        self.tail = self.dummy_head

    def get(self, index: int) -> int:
        curr = self.dummy_head.next
        i = 0
        while curr:
            if i == index:
                return curr.val
            i += 1
            curr = curr.next
        return -1 # Index out of bounds or list is empty
        
    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.dummy_head.next
        self.dummy_head.next = new_node
        if not new_node.next: # If list was empty before insertion
            self.tail = new_node
        

    def insertTail(self, val: int) -> None:
        self.tail.next = ListNode(val)
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        # curr is pointing to the node before the target node
        # and check if the node is the tail, if is update the tail
        i = 0
        curr = self.dummy_head
        while i < index and curr:
            i += 1
            curr = curr.next

        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True
        return False


    def getValues(self) -> List[int]:
        curr = self.dummy_head.next
        res = []

        while curr:
            res.append(curr.val)
            curr = curr.next
        
        return res
