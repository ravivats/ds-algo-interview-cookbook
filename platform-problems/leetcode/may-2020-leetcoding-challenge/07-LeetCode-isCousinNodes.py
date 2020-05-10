'''
In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

Return true if and only if the nodes corresponding to the values x and y are cousins.

Example 1:

Input: root = [1,2,3,4], x = 4, y = 3
Output: false

Example 2:

Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true

Example 3:

Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false

Note:
    The number of nodes in the tree will be between 2 and 100.
    Each node has a unique integer value from 1 to 100.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def searchDepth(root, key, currDepth):
    if root == None:
        return 0 ,0
    
    if (root.left != None and root.left.val == key) or (root.right != None and root.right.val == key):
        return root.val, currDepth+1
        
    root1, depth1 = searchDepth(root.left, key, currDepth+1)
    root2, depth2 = searchDepth(root.right, key, currDepth+1)
    
    if depth1 > depth2:
        return root1, depth1
    return root2, depth2
    
    
class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        currDepth = 0
        rootX, xD  = searchDepth(root,x,currDepth)
        rootY, yD = searchDepth(root,y,currDepth)
        return (xD == yD) and (rootX != rootY)