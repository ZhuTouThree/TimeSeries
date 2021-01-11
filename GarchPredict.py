import math
import numpy as np
import matplotlib.pyplot as plt
predict_2 = np.array([0.010578, 0.016508, -0.002111, -0.002295, -0.000108, 0.011290])
test_2 = np.array([-0.022728, 0.030563, -0.003798, -0.018067, -0.010999, -0.004850])

r = np.random.normal(0, 1, 6)
a_0 = 0
sigma_0 = np.mean(predict_2 - test_2)
a = []
sigma = []
a.append(a_0)
sigma.append(sigma_0)
# c0 c1 c2
c0 = 1.0426e-04
c1 =  0.1170
c2 = 0.8111
for i in range(1, 7):
    sigma_temp = math.sqrt(c0 + c1 * a[i - 1]**2 + c2 * sigma[i - 1]**2)
    sigma.append(sigma_temp)
    a_temp = sigma_temp * r[i - 1]
    a.append(a_temp)

predict_3 = []
for i in range(6):
    predict_3.append(predict_2[i] + a[1+i])
res_error = []
for i in range(6):
    res_error.append(test_2[i] - predict_3[i])

print("预测数据为：")
print(predict_3)

print("真实数据为：")
print(test_2)

test_3 = np.array(test_2)
predict_3 = np.array(predict_3)

MSE = np.sum(np.power((test_3 - predict_3), 2)) / len(test_3)
print("MSE:")
print(MSE)

print("波动率为：")
sigma = np.array(sigma)
print(sigma * sigma)

plt.plot(predict_2, color='blue',label='AR PREDICT')
plt.plot(predict_3, color='red',label='GARCH+AR PREDICT')
plt.plot(test_2,color='black',label='TRUE DATA')
plt.legend()
plt.show()