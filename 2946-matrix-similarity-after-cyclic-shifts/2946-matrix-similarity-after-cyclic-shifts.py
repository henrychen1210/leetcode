class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        m = len(mat)
        n = len(mat[0])
        k %= n

        for i in range(m):
            if i % 2 == 0:
                og = mat[i].copy()
                mat[i] = mat[i][k: n] + mat[i][:k]
                # print(og, mat[i])
                if og != mat[i]:
                    return False
            else:
                og = mat[i].copy()
                mat[i] = mat[i][-k: n] + mat[i][:-k]
                # print(og, mat[i])
                if og != mat[i]:
                    return False
        
        return True
