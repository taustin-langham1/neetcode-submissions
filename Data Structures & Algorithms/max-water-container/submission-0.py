class Solution:
    def maxArea(self, heights: List[int]) -> int:
        

        best_volume = 0

        left, right = 0, len(heights) - 1

        while left < right:

            current_volume = (right - left) * min(heights[left], heights[right])
            best_volume = max(current_volume, best_volume)

            if heights[left] < heights[right]:
                left += 1
            else: right -= 1

        return best_volume
