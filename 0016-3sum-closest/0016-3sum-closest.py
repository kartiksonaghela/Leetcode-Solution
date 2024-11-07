class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()  # Sort the array to use two pointers efficiently
        n = len(nums)
        closest_sum = float('inf')  # Initialize with a large value
        
        for i in range(n - 2):  # Loop through each element as the first element of the triplet
            # Skip duplicate first elements
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left, right = i + 1, n - 1  # Set left and right pointers to find the second and third elements
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                # Update closest_sum if we found a closer sum
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                
                # Move pointers
                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    return current_sum  # If the sum is exactly the target, return it immediately
        
        return closest_sum  # Return the closest sum found
