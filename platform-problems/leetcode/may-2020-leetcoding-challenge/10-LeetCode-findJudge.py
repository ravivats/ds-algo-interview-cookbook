'''
In a town, there are N people labelled from 1 to N.  There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given trust, an array of pairs trust[i] = [a, b] representing that the person labelled a trusts the person labelled b.

If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1.

Example 1:
Input: N = 2, trust = [[1,2]], Output: 2

Example 2:
Input: N = 3, trust = [[1,3],[2,3]], Output: 3

Example 3:
Input: N = 3, trust = [[1,3],[2,3],[3,1]], Output: -1

Example 4:
Input: N = 3, trust = [[1,2],[2,3]], Output: -1

Example 5:
Input: N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]], Output: 3

Note:
1 <= N <= 1000
trust.length <= 10000
trust[i] are all different
trust[i][0] != trust[i][1]
1 <= trust[i][0], trust[i][1] <= N
'''


class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        if len(trust) == 0 or N < 2:
            return 1

        # map of how many trust a given person i.e. {3:5}
        trustCount = {}
        # map of does a person trusts anybody i.e {3:True}
        doesTrustSomeone = {}
        for i in range(len(trust)):
            if trustCount.get(trust[i][1]) == None:
                trustCount[trust[i][1]] = 1
            else:
                trustCount[trust[i][1]] += 1

            if doesTrustSomeone.get(trust[i][0]) == None:
                doesTrustSomeone[trust[i][0]] = True

        for key in trustCount:
            if trustCount[key] >= N - 1 and doesTrustSomeone.get(key) == None:
                return key
        return -1
