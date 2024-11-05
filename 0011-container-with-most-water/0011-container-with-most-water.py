class Solution:
    def maxArea(self, height: List[int]) -> int:
        min_pointer = 0
        max_pointer = len(height) - 1
        max_area = 0
        while min_pointer<max_pointer:
            width = max_pointer - min_pointer
            temp_area = width * min(height[min_pointer], height[max_pointer])
            if temp_area>max_area:
                max_area=temp_area
            if height[min_pointer]>height[max_pointer]:
                max_pointer-=1
            else:
                min_pointer+=1
        return max_area