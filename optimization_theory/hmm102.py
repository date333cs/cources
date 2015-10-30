# -*- coding: utf-8 -*-
import math
import random

random.seed(20140123)

class HMM:
    def __init__(self, n):
        pass # 空関数のときは必要


def generate_x(n):
    x = [0]*n
    for i in range(0,n):
        x [i] = random.randint(0,1)
    return x

def generate_y(x,n,sigma):
    y = [0.0]*n
    for i in range(0,n):
        y [i] = random.gauss(x[i],sigma)
    return y


def demo():

    n = 200
    sigma = 0.7

    hmm = HMM(n) # 隠れマルコフモデルを作る．n: 入力信号の数

    x = generate_x(n)
    y = generate_y(x,n,sigma)

    for i in range(0,n):
        print x[i], y[i]

if __name__ == '__main__':

    demo()
