# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, node):
        if node:
            node.left, node.right = self.invertTree(node.right), self.invertTree(node.left)
            return node