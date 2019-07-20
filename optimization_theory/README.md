最適化理論 (Optimization Theory) 
============


動的計画法（隠れマルコフモデル）
------

- 動いた時には感動する．
- Start Small !!!  
  まずは，骨格を作る． そのあとで詳細を作る．

### C言語 ###
+ とりあえず日本語でコンピュータにさせたい作業を書く:  
  [hmm000.c](./hmm000.c) 
  [hmm001.c](./hmm001.c) 

+ 空の関数を作る:  
  [hmm002.c](./hmm002.c) 

+ 正規分布にしたがう擬似乱数の生成:  
  [hmm101.c](./hmm101.c) 

+ グローバル変数などを定義（いい方法ではない）:  
  [hmm102.c](./hmm102.c) 
  
+ 変数を定義:  
  [hmm103.c](./hmm103.c) 

+ 空関数の中身を少しづつ書いていく:  
  [hmm105.c](./hmm105.c) 

+ データ構造:  
  [hmm201.c](./hmm201.c) 

+ 空関数の中身を少しづつ書いていく:  
  [hmm202.c](./hmm202.c) 

+ テストコード（test20）:  
  [hmm211.c](./hmm211.c) 


### gnuplot ###
+ [gp301](./gp301), [gp301eps](./gp301eps), [gp301png](./gp301png)

  - eps ファイルを作成するときは最初の行の # をはずす．

### gnuplot を使って結果を表示 ###

    % gcc hmm201.c -lm
    % a.out > results.dat
    % gnuplot gp301 -persist
    % gnuplot gp301eps
    

### python ###

+ python で配列（リストとよばれている）を使うには：  
  [hmm101.py](./hmm101.py) 

+ クラスの作り方：  
  [hmm102.py](./hmm102.py)


+ matplotlib を使い結果を表示：  
  [hmm103.py](./hmm103.py)

+ pythonで2次元配列：  
  [hmm104.py](./hmm104.py)

+ テストコード（test20）:  
  [hmm211.py](./hmm211.py) 

+ pdf ファイルの作成:  
  [hmm212.py](./hmm212.py) 


### テスト用データ（yと xmap 20例）

+ [r20190702_20_test_cases](./r20190702_20_test_cases)


### LaTeX を使ったレポート作成
+ [sample190720report.tex](./sample190720report.tex)

