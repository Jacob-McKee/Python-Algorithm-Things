class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_index = 0

        if len(s) > 0:
            for value in t:
                if value == s[s_index]:
                    s_index += 1
                    
                    if s_index == len(s):
                        return True
        else:
            return True
        return False