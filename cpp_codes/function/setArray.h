#ifndef DEFINE_H
#define DEFINE_H
#include "../define.h"
#endif

#ifndef DELETENUMBER_H
#define DELETENUMBER_H
#include "./deleteNumber.h"
#endif

void setArray(int i, int j, int data){

  for(int k=0;k<ArraySize;k++){
    //同じ行のセルに対して
    if((int)x[i][k].size()>1){
      for(std::list<int>::iterator itr = x[i][k].begin(); itr != x[i][k].end(); itr++){
        if(*itr==data){
          x[i][k].erase(itr);
          break;
        }
      }
    }

    //同じ列のセルに対して
    if((int)x[k][j].size()>1){
      for(std::list<int>::iterator itr = x[k][j].begin(); itr != x[k][j].end(); itr++){
        if(*itr==data){
          x[k][j].erase(itr);
          break;
        }
      }
    }
  }

  //同じグループのセルに対して
  int s=0,t=0; //関数のトリガー
  if(0<=i && i<=2){
    if(0<=j && j<=2){ //左上
      s = 1;
      t = 1;
    }else if(3<=j && j<=5){ //中上
      s = 2;
      t = 1;
    }else if(6<=j && j<=8){ //右上
      s = 3;
      t = 1;
    }
  }else if(3<=i && i<=5){
    if(0<=j && j<=2){ //左中
      s = 1;
      t = 2;
    }else if(3<=j && j<=5){ //中々
      s = 2;
      t = 2;
    }else if(6<=j && j<=8){ //右中
      s = 3;
      t = 2;
    }
  }else if(6<=i && i<=8){
    if(0<=j && j<=2){ //左下
      s = 1;
      t = 3;
    }else if(3<=j && j<=5){ //中下
      s = 2;
      t = 3;
    }else if(6<=j && j<=8){ //右下
      s = 3;
      t = 3;
    }
  }
  if(s==0 || t==0){
    printf("error\n");
    exit(1);
  }else{
    deleteNumber(s,t,data);
  }
}
