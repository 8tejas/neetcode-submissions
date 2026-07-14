class Solution:
    def checkAnagram(self,s, t):
        countS = {}
        countT = {}
        if len(s) != len(t):
            return False
        for i, n in enumerate(s):
            countS[n] = 1 + countS.get(n, 0)
        for i, n in enumerate(t):
            countT[n] = 1 + countT.get(n,0)
        return countS == countT
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramDict = {}
        addedToList = []
        for i in range(len(strs)):
            if strs[i] in addedToList:
                continue
            anagramDict[strs[i]] = [strs[i]]
            
            for j in range(i+1, len(strs)):
                if self.checkAnagram(strs[i], strs[j]):
                        anagramDict[strs[i]].append(strs[j])
                        addedToList.append(strs[j])
        anagramList = []
        for i in anagramDict.values():
            anagramList.append(i)
        return anagramList
                    
