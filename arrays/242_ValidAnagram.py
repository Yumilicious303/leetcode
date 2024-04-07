#Valid Anagram
def isAnagram(s, t):
    dict = {}
    for char in s:
        if char in dict:
            dict[char][0] += 1
        else:
            dict[char] = [1, 0]
    for char in t:
        if char in dict:
            dict[char][1] += 1
        else:
            return False
    
    for count in dict.values():
        if count[0] != count[1]:
            return False
    return True


print(isAnagram('anagram', "nagaram"))
print(isAnagram('rat', "car"))
print(isAnagram('a', 'ab'))