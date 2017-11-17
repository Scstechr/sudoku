def UpdateOffset(num, offset):
    if num == 0:
        offset = 0
    elif num > 0 and num%3 == 0:
        offset += 1
    return offset

def CellPro(index, check, num, offset):
    rset = set()
    if index < 3:
        if num != 0:
            check['s'][3*offset].update(num)
        else:
            rset = check['s'][3*offset]
    elif index < 6:
        if num != 0:
            check['s'][3*offset+1].update(num)
        else:
            rset = check['s'][3*offset+1]
    else:
        if num != 0:
            check['s'][3*offset+2].update(num)
        else:
            rset = check['s'][3*offset+2]
    return rset

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
            check['c'].append(set())
            check['s'].append(set())
        row_count, offset = 0, 0
        for line in f:
            offset = UpdateOffset(row_count, offset)
            string = line.split()
            row = set()
            for num in string:
                if num != '0':
                    row.update(num)
                    check['c'][string.index(num)].update(num)
                    CellPro(string.index(num), check, num, offset)
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
                eset = eset.union(CellPro(col_count, check, 0, offset))
                # fill in here
                eset = full.difference(eset)
                if len(eset) == 1:
                    string = repr(eset)[2:-2]
                    sudoku[sudoku.index(lst)][col_count] = string
                    check['r'][sudoku.index(lst)].update(string)
                    check['c'][col_count].update(string)
                    CellPro(col_count, check, string, offset)
                else:
                    wlist.append('a')
            col_count += 1
    return len(wlist)
