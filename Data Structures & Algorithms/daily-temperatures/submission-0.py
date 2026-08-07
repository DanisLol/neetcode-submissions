class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        result = [0] * len(temperatures)
        temp = [] #contains (temperature, index)
        for i, t in enumerate(temperatures):

            while temp != [] and t > temp[-1][0]:
                popped_i = temp.pop()[1]
                
                result[popped_i] = i - popped_i

            temp.append((t,i))
        
        return result

