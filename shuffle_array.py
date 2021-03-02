class Solution:
    # Using list splicing and alternating list adding
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        result = [None] * len(nums)
        result[::2] = nums[: int(len(nums) / 2)]
        result[1::2] = nums[int(len(nums) / 2):]

        return result

    def shuffle_with_append(self, nums: list[int], n: int) -> list[int]:
        l = []

        for i in range(n):
            l.append(nums[i])
            l.append(nums[i + n])

        return l
