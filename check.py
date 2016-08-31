a = [[1,2,3],
     [6,7,8],
     [3,4,5]]

def trans(a):
    for lis in a:
        for item in list:

    row= []
    col = []
    rows = len(a) - 1
    i = 0
    j = 0
    while i < len(a):
        while j < len(a):
            col = col + [a[j][i]]
            j += 1
        row.append(col)
        col=[]
        j = 0
        i += 1
    return row

print trans(a)

