#Encode and Decode Strings
def encode(list1):
    x = ';:'.join(list1)
    print(x)
    return x
def decode(string1):
    x = string1.split(';:')
    print(x)



y = encode(['lint', 'code', 'love', 'you'])
decode(y)