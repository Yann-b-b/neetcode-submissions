class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = dict() 
        for num in nums:
            counts[num] = counts.get(num, 0) + 1   
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, c in counts.items():
            buckets[c].append(num)

        out = []
        for c in range(len(nums), 0, -1):  
            for num in buckets[c]:
                out.append(num)
                if len(out) == k:
                    return out