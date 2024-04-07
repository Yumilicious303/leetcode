#Backspace String Compare
def backspaceCompare(s, t):
    i, j = len(s) - 1, len(t) - 1
    sbackcount, tbackcount = 0, 0
    while i >= 0 and j >= 0:
        sletter = s[i]
        tletter = t[j]
        if sbackcount == 0 and tbackcount == 0: 
            if s[i] != '#' and t[j] != '#':
                if s[i] != t[j]:
                    return False
                i -= 1
                j -= 1
            else:
                if s[i] == '#':
                    sbackcount += 1
                    i -= 1
                if t[j] == '#':
                    tbackcount += 1
                    j -= 1
        else:
            if sbackcount >= 0:
                if s[i] != '#':
                    i -= 1
                    sbackcount -= 1
            if tbackcount >= 0:
                if t[j] != '#':
                    j -= 1
                    tbackcount -= 1
    if i == j:
        return True
    else:
        return False

def backspaceCompareNeet(s, t):
    def nextValidChar(str, index):
        backspace = 0
        while index >= 0:
            if backspace == 0 and str[index] != '#':
                break
            elif str[index] == '#':
                backspace += 1
            else:
                backspace -= 1
            index -= 1
        return index
    
    index_s, index_t = len(s) - 1, len(t) - 1
    while index_s >= 0 or index_t >= 0:
        index_s = nextValidChar(s, index_s)
        index_t = nextValidChar(t, index_t)

        char_s = s[index_s] if index_s >= 0 else ''
        char_t = t[index_t] if index_t >= 0 else ''
        if char_s != char_t:
            return False
        index_s -= 1
        index_t -= 1
    return True



print(backspaceCompareNeet("ab#c", "ad#c"))
print(backspaceCompareNeet("ab##", "c#d#"))
print(backspaceCompareNeet("a#c", "b"))
print(backspaceCompareNeet("xywrrmp", "xywrrmu#p"))
print(backspaceCompareNeet("gtc#uz#", "gtcm##uz#"))
        
