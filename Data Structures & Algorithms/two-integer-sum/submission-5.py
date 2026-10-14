class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = range(len(nums))
        keys = nums
        d = dict(zip(keys, values))
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in d and d[diff] != i:
                return[i, d[diff]]