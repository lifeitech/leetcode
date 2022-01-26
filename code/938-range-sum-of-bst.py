# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
        def rangeSumBST(self, root, L, R):
            ans = 0
            stack = [root]
            while stack:
                node = stack.pop()
                if node:
                    if L <= node.val <= R:
                        ans += node.val
                    if L < node.val:
                        stack.append(node.left)
                    if node.val < R:
                        stack.append(node.right)
            return ans