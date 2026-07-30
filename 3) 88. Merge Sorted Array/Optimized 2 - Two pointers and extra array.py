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
        
        while(i<m or j<n):
            if(i>=m):
                ans.append(nums2[j])
                j+=1
                continue
            elif(j>=n):
                ans.append(nums1[i])
                i+=1
                continue
            if(nums1[i]<=nums2[j]):
                ans.append(nums1[i])
                i+=1
            else:
                ans.append(nums2[j])
                j+=1
                
        for k in range(0, m+n):
            nums1[k]=ans[k]
