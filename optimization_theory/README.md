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
  [hmm002.c](https://github.com/date333cs/optimization/blob/master/hmm002.c) 

+ 正規分布にしたがう擬似乱数の生成:  
  [hmm101.c](https://github.com/date333cs/optimization/blob/master/hmm101.c) 

+ [hmm102.c](https://github.com/date333cs/optimization/blob/master/hmm102.c) 
+ [hmm103.c](https://github.com/date333cs/optimization/blob/master/hmm103.c) 
+ [hmm105.c](https://github.com/date333cs/optimization/blob/master/hmm105.c) 
+ [hmm201.c](https://github.com/date333cs/optimization/blob/master/hmm201.c) 


### gnuplot ###
+ [gp301](https://github.com/date333cs/optimization/blob/master/gp301), [gp301eps](https://github.com/date333cs/optimization/blob/master/gp301eps),   [gp301png](https://github.com/date333cs/optimization/blob/master/gp301png)

  - eps ファイルを作成するときは最初の行の # をはずす．

### gnuplot を使って結果を表示 ###

    % gcc hmm201.c -lm
    % a.out > results.dat
    % gnuplot gp301 -persist
    % gnuplot gp301eps
    

### python ###

+ [hmm101.py](https://github.com/date333cs/optimization/blob/master/hmm101.py) 
+ [hmm102.py](https://github.com/date333cs/optimization/blob/master/hmm102.py)
+ [hmm103.py](https://github.com/date333cs/optimization/blob/master/hmm103.py)
+ [hmm104.py](https://github.com/date333cs/optimization/blob/master/hmm104.py)
