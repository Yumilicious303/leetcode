#Valid Parantheses
def isValid(s):
    opening = {'{', '[', '(' }
    closing = {
        '}': '{',
        ']': '[',
        ')': '('
    }
    stack = []
    for c in s:
        if c in opening:
            stack.append(c)
        else:
            if stack and closing[c] == stack[-1]:
                stack.pop()
            else:
                return False
    if stack:
        return False
    else:
        return True



def isValidNeet(s):
    closeToOpen = {
        '}': '{',
        ']': '[',
        ')': '('
    }
    stack = []
    for c in s:
        if c in closeToOpen:
            if stack and stack[-1] == closeToOpen[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)
    if stack:
        return False
    else:
        return True
