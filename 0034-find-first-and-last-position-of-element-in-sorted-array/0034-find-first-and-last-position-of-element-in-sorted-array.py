class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        li=[]
        if target in nums:
            # n=c[target]
            li.append(nums.index(target))
            li.append(len(nums)-1-nums[::-1].index(target))
            return li
            
        else:
            return [-1,-1]