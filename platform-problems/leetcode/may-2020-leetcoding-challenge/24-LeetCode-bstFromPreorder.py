'''
Return the root node of a binary search tree that matches the given preorder traversal.

(Recall that a binary search tree is a binary tree where for every node, any descendant of node.
left has a value < node.val, and any descendant of node.right has a value > node.val.  
Also recall that a preorder traversal displays the value of the node first, 
then traverses node.left, then traverses node.right.)

It's guaranteed that for the given test cases there is always possible to find a 
binary search tree with the given requirements.

Example 1: Input: [8,5,1,7,10,12], Output: [8,5,10,1,7,null,12]
'''
import math

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def insertInBst(root, val):
    if root == None:
        root = TreeNode()
        root.val = val
        return root
    if val < root.val:
        root.left = insertInBst(root.left, val)
    if val > root.val:
        root.right = insertInBst(root.right, val)
    return root


class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        root = None
        for i in range(len(preorder)):
            root = insertInBst(root, preorder[i])
        return root