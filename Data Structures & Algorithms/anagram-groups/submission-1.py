class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramDict = {}
        for i in range(len(strs)):
            word = "".join(sorted(strs[i]))
            if word in anagramDict:
                anagramDict[word].append(strs[i])
            else:

                anagramDict[word] = [strs[i]]
        return list(anagramDict.values())