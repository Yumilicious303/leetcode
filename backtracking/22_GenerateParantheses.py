#Genergate Parenthesis
def generateParenthesis(n):
    res = []
    def backtrack(curr, openN, closedN):
        if openN == closedN == n:
            res.append(curr)
            return

        if openN < n:
            backtrack(curr + '(', openN + 1, closedN)
        if closedN < openN:
            backtrack(curr + ')', openN, closedN + 1)
    backtrack('', 0, 0)
    return res

def commentGenerateParenthesis(n):
        res = []
        def backtrack(open_n, closed_n, path):
            if open_n == closed_n == n:
                res.append(path)
                return

            if open_n < n:
                backtrack(open_n + 1, closed_n, path + "(")

            if closed_n < open_n:
                backtrack(open_n, closed_n + 1, path + ")")

        backtrack(0, 0, "")
        return res

def generateParenthesis(self, n: int) -> List[str]:
    result = []
    left = right = 0
    q = [(left, right, '')]
    while q:
        left, right, s = q.pop()
        if len(s) == 2 * n:
            result.append(s)
        if left < n:
            q.append((left + 1, right, s + '('))
        if right < left:
            q.append((left, right + 1, s + ')'))
    return result

print(generateParenthesis(3))
print(commentGenerateParenthesis(3))