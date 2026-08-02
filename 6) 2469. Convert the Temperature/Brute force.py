# Time complexity : O(1)
# Space complexity : O(1)

class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        ans=[]

        k=celsius+273.15
        f=(celsius*1.80)+32.00

        ans.append(k)
        ans.append(f)

        return ans
