class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        all_nums = set(nums)
        longest = 0
        prev = None
        cur_long = 0
        for i,n in enumerate(all_nums):
            length = 0
            if (n-1) not in all_nums:
                
                while(n+length) in all_nums:
                    length+=1
            longest = max(length,longest) 
        return longest
                
            