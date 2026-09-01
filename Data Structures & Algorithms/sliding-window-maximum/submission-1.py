class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        nums_len = len(nums)
        if k>nums_len:
            return []
        
        left, right = 0, k
        
        cur_max = nums[0]
        for i in range(0,k):
        
            cur_max = max(nums[i],cur_max)
        
        #print(cur_max)
        out = []
        out.append(cur_max)
        for i in range(k, nums_len):
            if cur_max == nums[i-k]:
                cur_max = nums[i-k+1]
                for j in range(i-k+2, i+1):
                    cur_max = max(nums[j], cur_max)
            else:
                cur_max = max(cur_max, nums[i])
            out.append(cur_max)
        return out