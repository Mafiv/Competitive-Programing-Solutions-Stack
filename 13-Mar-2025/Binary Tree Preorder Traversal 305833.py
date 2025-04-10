# Problem: Binary Tree Preorder Traversal - https://leetcode.com/problems/binary-tree-preorder-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self,node):
        if not (node):
            return 
        self.ans.append(node.val)
        self.dfs(node.left)
        self.dfs(node.right)
    
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.ans=[]
        self.dfs(root)
        return self.ans

        
        