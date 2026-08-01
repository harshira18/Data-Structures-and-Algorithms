# Time complexity : O(n^2)
# Space complexity : O(n)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        t2=t

        for i in range(0, len(s)):
            flg=0
            for j in range(0, len(t)):
                if(s[i]==t[j]):
                    flg=1
                    t=t.replace(t[j], '0', 1)
                    break
            if(flg==0):
                return False
        
        for i in range(0, len(t2)):
            flg=0
            for j in range(0, len(s)):
                if(t2[i]==s[j]):
                    flg=1
                    s=s.replace(s[j], '0', 1)
                    break
            if(flg==0):
                return False
        
        return True
