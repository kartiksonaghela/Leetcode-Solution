class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        output=set()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                l=j+1
                r=len(nums)-1
                while l<r:
                    out_set=(nums[i],nums[j],nums[l],nums[r])
                    if sum(out_set)==target and out_set not in output:
                        output.add(out_set)
                    elif sum(out_set)>target:
                        r-=1
                    else:
                        l+=1
        return list(output)
