class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        
        cars = sorted(zip(position, speed), reverse=True)
        temp = [] 
        
        for p, s in cars:
            time = (target - p) / s
            
            temp.append(time)
            
            #If there are at least 2 cars, check if the one we just added caught up
            if len(temp) >= 2 and temp[-1] <= temp[-2]:
                temp.pop()
                
        return len(temp)
    

        