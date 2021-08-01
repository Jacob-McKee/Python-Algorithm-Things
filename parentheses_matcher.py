class Solution:
    def isValid(self, string_to_test: str) -> bool:
        parentheses = {'(': ')', '[': ']', '{': '}'}
        stack = []

        for char in string_to_test:
            if char in '([{':
                stack.append(char)
            elif stack and parentheses[stack[-1]] == char:
                stack.pop()
            else:
                return False
 
        return len(stack) == 0
