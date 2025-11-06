class Solution:
    def isValid(self, s: str) -> bool:
        
        closeToOpen = { ']' : '[' ,  '}' : '{' ,  ')' : '(' }

        stack = []

        for char in s:
            if char in closeToOpen:
                if not stack or stack.pop() != closeToOpen[char]:
                    return False
            else:
                stack.append(char)
            
        if stack:
            return False
        
        return True