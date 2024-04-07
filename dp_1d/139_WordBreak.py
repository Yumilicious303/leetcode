#Word Break
def wordBreak(s, wordDict):
    def dfs(target):
        if len(target) == 0:
            return True
        if target in memo:
            return memo[target]
        for word in wordDict:
            if target[:len(word)] == word:
                if dfs(target[len(word):]):
                    memo[target] = True
                    return True
        memo[target] = False
        return False
    memo = {}
    return dfs(s)

def wordBreakNeet(s, wordDict):
    dp = [False] * (len(s) + 1)
    dp[len(s)] = True

    for i in range(len(s) - 1, -1, -1):
        for w in wordDict:
            if (i + len(w)) <= len(s) and s[i:i + len(w)] == w:
                dp[i] = dp[i + len(w)]
            if dp[i]:
                break
    return dp[0]
        




print(wordBreakNeet("applepenapple", ["apple","pen"]))
print(wordBreakNeet("catsandog", ["cats","dog","sand","and","cat"]))
print(wordBreakNeet("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]))
