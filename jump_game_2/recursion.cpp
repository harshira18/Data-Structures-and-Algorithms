class Solution {
public:
    int jump(vector<int>& nums) {
         int n = nums.size();

    // Pure recursive lambda function
    auto solve = [&](auto& self, int index) -> int {
        // Base Case: Arrived at or past the final index
        if (index >= n - 1) return 0;
        
        // Dead end: Cannot jump forward
        if (nums[index] == 0) return INT_MAX;
        
        int minJumps = INT_MAX;
        
        // Try every single valid jump step
        for (int i = 1; i <= nums[index]; i++) {
            int jumps = self(self, index + i);
            
            if (jumps != INT_MAX) {
                minJumps = min(minJumps, 1 + jumps);
            }
        }
        return minJumps;
        };

    // Begin recursion at the first index (0)
    return solve(solve, 0);

    }
};