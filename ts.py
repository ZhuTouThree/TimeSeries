import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.tsa.stattools as ts
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

import matplotlib.font_manager as fm
path='./ShanDongYaoBo.csv'
data=pd.read_csv(path)
lrr_data=data['lrr']
lrr_data=lrr_data.values
print(type(lrr_data))
close_data=data['close']
close_data=close_data.values
#ADF检验
result = ts.adfuller(lrr_data)
print(result)
#画图


plt.plot(lrr_data)
# plt.xticks(rotation=90) # 横坐标每个值旋转90度
plt.xlabel('time nodes')
plt.ylabel('log return rate')
plt.title('log return rate')
plt.show()
plot_acf(close_data,lags=50).show()
plot_pacf(close_data,lags=50).show()