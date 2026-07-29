# Time complexity : O(n^2)
# Space complexity : O(1)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mxp=0

        for i in range(0, len(prices)):
            for j in range(i+1, len(prices)):
                mxp=max(mxp, prices[j]-prices[i])
        
        return mxp
