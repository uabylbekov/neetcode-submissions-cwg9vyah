class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        count = {}
        
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        bucket = [[] for _ in range(len(nums) + 1)]
        
        for i, v in count.items():
            bucket[v].append(i)

        for i in range(len(nums), -1, -1):
            for j in range(len(bucket[i])):
                result.append(bucket[i][j])
                if len(result) == k:
                    return result
            
