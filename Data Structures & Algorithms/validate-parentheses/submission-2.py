class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if len(stack) != 0:
                print(f"top of stack has:{stack[-1]}")
                print(f"we are looking at: {s[i]}")
                if self.isPair(stack[-1], s[i]):
                    stack.pop()
                else:
                    print(f"adding: {s[i]} to the stack")
                    stack.append(s[i])
            else:
                print(f"adding: {s[i]} to the stack")
                stack.append(s[i])
        if len(stack) == 0:
            return True
        return False
            
            

    def isPair(self, l: str, r: str):
        if l == "[" and r == "]":
            return True
        elif l == "(" and r == ")":
            return True
        elif l == "{" and r == "}":
            return True 
        return False
        
