class Solution:
    def dailyTemperatures(self, nums: list[int]) -> list[int]:
        # Stack has (index, value)
        stack = []
        days_til_warmer = [0] * len(nums)

        for i in range(len(nums)-1, -1, -1):
            # Go through the stack until its empty
            while len(stack) > 0:
                # If the number on the top of the stack
                # is greater than the current temp we add it to
                # the days til warmer
                if stack[-1][1] > nums[i]:
                    days_til_warmer[i] = stack[-1][0] - i
                    break
                # If the number isn't higher we just get rid of it
                else:
                    stack.pop()

            stack.append((i, nums[i]))

        return days_til_warmer
