# Time complexity : O(m+n)
# Space complexity : O(m+n)

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ans=[]
        i=0
        j=0
        
        while(i<m and j<n):
            if(nums1[i]<=nums2[j]):
                ans.append(nums1[i])
                i+=1
            else:
                ans.append(nums2[j])
                j+=1
        
        if(i>=m):
            while(j<n):
                ans.append(nums2[j])
                j+=1
        elif(j>=n):
            while(i<m):
                ans.append(nums1[i])
                i+=1
                
        for k in range(0, m+n):
            nums1[k]=ans[k]
