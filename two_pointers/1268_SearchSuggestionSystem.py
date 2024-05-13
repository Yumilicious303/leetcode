#Search Suggestion System
class TrieNode:
    def __init__(self, start = None, end = None, next = None):
        self.start = start
        self.end = end
        self.next = {}
    
    def __repr__(self) -> str:
        return f'({self.start}, {self.end})'

def suggestedProductsTrie(products, searchWord):
    #create Trie
    root = TrieNode()
    products.sort()
    for i, product in enumerate(products):
        cur = root
        for c in product:
            if c not in cur.next:
                cur.next[c] = TrieNode(i, i)
            else:
                cur.next[c].end = i
            cur = cur.next[c]

    
    res = []
    cur = root
    for i, c in enumerate(searchWord):
        cur_query = []
        if c not in cur.next:
            for j in range(i, len(searchWord)):
                res.append([])
            return res
        for j in range(cur.next[c].start, cur.next[c].end + 1):
            if len(cur_query) == 3:
                break
            cur_query.append(products[j])
        res.append(cur_query)
        cur = cur.next[c]
    return res

def suggestedProductsNeet(products, searchWord):
    products.sort()
    res = []
    l, r = 0, len(products) - 1
    for i in range(len(searchWord)):
        c = searchWord[i]

        while l <= r and (len(products[l]) <= i or c != products[l][i]):
            l += 1
        while l <= r and (len(products[r]) <= i or c != products[r][i]):
            r -= 1


        res.append([])
        remain = r - l + 1
        for j in range(min(3, remain)):
            res[-1].append(products[l + j])
    return res

def suggestedProducts(products, searchWord): #Prefered solution
    products.sort()
    res = []
    l, r = 0, len(products) - 1
    for i, c in enumerate(searchWord):
        while l <= r and (i >= len(products[l]) or c != products[l][i]):
            l += 1
        while l <= r and (i >= len(products[r]) or c != products[r][i]):
            r -= 1

        cur = []
        for j in range(l, r + 1):
            if len(cur) == 3: break
            cur.append(products[j])
        res.append(cur)
    return res





print(suggestedProducts2(["mobile","mouse","moneypot","monitor","mousepad", 'money'], 'mouse'))
print(suggestedProducts2(['havana'], 'havana'))