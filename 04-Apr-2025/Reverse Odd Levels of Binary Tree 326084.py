# Problem: Reverse Odd Levels of Binary Tree - https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self,root,i):
        if not(root):
            return  0
        if(i%2!=0):            
            self.arr[i].append(root.val)
        self.helper(root.left,i+1)
        self.helper(root.right,i+1)
    def maker(self,root,i):
        if not(root):
            return  0
        if(i%2!=0):            
            root.val=self.arr[i].pop()
        self.maker(root.left,i+1)
        self.maker(root.right,i+1)        

    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.arr=defaultdict(list)
        self.helper(root,0)
        self.maker(root,0)
        return root
        