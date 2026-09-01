# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        if list1:
            tail.next = list1
        else:
            tail.next = list2
            
        return dummy.next


        # h1 = list1
        # h2 = list2
        # p = None
        # tail = None
        # # check values
        # if h1 == None:
        #     return h2
        # elif h2 == None:
        #     return h1
        # elif h1 == None and h2 == None:
        #     return []
        
        # if h1.val <= h2.val:
        #     p = h1
        #     tail = p
        # else:
        #     p = h2
        #     tail = p
    
        # while h1 and h2:
        #     temp1 = h1.next
        #     temp2 = h2.next
        #     if h1.val < h2.val:
        #         h1.next = h2
        #         h1 = temp1
        #     elif h1.val > h2.val:
        #         h2.next = h1
        #         h2 = temp2
        #     elif h1.val == h2.val:
        #         tail.next = h1
        #         h1 = temp1
        # return p
        