# Solution for leetcode based on Nick White from youtube https://www.youtube.com/watch?v=3IETreEybaA

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Window method - We have two pointers that slide along exposing
        # a limited scope of the list
        a_pointer = 0
        b_pointer = 0
        max_substring = 0
        curr_substring = []
        
        # We check the b pointer as it is the one that will move more and
        # will hit the end first
        while b_pointer < len(s):
            # If the character is not in the current_substring the add it
            if s[b_pointer] not in curr_substring:
                curr_substring.append(s[b_pointer])
                b_pointer += 1
                
                # Set the max substring depending on if the new substring is bigger
                max_substring = max(len(curr_substring), max_substring)
            else:
                # Delete the first element because you found a duplicate
                a_pointer += 1
                curr_substring.pop(0)
                
        return max_substring