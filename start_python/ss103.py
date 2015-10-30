# -*- coding: utf-8 -*-
import sys
import numpy
import matplotlib.pyplot as plt

y_vec = []
 
def read_data(filename):
    f = open(filename, 'r')
    line = f.readline()
    while line:
	y_vec.append(float(line))
	line = f.readline()

    f.close()
    return len(y_vec)
 
n = read_data("random200.dat")
print "#data =", n

data = numpy.array(y_vec)

# キャンバス
fig = plt.figure()

# プロット領域（1x1分割の1番目に領域を配置せよという意味）
ax = fig.add_subplot(111)

mu = numpy.mean(data)
sigma = numpy.std(data)

print 'データの平均値 ： %.5f' % mu
print 'データの標準偏差 ：%.5f' % sigma


# 任意のテキスト（$で囲むことでTeX表記も可能）
ax.text(-3,55, r'''
$\mu=%.1f$
$\sigma=%.2f$''' % (mu, sigma))
    
# 例1
# bin 幅 1.0 の場合，7本で，-3.5 から 3.5 をカバーする．  
# ax.hist(data, bins=7, range=(-3.5, 3.5), normed=False, facecolor='g')
#
# 例2
# bin 幅 0.5 の場合，15本で，-3.75 から 3.75 をカバーする．  
ax.hist(data, bins=15, range=(-3.75, 3.75), normed=False, facecolor='g')
# ヒストグラム（normedをTrueで指定すると確率表示になる）
# bin 幅を直接指定することはできない...
# 0 を中心に考える場合，bin の個数は奇数を指定する．
# x の右端，(15-1)/2 * bin幅(0.5)  + bin幅/2 (=0.25) = 3.75  
#
# 例3
# bin 幅 0.1 の場合，61本で，-3.05 から 3.05 をカバーする．  
#ax.hist(data, bins=61, range=(-3.05, 3.05), normed=False, facecolor='g')

# X軸の表示範囲
ax.set_xlim(-3.5, 3.5)
    
# グリッド表示
ax.grid(True)

ax.set_title('Histogram', size=16)

plt.show()

# ファイルにセーブ
plt.savefig('graph1.png', dpi=300)
