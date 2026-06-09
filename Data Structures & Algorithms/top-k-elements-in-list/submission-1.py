class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = {}
        for num in nums:
            if num in result:
                result[num] += 1
            else:
                result[num] = 1
        
        data = sorted(result.items(), key=lambda x: x[1], reverse=True)
        return [v[0] for v in data[0:k]]
        