class Solution:
    def isValid(self, s: str) -> bool:
        valid = {'{':'}','(':')','[':']'}
        stack = []
        for c in s:
            print(stack)
            if stack != [] and (stack[-1] in valid and c == valid[stack[-1]]):
                stack.pop()
            else:
                stack.append(c)
        return len(stack) == 0 