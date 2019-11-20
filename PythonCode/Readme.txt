1. FPR(False positive rate),也称为pf (probability of false alarm)或Type I Error Rate: 所有无缺陷模块中，被错误预测为有缺陷模块的比例。
2. FNR(False negative rate), 也称为Type II Error Rate: 所有有缺陷模块中，被错误预测为无缺陷模块的比例。
3. TNR(True negative rate),也称specificity: 所有无缺陷模块中，被预测正确的模块比例。
4. ER(Error rate): 所有模块中，被预测错误的模块比例。
5. Recall(查全率),也称为TPR(True positive rate), pd (probability of detection), sensitivity: 所有有缺陷模块中，被正确预测为有缺陷的模块比例。
6. Precision(查准率): 所有预测为有缺陷模块中，真正是有缺陷模块的比例。
7. Accuracy(准确率): 所有模块中，被预测正确的模块比例。
8. FMeasure，简称F1度量: 查准率和查全率的调和平均数。
9. MCC(Matthews Correlation Coefficient): 度量混淆矩阵中四个值TP,TN,FP,FN的相关系数。
10. GMeasure,简称G1度量，与FMeasure相比，多考虑了TN，计算TPR(recall)和TNR的调和平均数。
11. g-mean: TPR(recall)和TNR的几何平均数。
12. balance: 点(pd, pf)到点(1,0)的欧式距离[7]，即(pd, pf)到所期望的pd=1, pf=0的距离。
