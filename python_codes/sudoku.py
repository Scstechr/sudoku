import sys
import os

def main():
    # changing directry and question based on input
    path = sys.argv[1]
    filename = '{}/{}'.format(sys.argv[1],sys.argv[2])
    os.chdir(path)

    #input
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
        for line in f:
            if row_count == 0:
                offset = 0
            elif row_count > 0 and row_count%3 == 0:
                offset += 1
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

if __name__ == '__main__':
    main()