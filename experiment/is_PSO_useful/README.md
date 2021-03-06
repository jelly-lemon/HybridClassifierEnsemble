# 实验目的
PSO 粒子群优化是否有效果？做个实验看一下。

# 实验内容
粒子群优化算法，只使用一个目标函数，那就是 min|s*|ui-uj|^2|。

## 目标函数思想
该目标函数是一个启发式函数。
基于这样的启发：两个样本越相似，那么同属于一个类别的概率也越大。
所以我们认为，所有样本的 “样本相似度 * 样本类别差距” 加起来，值越小，预测结果越准确。

# 实验数据
## yeast-0-6 1205/279=4.32  
|                   |val_acc             |val_precision       |val_recall          |val_f1              |auc_value           |val_gmean
|----               |----                |----                |----                |----                |----                |----                       
|KNN                |0.8484 ±0.0077      |0.8941 ±0.0086      |0.9229 ±0.0181      |0.9081 ±0.0052      |0.8241 ±0.0300      |0.6936 ±0.0383
|KNN-PSO(steps=10)  |0.4852 ±0.0255      |0.8246 ±0.0233      |0.4645 ±0.0235      |0.5941 ±0.0239      |0.5172 ±0.0217      |0.5125 ±0.0415
|KNN-PSO(steps=100) |0.4751 ±0.0204      |0.8178 ±0.0328      |0.4546 ±0.0220      |0.5841 ±0.0233      |0.5167 ±0.0377      |0.5058 ±0.0303      
|KNN-PSO(steps=200) |0.4771 ±0.0394      |0.8195 ±0.0392      |0.4564 ±0.0261      |0.5862 ±0.0312      |0.5019 ±0.0675      |0.5045 ±0.0599

# 实验结论
毫无效果，结果只会越来越差。

        