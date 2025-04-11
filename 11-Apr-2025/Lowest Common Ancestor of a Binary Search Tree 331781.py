# Problem: Lowest Common Ancestor of a Binary Search Tree - https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def traverse(root,p,q):
            if not(root):
                return 
            if(root.val < q.val and root.val<p.val):
                a=traverse(root.right,p,q)
            elif(root.val>q.val and root.val>p.val):
                a=traverse(root.left,p,q)
            else:
                return root
            return a
            
        return traverse(root,p,q)
