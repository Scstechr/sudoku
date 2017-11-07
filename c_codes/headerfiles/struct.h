#ifndef STRUCT_H
#define STRUCT_H

typedef struct{
  int numeral;     //Actual Numeral
  int option[9];   //options: numerals that could fit in.
  int reveal;      //0:unrevealed 1:revealed
} Grid;

typedef struct{
  Grid row[9];
} Sudoku;

typedef struct{
  //storing values
  int inum;
  double dnum;
  //indices
  int startpoint;
  int next;
  int prev;
  //parameters
  int size;
} Fstack;

#endif