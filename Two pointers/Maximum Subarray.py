class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #idea 1: two pointers?
        #idea 2: sum whole array and then subtract indexes?
        #idea 3: look for if sums of any parts of the array are ever negative, then discard those parts
        #Note we have to handle negative numbers here too
        #Maximum can be negative

        #max element
        maxElem = float('-inf')

        #Note length is >= 1

        l,r = 0,0
        sumSubArray = 0
        maxSum = float('-inf')

        while r < len(nums):
            maxElem = max(maxElem,nums[r])
            sumSubArray += nums[r]
            r += 1
            maxSum = max(maxSum, sumSubArray)
            if sumSubArray < 0:
                l = r
                sumSubArray = 0
            
        return max(maxSum,maxElem)