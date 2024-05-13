#Reorder Data Log Files
def reorderLogFiles(logs):
    def hasNum(input):
        return any(char.isdigit() for char in input)
    
    letter_log, digit_log = [], []
    for i, log in enumerate(logs):
        vals = log.split(' ')
        if hasNum(vals[1:]):
            digit_log.append(log)
        else: 
            letter_log.append([' '.join(vals[1:]), vals[0], i])
    res = []

    for log in sorted(letter_log):
        res.append(logs[log[2]])
    
    return res + digit_log

