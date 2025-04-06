# Problem: Delete Node in a BST - https://leetcode.com/problems/delete-node-in-a-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def deleteRootNode(self, node):
        if not node.left:
            return node.right
        if not node.right:
            return node.left

        succ_parent = node
        succ = node.right
        while succ.left:
            succ_parent = succ
            succ = succ.left

        node.val = succ.val


        if succ_parent == node:
            succ_parent.right = succ.right
        else:
            succ_parent.left = succ.right
        return node

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            root = self.deleteRootNode(root)
        return root
