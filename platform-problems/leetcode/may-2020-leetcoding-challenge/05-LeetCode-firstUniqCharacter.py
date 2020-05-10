'''
 Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode" -> return 0.

s = "loveleetcode" -> return 2.

Note: You may assume the string contain only lowercase letters. 

'''
class Solution:
    def firstUniqChar(self, s: str) -> int:
        countMap = [[0 for x in range(2)] for y in range(26)]
        for i in range(0,len(s)):
            countMap[ord(s[i])-97][0] += 1
            countMap[ord(s[i])-97][1] = i
        res = 99999
        for j in range(0, len(countMap)):
            if  countMap[j][0] == 1:
                res = min(res,countMap[j][1])
        if res == 99999:
            return -1
        return res
        