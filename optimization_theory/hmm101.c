#include <stdio.h>
#include <stdlib.h> 
#include <math.h>

#define RAND_SEED 2014628

double nrnd();

void generate_x (){

}

void generate_y (){

}

void compute_xmap (){

}

void show_resuls(){

}

void test_nrnd(){

    int i;

    for (i=0; i<10; i++){
        printf("%.8lf\n", nrnd());
    }

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

/* 擬似乱数が本当に生成されているか，チェック  */
    test_nrnd();


/* 問題を作る（200 個のデータ生成） */
    generate_x ();
    generate_y ();
    
/* 復元する */
    compute_xmap (); 
    
/* 結果を表示する */
    show_resuls();



    
    return 0;
}
