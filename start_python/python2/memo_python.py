# これは python のプログラムではありません．メモです．


# range とは

In [23]: range(3)
Out[23]: [0, 1, 2]


In [25]: for i in range(3):
   ....:     print i
   ....:     
0
1
2

In [28]: range(5)
Out[28]: [0, 1, 2, 3, 4]

In [29]: 

In [29]: range(2,6)
Out[29]: [2, 3, 4, 5]

In [30]: 

In [30]: range(6, 1, -2)
Out[30]: [6, 4, 2]



In [33]: help(range)

range(...)
    range([start,] stop[, step]) -> list of integers
    
    Return a list containing an arithmetic progression of integers.
    range(i, j) returns [i, i+1, i+2, ..., j-1]; start (!) defaults to 0.
    When step is given, it specifies the increment (or decrement).
    For example, range(4) returns [0, 1, 2, 3].  The end point is omitted!
    These are exactly the valid indices for a list of 4 elements.



# 配列のようなもの

a = [false]*5


In [1]: a = [True]*3

In [2]: a
Out[2]: [True, True, True]

In [3]: 


In [3]: [1.0]*5
Out[3]: [1.0, 1.0, 1.0, 1.0, 1.0]


In [4]: m = []

In [5]: m.append([0.0]*3)

In [6]: m
Out[6]: [[0.0, 0.0, 0.0]]


In [7]: m.append([0.0]*3)

In [9]: m
Out[9]: [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0]]

# m[0][0] から mm[1][2] でアクセスできる

In [16]: m[0][2]
Out[16]: 0.0


In [22]: help()

help> keywords

Here is a list of the Python keywords.  Enter any keyword to get more help.

and                 elif                if                  print
as                  else                import              raise
assert              except              in                  return
break               exec                is                  try
class               finally             lambda              while
continue            for                 not                 with
def                 from                or                  yield
del                 global              pass 





if a > 10:
    a = 10



if a > 10:
    print 'a greater than 10'
elif a < 5:
    print 'a less than 5'
else:
    print 'a is', a




x=1
while x < 10:
    x = x*2


X = [5, 4, 3, 2, 1]
for v in X:
    print v


# 関数の定義

def sum_diff(x, y):
    """ Sum and diff of two values.

    x is the first value
    y is the second value
    """
    return x+y, x-y

v1, v2 = sum_diff(7,4)
v3 = sum_diff(7,4)

print "v1 = ", v1



from numpy import eye, array, dot, matrix   # 必要なものだけ読み込む

import numpy as np
np.eye(3)

# 行列

M = array([[1, 2], [2, 1]])   # これは octave なら M = [1 2; 2 1];

# numpy.matrix というのがある． 2x2 行列しかダメ？
M = matrix('1 2; 2 1')

print M*M
print dot（M,M)   # octave なら disp(M.*M)

M = xeros((3,4))
M = ones((3,4))
M = eye(3)
M = diag([1, 2, 3])
M = diag(A)
M = random.rand(3,4)

array([[ 0.29505734,  0.47833473,  0.58943495,  0.29380726],
       [ 0.83434117,  0.49842588,  0.93928041,  0.61694716],
       [ 0.29492864,  0.71675351,  0.56580125,  0.06057518]])

一様乱数 [0, 1) を返す．


M = tile(A, (m,n))    # M - repmat(A, m, n);

# 行列 その２


In [1]: from numpy import *

In [2]: a = [ [4,-2,-1], [5, -3, -1], [2, -2, 1]]

In [3]: A = mat(a)   # mat は本来は matrix と略さず書くべき？ 略して書いても通じるのはなぜ？

In [4]: A
Out[4]: 
matrix([[ 4, -2, -1],
        [ 5, -3, -1],
        [ 2, -2,  1]])

In [5]: a
Out[5]: [[4, -2, -1], [5, -3, -1], [2, -2, 1]]


# 固有値・固有ベクトル
In [6]: linalg.eig(A)
Out[6]: 
(array([-1.,  2.,  1.]),
 matrix([[ -4.08248290e-01,  -7.07106781e-01,   5.77350269e-01],
        [ -8.16496581e-01,  -7.07106781e-01,   5.77350269e-01],
        [ -4.08248290e-01,  -4.27880387e-16,   5.77350269e-01]]))

# 転置
In [7]: A.T
Out[7]: 
matrix([[ 4,  5,  2],
        [-2, -3, -2],
        [-1, -1,  1]])


# 逆行列
In [8]: A.I
Out[8]: 
matrix([[ 2.5, -2. ,  0.5],
        [ 3.5, -3. ,  0.5],
        [ 2. , -2. ,  1. ]])

# A の行列式
In [9]: linalg.det(A)
Out[9]: -2.0000000000000009


# 

In [26]: A*A.I
Out[26]: 
matrix([[  1.00000000e+00,   8.88178420e-16,  -1.11022302e-16],
        [  1.33226763e-15,   1.00000000e+00,   5.55111512e-17],
        [  4.44089210e-16,   4.44089210e-16,   1.00000000e+00]])


In [30]: A
Out[30]: 
matrix([[ 4, -2, -1],
        [ 5, -3, -1],
        [ 2, -2,  1]])

In [31]: A[0]
Out[31]: matrix([[ 4, -2, -1]])

# A の３列目をとりだすには
In [40]: A.T[2]
Out[40]: matrix([[-1, -1,  1]])


# 行列の掛け算


In [54]: a = [ [1,-2], [3,4] ]

In [55]: A = mat(A)

In [56]: A
Out[56]: 
matrix([[ 1, -2],
        [ 3,  4]])


In [46]: x = [ [-1], [3] ]

In [47]: X = mat(x)

In [48]: X
Out[48]: 
matrix([[-1],
        [ 3]])


In [50]: A*X
Out[50]: 
matrix([[-7],
        [ 9]])
# 行列とベクトルの掛け算．ぜんぶ matrix として扱うと計算できるが，そうでないやり方が普通？






In [62]: help(matrix)


# いろいろな書き方がある？

In [68]: m = '1 2; 2 1'

In [69]: m
Out[69]: '1 2; 2 1'

In [70]: M = mat(m)

In [71]: M
Out[71]: 
matrix([[1, 2],
        [2, 1]])


# (1,1,1) という縦ベクトル
In [72]: x= mat('1; 1; 1')

In [73]: x
Out[73]: 
matrix([[1],
        [1],
        [1]])


# 長さ（ノルム）を1にする
In [74]: x / linalg.norm(x)
Out[74]: 
matrix([[ 0.57735027],
        [ 0.57735027],
        [ 0.57735027]])

In [78]: y = x / linalg.norm(x)

In [79]: linalg.norm(y)
Out[79]: 1.0

In [80]: y
Out[80]: 
matrix([[ 0.57735027],
        [ 0.57735027],
        [ 0.57735027]])



In [87]: numpy.identity(3)
Out[87]: 
array([[ 1.,  0.,  0.],
       [ 0.,  1.,  0.],
       [ 0.,  0.,  1.]])

In [88]: I = mat(numpy.identity(3))

In [89]: I
Out[89]: 
matrix([[ 1.,  0.,  0.],
        [ 0.,  1.,  0.],
        [ 0.,  0.,  1.]])


In [100]: M = random.rand(3,3)

In [101]: M
Out[101]: 
array([[ 0.38785972,  0.31693765,  0.10919879],
       [ 0.84935365,  0.17680173,  0.12798689],
       [ 0.28273302,  0.06883939,  0.99522043]])

In [102]: M[0][0]
Out[102]: 0.38785972193003437
In [104]: M[2][0]
Out[104]: 0.28273301592388667


############### 行列3


In [115]: import numpy as np

In [116]: np.eye(3)
Out[116]: 
array([[ 1.,  0.,  0.],
       [ 0.,  1.,  0.],
       [ 0.,  0.,  1.]])

In [117]: B = np.eye(3)

In [118]: C = mat(B)

In [119]: B
Out[119]: 
array([[ 1.,  0.,  0.],
       [ 0.,  1.,  0.],
       [ 0.,  0.,  1.]])

In [120]: C
Out[120]: 
matrix([[ 1.,  0.,  0.],
        [ 0.,  1.,  0.],
        [ 0.,  0.,  1.]])



In [121]: help(linalg)

NAME
    numpy.linalg

    - norm            Vector or matrix norm
    - inv             Inverse of a square matrix
    - solve           Solve a linear system of equations
    - det             Determinant of a square matrix
    - lstsq           Solve linear least-squares problem
    - pinv            Pseudo-inverse (Moore-Penrose) calculated using a singula
r
                      value decomposition
    - matrix_power    Integer power of a square matrix
    
    Eigenvalues and decompositions:
    
    - eig             Eigenvalues and vectors of a square matrix
    - eigh            Eigenvalues and eigenvectors of a Hermitian matrix
    - eigvals         Eigenvalues of a square matrix
    - eigvalsh        Eigenvalues of a Hermitian matrix
    - qr              QR decomposition of a matrix
    - svd             Singular value decomposition of a matrix
    - cholesky        Cholesky decomposition of a matrix



In [123]: help(dot)


dot(...)
    dot(a, b, out=None)
    
    Dot product of two arrays.
    
    For 2-D arrays it is equivalent to matrix multiplication, and for 1-D
    arrays to inner product of vectors (without complex conjugation). For
    N dimensions it is a sum product over the last axis of `a` and
    the second-to-last of `b`::
    
        dot(a, b)[i,j,k,m] = sum(a[i,j,:] * b[k,:,m])


In [5]: a = [[1, 0], [0, 1]]

In [6]: a
Out[6]: [[1, 0], [0, 1]]

In [7]: b = [[4, 1], [2, 2]]

In [8]: np.dot(a, b)
Out[8]: 
array([[4, 1],
       [2, 2]])

In [9]: a = [[1, 1], [0, 1]]

In [10]: np.dot(a, b)
Out[10]: 
array([[6, 3],
       [2, 2]])

# 行列のかけざんに dot は無いような....  matrix に変換して使おう．

In [14]: np.mat(a)*np.mat(b)
Out[14]: 
matrix([[6, 3],
        [2, 2]])




















