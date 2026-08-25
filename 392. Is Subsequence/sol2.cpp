class Solution {
public:
    bool isSubsequence(string s, string t) {
        int sp = 0;
        int tp = 0;

        while (sp < s.length() && tp < t.length()) {
            if (s[sp] == t[tp]) {
                sp++;
            }
            tp++;
        }

        return sp == s.length();        
    }
};

// difference between this solution and the previous one is that in this solution we are using two pointers to traverse both strings s and t, while in the previous solution we are using a nested loop to traverse string t for each character in string s. The time complexity of this solution is O(n) where n is the length of string t, while the time complexity of the previous solution is O(n) where n is the length of string t. The space complexity of both solutions is O(1) as we are using only a constant amount of extra space.