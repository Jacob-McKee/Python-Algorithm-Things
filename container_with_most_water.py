from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        MAX = 0
        x = 0
        y = len(height) - 1

        while x != y:
            if height[x] < height[y]:
                area = height[x] * (y - x)
                x += 1
            else:
                area = height[y] * (y - x)
                y -= 1

            MAX = max(MAX, area)

        return MAX
