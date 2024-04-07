#Valid Paranthesis String
def checkValidString(s):
    def dfs(j, openLeft):
        for i in range(j, len(s)):
            if (i, openLeft) in memo:
                return memo[(i, openLeft)]
            
            if s[i] == ')':
                if openLeft: openLeft -= 1
                else: 
                    memo[(i, openLeft)] = False
                    return False
            elif s[i] == '(': 
                openLeft += 1
            else:
                if dfs(i + 1, openLeft): return True #blank
                if dfs(i + 1, openLeft + 1): return True #left paranthesis
                if openLeft and dfs(i + 1, openLeft - 1): return True  #right paranthesis

                memo[(i, openLeft)] = False
                return False
            
        if openLeft: return False
        else: return True
    memo = {}
    return dfs(0, 0)

def checkValidStringNeetDP(s):
    dp = {}  # key=(i, leftCount) -> isValid
    def dfs(i, openLeft):
        if i == len(s) or openLeft < 0:
            return openLeft == 0
        if (i, openLeft) in dp:
            return dp[(i, openLeft)]
        if s[i] == "(":
            dp[(i, openLeft)] = dfs(i + 1, openLeft + 1)
        elif s[i] == ")":
            dp[(i, openLeft)] = dfs(i + 1, openLeft - 1)
        else:
            dp[(i, openLeft)] = (
                dfs(i + 1, openLeft + 1) or dfs(i + 1, openLeft - 1) or dfs(i + 1, openLeft)
            )
        return dp[(i, openLeft)]
    return dfs(0, 0)

def checkValidStringNeetGreedy(s):
    leftMin, leftMax = 0, 0
    for c in s:
        if c == "(":
            leftMin, leftMax = leftMin + 1, leftMax + 1
        elif c == ")":
            leftMin, leftMax = leftMin - 1, leftMax - 1
        else:
            leftMin, leftMax = leftMin - 1, leftMax + 1
        if leftMax < 0:
            return False
        if leftMin < 0:  # required because -> s = ( * ) (
            leftMin = 0
    return leftMin == 0
    

print(checkValidStringNeetDP('*('))
print(checkValidStringNeetDP('(*))'))
print(checkValidStringNeetDP('()*(())'))
print(checkValidStringNeetDP("()*()(()(*()(((())()()())*))()*()(*)(((*))(())(())((*()*(()(())()*(((*(**))((())*)(((()()))(())()))"))
print(checkValidStringNeetDP("(()(())()())*((()(())))*()(*)()()(*((()((*(*))))()*()(()((()(*((()))*(((())(())))*))(()*))(()*)"))

