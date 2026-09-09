class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        s = str(n)
        st = set(s)
        d = {}
        for i in s:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        sui = 0
        for k in d:
            sui += (int(d[k]) * int(k))

        return sui