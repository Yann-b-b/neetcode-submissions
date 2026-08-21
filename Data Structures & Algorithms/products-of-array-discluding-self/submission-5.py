class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        num_zeros = nums.count(0)
        prod_nonzero = math.prod(n for n in nums if n != 0)

        handlers = {
            0: lambda nums: [prod_nonzero // n for n in nums],
            1: lambda nums: [prod_nonzero if n == 0 else 0 for n in nums],
            2: lambda nums: [0] * len(nums),
        }
        return handlers[min(num_zeros, 2)](nums)
