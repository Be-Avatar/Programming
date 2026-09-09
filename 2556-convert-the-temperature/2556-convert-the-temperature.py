class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        arr = []  
        arr.append(celsius + 5463/20)  
        arr.append(celsius * 9/5 + 32)  
        return arr