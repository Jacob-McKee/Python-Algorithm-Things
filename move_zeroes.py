class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        # Get two indexes. We will decrease the stop index everytime we pop a 
        # 0 out so we don't keep popping and adding 0s
        index = 0
        stop_index = len(nums) - 1

        while index <= stop_index:
            if nums[index] == 0:
                nums.pop(index)
                nums.append(0)
                stop_index -= 1
            else:
                index += 1
