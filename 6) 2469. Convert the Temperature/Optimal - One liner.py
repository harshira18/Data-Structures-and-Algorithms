# Time complexity : O(1)
# Space complexity : O(1)

class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        return [celsius+273.15, (celsius*1.80)+32.00]
