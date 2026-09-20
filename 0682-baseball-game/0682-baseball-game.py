class Solution:
    def calPoints(self, operations: list[str]) -> int:
        s = []
        l = 0
        for i in operations:
            try:
                s.append(int(i))
            except ValueError:
                if i == 'C':
                    if s:
                        s.pop()
                    else:
                        s = s
                elif i == 'D':
                    if s:
                        m = s[-1] * 2
                        s.append(m)
                    else:
                        s = s
                elif i == '+':
                    l = s[-1] + s[-2]
                    s.append(l)
                    l = 0
        return sum(s)