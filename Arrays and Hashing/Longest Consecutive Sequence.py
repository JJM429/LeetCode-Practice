class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        max_length = 0
        #check if num - 1 in nums and if not count ahead in nums for sequence
        for num in set_nums:
            if (num-1) not in set_nums:
                length = 1

                while num + length in set_nums:
                    length += 1

                max_length = max(length,max_length)
        return max_length