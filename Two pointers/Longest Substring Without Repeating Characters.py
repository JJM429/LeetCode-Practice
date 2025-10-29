class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l,r = 0,0
        charSet = set()

        max_length = 0

        while r < len(s):
            #check if s[r] in set
            #if yes slide window
            #if no add to charSet and increase currentlength
            if s[r] in charSet:
                while s[l] != s[r]:
                    charSet.remove(s[l])
                    l += 1     
                l += 1
            else:
                charSet.add(s[r])
                max_length = max(max_length, r - l + 1) #length plus one as inclusive of l and r
            r += 1
        return max_length
            