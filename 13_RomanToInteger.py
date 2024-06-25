#Roman to Integer
def romanToInt(s: str) -> int:
    symbol_to_value = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    res = 0

    for i in range(len(s)):
        cur_val = symbol_to_value[s[i]]
        prev_val = symbol_to_value[s[i - 1]] if i - 1 >= 0 else float('inf')
        if prev_val < cur_val:
            res -= prev_val
            res += (cur_val - prev_val)
        else:
            res += cur_val
    return res


def romanToIntNeet(s: str) -> int:
    roman = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    res = 0

    for i in range(len(s)):
        if i + 1 < len(s) and roman[s[i]] < roman[s[i + 1]]:
            res -= roman[s[i]]
        else:
            res += roman[s[i]]
    return res


print(romanToIntNeet('III'))
print(romanToIntNeet('LVIII'))
print(romanToIntNeet('MCMXCIV'))
            