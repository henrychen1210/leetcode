class Solution:
    def isValid(self, s: str) -> bool:
        '''
        stack = []
        '''
        stack = []
        for c in s:
            if c == "(":
                stack.append(")")
            elif c == "{":
                stack.append("}")
            elif c == "[":
                stack.append("]")
            else:
                if stack and stack.pop() == c:
                    continue
                else:
                    return False
        return True if len(stack) == 0 else False
    