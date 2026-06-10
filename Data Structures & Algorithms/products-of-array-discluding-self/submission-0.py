class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_result = [1] * len(nums)
        postfix_result = [1] * len(nums)
        result = [1] * len(nums)
        for i in range(0, len(nums)):
            prefix_result[i] = prefix_result[i-1] * nums[i-1] if i > 0 else 1
        for j in range(len(nums)-1,-1,-1):
            postfix_result[j] = postfix_result[j+1] * nums[j+1] if j < len(nums) - 1 else 1
        for i in range(0, len(nums)):
            result[i] = postfix_result[i] * prefix_result[i]

        return result

        