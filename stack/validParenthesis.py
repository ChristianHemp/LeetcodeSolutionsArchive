class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if s[0] != '(' and s[0] != '{' and s[0] != '[':
            return False
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                stack.append(s[i])
            elif len(stack) >= 1:
                top = stack.pop()
                if s[i] == ')' and top != '(':
                    return False
                elif s[i] == '}' and top != '{':
                    return False
                elif s[i] == ']' and top != '[':
                    return False
            else:
                return False
        return len(stack) == 0
