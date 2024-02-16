class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # The efficient way
        index = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[index] = nums[i]
                index += 1
        return index

        # The way I did it first without realizing it didn't need to be sorted
        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = '_'
        nums.sort()

        return len(nums) - nums.count('_')