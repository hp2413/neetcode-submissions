class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for char in s:
            if char == '{':
                st.append('}')
            elif char == '[':
                st.append(']')
            elif char == '(':
                st.append(')')
            else:
                if st and st[-1] == char:
                    st.pop()
                else:
                    return False
        if len(st) > 0:
            return False
        return True
        