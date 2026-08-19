class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                #print("new nums")
                #print(i)
                #print(j)
                if nums[i] + nums[j] == target:
                    a = list([i,j])
                    return a
        return [0,0]