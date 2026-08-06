class Solution:

    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for i in tokens:
            if i == "+":
                v= s.pop() + s.pop()
                s.append(v)
            elif i == "-":
                v = -s.pop() + s.pop()
                s.append(v)
            elif i == "*":
                v = s.pop() * s.pop()
                s.append(v)
            elif i == "/":
                d = s.pop()
                n = s.pop()
                v = int(n/d)
                s.append(v)
            else:
                s.append(int(i))
            
        return s[0]




