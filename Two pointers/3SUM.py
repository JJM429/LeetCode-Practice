class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []

        for i in range(len(nums)-1):
            l = i + 1
            r = len(nums) - 1
            target = 0 - nums[i]

            if i>=1 and nums[i] == nums[i-1]:
                continue

            while l < r:
                currentTarget = nums[l] + nums[r]

                if currentTarget == target:
                    res.append([nums[i],nums[l],nums[r]])
                    temp = nums[l]
                    while l<r and nums[l] == temp:
                        l += 1
                elif currentTarget < target:
                    l += 1
                else: 
                    r -= 1
        
        return res