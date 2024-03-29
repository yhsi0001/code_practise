"""
Given two integer arrays nums1 and nums2, return an array of their intersection. 
Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.
"""
"""
Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.


"""

#solution
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        d = {}
        for i in nums1:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
                
        ans = []
        for e in nums2 :
            if e in d and d[e] > 0:
                ans.append(e)
                d[e] -= 1
                if d[e] == 0:
                    del d[e]
        return ans
        """
        count = Counter(nums1)
        res = []
        for i in nums2:
            if count[i] > 0:
                res.append(i)
                count[i] -=1
        return res