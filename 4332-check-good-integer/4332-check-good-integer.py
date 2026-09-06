class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        d = 0
        sq = 0
        for i in str(n):
            d += int(i)
            sq += (int(i) * int(i))
        return sq - d >= 50