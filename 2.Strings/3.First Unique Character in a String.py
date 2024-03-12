"""
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
"""
"""
Example 1:
Input: s = "leetcode"
Output: 0

Example 2:
Input: s = "loveleetcode"
Output: 2
"""
#solution

class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = Counter(s)
        
        for i,c in enumerate(s):
            if count[c] == 1:
                return i
        return -1
        