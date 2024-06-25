#Word Ladder II
from collections import defaultdict
from collections import deque
def findLadders(beginWord, endWord, wordList):
    wordList.append(beginWord)

    patterns = defaultdict(list)

    for word in wordList:
        for i, c in enumerate(word):
            pattern = word[:i] + '_' + word[i + 1:]
            patterns[pattern].append(word)

    visited = set()
    childToParent = defaultdict(list)
    q = deque([beginWord])
    while q:
        for i in range(len(q)):
            word = q.popleft()
            if word not in visited:
                visited.add(word)
                for i, c in enumerate(word):
                    pattern = word[:i] + '_' + word[i + 1:]
                    for neighbor in patterns[pattern]:
                        q.append(neighbor)
                        childToParent[neighbor].append(word)
        if endWord in visited:
            
    




print(findLadders(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]))
