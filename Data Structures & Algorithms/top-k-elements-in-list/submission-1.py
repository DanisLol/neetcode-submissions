class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = []
        for i in range(len(nums) +1):
            freq.append([])
        
        #create a dict with element: frequency
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        #go through the keys/elements in count
        for n in count:
            #look up the frequency of the element
            c = count[n]
            #the frequency is the index so append that element in that index
            freq[c].append(n)
        
        result = []
        for i in range(len(nums), 0, -1):
            for n in freq[i]:
                result.append(n)
                if len(result) == k:
                    return result