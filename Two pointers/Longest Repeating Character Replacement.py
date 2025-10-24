class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #sliding window approach
        #sliding window has max size k+n, where n = number of repeating elements from start of window

        l = 0
        countDict = {}

        for r in range(len(s)):
            #add all of the terms to a dictionary to count them
            countDict.update({ s[r] : 1 + countDict.get(s[r],0) })

            #within window check which character is most frequent and expand and shrink window accordingly
            highest_count_char = max(countDict)
            highest_count = max(countDict.values())
            
            #if window is too large,
            #slide window and update dict
            if r-l + 1 > k + highest_count:
                countDict.update({ s[l] : countDict.get(s[l]) - 1 })
                l += 1
                
        return r - l + 1 