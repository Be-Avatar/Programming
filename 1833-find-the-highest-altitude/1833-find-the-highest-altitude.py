class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        gain.insert(0,0)
        pain = gain
        pain.append(0)
        n = len(gain)
        for i in range(n):
            gain[i] += pain[i - 1]
        return max(gain)