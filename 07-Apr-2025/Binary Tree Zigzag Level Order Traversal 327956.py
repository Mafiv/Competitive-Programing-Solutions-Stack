# Problem: Binary Tree Zigzag Level Order Traversal - https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.arr = defaultdict(deque)
        def helper(root , c):
            if not root:
                return
            if c % 2:
                self.arr[c].appendleft(root.val)
            else:
                self.arr[c].append(root.val)
            helper(root.left , c+1)
            helper(root.right , c+1)
        helper(root , 0)
        ans = []
        for i in self.arr:
            ans.append(list(self.arr[i]))
        return ans
        