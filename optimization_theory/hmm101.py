# -*- coding: utf-8 -*-
import math
import random

random.seed(20140123)

class HMM:
    def __init__(self, n):
        pass # 空関数のときは必要


def demo():

    n = 200
    sigma = 0.7
    x = [0]*n
    y = [0.0]*n

    hmm = HMM(n) # 隠れマルコフモデルを作る．n: 入力信号の数

    for i in range(0,n):
        x [i] = random.randint(0,1)
        y [i] = random.gauss(x[i],sigma)
        print (x[i], y[i])


if __name__ == '__main__':

    demo()
