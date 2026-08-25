class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        unordered_map<char, int> dict;

        for(char c: magazine){
            if(dict.find(c) == dict.end()){
                dict[c] = 1;
            }else{
                dict[c]++;
            }
        }

        for(char c : ransomNote){
            if(dict.find(c) != dict.end() && dict[c] > 0) {
                dict[c]--;
            }else{
                return false;
            }
        }
        return true;
    }
};

// Time complexity of this solution is O(n) and space complexity is
// Hashmap is used to store the frequency of characters in magazine, so the space complexity is O(n) where n is the length of magazine.