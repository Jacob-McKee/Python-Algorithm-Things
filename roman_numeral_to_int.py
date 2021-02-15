class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000,
        }
        
        number = 0
        
        # So we are going to loop through the string we are given
        # We subtract one to avoid going out of range
        for i in range(len(s)-1):
            # This is the important part. Because the numbers after should be lower
            # If they aren't it meants we have a subtracted numeral
            # Which means we should subtract the amount to equal it
            if roman_to_int[s[i]] < roman_to_int[s[i + 1]]:
                number -= roman_to_int[s[i]]
            #Otherwise we just add the value to our total
            else:
                number += roman_to_int[s[i]]
        # Grab the last value because we had to skip it
        number += roman_to_int[s[-1]]
            
        return number
           
            