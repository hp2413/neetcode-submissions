# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # base
        if root is None:
            return 0
        # logic
        cnt_l = self.maxDepth(root.left)
        cnt_r = self.maxDepth(root.right)
        return max(cnt_l, cnt_r) + 1

        