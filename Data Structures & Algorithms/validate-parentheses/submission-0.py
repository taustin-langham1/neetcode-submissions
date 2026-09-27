class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        pairs = {
            '{':'}',
            '(':')',
            '[':']'
        }

        for i in s:
            if i in pairs:
                stack.append(i)
            elif i in pairs.values():
                # if stack is empty
                if not stack:
                    return False # then it doesn't meet our criteria, only closing left
                checking = stack.pop()
                if pairs[checking] != i: # so if the value of the last value in the stack isnt the closing value from our dict then its a failure
                    return False
            
        if stack:
            return False # if the stack still exists, its invalid
        
        return True