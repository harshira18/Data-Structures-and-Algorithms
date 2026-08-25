class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        for(int i = 0;i < ransomNote.size(); ++i){
            bool ch = false;
            for(int j = 0; j < magazine.size(); ++j){
                if(ransomNote[i] == magazine[j]){
                    magazine[j] = '\0';
                    ch = true;
                    break;
                }
            }
            if(ch == false){return false;}
        }
        return true;
    }
};

// time complexity of this solution is O(m * n) where m is the length of ransomNote and n is the length of magazine, as we are using a nested loop to traverse both strings. The space complexity is O(1) as we are using only a constant amount of extra space.