"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def postorder(self, root):
        return [] if not root else [j for i in root.children for j in self.postorder(i)] + [root.val]