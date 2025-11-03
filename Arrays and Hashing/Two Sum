class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_map = {}  # Dictionary to store value -> index pairs

        for index, elem in enumerate(nums):
            complement = target - elem
            if complement in prev_map:
                # If the complement exists in our map, we have our solution!
                return [prev_map[complement], index]
            
            # Otherwise, add the current number and its index to the map
            # for future elements to check against.
            prev_map[elem] = index
        return [-1]
    
            