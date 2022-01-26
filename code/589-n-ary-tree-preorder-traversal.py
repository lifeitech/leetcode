"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def preorder(self, root):
        if not root:
            return []
        traversal = [root.val]
        for child in root.children:
            traversal.extend(self.preorder(child))
        return traversal