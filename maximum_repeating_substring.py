class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        # So we will incrememt i and multiply it by the word
        # and check if each multiplication is in the word
        i = 1

        while word * i in sequence:
            i += 1

        return i - 1
