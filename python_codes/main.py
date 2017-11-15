import sys
import os
from sudoku import *

def main():
    # changing directry and question based on input
    path = sys.argv[1]
    name = sys.argv[2]
    level = name[name.find('.')-1:name.find('.')]
    filename = f'../qs/level{level}/{name}'
    os.chdir(path)

    #input
    sudoku = InputSudoku(filename)
    check = sudoku.pop()
    sudoku = sudoku.pop()
    previous = 81
    while(1):
        present = CheckSudoku(sudoku, check)
        if present == 0 or present == previous:
            PrintSudoku(sudoku)
            if(present!=0):
                 print(present)
            break
        else:
            previous = present


if __name__ == '__main__':
    main()