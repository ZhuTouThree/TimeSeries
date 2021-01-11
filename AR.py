
import pandas as pd
from statsmodels.tsa.ar_model import AR
from sklearn.metrics import mean_squared_error

import matplotlib.pyplot as plt


# 宁德时代预测
series = pd.read_csv('ShanDongYaoBo.csv', header=0)
Y = list(series['lrr'])
X = list()
for i in range(len(list(series['lrr']))):
    X.append(str(list(series['trade_date'])[i]))
# 切割数据集
L = 330

train = Y[0:L]
# 训练模型
model = AR(train)
model_fit = model.fit()
print(model_fit.summary())
print('宁德时代多期预测')
print('============================================================================================')
print('AR阶数 %s' % model_fit.k_ar)
print('各个参数: %s' % model_fit.params)
# make predictions
test_num=6
test = Y[L:L + test_num]
#多步预测
# predictions = model_fit.predict(start=len(train), end=len(train) + len(test) - 1, dynamic=False)
# for i in range(len(predictions)):
#     print('预测值=%f, 实际值=%f' % (predictions[i], test[i]))
# error = mean_squared_error(test, predictions)
# print('均方差: %.3f' % error)
# # plot results
# plt.plot(X[L:L + test_num], test)
# plt.plot(X[L:L + test_num], predictions, color='red')
# plt.xticks(rotation=270)
# plt.show()
# train autoregression

window = model_fit.k_ar
coef = model_fit.params

# 单步预测
history = train[len(train) - window:]
history = [history[i] for i in range(len(history))]
predictions = list()

for t in range(len(test)):
    length = len(history)
    lag = [history[i] for i in range(length - window, length)]
    yhat = coef[0]
    for d in range(window):
        yhat += coef[d + 1] * lag[window - d - 1]
    obs = test[t]
    predictions.append(yhat)
    history.append(obs)
    print('预测=%f, 预期=%f' % (yhat, obs))

error = mean_squared_error(test, predictions)
print('Test MSE(均方误差): %.3f' % error)



# plot
plt.plot(X[L:L + test_num], test)
plt.plot(X[L:L + test_num], predictions, color='red')
plt.show()

# fig, axes = plt.subplots(1, 2)
# sns.distplot(test, ax=axes[0], kde=True, rug=True)  # kde 密度曲线  rug 边际毛毯
# sns.kdeplot(test, ax=axes[1], shade=True)  # shade  阴影
# plt.show()