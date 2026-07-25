# Jump Game

## Problem Idea

Given an array `nums`, each element represents the maximum number of steps you can jump forward from that index. The goal is to determine whether you can reach the last index.

## Greedy Approach

We keep track of the furthest index we can reach so far.

- `mjump` stores the maximum reachable index.
- While iterating through the array:
  - If the current index is greater than `mjump`, then it is impossible to reach this position, so return `false`.
  - Otherwise, update `mjump` using `i + nums[i]`.
- If the loop finishes, then the last index is reachable.

## C++ Solution

```cpp
class Solution {
public:
    bool canJump(vector<int>& nums) {
        int mjump = 0;
        for (int i = 0; i < nums.size(); i++) {
            if (i > mjump) return false;
            mjump = max(mjump, i + nums[i]);
        }
        return true;
    }
};
```

## Why This Works

At every step, `mjump` represents the farthest position that can be reached from the part of the array processed so far. If we never get stuck before the end, then reaching the last index is possible.

## Time Complexity

- O(n)

## Space Complexity

- O(1)
