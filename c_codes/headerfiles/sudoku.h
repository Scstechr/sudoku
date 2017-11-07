#ifndef SUDOKU_H
#define SUDOKU_H

void InitSudoku(Sudoku *sudoku){
  for(int hor=0;hor<9;hor++){
    for(int ver=0;ver<9;ver++){
      sudoku[hor].row[ver].numeral=0;
      sudoku[hor].row[ver].reveal=0;
      for(int opt=0;opt<9;opt++) {
        sudoku[hor].row[ver].option[opt]=0;
      }
    }
  }
};

void InsertSudoku(Sudoku *sudoku, int colnum, int rownum, int num){
  sudoku[colnum].row[rownum].numeral = num;
  sudoku[colnum].row[rownum].reveal = 1;
}

void PrintSudoku(Sudoku *sudoku){
  printf("\n"); int temp;
  for(int hor=0;hor<9;hor++){
    for(int ver=0;ver<9;ver++){
      temp = sudoku[hor].row[ver].numeral;
      if(temp!=0) printf("%d",temp);
      else printf(" ");
      if(ver%3==2&&ver!=8) printf("|");
    }
    if(hor%3==2&&hor!=8){
      printf("\n-");
      for(int line=0;line<10;line++) {
        if(line%4==2) printf("+");
        else printf("-");
      }
    }
    printf("\n");
  }
};

void RefreshSudoku(Sudoku *sudoku){
  int temp;
  for(int hor=0;hor<9;hor++){
    for(int ver=0;ver<9;ver++){
      temp = sudoku[hor].row[ver].numeral;
      if(temp!=0) sudoku[hor].row[ver].reveal=1;
    }
  }
};

#endif