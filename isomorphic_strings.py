class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # The dictionary that will store the new keys for what to replace with what
        key_dict = {}
        # The word that will be checked against s
        word = ""

        # The idea is that we will loop through t, check if the letter is in our key_dict
        # If it is, we will add the value to the word and then continue
        for index, value in enumerate(t):
            if value in key_dict:
                word += key_dict[value]
            else:
                # If the key isn't in the dicitonary, we are going to check to make sure the
                # s value isn't already in there because it can mess up for words that repeat 
                # characters on the first string
                if s[index] in key_dict.values():
                    return False

                # Add the key and value and update the word
                key_dict[value] = s[index]
                word += key_dict[value]


        # Check that they're equal, if not return false
        if s == word:
            return True
        return False
        