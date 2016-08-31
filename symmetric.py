import numpy as np

def symmetric(inp):
    a = len(inp) - 1
    i = 0
    j = 0
    a = 0
    b = 0
    if len(inp) != len(inp[0]):
        return False

    if inp[0][0] != inp[a][a]:
        return False

    trans = np.transpose(inp)
    trans = trans.tolist()

    if trans == inp:
        return True
    else:
        return False

print symmetric([["cat", "dog", "fish"],
                ["dog", "dog", "dog"],
                ["fish","cat","cat"]])
#>>> False
#>>> False
