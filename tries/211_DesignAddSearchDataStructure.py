#Design Add Search Data Structure
class TrieNode():
    def __init__(self, letter= None, last_letter=False):
        self.letter = letter
        self.next_letter = {}
        self.last_letter = last_letter

    def __repr__(self) -> str:
        return self.letter

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        cur = self.root
        for i, c in enumerate(word):
            if c not in cur.next_letter:
                if i == len(word) - 1:
                    cur.next_letter[c] = TrieNode(c, True)
                cur.next_letter[c] = TrieNode(c)
            cur = cur.next_letter[c]
        

    def search(self, word):
        def dfs(i, cur):
            if i == len(word):
                if cur.last_letter: return True
                return False
            if word[i] != '.':
                if word[i + 1] in cur.next_letter:
                    if dfs(i + 1, cur.next_letter[word[i]]): return True
                else: return False
            else:
                for next in cur.next_letter:
                    if dfs(i + 1, cur.next_letter[next]): return True
            return False
                
        return dfs(0, self.root)
    
class TrieNodeNeet():
    def __init__(self):
        self.children = {}
        self.word = False


class WordDictionaryNeet:

    def __init__(self):
        self.root = TrieNodeNeet()

    def addWord(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNodeNeet()
            cur = cur.children[c]
        cur.word = True
        

    def search(self, word):
        def dfs(j, root):
            cur = root

            for i in range(j, len(word)):
                c = word[i]

                if c == '.':
                    for child in cur.children.values():
                        if dfs(i + 1, child): return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.word

                
        return dfs(0, self.root)



def testCase1():
    wordD = WordDictionary()
    wordD.addWord('bad')
    wordD.addWord('dad')
    print(f'{wordD.search('pad')}, Expected: False')
    print(f'{wordD.search('bad')}, Expected: True')
    print(f'{wordD.search('.ad')}, Expected: True')
    print(f'{wordD.search('b..')}, Expected: True')
    print(f'{wordD.search('badge')}, Expected: False')
    print(f'{wordD.search('bad..')}, Expected: False')



def testCase16():
    wordD = WordDictionaryNeet()
    wordD.addWord('at')
    wordD.addWord('and')
    wordD.addWord('an')
    wordD.addWord('add')
    print(wordD.search('a'))
    print(wordD.search('.at'))
    wordD.addWord('bat')
    print(wordD.search('.at'))
    print(wordD.search('an.'))
    print(wordD.search('a.d.'))

def testCase16():
    wordD = WordDictionaryNeet()
    wordD.addWord('at')
    wordD.addWord('and')
    wordD.addWord('an')
    wordD.addWord('add')
    print(f'{wordD.search('a')}, Expected: False')
    print(f'{wordD.search('.at')}, Expected: False')
    wordD.addWord('bat')
    print(f'{wordD.search('.at')}, Expected: True')
    print(f'{wordD.search('an.')}, Expected: True')
    print(f'{wordD.search('a.d.')}, Expected: False')
    print(f'{wordD.search('b.')}, Expected: False')
    print(f'{wordD.search('a.d')}, Expected: True')
    print(f'{wordD.search('.')}, Expected: False')

testCase16()



