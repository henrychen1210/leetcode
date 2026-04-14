class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        '''
        a, b, c
        d, e, f

        helper(i, digits, curr, res)

            if curr == len(digits)

            helper(1, digits, a, res)
            helper(1, digits, b, res)
            helper(1, digits, c, res)

            return



        '''

        nums = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz"
        }

        def helper(i, digits, curr, res):
            if len(curr) == len(digits):
                res.append(curr)
                return
            
            for c in nums[int(digits[i])]:
                helper(i + 1, digits, curr + c, res)

            return
        
        res = []
        helper(0, digits, "", res)
        return res
