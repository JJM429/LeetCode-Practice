class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        sum1 = 1
        sum2 = 1
        non_zeros = 0
        zeros = 0
        for num in nums:
            sum1 *= num
            if not num == 0:
                non_zeros += 1
                sum2 *= num
            else:
                zeros += 1
        res = []
        for num in nums:
            if zeros > 1:
                res.append(0)
                continue
            try:
                res.append(int(sum1/num))
            except ZeroDivisionError:
                res.append(sum2)
        return res