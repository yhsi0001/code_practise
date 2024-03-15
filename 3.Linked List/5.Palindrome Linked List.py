"""
Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

"""
"""
Example 1:
Input: head = [1,2,2,1]
Output: true

Example 2:
Input: head = [1,2]
Output: false

"""
#solution
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head
        
        #find middle (slow point)
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        #reverse from middle to end  1 -> 2 -> 2 <- 1 
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
            
        # check (l = head, r = prev) 1 -> 2 -> 2 <- 1 
        #                            l              r
        l = head
        r = prev
        while r:
            if l.val != r.val:
                return False
            l = l.next
            r = r.next
        return True