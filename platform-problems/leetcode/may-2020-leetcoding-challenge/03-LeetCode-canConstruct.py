'''
Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
'''
class Solution:
    def canConstruct(self, J: str, S: str) -> bool:
        mapdict = {}
        for i in range(0, len(S)):
            if mapdict.get(S[i]) != None:
                mapdict[S[i]] = mapdict[S[i]] + 1
            else:
                mapdict[S[i]] = 1
        for j in range(0, len(J)):
            if mapdict.get(J[j], 0) == 0:
                return False
            else:
                mapdict[J[j]] = mapdict[J[j]] - 1
        return True

if __name__ == '__main__':
    Solution s = Solution()
    Solution.canConstruct("aa", "aab")
    