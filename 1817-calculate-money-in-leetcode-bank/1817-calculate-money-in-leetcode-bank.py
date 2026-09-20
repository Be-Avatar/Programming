class Solution:
    def totalMoney(self, n: int) -> int:
        d = n // 7
        r = n % 7
        ans = 0
        m = 1
        for i in range(d):
            ans += (28 + i * 7)
            m += 1
        for i in range(r):
            ans += (m + i)
        return ans