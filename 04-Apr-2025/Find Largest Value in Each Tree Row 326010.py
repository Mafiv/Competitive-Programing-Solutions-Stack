# Problem: Find Largest Value in Each Tree Row - https://leetcode.com/problems/find-largest-value-in-each-tree-row/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def comp(self,root,i):
        if not(root):
            return 0
        if(root.val>=self.arr[i]):
            self.arr[i]=root.val
        if(root.left):
            self.comp(root.left,i+1)
        if(root.right):
            self.comp(root.right,i+1)
        return 0    
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        a=(-2)**31
        self.arr=defaultdict(lambda: int(a)) 
        self.comp(root,0)
        ans=[]
        for i in self.arr:
            ans.append(self.arr[i])
        return ans


        