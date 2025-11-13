class Solution:
    def findMin(self, nums: List[int]) -> int:

        l,mid,r = 0,len(nums)//2,len(nums)-1
        minimum = float('inf')
        #determine if minimum is in left or right sorted array

        while l<=r: #<=?
            if nums[mid] < nums[l]:
                minimum = min(minimum, nums[mid])
                r = mid
            else:
                minimum = min(minimum, nums[l])
                l = mid + 1
            mid = l + (r-l)//2
        
        return minimum