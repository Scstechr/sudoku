#ifndef DEFINE_H
#define DEFINE_H
#include "../define.h"
#endif

/*
key1 : (0,1,2) = (左,中,右)
key2 : (0,1,2) = (上,中,下)
*/
void deleteNumber(int s, int t, int data){
  int x_start, x_end;
  int y_start, y_end;

  //s,tの順番に注意
  if(t==1){
    x_start = 0;
    x_end = 3;
  }else if(t==2){
    x_start = 3;
    x_end = 6;
  }else if(t==3){
    x_start = 6;
    x_end = 9;
  }
  if(s==1){
    y_start = 0;
    y_end = 3;
  }else if(s==2){
    y_start = 3;
    y_end = 6;
  }else if(s==3){
    y_start = 6;
    y_end = 9;
  }

  for(int i=x_start;i<x_end;i++){
    for(int j=y_start;j<y_end;j++){
      if((int)x[i][j].size()>1){
        for(std::list<int>::iterator itr = x[i][j].begin(); itr != x[i][j].end(); itr++){
          if(*itr==data){
            x[i][j].erase(itr);
            break;
          }
        }
      }
    }
  }
}
