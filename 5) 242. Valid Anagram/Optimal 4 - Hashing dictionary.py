# Time complexity : O(n)
# Space complexity : O(1)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
            return False

        d={}

        for i in range(0, len(s)):
            if(s[i] not in d):
                d[s[i]]=0
            d[s[i]]+=1
        
        for i in range(0, len(t)):
            if(t[i] not in d or d[t[i]]==0):
                return False
            d[t[i]]-=1
        
        return True
