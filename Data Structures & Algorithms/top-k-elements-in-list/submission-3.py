class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Brute force first:
        x = dict()
        for num in nums:
            x[num] = x.get(num,0) +1

        out = []
        
        for i in range(0,k):
            out.append(sorted(x,key = lambda n: x.get(n,0), reverse=True)[i])
        return out