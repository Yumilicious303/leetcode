#Word Ladder
from collections import defaultdict
from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        #build graph
        if endWord not in wordList: return 0

        graph = defaultdict(list)
        for word in wordList:
            if self.offByOne(beginWord, word): 
                graph[beginWord].append(word)
        for i in range(len(wordList)):
            for j in range(i + 1, len(wordList)):
                if self.offByOne(wordList[i], wordList[j]):
                    graph[wordList[i]].append(wordList[j])
                    graph[wordList[j]].append(wordList[i])
        
        
        q = deque([beginWord])
        visited = set()
        res = 1
        while q:
            for i in range(len(q)):
                cur = q.popleft()
                if cur == endWord:
                    return res
                visited.add(cur)
                for adjWord in graph[cur]:
                    if adjWord not in visited:
                        q.append(adjWord)
            res += 1
        return 0

    def offByOne(self, word1, word2):
        differences = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                differences += 1
            if differences > 1:
                return False
        if differences == 0: return False
        return True
    

class SolutionNeet:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        if endWord not in wordList:
            return 0

        nei = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1 :]
                nei[pattern].append(word)

        visit = set([beginWord])
        q = deque([beginWord])
        res = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1 :]
                    for neiWord in nei[pattern]:
                        if neiWord not in visit:
                            visit.add(neiWord)
                            q.append(neiWord)
            res += 1
        return 0

sol = SolutionNeet()


print(sol.ladderLength(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]))
