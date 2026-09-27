class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0

        s = set()

        for num in nums:
            if num not in s: s.add(num)

        count = 1
        for num in s:
            if num - 1 not in s: # then this is a possible start
                length = 1
                while num + length in s:
                    length  += 1
                    count = max(length, count)
        return count
