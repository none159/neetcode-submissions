class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        i = 0
        nums = []
        while len(tokens) != 1:
            nums = []
            i = 0
            while  len(tokens) != 1  and tokens[i] not in ('+','-','*','/'):
                nums.append(tokens[i])
                i += 1
            if len(nums)>=2:
                if tokens[i] == '+':
                    tokens[i] = int(nums.pop()) + int(nums.pop())
                    tokens.pop(i - 1)
                    tokens.pop(i - 2)
                elif tokens[i] == '-':
                    l = int(nums.pop()) 
                    bl = int(nums.pop()) 
                    tokens[i] = bl - l
                    tokens.pop(i - 1)
                    tokens.pop(i - 2)
                
                elif tokens[i] == '*':
                    tokens[i] = int(nums.pop()) *  int(nums.pop())
                    tokens.pop(i - 1)
                    tokens.pop(i - 2)
    
                elif tokens[i] == '/':
                    l = int(nums.pop()) 
                    bl = int(nums.pop()) 
                    tokens[i] = int(bl/l)
                    tokens.pop(i - 1)
                    tokens.pop(i - 2)
                
        return int(tokens[0])

# Brute force solution with a hint : time:o(n^2), space:o(n)