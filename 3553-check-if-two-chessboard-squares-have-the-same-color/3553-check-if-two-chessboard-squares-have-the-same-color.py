class Solution:
    def checkTwoChessboards(self, c1: str, c2: str) -> bool:
        dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
        return ((dict[c1[0]] + int(c1[1])) % 2 == 0) == ((dict[c2[0]] + int(c2[1])) % 2 == 0)