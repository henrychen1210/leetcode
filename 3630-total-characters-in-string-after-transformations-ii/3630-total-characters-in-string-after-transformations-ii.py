from typing import List

MOD = 10**9 + 7

def mat_mult(A, B):
    size = len(A)
    result = [[0]*size for _ in range(size)]
    for i in range(size):
        for k in range(size):
            if A[i][k]:
                for j in range(size):
                    result[i][j] = (result[i][j] + A[i][k] * B[k][j]) % MOD
    return result

def mat_pow(mat, power):
    size = len(mat)
    result = [[int(i == j) for j in range(size)] for i in range(size)]  # identity matrix
    while power:
        if power % 2:
            result = mat_mult(result, mat)
        mat = mat_mult(mat, mat)
        power //= 2
    return result

class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        size = 26
        initial = [0] * size
        for c in s:
            initial[ord(c) - ord('a')] += 1

        # Build transformation matrix M
        M = [[0]*size for _ in range(size)]

        for i in range(size):  # for each letter i
            for j in range(1, nums[i]+1):
                M[(i + j) % size][i] += 1

        # Exponentiate M to the power t
        Mt = mat_pow(M, t)

        # Multiply M^t by the initial vector
        result = 0
        for i in range(size):
            for j in range(size):
                result = (result + Mt[i][j] * initial[j]) % MOD

        return result
