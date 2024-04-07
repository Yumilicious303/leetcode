#Multiply Strings
def multiply(num1, num2):
    def convertToInt(num):
        i = 1
        res = 0
        for d in range(len(num) - 1, - 1, -1):
            res += (ord(num[d]) - ord('0')) * i
            i *= 10
        return res

        
    
    num1 = convertToInt(num1)
    num2 = convertToInt(num2)
    return num1 * num2

print(multiply('123', '456'))
print(multiply('2', '3'))