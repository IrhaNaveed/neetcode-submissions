class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = {}
        for num in range(0, len(nums)):
            value = target - nums[num]
            if value in result: 
                return [result[value], num]
            else:
                result[nums[num]] = num
        
        return None