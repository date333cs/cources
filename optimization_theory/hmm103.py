# -*- coding: utf-8 -*-
import math
import random
import matplotlib.pyplot as plt

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

    t = range(n)
    plt.plot(t, x, label='x')
    plt.plot(t, y, '.g', label='y') # g は緑色， * は点

    plt.title('Original Signal, Observations') 
    plt.xlabel('t') # X 軸
    plt.ylabel('x, y') # Y 軸
    plt.legend() # 描画

    plt.show() # 描画

if __name__ == '__main__':

    demo()
