import sys
import os
from sudoku import *

def main():
    # changing directry and question based on input
    path = sys.argv[1]
    filename = f'{sys.argv[1]}/{sys.argv[2]}'
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