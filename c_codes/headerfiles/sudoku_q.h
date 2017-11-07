#ifndef SUDOKU_Q_H
#define SUDOKU_Q_H

void QueSudoku(Sudoku *sudoku){
  int temp0[9] = {0, 0, 0, 0, 0, 0, 0, 0, 0};
  int temp1[9] = {0, 0, 0, 0, 0, 0, 0, 2, 7};
  int temp2[9] = {4, 0, 0, 6, 0, 8, 0, 0, 0};
  int temp3[9] = {0, 7, 1, 0, 0, 0, 3, 0, 0};
  int temp4[9] = {2, 3, 8, 5, 0, 6, 4, 1, 9};
  int temp5[9] = {9, 6, 4, 1, 0, 0, 7, 5, 0};
  int temp6[9] = {3, 9, 5, 0, 2, 7, 8, 0, 0};
  int temp7[9] = {1, 8, 2, 0, 6, 0, 9, 7, 4};
  int temp8[9] = {0, 4, 6, 8, 1, 9, 2, 0, 5};
  for(int j=0; j<9; j++){
    InsertSudoku(sudoku, 0, j, temp0[j]);
    InsertSudoku(sudoku, 1, j, temp1[j]);
    InsertSudoku(sudoku, 2, j, temp2[j]);
    InsertSudoku(sudoku, 3, j, temp3[j]);
    InsertSudoku(sudoku, 4, j, temp4[j]);
    InsertSudoku(sudoku, 5, j, temp5[j]);
    InsertSudoku(sudoku, 6, j, temp6[j]);
    InsertSudoku(sudoku, 7, j, temp7[j]);
    InsertSudoku(sudoku, 8, j, temp8[j]);
  }
}

#endif