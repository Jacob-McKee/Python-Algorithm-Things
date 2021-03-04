class Solution:
    def compress(self, chars: list[str]) -> int:
        s = ''

        # Do a window method to keep track of the number of letters
        first_index = 0
        second_index = 0
        current_letter = chars[0]

        while second_index < len(chars):
            # As soon as we hit a letter that isn't the same
            # We will add the letter to the string and the number 
            # of times it's shown
            if chars[second_index] != current_letter:
                value = second_index - first_index
                s += current_letter

                if value != 1:
                    s += str(value)

                first_index = second_index
                current_letter = chars[second_index]

            second_index += 1

        # Just to clean up the last bit
        s += current_letter
        if second_index - first_index > 1:
            s += str(second_index - first_index)

        chars[:] = [i for i in s]

        return len(chars)
