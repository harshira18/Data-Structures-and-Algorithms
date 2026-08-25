class Solution {
public:
    bool isSubsequence(string s, string t) {
                    int k = 0;

        for(int i = 0;i < size(s);++i){
            bool flag = false;
            for(k;k< size(t); ++k){
                if(s[i] == t[k]){
                    flag = true;
                    k++;
                    break;
                }
            }
            if(flag == false){
                return false;
            }
            
        }
        return true;
    }
};

// Time complexity : O(n) where n is the length of string t. In the worst case, we may have to traverse the entire string t for each character in string s.
// space complexity : O(1) as we are using only a constant amount of extra space.