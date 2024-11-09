from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = set()
        
        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1
            while l < r:
                out_set = (nums[i], nums[l], nums[r])
                temp_sum = sum(out_set)
                
                if temp_sum == 0:
                    output.add(out_set)
                    l += 1
                    r -= 1  # Move both pointers to find other unique triplets
                elif temp_sum > 0:
                    r -= 1
                else:
                    l += 1
                    
        return [list(triplet) for triplet in output]
