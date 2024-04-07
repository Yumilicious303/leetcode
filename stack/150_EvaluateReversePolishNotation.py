#Evaluate Reverse Polish Notation
def evalRPN(tokens):
    stack = []
    expressions = {'+', '-', '*', '/'}
    for t in tokens:
        if t in expressions:
            two = stack.pop()
            one = stack.pop()
            stack.append(int(eval(str(one) + str(t) + str(two))))
        else:
            stack.append(int(t))
    return stack[0]

def evalRPNNeet(tokens):
    stack = []
    for c in tokens:
        if c == '+':
            stack.append(stack.pop() + stack.pop())
        elif c == '-':
            a, b = stack.pop(), stack.pop()
            stack.append(b - a)
        elif c == '*':
            stack.append(stack.pop() * stack.pop())
        elif c == '/':
            a, b = stack.pop(), stack.pop()
            stack.append(int(b / a))
        else:
            stack.append(int(c))
    return stack[0]

print(evalRPNNeet(["2","1","+","3","*"]))
print(evalRPNNeet(["4","13","5","/","+"]))
print(evalRPNNeet(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
