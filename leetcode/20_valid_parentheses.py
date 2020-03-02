class Solution:
    def isValid(self, s):
        if len(s) % 2 == 1:
            return False

        stack = []

        for c in s:
            if c == "(" or c == "[" or c == "{":
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False

                left = stack.pop()
                if (not left == "(" and c == ")") \
                        or (not left == "[" and c == "]")\
                        or (not left == "{" and c == "}"):
                    return False

        if len(stack) > 0:
            return False

        return True


solution = Solution()

assert (solution.isValid("()") == True)
assert (solution.isValid("()[]{}") == True)
assert (solution.isValid("(]") == False)
assert (solution.isValid("([)]") == False)
assert (solution.isValid("{[]}") == True)
assert (solution.isValid("[") == False)
assert (solution.isValid("((") == False)
assert (solution.isValid("){") == False)
