class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # create a dict to count the count of the numbers
        count = {}

        # create an array to sort the frequency
        # indicies represent the frequency
        # values represent which elements
        freq = [[] for i in range(len(nums) + 1)]

        # iterate through the list
        for num in nums:
            # increment the counter if element was seen before
            count[num] = 1 + count.get(num, 0)

        # iterate through count dict
        for i, v in count.items():
            # index is count
            # value is the list of numbers
            freq[v].append(i)
        
        result = []

        # iterate trhough the list from end
        # bigger index means more frequent elements
        for i in range(len(freq) - 1, 0, -1):

            # iterate through the list of numbers
            for num in freq[i]:
                # add the list  to result list until k  is equal the length of the result
                result.append(num)
                if len(result) == k:
                    return result
        
