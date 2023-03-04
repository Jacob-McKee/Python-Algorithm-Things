class Solution:
    # First slightly bad way
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
    
    # 2 MS better but a bit cleaner
    def isSubsequence_2(self, s: str, t: str) -> bool:
        if not s:
            return True

        index = 0

        for i in t:
            if s[index] == i:
                index += 1
            if index == len(s):
                return True
        
        return False