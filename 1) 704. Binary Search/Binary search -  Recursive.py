# Time complexity : O(log n)
# Space complexity : O(log n)

class Solution:
    def func(self, nums: List[int], t: int, l: int, h: int) -> int:
        if(l>h):
            return -1
    
        mid=(l+h)//2

        if(nums[mid]==t):
            return mid
        elif(nums[mid]>t):
            return self.func(nums, t, l, mid-1)
        else:
            return self.func(nums, t, mid+1, h)

    def search(self, nums: List[int], target: int) -> int:
        return self.func(nums, target, 0, len(nums)-1)
