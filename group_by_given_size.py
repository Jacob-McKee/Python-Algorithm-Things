"""
Example:
Input: groupSizes = [3,3,3,3,3,1,3]
Output: [[5],[0,1,2],[3,4,6]]
Explanation: 
The first group is [5]. The size is 1, and groupSizes[5] = 1.
The second group is [0,1,2]. The size is 3, and groupSizes[0] = groupSizes[1] = groupSizes[2] = 3.
The third group is [3,4,6]. The size is 3, and groupSizes[3] = groupSizes[4] = groupSizes[6] = 3.
Other possible solutions are [[2,1,6],[5],[0,4,3]] and [[5],[0,6,2],[4,3,1]].
"""


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        nums = dict()
        res = []

        for i, j in enumerate(groupSizes):
            if j not in nums.keys():
                nums[j] = [i]
            else:
                nums[j].append(i)

        for i, j in nums.items():
            for k in range(0, len(j), i):
                res.append(j[k:k + i])

        return res
