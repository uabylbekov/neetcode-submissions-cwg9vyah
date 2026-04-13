class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create a dict to return the result 
        group = {}

        # iterate through the array
        for s in strs:

            # create a list, each index represents a letter, 
            # value represents the frequency of the letter
            count = [0] * 26

            # iterate through the string
            for c in s:

                # example if char is b, we deduct ascii number a from b
                # the index will be equal to a = 0, b = 1, c =2 and etc.
                count[ord(c) -  ord('a')] += 1
        
            # we put the list into tuple, only immutable values can be used as dict key
            key = tuple(count)

            # if key in group add it to the group
            # { (1, 1, 1): ['abc, 'cba', 'bca', 'acb']
            if key in group:
                group[key].append(s)
            else:
                group[key] = [s]
        
        # return the list of the group values
        return list(group.values())