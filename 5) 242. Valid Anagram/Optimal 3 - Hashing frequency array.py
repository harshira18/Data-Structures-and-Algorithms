# Time complexity : O(n)
# Space complexity : O(1)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
            return False

        f=[0]*26

        for i in range(0, len(s)):
            f[ord(s[i])-ord('a')]+=1
            f[ord(t[i])-ord('a')]-=1
        
        for i in f:
            if(i!=0):
                return False
            
        return True
