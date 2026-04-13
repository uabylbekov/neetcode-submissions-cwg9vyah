# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list3 = ListNode()
        current = list3

        while list1 and list2:
            if list1.val <= list2.val:
                current.next = ListNode(list1.val)
                current = current.next
                list1 = list1.next
            elif list1.val > list2.val:
                current.next = ListNode(list2.val)
                current = current.next
                list2 = list2.next
        
        if list1 is None and list2:
            current.next = list2
        elif list2 is None and list1:
            current.next = list1
        
        return list3.next
                