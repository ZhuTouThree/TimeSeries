import pandas as pd
from statsmodels.tsa.ar_model import AR
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.stats.diagnostic import acorr_ljungbox as lb_test

# 宁德时代预测
series = pd.read_csv('ShanDongYaoBo.csv', header=0)
Y = list(series['lrr'])
X = list()
totalNum = len(list(series['lrr']))
for i in range(len(list(series['lrr']))):
    X.append(str(list(series['trade_date'])[i]))
# 切割数据集
L = 330

train = Y[0:L]

# train autoregression
model = AR(train)
model_fit = model.fit()
print(model_fit.summary())
print('宁德时代多期预测')
print('============================================================================================')
print('AR阶数 %s' % model_fit.k_ar)
print('各个参数: %s' % model_fit.params)
test = Y[L:L + totalNum]
window = model_fit.k_ar
coef = model_fit.params

# 单步预测
history = train[len(train) - window:]
history = [history[i] for i in range(len(history))]
predictions = list()
res = list()
for t in range(len(test)):
    length = len(history)
    lag = [history[i] for i in range(length - window, length)]
    yhat = coef[0]
    for d in range(window):
        yhat += coef[d + 1] * lag[window - d - 1]
    obs = test[t]
    predictions.append(yhat)
    history.append(obs)
    # print('预测=%f, 预期=%f' % (yhat, obs))
    res.append(obs - yhat)
res = np.array(res)
pd.DataFrame(res).to_csv('at.csv')
res = res ** 2

plt.plot(res)
plt.title('Residual square sequence')
plt.xlabel('time nodes')
plt.ylabel('residual square')
plt.show()
print(lb_test(res, return_df=True))

# pd.DataFrame(res).to_csv('at^2.csv')
