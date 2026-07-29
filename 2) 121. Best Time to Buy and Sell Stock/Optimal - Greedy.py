# Time complexity : O(n)
# Space complexity : O(1)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mxp=0
        minpr=prices[0]

        for i in range(1, len(prices)):
            if(prices[i]<minpr):
                minpr=prices[i]
                continue
            mxp=max(mxp, prices[i]-minpr)
        
        return mxp
