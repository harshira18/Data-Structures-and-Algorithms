# Time complexity : O(nlogn)
# Space complexity : O(n)

class Solution:
    def search(self, nums: List[int], t:int) -> int:
        l=0
        h=len(nums)-1

        while(l<=h):
            mid=(l+h)//2

            if(nums[mid]==t):
                return mid
            elif(nums[mid]>t):
                h=mid-1
            else:
                l=mid+1

        return -1

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans=[]
        nums2=[i for i in nums]
        nums2.sort()

        for i in range(0, len(nums2)):
            idx=self.search(nums2, target-nums2[i])
            if(idx!=-1 and idx!=i):
                n1=nums2[i]
                n2=nums2[idx]
                break
        
        for i in range(0, len(nums)):
            if(nums[i]==n1 or nums[i]==n2):
                ans.append(i)
            if(len(ans)==2):
                break
        
        return ans
