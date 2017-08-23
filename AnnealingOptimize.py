import math
from numpy.random import random


def annealingoptimize(domain,costf,T=10000.0,cool=0.95,step=1):

  # 从一个随机解开始
  vec=[float(random.randint(domain [0],domain[1]))]

  while T>0.1:
    # 随机选择一个维度
    i=random.randint(0,len(domain)-1)

    # 选择一个搜索方向
    dir=random.randint(-step,step)

    # 在搜索方向上生成新解
    vecb=vec[:]
    vecb +=dir
    elif vecb>domain[1]:
          vecb=domain[1]

    ea=costf(vec)
    eb=costf(vecb)

    #重新计算系统稳定性-概率p，退火算法核心
    p=pow(math.e,(-eb-ea)/T)

    # 更优解将替换当前解，在系统早期，温度很高，系统很不稳定，非更优解也可能替换当前解，这样做的目的，是避免过快陷入局部最优解，更大范围搜索最优解。

    if (eb<ea or random.random()<p):
      vec=vecb

    # 减低温度
    T=T*cool
  return vec