# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        def dfs(root, level):
            # base 
            if not root:
                return
            # logic
            if len(res) == level:
                res.append(0)
            dfs(root.left, level+1)
            dfs(root.right, level+1)
            res[level] = root.val
        dfs(root, 0)
        return res