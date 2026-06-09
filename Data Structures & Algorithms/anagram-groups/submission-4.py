class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #will review again
        result = [[strs[0]]]
        for s in strs[1:]:
            for i in range(len(result)):
                if sorted(s) == sorted(result[i][0]):
                    result[i].append(s)
                    break
            else:
                result.append([s])
        return result
        