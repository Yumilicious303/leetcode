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


print(generateParenthesis(3))
print(commentGenerateParenthesis(3))