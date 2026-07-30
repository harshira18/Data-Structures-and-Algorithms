# Time complexity : O((m+n)log(m+n))
# Space complexity : O(m+n)

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ans=[]

        for i in range(0, m):
            ans.append(nums1[i])
        
        for i in range(0, n):
            ans.append(nums2[i])
        
        ans.sort()

        for i in range(0, m+n):
            nums1[i]=ans[i]
