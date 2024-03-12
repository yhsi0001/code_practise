"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""
"""
Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
"""
#solution
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        # 把 s 加進 dict
        for i in s: 
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        
        # 看 j 有無在 dict 中, 如果沒有返回 false 如果有 dict[j] -= 1
        for j in t:
            if j not in d:
                return False
            else:
                d[j] -= 1
        
        # 看 dict 裡面是否有 0 的 值, 有則返回 false
        for k in d:
            if d[k] != 0:
                return False
        return True