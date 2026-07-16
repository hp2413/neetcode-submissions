class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # ["1","2","+","3","*","4","-"]
        st = []
        for ch in tokens:
            if ch == '+':
                a = st.pop()
                b = st.pop()
                st.append(b+a)
            elif ch == '-':
                a = st.pop()
                b = st.pop()
                st.append(b-a)
            elif ch == '*':
                a = st.pop()
                b = st.pop()
                st.append(b*a)
            elif ch == '/':
                a = st.pop()
                b = st.pop()
                st.append(int(float(b)/a))
            else:
                st.append(int(ch))
        
        return st.pop()

        