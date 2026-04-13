class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        num_n = Counter(nums)
        bucket = [[] for _ in range(len(nums) + 1)]

        for i, v in num_n.items():
            bucket[v].append(i)

        for i in range(len(bucket)-1, -1, -1):
            for j in range(len(bucket[i])):
                result.append(bucket[i][j])
                if len(result) == k:
                    return result
