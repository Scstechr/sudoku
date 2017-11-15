import sys
import os

def UpdateOffset(num, offset):
    if num == 0:
        offset = 0
    elif num > 0 and num%3 == 0:
        offset += 1
    return offset

def PrintSudoku(sudoku):
    offset = 0
    for line in sudoku:
        str1 = ' '.join(line[0:3])
        str2 = ' '.join(line[3:6])
        str3 = ' '.join(line[6:])
        print(f'{str1}|{str2}|{str3}')
        if offset == 2 and sudoku.index(line)!=8:
            print('-----+-----+-----')
            offset = 0
        else:
            offset += 1

def InputSudoku(filename):
    rlist = [] # returning list
    with open(filename, 'r') as f:
        sudoku = []

        check = {}      # empty
        check['r'] = [] # rows
        check['c'] = [] # columns
        check['s'] = [] # squares
        for i in range(9):
            column = set()
            square = set()
            check['c'].append(column)
            check['s'].append(square)
        row_count = 0
        offset = 0
        for line in f:
            offset = UpdateOffset(row_count, offset)
            string = line.split()
            row = set()
            for num in string:
                if num != '0':
                    row.update(num)
                    check['c'][string.index(num)].update(num)
                    if string.index(num) < 3:
                        check['s'][3*offset].update(num)
                    elif string.index(num) < 6:
                        check['s'][3*offset+1].update(num)
                    else:
                        check['s'][3*offset+2].update(num)
            check['r'].append(row)
            sudoku.append(string)
            row_count += 1

    rlist.append(sudoku)
    rlist.append(check)
    return rlist

def CheckSudoku(sudoku, check):
    wlist = [] # working list
    full = set()
    for num in range(9):
        string = f'{num+1}'
        full.update(string)
    offset = 0
    for lst in sudoku:
        col_count = 0
        offset = UpdateOffset(sudoku.index(lst), offset)
        for num in lst:
            if num == '0':
                eset = check['r'][sudoku.index(lst)].union(check['c'][col_count])
                if col_count < 3:
                    eset = eset.union(check['s'][3*offset])
                elif col_count < 6:
                    eset = eset.union(check['s'][3*offset+1])
                else:
                    eset = eset.union(check['s'][3*offset+2])
                eset = full.difference(eset)
                if len(eset) == 1:
                    string = repr(eset)[2:-2]
                    sudoku[sudoku.index(lst)][col_count] = string
                    check['r'][sudoku.index(lst)].update(string)
                    check['c'][col_count].update(string)
                    if col_count < 3:
                        check['s'][3*offset].update(string)
                    elif col_count < 6:
                        check['s'][3*offset+1].update(string)
                    else:
                        check['s'][3*offset+2].update(string)
                else:
                    wlist.append('a')
            col_count += 1
    return len(wlist)

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