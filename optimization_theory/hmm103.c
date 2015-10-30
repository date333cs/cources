#include <stdio.h>
#include <stdlib.h> 
#include <math.h>

#define RAND_SEED 2014628
#define N_DATA 200

#define P00 0.99 // 状態遷移確率の定義．P01 は 0→1 の遷移確率
#define P01 0.01
#define P10 0.03
#define P11 0.97

/* ここではグローバル変数を使う．コードを短くし，分かりやすくするため． */
int x[N_DATA]; // もともとの信号． 0 か 1
int xmap[N_DATA]; // 推定値． 0 か 1
double y[N_DATA];  // 観測データ


void generate_x (){

}

void generate_y (){

}

void compute_xmap (){

}

void show_resuls(){

}



/* 標準正規分布にしたがう擬似乱数の生成 */
double nrnd(){
    static int sw=0;
    static double r1,r2,s;
    
    if (sw==0){
        sw=1;
        do {
            r1=2.0*drand48()-1.0;
            r2=2.0*drand48()-1.0;
            s=r1*r1+r2*r2;
        } while (s>1.0 || s==0.0);
        s=sqrt(-2.0*log(s)/s);
        return(r1*s);
    }
    else {
        sw=0;
        return(r2*s);
    }
}


int main ( int argc , char * argv []){

    srand48(RAND_SEED); /* 擬似乱数の種を設定 */


/* 問題を作る（200 個のデータ生成） */
    generate_x ();
    generate_y ();
    
/* 復元する */
    compute_xmap (); 
    
/* 結果を表示する */
    show_resuls();



    
    return 0;
}
