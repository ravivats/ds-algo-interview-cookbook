def removeZeros(num):
    numCopy = num
    for i in range(len(num)):
        if num[i] == '0':
            numCopy = numCopy.replace(num[i], '', 1)
        else:
            return numCopy
    return '0'


class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        if k >= len(num):
            return '0'
        elif len(num) - k == 1:
            numList = list(num)
            numList.sort()
            return numList[0]

        for j in range(k):
            i = 0
            while i + 1 < len(num) and num[i] <= num[i + 1]:
                i += 1
            # remove the character
            num = num[:i] + num[i + 1:]
        return removeZeros(num)


if __name__ == '__main__':
    s = Solution()
    print(s.removeKdigits("122519", 3))