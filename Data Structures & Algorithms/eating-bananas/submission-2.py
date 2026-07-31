class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # k = 
        # i is a pile
        #les than k banan in a pile, finish eat but can't eat from another #pile in the same horu
        #return min k such taht you can eat all bananas withitn h hours
        

        a = 1
        b = max(piles)
        
        while a <= b:
            c = 0
            m = (a+b)//2
            
            for i in piles:
                c += math.ceil(i/m)
            if c <= h:
                k = m
                b = m - 1
                k = min(k, m)
            if c > h:
                a = m + 1
        return k



