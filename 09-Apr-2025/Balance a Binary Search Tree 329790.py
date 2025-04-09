# Problem: Balance a Binary Search Tree - https://leetcode.com/problems/balance-a-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        ans=[]
        def dfs(root):
            if not(root):
                return 
            dfs(root.left)
            ans.append(root.val)
            dfs(root.right)
        
        def construct(arr):
            if(len(arr)==0):
                return 
            mid=len(arr)//2
            root=TreeNode(arr[mid])
            root.left=construct(arr[:mid])
            root.right=construct(arr[mid+1:])
            return root
        dfs(root)
        a=construct(ans)
        return a

