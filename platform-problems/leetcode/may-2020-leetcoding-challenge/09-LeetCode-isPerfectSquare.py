'''
Given a positive integer num, write a function which returns True if num is a perfect square else False.
Note: Do not use any built-in library function such as sqrt.

Example 1: Input: 16, Output: true

Example 2: Input: 14, Output: false
'''


class Solution(object):
    def isPerfectSquare(self, n):
        """
        :type num: int
        :rtype: bool
        """
        i = 1
        while i * i <= n:
            if n % i == 0 and n / i == i:
                return True
            i += 1
        return False