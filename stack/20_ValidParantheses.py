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
    for char in s:
        if char in closeToOpen:
            if stack and stack[-1] == closeToOpen[char]: stack.pop()
            else: return False
        else: stack.append(char)
            
    return True if stack else False
