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
        totalRemoved = 0
        numClone = num
        for i in range(len(num) - 1):
            if num[i] > num[i + 1]:
                numClone = numClone.replace(num[i], '', 1)
                totalRemoved += 1
                if totalRemoved == k:
                    break
        return removeZeros(numClone[:len(numClone) - k + totalRemoved])


if __name__ == '__main__':
    s = Solution()
    print(s.removeKdigits("1234567890", 9))