# 山东大学金融时间序列分析课程结课题目3



选择某只自己感兴趣的股票，分析其日对数收益率的时序特征，从线性时间序列分析，到异方差世间序列分析，构建该股票日对数收益率的最优时序模型，进而说明其时序变化的时序特征。

本实验中选取了山东药玻(600529.SH)从2019年1月1日到2020年12月31日的日线行情数据，选取了前330个数据点作为训练数据。实验数据来源Tushare大数据社区（https://tushare.pro/）。

## (1) 对数据进行建模前的时序图分析；

对应项目中ts.py文件，将对数收益率时序图画出来。

## (2) 选择适合的线性时序模型，并进行相应的模型识别；

选择ar模型进行建模，调用相关库函数，对应AR.py

## (3) 估计模型中参数，并进行全面的模型充分性检验；

ADF充分性检验，检验时间序列是否平稳，对应ts.py

## (4) 进一步检验残差的ARCH效应，如果ARCH效应显著，进行相应的异方差建模；

检验残差平方序列是否有arch效应。对应arch_qtest.py,对残差序列进行异方差建模，建立GARCH（1,1）模型，对应arch_model.py

## (5) 建模工作完成后，做对数收益率及其波动率的6期预测，并通过模型分析其波动率时序变化特征。

画出AR与AR+garch预测的6期预测值，进行对比，对应GarchPredict.py

## (6) 给出95%置信水平下的VaR和ES度量。

分别对应es.py与VaR.py

## 数据来源：Tushsre大数据社区（强烈推荐使用）

## tushare特点

![数据](https://tushare.pro/static/frontend/images/features_api.png?v=75e325d70f3ff819b108f298457b174b)

### 数据丰富

拥有丰富的数据内容，如股票、基金、期货、数字货币等行情数据，公司财务、基金经理等基本面数据

![Cloud Infrastructure](https://tushare.pro/static/frontend/images/features_cloud.png?v=68f8232393f641b8ddb544b28775be83)

### 获取简单

SDK开发包支持语言，同时提供HTTP Restful接口，最大程度方便不同人群的使用

![Managing Multiple Data Centers](https://tushare.pro/static/frontend/images/features_datacenters.png?v=b58113d2344ac2dc1f9e6da852e4c5dc)

### 落地方便

提供多种数据储存方式，如Oracle、MySQL，MongoDB、HDF5、CSV等，为数据获取提供了性能保证

## 作者TushareID：393790

