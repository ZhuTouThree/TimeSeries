from arch import arch_model
import pandas as pd
import numpy as np
# 宁德时代预测
series = pd.read_csv('at.csv', header=0)
Y = list(series['0'])
L=150
totalNum=len(list(series['0']))
train = Y[0:L]
train=np.array(train)
train=train
test=np.array(Y[L:totalNum])
test=test
arch=arch_model(train)
model_fit=arch.fit()
print(model_fit.summary())

# print('山东药玻多期预测')
# print('============================================================================================')
# print('AR阶数 %s' % model_fit.k_arch)
# print('各个参数: %s' % model_fit.params)

