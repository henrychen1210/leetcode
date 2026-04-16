class Solution:
    def isNumber(self, s: str) -> bool:
        numSeen = False
        dotSeen = False
        eSeen = False
        numAfterE = True

        for i, c in enumerate(s):
            if c.isdigit():
                numSeen = True
                numAfterE = True
            elif c == ".":
                if dotSeen or eSeen:
                    return False
                dotSeen = True
            elif c in "eE":
                if not numSeen or eSeen:
                    return False
                eSeen = True
                numAfterE = False
            elif c in "-+":
                if i > 0 and s[i - 1] not in "eE":
                    return False
            else:
                return False
        
        return numSeen and numAfterE