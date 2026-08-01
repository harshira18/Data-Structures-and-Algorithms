# Time complexity : O(n)
# Space complexity : O(n)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}

        for i in range(0, len(nums)):
            d[nums[i]]=i
        
        for i in range(0, len(nums)):
            if(target-nums[i] in d and d[target-nums[i]]!=i):
                return [i, d[target-nums[i]]]
        
        return []
