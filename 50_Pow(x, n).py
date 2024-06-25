#Pow(x, n)
def myPow(x, n):
    pow = 1
    if n >= 0:
        for i in range(n):
            pow = pow * x
    return pow if n >= 0 else 1 / pow

def myPowNeet(x, n):
    def dfs(n):
        if n == 0: return 1
        #if x == 0: return 0

        res = dfs(n // 2)
        res = res * res
        return x * res if n % 2 else res

    res = dfs(abs(n))
    return res if n >= 0 else 1 / res
#print(myPowNeet(2, -3))
#print(myPowNeet(2, 10))
#print(myPowNeet(2.1, 3))
print(myPowNeet(5, 0.5))