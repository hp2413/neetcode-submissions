class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # [7,1,7,2,2,4]
        # [0,1,2,3,4,5]
        # max = 7
        # [1,3,4,5]
        st = [-1]
        res = 0
        for i, h in enumerate(heights):
            while st[-1] != -1 and heights[st[-1]] > heights[i]:
                top = st.pop()
                res = max(res, heights[top] * (i - st[-1] - 1))
            st.append(i)
        i = len(heights)
        while len(st) != 1:
            top = st.pop()
            res = max(res, heights[top] * (i - st[-1] - 1))
        return res        