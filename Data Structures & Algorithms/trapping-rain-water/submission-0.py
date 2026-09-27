class Solution:
    def trap(self, height: List[int]) -> int:
        
        # try pointer technique from the extremeties
        if not height:
            return 0

        left, right = 0, len(height) - 1

        count = 0

        left_maximum, right_maximum = height[left], height[right]

        while left < right:

            if left_maximum < right_maximum:
                # so if the element on the left is less than the element on the right, then the left hand side is the limiting factor
                left += 1 # move left one step
                left_maximum = max(left_maximum, height[left])

                count += left_maximum - height[left]
            else:
                right -= 1
                right_maximum = max(right_maximum, height[right])

                count += right_maximum - height[right]
        
        return count