
import numpy as np

correct = [[1,2,9],
           [2,3,1],
           [3,1,2]]

incorrect = [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,4]]

incorrect2 = [[1,2,3,4],
             [2,3,1,4],
             [4,1,2,3],
             [3,4,1,2]]

incorrect3 = [[1,2,3,4,5],
              [2,3,1,5,6],
              [4,5,2,1,3],
              [3,4,5,2,1],
              [5,6,4,3,2]]



def check_sudoku(inp):
    for a in inp:
        for b in a:
            p = a.count(b)
            if p == 2:
                return ("its not a sudoku")
                break
            if isinstance(b,int)==False:
                return ("its not a sudoku")
                break
            if b % 1 !=0:
                return ("its not a sudoku")
                break
    trans = np.transpose(inp)
    trans = trans.tolist()
    counter = 0
    for a in trans:
        for b in a:
            p = a.count(b)
            if p == 2:
                return ("its not a sudoku")
                break
            counter +=1
            if counter + 1 == len(inp)*len(inp):
                return ("This is correct")
                break


incorrect4 = [['a','b','c'],
              ['b','c','a'],
              ['c','a','b']]

incorrect5 = [ [1, 1.5],
               [1.5, 1]]

print check_sudoku(correct)
#>>> False

