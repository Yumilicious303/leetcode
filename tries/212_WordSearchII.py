#Word Search II
class TrieNode:
    def __init__(self):
        self.next = {}
        self.endOfWord = False
    def __repr__(self) -> str:
        return str(list(self.next.keys()))



def findWords(board, words):
    ROWS, COLS = len(board), len(board[0])
    root = TrieNode()
    visited = set()
    res = []
    def dfs(node, row, col):
        if (row >= ROWS or
            row < 0 or
            col >= COLS or
            col < 0 or
            (row, col) in visited):
            return
        
        letter = board[row][col]
        if letter not in node.next:
            node.next[letter] = TrieNode()
        visited.add((row, col))

        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        for r, c in directions:
            dfs(node.next[letter], row + r, col + c)
        visited.remove((row, col))
    
    def wordFound(word):
        cur = root
        for i in range(len(word)):
            if word[i] in cur.next:
                cur = cur.next[word[i]]
            else:
                return
        res.append(word)


    for row in range(ROWS):
        for col in range(COLS):
            dfs(root, row, col) 
    
    for word in words:
        wordFound(word)
    
    return res


board1 = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words1 = ["oath","pea","eat","rain"]

board2 = [['a', 'c'], ['p', 'e']]
words2 = ['app', 'ape', 'ace']
print(findWords(board1, words1))
print(findWords(board2, words2))


class TrieNodeNeet:
    def __init__(self):
        self.children = {}
        self.isWord = False

    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True


class SolutionNeet:
    def findWords(self, board, words):
        root = TrieNode()
        for w in words:
            root.addWord(w)

        ROWS, COLS = len(board), len(board[0])
        res, visit = set(), set()

        def dfs(r, c, node, word):
            if (r not in range(ROWS) 
                or c not in range(COLS)
                or board[r][c] not in node.children
                or (r, c) in visit):
                return

            visit.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                node.isWord = False
                res.add(word)

            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
            visit.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")

        return list(res)