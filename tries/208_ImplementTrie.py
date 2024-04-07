#Implement Trie
class TrieNode:
    def __init__(self, letter, is_last_letter=False):
        self.letter = letter
        self.next_letters = {}
        self.is_last_letter = is_last_letter

    def __repr__(self):
        return self.letter


class Trie(object):
    def __init__(self):
        self.root = TrieNode(None)

    def insert(self, word):
        def dfs(node, word_segment):
            if len(word_segment) == 0:
                node.is_last_letter = True
                return
            first_letter = word_segment[0]
            if first_letter not in node.next_letters:
                node.next_letters[first_letter] = TrieNode(first_letter)
            dfs(node.next_letters[first_letter], word_segment[1:]) 

        dfs(self.root, word)



    def search(self, word):
        def dfs(node, word_segment):
            if len(word_segment) == 0:
                if node.is_last_letter: return True
                else: return False
            if word_segment[0] not in node.next_letters:
                return False
            
            return dfs(node.next_letters[word_segment[0]], word_segment[1:])
        
        return dfs(self.root, word)
           


    def startsWith(self, prefix):
        def dfs(node, prefix_segment):
            if len(prefix_segment) == 0: return True

            if prefix_segment[0] not in node.next_letters:
                return False
            
            return dfs(node.next_letters[prefix_segment[0]], prefix_segment[1:])
        
        return dfs(self.root, prefix)



class TrieNodeNeet:
    def __init__(self):
        self.children = {}
        self.endOfWord = False


class TrieNeet:
    def __init__(self):
        self.root = TrieNodeNeet()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNodeNeet()
            cur = cur.children[c]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        cur = self.root

        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.endOfWord

    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True

trie = TrieNeet()
trie.insert('apple')
print(trie.search('apple'))
print(trie.search('app'))
print(trie.startsWith('app'))
trie.insert('app')
print(trie.search('app'))