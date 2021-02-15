class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        # Grab the shortest string in the list
        shortest = min(strs, key=len)

        # Loop through the shortest and compare the characters
        # in the shortest with the characters in the rest of the list
        for i, ch in enumerate(shortest):
            for other in strs:
                # While looping through the other strings
                # if you hit one that doesn't match then we break
                # And send the current i position as it is the longest
                # matching sequence
                if other[i] != ch:
                    return shortest[:i]
        
        return shortest