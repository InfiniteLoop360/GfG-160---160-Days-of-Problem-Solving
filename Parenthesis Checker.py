class Solution:
    def isBalanced(self, s):
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in mapping.values():
                stack.append(char)
            elif char in mapping:
                if not stack or stack[-1] != mapping[char]:
                    return False
                stack.pop()
        
        return not stack
