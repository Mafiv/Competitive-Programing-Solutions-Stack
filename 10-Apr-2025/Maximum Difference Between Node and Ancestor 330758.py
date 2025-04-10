# Problem: Maximum Difference Between Node and Ancestor - https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.diff=0
        def traverse(root,mn,mx):
            if not(root):
                return
            self.diff=max(self.diff,abs(mn-root.val),abs(root.val-mx))
            mn=min(root.val,mn)
            mx=max(root.val,mx)
            traverse(root.left,mn,mx)
            traverse(root.right,mn,mx)
        traverse(root,root.val,root.val)
        return self.diff



        