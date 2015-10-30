# -*- coding: utf-8 -*-
import random

n_trials = 10000   # 何回，シミュレーションするか
n_success = 0      # 当たった回数

for i in range(n_trials):

    hit = [False]*3  # ドアは3つ
    car = random.randint(0,2)  # randint(a,b) で，整数 a,a+1,a+2,..., b のうち一つを等確率で選ぶ．
    hit [ car ] = True  # 当たりのドアを乱数で決める

    # プレイヤーはどれかのドアをランダムに選ぶ
    player = random.randint(0,2)
    
    # モンティホールさんの操作．はずれのドアのうち一つをあける（もちろんプレイヤーの選んだドアは開けない）
    monty = random.randint(0,2)
    while hit [monty] == True or monty == player :
	monty = random.randint(0,2) 

    print i+1, '回目'
    print '新車があるのは', car ,'番目のドアです．'
    print 'プレイヤーは', player ,'番目のドアを選択しました．'
    print 'モンティさんは', monty ,'番目のドアを開けました．'

    
    # ここから自分で書いてみる！！！ 3パターン試せる！
    # 1. 常に，開けるドアを変更する！ こんどは2つのドア（モンティさんが開けたドア以外）のうち，どれかを選ぶ
    #    開けていないのは，車があるドア（car）とプレイヤが先に選んだドア（player）
    # 2. 常に，変更しない． このままのコード．当たる確率は 0.33333...．
    # 3. 開けられていないドア2つから，選びなおす．(半分の確率で変更しない)
   
    
#    print 'プレイヤーは開けるドアを', player ,'番目に変更しました．'
    print

    if car == player:
	n_success +=1

print float(n_success)/float(n_trials)

