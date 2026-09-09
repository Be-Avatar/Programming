class Solution:
    def countCommas(self, n: int) -> int:
        if n < 1000:
            return 0
        l = len(str(n))
        r = l // 3
        if l % 3 == 0:
            r -= 1
        rr = r * n
        while(r > 0):
            rr -= (1000)**r - 1
            r -= 1
        return rr
 
