class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = {}
        for value in s:
            if value in dict_s:
                dict_s[value] += 1
            else:
                dict_s[value] = 1
        
        for val in t:
            if val in dict_s and dict_s[val] != 0:
                dict_s[val] -=1
            else:
                return False
        
        #check if the dict_s contains all the 0 if not then it's not anagram
        for val in dict_s.values():
            if val != 0:
                return False
        return True