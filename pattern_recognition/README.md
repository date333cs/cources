Pattern_Recognition
===================

* 統計的機械学習

  - 第2章
    - 基本用語： 同時確率，周辺確率，条件付き確率．
    - 独立とは？ 無相関とは？ 
    - 正規分布とは？





* 2.2.2




        from math import *


  -  ↑これで log(7) とか exp(10), sin(0.5*pi) が動く．
  -  もしくは


    import math
    
    として，
    
    math.pi とか，math.log(20) 
    
    


* 2.2.3


          from numpy import eye, array, dot, matrix
          # 行列の掛け算
          A = matrix('1 2; 3 4')
          print A*A
          b = matrix('3;4')
          print A*b
          c = A*b; # 行末に ; をつけると値を表示しない
          d = c.transpose()
          
In [59]: A[0]
Out[59]: matrix([[1, 2]])

In [60]: A[1]
Out[60]: matrix([[3, 4]])

http://www.kamishima.net/mlmpyja/nbayes1/ndarray.html
