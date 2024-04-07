#Encode and Decode Strings
class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        # write your code here
        key = ''
        currentLength = 0
        for string in strs:
            key += str(currentLength + len(string)) + ';'
            currentLength += len(string)
        return key + 'X' + ''.join(strs)
    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    def decode(self, str):
        # write your code here
        strbreak = str.find('X')
        key = str[:strbreak]
        keyList = key.split(';')
        text = str[strbreak + 1:]
        
        decodedList = []
        prev = 0
        for i in keyList:
            if i != '':
                decodedList.append(text[prev:int(i)])
                prev = int(i)
        return decodedList
    
class SolutionNeet:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        res = ''
        for s in strs:
            res += str(len(s)) + '#' + s
        return res
    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    def decode(self, str):
        res, i = [], 0

        while i < len(str):
            j = i
            while str[j] != '#':
                j += 1
            length = int(str[i:j])
            res.append(str[j + 1: j + 1 + length])
            i = j + 1 + length
        return res




sol = SolutionNeet()
encoded = sol.encode(["lint","code","love","you"])
print(encoded)
print(sol.decode(encoded))
