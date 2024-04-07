#Decode Ways
def numDecodings(s):
    possible_digits = set()
    for x in range(1, 26 + 1):
        possible_digits.add(str(x))
    memo = {}
    
    def dfs(i, j):
        if j in memo:
            return memo[j]
        if i >= len(s) or j > len(s):
            return 0
        if s[i:j] not in possible_digits:
            return 0
        
        if j == len(s):
            return 1
        
        nextonedigit = dfs(j, j + 1)
        nexttwodigits = dfs(j, j + 2)

        memo[j] = nextonedigit + nexttwodigits

        return nextonedigit + nexttwodigits

    return dfs(0,1) + dfs(0,2)

def numDecodings2(s):
    possible_digits = set()
    for x in range(1, 26 + 1):
        possible_digits.add(str(x))
    memo = {}
    
    def dfs(i, j):
        if j in memo:
            return memo[s[i:]]
        if i >= len(s) or j > len(s):
            return 0
        if s[i:j] not in possible_digits:
            return 0
        
        if j == len(s):
            return 1
        
        nextonedigit = dfs(j, j + 1)
        nexttwodigits = dfs(j, j + 2)

        memo[s[i:]] = nextonedigit + nexttwodigits

        return nextonedigit + nexttwodigits

    answer = dfs(0,1) + dfs(0,2)
    return answer

def numDecodings3(s):
    possible_digits = set()
    for x in range(1, 26 + 1):
        possible_digits.add(str(x))
    memo = {}
    
    def dfs(s_curr):
        if s_curr in memo:
            return memo[s_curr]
        if len(s_curr) == 1:
            if s_curr in possible_digits: return 1
            else: return 0
        if s_curr == '':
            return 1

        one, two = 0, 0
        if s_curr[:1] in possible_digits:
            one = dfs(s_curr[1:])
        if s_curr[:2] in possible_digits:
            two = dfs(s_curr[2:])
        memo[s_curr] = one + two
        return memo[s_curr]
        
        
        

    answer = dfs(s)
    return answer

class SolutionLeet:
    def numDecodings(self, s: str) -> int:
        self.memo = {}
        return self.helper(s)

    def helper(self, s: str) -> int:
        if len(s) == 0: return 1
        if s in self.memo: return self.memo[s]
        
        takeOne = takeTwo = 0
        
        if int(s[:1]) >= 1 and int(s[:1]) <= 9:
            takeOne = self.helper(s[1:])
        
        if int(s[:2]) >= 10 and int(s[:2]) <= 26: 
            takeTwo = self.helper(s[2:])
        
        self.memo[s] = takeOne + takeTwo
        
        return self.memo[s]


def numDecodingsLeet(s):
    def dfs(s_curr):
        if len(s_curr) == 0: return 1
        if s_curr in memo: return memo[s_curr]
        
        takeOne = takeTwo = 0
        
        if int(s_curr[:1]) >= 1 and int(s_curr[:1]) <= 9:
            takeOne = dfs(s_curr[1:])
        
        if int(s_curr[:2]) >= 10 and int(s_curr[:2]) <= 26: 
            takeTwo = dfs(s_curr[2:])
        
        memo[s_curr] = takeOne + takeTwo
        
        return memo[s_curr]
    memo = {}
    return dfs(s)

class Solution:
    def numDecodings(self, s):
        if not s or s[0] == '0':
            return 0

        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 1):
            one_digit = int(s[i - 1])
            two_digits = int(s[i - 2:i])

            if one_digit != 0:
                dp[i] += dp[i - 1]

            if 10 <= two_digits <= 26:
                dp[i] += dp[i - 2]

        return dp[n]

sol = Solution()
print(sol.numDecodings('12'))
#print(sol.numDecodings('226'))
#print(sol.numDecodings('206'))
#print(sol.numDecodings('06'))
#print(sol.numDecodings('111111111111111111111111111111111111111111111'))
#print(sol.numDecodings('123123'))

        