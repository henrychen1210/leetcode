class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        all_odd, all_even, even_odd, odd_even = [], [], [], []
        
        for n in nums:
            if n % 2 == 0:
                all_even.append(n)
                if len(even_odd) == 0 or even_odd[-1] % 2 == 1:
                    even_odd.append(n)
                if len(odd_even) > 0 and odd_even[-1] % 2 == 1:
                    odd_even.append(n)
            else:
                all_odd.append(n)
                if len(even_odd) > 0 and even_odd[-1] % 2 == 0:
                    even_odd.append(n)
                if len(odd_even) == 0 or odd_even[-1] % 2 == 0:
                    odd_even.append(n)
        
        res = max(len(all_odd), len(all_even), len(even_odd), len(odd_even))

        return res