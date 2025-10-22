class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS = {}
        for char in s:
            countS.update({ char : 1 + countS.get(char, 0) })
        
        countT = {}
        for char in t:
            countT.update({ char : 1 + countT.get(char, 0) })
        
        return countS == countT