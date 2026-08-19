class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = dict()
        for i,x in enumerate(nums):
            key_to_find = target -x
            if key_to_find in a:
                return [a.get(target-x,0),i]
            a[x] = i
            print(a[x])
        
        """
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                #print("new nums")
                #print(i)
                #print(j)
                if nums[i] + nums[j] == target:
                    a = list([i,j])
                    return a
        """