class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #take a two pointer approach?

        #start at either end of the array, if number is too large, move right pointer left, if too small, move left pointer right
        
        l = 0
        r = len(numbers) - 1

        while l < r:
            if numbers[l] + numbers[r] > target:
                r -= 1
            elif numbers[l] + numbers[r] == target:
                return [l+1, r+1] # 1-indexed
            else:
                l += 1

        return []