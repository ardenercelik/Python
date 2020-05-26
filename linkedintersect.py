# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        a = headA
        b = headB
        counterA = 0
        counterB = 0
        while a != None:
            a = a.next
            counterA = counterA + 1
        while b is not None:
            b = b.next
            counterB += 1
        
        a = headA
        b = headB
        if counterA > counterB:
            dif = counterA - counterB
            for i in range(dif):
                if a == b:
                    return a
                a = a.next
            
        elif counterB > counterA:
            dif = counterB - counterA
            for i in range(dif):
                if a == b:
                    return a
                b = b.next
            
        while a != b:
            a = a.next
            b = b.next
        return a