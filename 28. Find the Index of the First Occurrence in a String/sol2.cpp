class Solution {
public:
int solve(string &s,string &part){
    int ind = s.find(part);
    if(ind != string::npos) return ind;
    return -1;
}
    int strStr(string haystack, string needle) {
        // return solve(haystack, needle);
         int n=haystack.size();
        int m=needle.size();
        for(int i=0;i<n;i++){
            if(haystack[i]==needle[0]){
                bool flag=true;
                for(int k=0;k<m;k++){
                    if(needle[k]!=haystack[i+k]){
                        flag=false;
                        break;
                    }
                }
                if(flag)
                return i;
            }
        }
        return -1;
    }
};