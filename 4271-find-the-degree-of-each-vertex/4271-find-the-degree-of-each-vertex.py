class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        ans = []
        for i in matrix:
            s = 0
            for j in range(0, len(matrix)):
                s += i[j]
            ans.append(s)
        return ans