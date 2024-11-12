from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Initialize variables for Kadane's algorithm
        max_sum = float('-inf')
        current_sum = 0

        # Traverse the list
        for num in nums:
            current_sum = max(num, current_sum + num)  # Max of starting new or continuing
            max_sum = max(max_sum, current_sum)        # Update max_sum if current_sum is higher

        return max_sum
