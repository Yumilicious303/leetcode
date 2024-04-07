def dailyTemperatures(temperatures):
    res = [0] * len(temperatures)
    stack = []

    for i in range(len(temperatures)):
        while stack and temperatures[i] > stack[-1][0]:
            prev_temp, prev_index = stack.pop()
            res[prev_index] = i - prev_index
        stack.append([temperatures[i], i])
    return res


print(dailyTemperatures([73,74,75,71,69,72,76,73]))
print(dailyTemperatures([30,40,50,60]))
