'''
Given a circular array C of integers represented by A, find the maximum possible sum of a non-empty SubArray of C.

Here, a circular array means the end of the array connects to the beginning of the array.
(Formally, C[i] = A[i] when 0 <= i < A.length, and C[i+A.length] = C[i] when i >= 0.)

Also, a SubArray may only include each element of the fixed buffer A at most once.
(Formally, for a SubArray C[i], C[i+1], ..., C[j], there does not exist i <= k1, k2 <= j with k1 % A.length = k2 % A.length.)

Example 1: Input: [1,-2,3,-2], Output: 3
Explanation: SubArray [3] has maximum sum 3

Example 2: Input: [5,-3,5], Output: 10
Explanation: SubArray [5,5] has maximum sum 5 + 5 = 10

Example 3: Input: [3,-1,2,-1], Output: 4
Explanation: SubArray [2,-1,3] has maximum sum 2 + (-1) + 3 = 4

Example 4: Input: [3,-2,2,-3], Output: 3
Explanation: SubArray [3] and [3,-2,2] both have maximum sum 3

Example 5: Input: [-2,-3,-1], Output: -1
Explanation: SubArray [-1] has maximum sum -1
 
Note: -30000 <= A[i] <= 30000, 1 <= A.length <= 30000

Explanation of solution: https://www.youtube.com/watch?time_continue=444&v=uOMqWzkTRNw&feature=emb_logo

MaxSubArray sum of an array = Kadane's Algorithm
MaxSubArray sum of a circular array = max(MaxSubArray sum, Sum - MinSubArray sum)  <-- to delete the negative link
'''

class Solution(object):
    def maxSubArraySumCircular(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) == 0:
            return 0
        
        currMax, maxSum, currMin, minSum = A[0], A[0], A[0], A[0]
        sumArr = sum(A)
        for i in range(1, len(A)):
            n = A[i]
            currMax = max(n, currMax + n)
            maxSum = max(maxSum, currMax)
            currMin = min(n, currMin + n)
            minSum = min(minSum, currMin)
        
        print(sumArr, minSum, maxSum)
        # because we have to find the maximum possible sum of a non-empty SubArray of A
        if sumArr == minSum:
            return maxSum
        
        return max(sumArr - minSum, maxSum)