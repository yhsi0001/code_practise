"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

"""
"""
Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]
"""
#solution
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        ans = ListNode()
        anshead = ans
        
        while list1 or list2:
            # if list1 has nothing put list2
            if not list1:
                ans.next = list2
                list2 = list2.next
            # if list2 has nothing put list1
            elif not list2:
                ans.next =  list1
                list1 = list1.next
            else:
                if list1.val <= list2.val:
                    ans.next = list1
                    list1 = list1.next
                else:
                    ans.next = list2
                    list2 = list2.next
            ans = ans.next
            
        return anshead.next