class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # oh this is fun!
        full = 1
        full_one_zero = 1
        #get the full mult
        num_zeros = 0
        for num in nums: 
            if num == 0:
                num_zeros +=1
            else:
                full_one_zero *= num
            full*= num
        #make list dividing by ith value
        output = []
        if num_zeros ==0:
            for num in nums:
                if num == 0:
                    output.append(full/1)
                else:
                    output.append(int(full/num))
        elif num_zeros == 1: 
            for num in nums:
                if num == 0:
                    output.append(int(full_one_zero/1))
                else:
                    output.append(int(full/num))
        else:
            output = [0]* len(nums)
        return output