# Best Time to Buy and Sell Stock

## Problem Statement

You are given an integer array `prices`, where `prices[i]` is the price of a stock on day `i`.

You may buy and sell the stock multiple times, but you can hold at most one share at a time. The goal is to maximize the total profit.

## Greedy Approach

The idea is simple: whenever the price rises from one day to the next, we add that increase to the profit.

### Steps

1. Initialize `profit = 0`.
2. Traverse the array from day `1` to `n - 1`.
3. If `prices[i] > prices[i - 1]`, add `prices[i] - prices[i - 1]` to the profit.
4. Return the total profit.

### Why It Works

If the price goes up over several days, the total gain is simply the sum of each small increase.

Example:
- `1 -> 3 -> 5`
- Profit = `(3 - 1) + (5 - 3) = 5 - 1`

So, adding every positive difference gives the maximum possible profit.

## C++ Solution

```cpp
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int profit = 0;

        for (int i = 1; i < prices.size(); ++i) {
            if (prices[i] > prices[i - 1]) {
                profit += prices[i] - prices[i - 1];
            }
        }

        return profit;
    }
};
```

## Complexity Analysis

- Time Complexity: O(n)
- Space Complexity: O(1)
