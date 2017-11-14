#ifndef DEFINE_H
#define DEFINE_H
#include "./define.h"
#endif

#ifndef FUNCTION_H
#define FUNCTION_H
#include "./function.h"
#endif

int main(void){
  int checked[ArraySize][ArraySize] = {0}; // (0,1)

  //ファイル読み込み
  FILE *fp; //入出力用
  fp = fopen("./a.txt", "r");
  if(fp==NULL){
    printf("ファイルオープンエラー\n");
    exit(1);
  }
  for(int i=0;i<ArraySize;i++){
    for(int j=0;j<ArraySize;j++){
      int data;
      fscanf(fp,"%d",&data);
      if(data!=0){ //数字が与えられていれば, 代入
        x[i][j].push_back(data);
      }else{ //数字が与えられていなければ, [1-9]を代入
        for(int k=1;k<=ArraySize;k++){
          x[i][j].push_back(k);
        }
      }
    }
  }
  fclose(fp);

  //解く
  int stopper = 0;
  while(1){

    //数字が決定しているセルの捜索
    for(int i=0;i<ArraySize;i++){
      for(int j=0;j<ArraySize;j++){
        if((int)x[i][j].size()==1 && checked[i][j]==0){
          setArray(i, j, x[i][j].front());
          checked[i][j] = 1;
        }
      }
    }

    int counter = 0; //数字が決定したセルの個数
    for(int i=0;i<ArraySize;i++){
      for(int j=0;j<ArraySize;j++){
        if((int)x[i][j].size()==1){
          counter++;
        }
      }
    }

    //(セルが全て埋まる || 今回のサイクルで一つも埋まらない) で終了
    if(counter==ArraySize*ArraySize || counter==stopper){
      break;
    }
    stopper = counter;
  }

  //結果の出力
  for(int i=0;i<ArraySize;i++){
    if(i==3 || i==6){
      printf("------+------+-----\n");
    }
    for(int j=0;j<ArraySize;j++){
      if(j==3 || j==6){
        printf("|");
      }
      if((int)x[i][j].size()==1){
        printf("%d ",*(x[i][j].begin()));
      }else{
        printf("  ");
      }
    }
    printf("\n");
  }

  return 0;
}

