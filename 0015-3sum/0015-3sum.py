class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output=set()
        for i in range(len(nums)):
            l=i+1
            r=len(nums)-1
            while l<r:
                out_set=(nums[i],nums[l],nums[r])
                if sum(out_set)==0:
                    output.add(out_set)
                    l+=1
                    r-=1
                elif sum(out_set)>0:
                    r-=1
                else:
                    l+=1
        return  [list(triplet) for triplet in output]