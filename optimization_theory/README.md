最適化理論 (Optimization Theory) 
============


動的計画法（隠れマルコフモデル）
------


- Start Small !!!
- 動いた時には感動する．


### C言語 ###
+ とりあえず日本語でコンピュータにさせたい作業を書く:  
  [hmm001.c](./hmm001.c) 

+ 空の関数を作る:  
  [hmm002.c](./hmm002.c) 

+ 正規分布にしたがう擬似乱数の生成:  
  [hmm101.c](./hmm101.c) 

+ [hmm102.c](./hmm102.c) 
+ [hmm103.c](./hmm103.c) 
+ [hmm105.c](./hmm105.c) 
+ [hmm201.c](./hmm201.c) 


### gnuplot ###
+ [gp301](./gp301), [gp301eps](./gp301eps), [gp301png](./gp301png)

  - eps ファイルを作成するときは最初の行の # をはずす．

### gnuplot を使って結果を表示 ###

    % gcc hmm201.c -lm
    % a.out > results.dat
    % gnuplot gp301 -persist
    % gnuplot gp301eps
    

### python ###

+ [hmm101.py](./hmm101.py) 
+ [hmm102.py](./hmm102.py)
+ [hmm103.py](./hmm103.py)
+ [hmm104.py](./hmm104.py)
