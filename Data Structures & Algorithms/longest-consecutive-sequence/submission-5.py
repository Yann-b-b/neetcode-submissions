class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        all_nums = set(nums)
            
        all_nums = sorted(all_nums)
        longest = 0
        prev = None
        cur_long = 0
        for i,n in enumerate(all_nums):
            
            if i == 0:
                prev = n
                cur_long = 1
                longest = 1
                
            if n == 1+prev:
                prev = n
                cur_long+=1
                longest = max(longest,cur_long)
            else:
                cur_long = 1
                prev=n
        
        return longest
                
            