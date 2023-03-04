class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = 0
        right = sum(nums)

        # Leaving out the middle while checking whether both sides are
        # even gives you the pivot index
        for index, value in enumerate(nums):
            right -= value
            if left == right:
                return index
            left += value
        
        return -1