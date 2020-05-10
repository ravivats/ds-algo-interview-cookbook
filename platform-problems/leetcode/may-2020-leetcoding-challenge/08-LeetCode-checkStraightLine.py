'''
You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate 
of a point. Check if these points make a straight line in the XY plane.

Example 1:
Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: true

Example 2:
Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
Output: false

Constraints: 
 -> 2 <= coordinates.length <= 1000
 -> coordinates[i].length == 2
 -> -10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
 -> coordinates contains no duplicate point.
'''

class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        if len(coordinates) <= 2:
            return True
        x0_diff = (coordinates[1][0] - coordinates[0][0])
        if x0_diff == 0:
            ratio = 999999
        else:
            ratio = (coordinates[1][1] - coordinates[0][1])/x0_diff
        
        for i in range(1, len(coordinates)-1):
            x_diff = (coordinates[i+1][0] - coordinates[i][0])
            if x_diff == 0:
                if x0_diff != 0:
                    return False
            else:
                n_ratio = (coordinates[i+1][1] - coordinates[i][1])/x_diff
            if ratio != n_ratio:
                return False
        return True
