class Solution:
    def containsPattern(self, arr: list[int], m: int, k: int) -> bool:
        repeating = 0
        
        # Loop through the array subtracted by the length of the pattern
        for i in range(len(arr)-m):
            # If it hits an index that repeats itself then set repeating
            # equal everytime it matches. If it matches the expected
            # number of times return True
            repeating = repeating + 1 if arr[i] == arr[i+m] else 0
            if repeating == (k-1)*m: return True
        
        return False
    