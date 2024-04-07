#Plus One
def plusOne(digits):
    for i in range(len(digits)):
        digits[i] = str(digits[i])
    j = ''.join(digits)
    k = int(j) + 1
    l = str(k)
    m = []
    for c in l:
        m.append(c)
    for i in range(len(m)):
        m[i] = int(m[i])
    return m
    



print(plusOne([1,2,3]))