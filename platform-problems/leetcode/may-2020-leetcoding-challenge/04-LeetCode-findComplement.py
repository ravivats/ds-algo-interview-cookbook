'''
Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.

Example 1:
Input: 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.

Example 2:
Input: 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.

Note:
    The given integer is guaranteed to fit within the range of a 32-bit signed integer.
    You could assume no leading zero bit in the integer’s binary representation.
    This question is the same as 1009: https://leetcode.com/problems/complement-of-base-10-integer/
'''


def findBinary(num: int) -> str:
    str1 = ''
    while (num != 0):
        str1 = str(num % 2) + str1
        num = num // 2
    return str1


class Solution:
    def findComplement(self, num: int) -> int:
        binStr = findBinary(num)
        total = 0
        mult = 1
        for i in reversed(range(0, len(binStr))):
            if binStr[i] == '0':
                total += mult
            mult *= 2
        return total
