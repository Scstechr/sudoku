#include "./headerfiles/header.h"

int main(){
  Sudoku sudoku[9];

  InitSudoku(sudoku);
  QueSudoku(sudoku);
  PrintSudoku(sudoku);

  return 0;
}