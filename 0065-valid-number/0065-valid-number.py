class Solution:
    def isNumber(self, s: str) -> bool:
        '''
        e_, E_
        e__, E__
        -/+ _
        -/+ __
        .__
        __.__
        __.

        '''
        numSeen = False
        dotSeen = False
        eSeen = False
        numAfterE = False


        for i, c in enumerate(s):
            if c.isdigit():
                numSeen = True
                numAfterE = True
            elif c == '.':
                if dotSeen or eSeen:
                    return False
                dotSeen = True
            elif c in "eE":
                if eSeen or not numSeen:
                    return False
                eSeen = True
                numAfterE = False
            elif c in "-+":
                if i > 0 and s[i - 1] not in "eE":
                    return False
            else:
                return False
        return numSeen and numAfterE


