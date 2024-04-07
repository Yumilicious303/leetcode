#Daily Temperatures
def dailyTemperatures(temperatures):
    res = [0 for i in range(len(temperatures))]
    stack = []
    for index, temp in enumerate(temperatures):
        if len(stack) == 0:
            stack.append([index, temp])
        else:
            while stack and temp > stack[-1][1]:
                res[stack[-1][0]] = index - stack[-1][0]
                stack.pop()
            stack.append([index, temp])
    return res

def dailyTemperatures2(temperatures):
    res = [0 for i in range(len(temperatures))]
    stack = []
    for index in range(len(temperatures)):
        if len(stack) == 0:
            stack.append(index)
        else:
            while stack and temperatures[index] > temperatures[stack[-1]]:
                res[stack[-1]] = index - stack[-1]
                stack.pop()
            stack.append(index)
    return res

def dailyTemperaturesNeet(temperatures):
    res = [0] * len(temperatures)
    stack = []

    for i, temp in enumerate(temperatures):
        while stack and temp > stack[-1][0]:
            stack_temp, stack_index = stack.pop()
            res[stack_index] = i - stack_index
        stack.append([temp, i])
    return res


print(dailyTemperaturesNeet([73,74,75,71,69,72,76,73]))

