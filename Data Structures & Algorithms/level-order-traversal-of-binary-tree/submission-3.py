# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # bfs
    # def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    #     res = []
    #     if not root:
    #         return res
    #     q = collections.deque()
    #     q.append(root)
    #     while q:
    #         l = len(q)
    #         ls = []
    #         for i in range(l):
    #             curr = q.popleft()
    #             if curr:
    #                 ls.append(curr.val)
    #             if curr and curr.left:
    #                 q.append(curr.left)
    #             if curr and curr.right:
    #                 q.append(curr.right)
    #         res.append(ls)
    #     return res 

    # dfs
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res
        def dfs(root, level):
            # base 
            if not root:
                return
            # logic
            if len(res) == level:
                res.append([])
            res[level].append(root.val)
            dfs(root.left, level+1)
            dfs(root.right, level+1)
        dfs(root, 0)
        return res
    
    