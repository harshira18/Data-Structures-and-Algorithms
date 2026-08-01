# Time complexity : O(n^2)
# Space complexity : O(n)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
            return False

        for i in range(0, len(s)):
            flg=0
            for j in range(0, len(t)):
                if(s[i]==t[j]):
                    flg=1
                    t=t.replace(t[j], '0', 1)
                    break
            if(flg==0):
                return False
        
        return True
