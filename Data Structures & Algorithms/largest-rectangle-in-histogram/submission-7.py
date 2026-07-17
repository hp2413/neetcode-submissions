class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # [7,1,7,2,2,4]
        #  0 1 2 3 4 5
        # [-1, 1, 3, 4, 5]
        # 7 * (6 )
        res = 0
        st = [-1]
        n = len(heights)
        for i, h in enumerate(heights):
            while st[-1] != -1 and heights[st[-1]] > heights[i]:
                # print(st, i)
                top = st.pop()
                res = max(res, heights[top] * ( i - st[-1] - 1 ))
            st.append(i)
        i = n
        while len(st) != 1:
            # print(st, i)
            top = st.pop()
            res = max(res, heights[top] * ( i - st[-1] - 1 ))
        return res