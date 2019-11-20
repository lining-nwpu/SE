# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'connect_me.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
#导入程序运行必须模块
import sys
import os
import pandas as pd
import numpy as np
from sympy import *
#PyQt5中使用的基本控件都在PyQt5.QtWidgets模块中
from PyQt5.QtWidgets import QApplication, QMainWindow,QFileDialog,QMessageBox
from PyQt5.QtCore import Qt,QVersionNumber,QCoreApplication
from PyQt5.QtGui import QFont,QGuiApplication
#导入designer工具生成的login模块
from BCQualityCheck import Ui_BCQualityCheck
from InputTemplate import Input_Dialog
from PyQt5 import  QtCore
import math

class MyMainForm(QMainWindow, Ui_BCQualityCheck):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)
        font = QFont("宋体")
        font.setPixelSize(15)
        self.label.setFont(font)
        self.label_2.setFont(font)
        self.label_3.setFont(font)
        self.label_4.setFont(font)
        self.label_5.setFont(font)
        self.label_6.setFont(font)
        self.label_7.setFont(font)
        self.label_8.setFont(font)
        self.label_9.setFont(font)
        self.label_10.setFont(font)
        self.label_11.setFont(font)
        self.label_12.setFont(font)
        self.label_13.setFont(font)
        self.label_14.setFont(font)
        self.label_15.setFont(font)
        self.label_16.setFont(font)
        self.label_17.setFont(font)
        self.label_18.setFont(font)
        self.label_19.setFont(font)
        self.label_20.setFont(font)
        self.label_21.setFont(font)
        self.label_22.setFont(font)
        self.label_23.setFont(font)
        self.label_24.setFont(font)
        self.label_25.setFont(font)
        self.label_26.setFont(font)
        self.label_27.setFont(font)
        self.label_28.setFont(font)
        self.label_29.setFont(font)
        self.label_30.setFont(font)
        self.label_31.setFont(font)
        self.label_32.setFont(font)
        self.label_33.setFont(font)
        self.label_34.setFont(font)
        self.label_35.setFont(font)
        font1 = QFont("宋体")
        font1.setPixelSize(12)
        self.label_36.setFont(font1)
        self.label_37.setFont(font1)
        self.label_38.setFont(font1)
        self.label_39.setFont(font1)
        self.label_40.setFont(font1)
        self.label_41.setFont(font1)
        self.label_42.setFont(font1)
        self.label_43.setFont(font1)
        self.label_44.setFont(font1)
        self.label_45.setFont(font1)
        self.label_46.setFont(font1)
        self.label_47.setFont(font1)
        self.label_48.setFont(font1)
        self.label_49.setFont(font1)

        self.pushButton.setFont(font)
        self.pushButton_2.setFont(font)
        self.pushButton_3.setFont(font)
        self.pushButton_4.setFont(font)
        self.pushButton_5.setFont(font)
        self.pushButton_6.setFont(font)
        self.pushButton_7.setFont(font)
        self.pushButton_8.setFont(font)
        self.pushButton_9.setFont(font)
        self.lineEdit.setFont(font)
        self.lineEdit_2.setFont(font)
        self.lineEdit_3.setFont(font)
        self.lineEdit_4.setFont(font)
        self.lineEdit_5.setFont(font)
        self.lineEdit_6.setFont(font)
        self.lineEdit_7.setFont(font)
        self.lineEdit_8.setFont(font)
        self.lineEdit_9.setFont(font)
        self.lineEdit_10.setFont(font)
        self.lineEdit_11.setFont(font)
        self.lineEdit_12.setFont(font)
        self.lineEdit_13.setFont(font)
        self.lineEdit_14.setFont(font)
        self.lineEdit_15.setFont(font)
        self.lineEdit_16.setFont(font)
        self.lineEdit_17.setFont(font)
        self.lineEdit_18.setFont(font)
        self.lineEdit_19.setFont(font)
        self.lineEdit_20.setFont(font)
        self.lineEdit_21.setFont(font)
        self.lineEdit_22.setFont(font)
        self.lineEdit_23.setFont(font)
        self.lineEdit_24.setFont(font)
        self.lineEdit_25.setFont(font)
        self.lineEdit_26.setFont(font)
        self.lineEdit_27.setFont(font)
        self.lineEdit_28.setFont(font)
        self.lineEdit_29.setFont(font)
        self.lineEdit_30.setFont(font)
        self.lineEdit_31.setFont(font)
        self.lineEdit_32.setFont(font)
        self.lineEdit_33.setFont(font)
        self.lineEdit_34.setFont(font)
        self.groupBox.setFont(font)
        self.groupBox_2.setFont(font)
        self.groupBox_3.setFont(font)
        self.groupBox_4.setFont(font)
        self.groupBox_5.setFont(font)



        self.cwd = os.getcwd()
        self.fileName = None
        self.pushButton.clicked.connect(self.getPerformance)
        self.pushButton_2.clicked.connect(self.getConfusionMatrix)
        self.pushButton_3.clicked.connect(self.showDescription)
        self.pushButton_4.clicked.connect(self.setThreshold)
        self.pushButton_5.clicked.connect(self.getThresholdDefault)
        self.pushButton_6.clicked.connect(self.findInputFilename)
        self.pushButton_7.clicked.connect(self.findOutputDir)
        self.pushButton_8.clicked.connect(self.showInputTemplate)
        self.pushButton_9.clicked.connect(self.OutputResult)

    def showInputTemplate(self):
        self.dialog = Input_Dialog()
        self.dialog.show()

    def showDescription(self):
    #     self.dialog = Dialog()
    #     self.dialog.show()
    #     self.dialog.label.setText("1. FPR(False positive rate),也称为pf (probability of false alarm)或Type I Error Rate: 所有无缺陷模块中，被错误预测为有缺陷模块的比例。\
    #                              2. FNR(False negative rate), 也称为Type II Error Rate: 所有有缺陷模块中，被错误预测为无缺陷模块的比例。\
    #                               3. TNR(True negative rate),也称specificity: 所有无缺陷模块中，被预测正确的模块比例。\
    #                               4. ER(Error rate): 所有模块中，被预测错误的模块比例。\
    #                               5. Recall(查全率),也称为TPR(True positive rate), pd (probability of detection), sensitivity: 所有有缺陷模块中，被正确预测为有缺陷的模块比例。\
    #                               6. Precision(查准率): 所有预测为有缺陷模块中，真正是有缺陷模块的比例。\
    #                               7. Accuracy(准确率): 所有模块中，被预测正确的模块比例。\
    #                               8. FMeasure，简称F1度量: 查准率和查全率的调和平均数。\
    #                               9. MCC(Matthews Correlation Coefficient): 度量混淆矩阵中四个值TP,TN,FP,FN的相关系数。\
    #                               10. GMeasure,简称G1度量，与FMeasure相比，多考虑了TN，计算TPR(recall)和TNR的调和平均数。\
    #                               11. g-mean: TPR(recall)和TNR的几何平均数。\
    #                               12. balance: 点(pd, pf)到点(1,0)的欧式距离[7]，即(pd, pf)到所期望的pd=1, pf=0的距离。")
    #
    #     self.dialog.label.setWordWrap(True)
    #     self.dialog.label.setAlignment(Qt.AlignTop)
    #     self.dialog.exec()
    #     fname = QFileDialog.getOpenFileName(self, '打开文件', 'Readme.txt', '*.txt')
        try:
            f = open("D:/Data/Project/DBkpipredict/07-Code/dbkpipredict/Readme.txt", 'r')
            with f:
                data = f.read()
                QMessageBox.about(self,"帮助",data)
        except FileNotFoundError:
            QMessageBox.about(self, "输入文件错误", "请确认文件是否存在")

    def OutputResult(self):
        try:
            df = pd.read_excel(self.fileName,encoding="utf-8")
        except Exception:
            QMessageBox.information(self,"compute","请输入文件名")
            return

        data = []
        for i in range(df.shape[0]):
            TP = np.nan
            FP = np.nan
            TN = np.nan
            FN = np.nan
            FPR = np.nan
            FNR = np.nan
            TNR = np.nan
            ER = np.nan
            Recall = np.nan
            Precision = np.nan
            Accuracy = np.nan
            FMeasure = np.nan
            GMeasure = np.nan
            GMean = np.nan
            MCC = np.nan
            Balance = np.nan
            Density = np.nan
            if (not(np.isnan(df.loc[i,"FPR"])) and not(np.isnan(df.loc[i,"Recall"])) and not(np.isnan(df.loc[i,"Accuracy"])))or(
                not(np.isnan(df.loc[i,"FPR"])) and not(np.isnan(df.loc[i,"Recall"])) and not(np.isnan(df.loc[i,"ER"])))or(
                not (np.isnan(df.loc[i, "FPR"])) and not (np.isnan(df.loc[i, "FNR"])) and not (np.isnan(df.loc[i, "Accuracy"])))or(
                not (np.isnan(df.loc[i, "FPR"])) and not (np.isnan(df.loc[i, "FNR"])) and not (np.isnan(df.loc[i, "ER"])))or(
                not (np.isnan(df.loc[i, "TNR"])) and not (np.isnan(df.loc[i, "Recall"])) and not (np.isnan(df.loc[i, "Accuracy"]))) or (
                not (np.isnan(df.loc[i, "TNR"])) and not (np.isnan(df.loc[i, "Recall"])) and not (np.isnan(df.loc[i, "ER"]))) or (
                not (np.isnan(df.loc[i, "TNR"])) and not (np.isnan(df.loc[i, "FNR"])) and not (np.isnan(df.loc[i, "Accuracy"]))) or (
                not (np.isnan(df.loc[i, "TNR"])) and not (np.isnan(df.loc[i, "FNR"])) and not (np.isnan(df.loc[i, "ER"]))
            ):
                if not(np.isnan(df.loc[i,"FPR"])) and not(np.isnan(df.loc[i,"Recall"])) and not(np.isnan(df.loc[i,"Accuracy"])):
                    FPR = df.loc[i,"FPR"]
                    Recall = df.loc[i,"Recall"]
                    Accuracy = df.loc[i,"Accuracy"]
                elif not(np.isnan(df.loc[i,"FPR"])) and not(np.isnan(df.loc[i,"Recall"])) and not(np.isnan(df.loc[i,"ER"])):
                    FPR = df.loc[i, "FPR"]
                    Recall = df.loc[i, "Recall"]
                    Accuracy = 1 - df.loc[i, "ER"]
                elif not (np.isnan(df.loc[i, "FPR"])) and not (np.isnan(df.loc[i, "FNR"])) and not (np.isnan(df.loc[i, "Accuracy"])):
                    FPR = df.loc[i, "FPR"]
                    Recall = 1 - df.loc[i, "FNR"]
                    Accuracy = df.loc[i, "Accuracy"]
                elif not (np.isnan(df.loc[i, "FPR"])) and not (np.isnan(df.loc[i, "FNR"])) and not (np.isnan(df.loc[i, "ER"])):
                    FPR = df.loc[i, "FPR"]
                    Recall = 1 - df.loc[i, "FNR"]
                    Accuracy = 1 - df.loc[i, "ER"]
                elif not (np.isnan(df.loc[i, "TNR"])) and not (np.isnan(df.loc[i, "Recall"])) and not (np.isnan(df.loc[i, "Accuracy"])):
                    FPR = 1- df.loc[i, "TNR"]
                    Recall = df.loc[i, "Recall"]
                    Accuracy = df.loc[i, "Accuracy"]
                elif not (np.isnan(df.loc[i, "TNR"])) and not (np.isnan(df.loc[i, "Recall"])) and not (np.isnan(df.loc[i, "ER"])):
                    FPR = 1- df.loc[i, "TNR"]
                    Recall = df.loc[i, "Recall"]
                    Accuracy = 1 - df.loc[i, "ER"]
                elif not (np.isnan(df.loc[i, "TNR"])) and not (np.isnan(df.loc[i, "FNR"])) and not (np.isnan(df.loc[i, "Accuracy"])):
                    FPR = 1 - df.loc[i, "TNR"]
                    Recall = 1 - df.loc[i, "FNR"]
                    Accuracy =  df.loc[i, "Accuracy"]
                elif not (np.isnan(df.loc[i, "TNR"])) and not (np.isnan(df.loc[i, "FNR"])) and not (np.isnan(df.loc[i, "ER"])):
                    FPR = 1 - df.loc[i, "TNR"]
                    Recall = 1 - df.loc[i, "FNR"]
                    Accuracy = 1- df.loc[i, "ER"]
                flag,result_TP,result_TN,result_FP,result_FN = self.fun1(FPR,Recall,Accuracy)
                if flag == 0:
                    TP = result_TP
                    TN = result_TN
                    FP = result_FP
                    FN = result_FN
                else:
                    TP = np.nan
                    TN = np.nan
                    FP = np.nan
                    FN = np.nan

            elif (not(np.isnan(df.loc[i,"FPR"])) and not(np.isnan(df.loc[i,"Recall"])) and not(np.isnan(df.loc[i,"Precision"] )))or(
                 not (np.isnan(df.loc[i, "FPR"])) and not (np.isnan(df.loc[i, "FNR"])) and not (np.isnan(df.loc[i, "Precision"])))or(
                 not (np.isnan(df.loc[i, "TNR"])) and not (np.isnan(df.loc[i, "Recall"])) and not (np.isnan(df.loc[i, "Precision"])))or(
                 not (np.isnan(df.loc[i, "TNR"])) and not (np.isnan(df.loc[i, "FNR"])) and not (np.isnan(df.loc[i, "Precision"]))
            ):
                if not(np.isnan(df.loc[i,"FPR"])) and not(np.isnan(df.loc[i,"Recall"])) and not(np.isnan(df.loc[i,"Precision"] )):
                    FPR = df.loc[i,"FPR"]
                    Recall = df.loc[i,"Recall"]
                    Precision = df.loc[i,"Precision"]
                elif not (np.isnan(df.loc[i, "FPR"])) and not (np.isnan(df.loc[i, "FNR"])) and not (np.isnan(df.loc[i, "Precision"])):
                    FPR = df.loc[i, "FPR"]
                    Recall = 1 - df.loc[i, "FNR"]
                    Precision = df.loc[i, "Precision"]
                elif not (np.isnan(df.loc[i, "TNR"])) and not (np.isnan(df.loc[i, "Recall"])) and not (np.isnan(df.loc[i, "Precision"])):
                    FPR = 1 - df.loc[i, "TNR"]
                    Recall = df.loc[i, "Recall"]
                    Precision = df.loc[i, "Precision"]
                elif not (np.isnan(df.loc[i, "TNR"])) and not (np.isnan(df.loc[i, "FNR"])) and not (np.isnan(df.loc[i, "Precision"])):
                    FPR = 1 - df.loc[i, "TNR"]
                    Recall = 1 - df.loc[i, "FNR"]
                    Precision = df.loc[i, "Precision"]
                flag,result_TP,result_TN,result_FP,result_FN = self.fun2(FPR,Recall,Precision)
                if flag == 0:
                    TP = result_TP
                    TN = result_TN
                    FP = result_FP
                    FN = result_FN
                else:
                    TP = np.nan
                    TN = np.nan
                    FP = np.nan
                    FN = np.nan

            elif  (not(np.isnan(df.loc[i,"FPR"])) and not(np.isnan(df.loc[i,"Recall"])) and not(np.isnan(df.loc[i,"FMeasure"])))or(
                    not (np.isnan(df.loc[i, "FPR"])) and not (np.isnan(df.loc[i, "FNR"])) and not (np.isnan(df.loc[i, "FMeasure"])))or(
                    not (np.isnan(df.loc[i, "TNR"])) and not (np.isnan(df.loc[i, "Recall"])) and not (np.isnan(df.loc[i, "FMeasure"])))or(
                    not (np.isnan(df.loc[i, "TNR"])) and not (np.isnan(df.loc[i, "FNR"])) and not (np.isnan(df.loc[i, "FMeasure"]))
            ):
                if not(np.isnan(df.loc[i,"FPR"])) and not(np.isnan(df.loc[i,"Recall"])) and not(np.isnan(df.loc[i,"FMeasure"])):
                    FPR = df.loc[i,"FPR"]
                    Recall = df.loc[i,"Recall"]
                    FMeasure = df.loc[i,"FMeasure"]
                elif not (np.isnan(df.loc[i, "FPR"])) and not (np.isnan(df.loc[i, "FNR"])) and not (np.isnan(df.loc[i, "FMeasure"])):
                    FPR = df.loc[i, "FPR"]
                    Recall = 1-df.loc[i, "FNR"]
                    FMeasure = df.loc[i, "FMeasure"]
                elif not (np.isnan(df.loc[i, "TNR"])) and not (np.isnan(df.loc[i, "Recall"])) and not (np.isnan(df.loc[i, "FMeasure"])):
                    FPR = 1-df.loc[i, "TNR"]
                    Recall = df.loc[i, "Recall"]
                    FMeasure = df.loc[i, "FMeasure"]
                elif not (np.isnan(df.loc[i, "TNR"])) and not (np.isnan(df.loc[i, "FNR"])) and not (np.isnan(df.loc[i, "FMeasure"])):
                    FPR = 1 - df.loc[i, "TNR"]
                    Recall = 1 - df.loc[i, "FNR"]
                    FMeasure = df.loc[i, "FMeasure"]
                flag,result_TP,result_TN,result_FP,result_FN = self.fun3(FPR,Recall,FMeasure)
                if flag == 0:
                    TP = result_TP
                    TN = result_TN
                    FP = result_FP
                    FN = result_FN
                else:
                    TP = np.nan
                    TN = np.nan
                    FP = np.nan
                    FN = np.nan

            elif  (not(np.isnan(df.loc[i,"FPR"])) and not(np.isnan(df.loc[i,"Accuracy"])) and not(np.isnan(df.loc[i,"Precision"])))or(
                    not (np.isnan(df.loc[i, "FPR"])) and not (np.isnan(df.loc[i, "FNR"])) and not (np.isnan(df.loc[i, "Precision"])))or(
                    not (np.isnan(df.loc[i, "TNR"])) and not (np.isnan(df.loc[i, "Accuracy"])) and not (np.isnan(df.loc[i, "Precision"])))or(
                    not (np.isnan(df.loc[i, "TNR"])) and not (np.isnan(df.loc[i, "FNR"])) and not (np.isnan(df.loc[i, "Precision"]))
            ):
                if not(np.isnan(df.loc[i,"FPR"])) and not(np.isnan(df.loc[i,"Accuracy"])) and not(np.isnan(df.loc[i,"Precision"])):
                    FPR = df.loc[i,"FPR"]
                    Accuracy = df.loc[i,"Accuracy"]
                    Precision = df.loc[i,"Precision"]
                elif not (np.isnan(df.loc[i, "FPR"])) and not (np.isnan(df.loc[i, "FNR"])) and not (np.isnan(df.loc[i, "Precision"])):
                    FPR = df.loc[i, "FPR"]
                    Accuracy = 1 - df.loc[i, "FNR"]
                    Precision = df.loc[i, "Precision"]
                elif not (np.isnan(df.loc[i, "TNR"])) and not (np.isnan(df.loc[i, "Accuracy"])) and not (np.isnan(df.loc[i, "Precision"])):
                    FPR = 1 - df.loc[i, "TNR"]
                    Accuracy = df.loc[i, "Accuracy"]
                    Precision = df.loc[i, "Precision"]
                elif not (np.isnan(df.loc[i, "TNR"])) and not (np.isnan(df.loc[i, "FNR"])) and not (np.isnan(df.loc[i, "Precision"])):
                    FPR = 1 - df.loc[i, "TNR"]
                    Accuracy = 1 - df.loc[i, "FNR"]
                    Precision = df.loc[i, "Precision"]
                flag,result_TP,result_TN,result_FP,result_FN = self.fun4(FPR,Accuracy,Precision)
                if flag == 0:
                    TP = result_TP
                    TN = result_TN
                    FP = result_FP
                    FN = result_FN
                else:
                    TP = np.nan
                    TN = np.nan
                    FP = np.nan
                    FN = np.nan

            elif  (not(np.isnan(df.loc[i,'FPR'])) and not(np.isnan(df.loc[i,'Accuracy'])) and not(np.isnan(df.loc[i,'FMeasure'])))or(
                    not (np.isnan(df.loc[i, 'FPR'])) and not (np.isnan(df.loc[i, 'FNR'])) and not (np.isnan(df.loc[i, 'FMeasure'])))or(
                    not (np.isnan(df.loc[i, 'TNR'])) and not (np.isnan(df.loc[i, 'Accuracy'])) and not (np.isnan(df.loc[i, 'FMeasure'])))or(
                    not (np.isnan(df.loc[i, 'TNR'])) and not (np.isnan(df.loc[i, 'FNR'])) and not (np.isnan(df.loc[i, 'FMeasure']))
            ):
                if not(np.isnan(df.loc[i,'FPR'])) and not(np.isnan(df.loc[i,'Accuracy'])) and not(np.isnan(df.loc[i,'FMeasure'])):
                    FPR = df.loc[i,'FPR']
                    Accuracy = df.loc[i,'Accuracy']
                    FMeasure = df.loc[i,'FMeasure']
                elif not (np.isnan(df.loc[i, 'FPR'])) and not (np.isnan(df.loc[i, 'FNR'])) and not (np.isnan(df.loc[i, 'FMeasure'])):
                    FPR = df.loc[i, 'FPR']
                    Accuracy = 1 - df.loc[i, 'FNR']
                    FMeasure = df.loc[i, 'FMeasure']
                elif not (np.isnan(df.loc[i, 'TNR'])) and not (np.isnan(df.loc[i, 'Accuracy'])) and not (np.isnan(df.loc[i, 'FMeasure'])):
                    FPR = 1 - df.loc[i, 'TNR']
                    Accuracy = df.loc[i, 'Accuracy']
                    FMeasure = df.loc[i, 'FMeasure']
                elif not (np.isnan(df.loc[i, 'TNR'])) and not (np.isnan(df.loc[i, 'FNR'])) and not (np.isnan(df.loc[i, 'FMeasure'])):
                    FPR = 1 - df.loc[i, 'TNR']
                    Accuracy = 1 - df.loc[i, 'FNR']
                    FMeasure = df.loc[i, 'FMeasure']
                flag,result_TP,result_TN,result_FP,result_FN = self.fun5(FPR,Accuracy,FMeasure)
                if flag == 0:
                    TP = result_TP
                    TN = result_TN
                    FP = result_FP
                    FN = result_FN
                else:
                    TP = np.nan
                    TN = np.nan
                    FP = np.nan
                    FN = np.nan
            elif  (not(np.isnan(df.loc[i,'FPR'])) and not(np.isnan(df.loc[i,'Precision'])) and not(np.isnan(df.loc[i,'FMeasure'])))or(
                    not (np.isnan(df.loc[i, 'TNR'])) and not (np.isnan(df.loc[i, 'Precision'])) and not (np.isnan(df.loc[i, 'FMeasure']))
            ):
                if not(np.isnan(df.loc[i,'FPR'])) and not(np.isnan(df.loc[i,'Precision'])) and not(np.isnan(df.loc[i,'FMeasure'])):
                    FPR = df.loc[i,'FPR']
                    Precision = df.loc[i,'Precision']
                    FMeasure = df.loc[i,'FMeasure']
                elif not (np.isnan(df.loc[i, 'TNR'])) and not (np.isnan(df.loc[i, 'Precision'])) and not (np.isnan(df.loc[i, 'FMeasure'])):
                    FPR = 1 - df.loc[i, 'TNR']
                    Precision = df.loc[i, 'Precision']
                    FMeasure = df.loc[i, 'FMeasure']
                flag,result_TP,result_TN,result_FP,result_FN = self.fun6(FPR,Precision,FMeasure)
                if flag == 0:
                    TP = result_TP
                    TN = result_TN
                    FP = result_FP
                    FN = result_FN
                else:
                    TP = np.nan
                    TN = np.nan
                    FP = np.nan
                    FN = np.nan
            elif  (not(np.isnan(df.loc[i,'Recall'])) and not(np.isnan(df.loc[i,'Accuracy'])) and not(np.isnan(df.loc[i,'Precision'])))or(
                    not (np.isnan(df.loc[i, 'Recall'])) and not (np.isnan(df.loc[i, 'ER'])) and not (np.isnan(df.loc[i, 'Precision'])))or(
                    not (np.isnan(df.loc[i, 'FNR'])) and not (np.isnan(df.loc[i, 'Accuracy'])) and not (np.isnan(df.loc[i, 'Precision'])))or(
                    not (np.isnan(df.loc[i, 'FNR'])) and not (np.isnan(df.loc[i, 'ER'])) and not (np.isnan(df.loc[i, 'Precision']))
            ):
                if not(np.isnan(df.loc[i,'Recall'])) and not(np.isnan(df.loc[i,'Accuracy'])) and not(np.isnan(df.loc[i,'Precision'])):
                    Recall = df.loc[i,'Recall']
                    Accuracy = df.loc[i,'Accuracy']
                    Precision = df.loc[i,'Precision']
                elif not (np.isnan(df.loc[i, 'Recall'])) and not (np.isnan(df.loc[i, 'ER'])) and not (np.isnan(df.loc[i, 'Precision'])):
                    Recall = df.loc[i, 'Recall']
                    Accuracy = 1 - df.loc[i, 'ER']
                    Precision = df.loc[i, 'Precision']
                elif not (np.isnan(df.loc[i, 'FNR'])) and not (np.isnan(df.loc[i, 'Accuracy'])) and not (np.isnan(df.loc[i, 'Precision'])):
                    Recall = 1 - df.loc[i, 'FNR']
                    Accuracy = df.loc[i, 'Accuracy']
                    Precision = df.loc[i, 'Precision']
                elif not (np.isnan(df.loc[i, 'FNR'])) and not (np.isnan(df.loc[i, 'ER'])) and not (np.isnan(df.loc[i, 'Precision'])):
                    Recall =1 - df.loc[i, 'FNR']
                    Accuracy = 1 - df.loc[i, 'ER']
                    Precision = df.loc[i, 'Precision']
                flag,result_TP,result_TN,result_FP,result_FN = self.fun7(Recall,Accuracy,Precision)
                if flag == 0:
                    TP = result_TP
                    TN = result_TN
                    FP = result_FP
                    FN = result_FN
                else:
                    TP = np.nan
                    TN = np.nan
                    FP = np.nan
                    FN = np.nan
            elif  (not(np.isnan(df.loc[i,'Recall'])) and not(np.isnan(df.loc[i,'Accuracy'])) and not(np.isnan(df.loc[i,'FMeasure'])))or(
                    not (np.isnan(df.loc[i, 'Recall'])) and not (np.isnan(df.loc[i, 'ER'])) and not (np.isnan(df.loc[i, 'FMeasure'])))or(
                    not (np.isnan(df.loc[i, 'FNR'])) and not (np.isnan(df.loc[i, 'Accuracy'])) and not (np.isnan(df.loc[i, 'FMeasure'])))or(
                    not (np.isnan(df.loc[i, 'FNR'])) and not (np.isnan(df.loc[i, 'ER'])) and not (np.isnan(df.loc[i, 'FMeasure']))
            ):
                if not(np.isnan(df.loc[i,'Recall'])) and not(np.isnan(df.loc[i,'Accuracy'])) and not(np.isnan(df.loc[i,'FMeasure'])):
                    Recall = df.loc[i,'Recall']
                    Accuracy = df.loc[i,'Accuracy']
                    FMeasure = df.loc[i,'FMeasure']
                elif not (np.isnan(df.loc[i, 'Recall'])) and not (np.isnan(df.loc[i, 'ER'])) and not (np.isnan(df.loc[i, 'FMeasure'])):
                    Recall = df.loc[i, 'Recall']
                    Accuracy = 1 - df.loc[i, 'ER']
                    FMeasure = df.loc[i, 'FMeasure']
                elif not (np.isnan(df.loc[i, 'FNR'])) and not (np.isnan(df.loc[i, 'Accuracy'])) and not (np.isnan(df.loc[i, 'FMeasure'])):
                    Recall = 1 - df.loc[i, 'FNR']
                    Accuracy =  df.loc[i, 'Accuracy']
                    FMeasure = df.loc[i, 'FMeasure']
                elif not (np.isnan(df.loc[i, 'FNR'])) and not (np.isnan(df.loc[i, 'ER'])) and not (np.isnan(df.loc[i, 'FMeasure'])):
                    Recall = 1 - df.loc[i, 'FNR']
                    Accuracy = 1 - df.loc[i, 'ER']
                    FMeasure = df.loc[i, 'FMeasure']
                flag,result_TP,result_TN,result_FP,result_FN = self.fun8(Recall,Accuracy,FMeasure)
                if flag == 0:
                    TP = result_TP
                    TN = result_TN
                    FP = result_FP
                    FN = result_FN
                else:
                    TP = np.nan
                    TN = np.nan
                    FP = np.nan
                    FN = np.nan
            elif  (not(np.isnan(df.loc[i,'Precision'])) and not(np.isnan(df.loc[i,'Accuracy'])) and not(np.isnan(df.loc[i,'FMeasure'])))or(
                    not (np.isnan(df.loc[i, 'Precision'])) and not (np.isnan(df.loc[i, 'ER'])) and not (np.isnan(df.loc[i, 'FMeasure']))
            ):
                if not(np.isnan(df.loc[i,'Precision'])) and not(np.isnan(df.loc[i,'Accuracy'])) and not(np.isnan(df.loc[i,'FMeasure'])):
                    Precision = df.loc[i,'Precision']
                    Accuracy = df.loc[i,'Accuracy']
                    FMeasure = df.loc[i,'FMeasure']
                elif not (np.isnan(df.loc[i, 'Precision'])) and not (np.isnan(df.loc[i, 'ER'])) and not (np.isnan(df.loc[i, 'FMeasure'])):
                    Precision = df.loc[i, 'Precision']
                    Accuracy = 1 - df.loc[i, 'ER']
                    FMeasure = df.loc[i, 'FMeasure']
                flag,result_TP,result_TN,result_FP,result_FN = self.fun9(Precision,Accuracy,FMeasure)
                if flag == 0:
                    TP = result_TP
                    TN = result_TN
                    FP = result_FP
                    FN = result_FN
                else:
                    TP = np.nan
                    TN = np.nan
                    FP = np.nan
                    FN = np.nan

            elif  (not(np.isnan(df.loc[i,'FPR'])) and not(np.isnan(df.loc[i,'Recall'])) and not(np.isnan(df.loc[i,'Density'])))or(
                    not (np.isnan(df.loc[i, 'FPR'])) and not (np.isnan(df.loc[i, 'FNR'])) and not (np.isnan(df.loc[i, 'Density'])))or(
                    not (np.isnan(df.loc[i, 'TNR'])) and not (np.isnan(df.loc[i, 'Recall'])) and not (np.isnan(df.loc[i, 'Density'])))or(
                    not (np.isnan(df.loc[i, 'TNR'])) and not (np.isnan(df.loc[i, 'FNR'])) and not (np.isnan(df.loc[i, 'Density']))
            ):
                if not(np.isnan(df.loc[i,'FPR'])) and not(np.isnan(df.loc[i,'Recall'])) and not(np.isnan(df.loc[i,'Density'])):
                    FPR = df.loc[i,'FPR']
                    Recall = df.loc[i,'Recall']
                    Density = df.loc[i,'Density']
                elif not(np.isnan(df.loc[i,'FPR'])) and not(np.isnan(df.loc[i,'FNR'])) and not(np.isnan(df.loc[i,'Density'])):
                    FPR = df.loc[i, 'FPR']
                    Recall = 1 - df.loc[i, 'FNR']
                    Density = df.loc[i, 'Density']
                elif not (np.isnan(df.loc[i, 'TNR'])) and not (np.isnan(df.loc[i, 'Recall'])) and not (np.isnan(df.loc[i, 'Density'])):
                    FPR = 1 - df.loc[i, 'TNR']
                    Recall = df.loc[i, 'Recall']
                    Density = df.loc[i, 'Density']
                elif not (np.isnan(df.loc[i, 'TNR'])) and not (np.isnan(df.loc[i, 'FNR'])) and not (np.isnan(df.loc[i, 'Density'])):
                    FPR = 1 - df.loc[i, 'TNR']
                    Recall = 1 - df.loc[i, 'FNR']
                    Density = df.loc[i, 'Density']
                flag,result_TP,result_TN,result_FP,result_FN = self.fun11(FPR,Recall,Density)
                if flag == 0:
                    TP = result_TP
                    TN = result_TN
                    FP = result_FP
                    FN = result_FN
                else:
                    TP = np.nan
                    TN = np.nan
                    FP = np.nan
                    FN = np.nan

            elif  (not(np.isnan(df.loc[i,'FPR'])) and not(np.isnan(df.loc[i,'Accuracy'])) and not(np.isnan(df.loc[i,'Density'])))or(
                    not (np.isnan(df.loc[i, 'FPR'])) and not (np.isnan(df.loc[i, 'ER'])) and not (np.isnan(df.loc[i, 'Density'])))or(
                    not (np.isnan(df.loc[i, 'TNR'])) and not (np.isnan(df.loc[i, 'Accuracy'])) and not (np.isnan(df.loc[i, 'Density'])))or(
                    not (np.isnan(df.loc[i, 'TNR'])) and not (np.isnan(df.loc[i, 'ER'])) and not (np.isnan(df.loc[i, 'Density']))
            ):
                if not(np.isnan(df.loc[i,'FPR'])) and not(np.isnan(df.loc[i,'Accuracy'])) and not(np.isnan(df.loc[i,'Density'])):
                    FPR = df.loc[i,'FPR']
                    Accuracy = df.loc[i,'Accuracy']
                    Density = df.loc[i,'Density']
                elif not (np.isnan(df.loc[i, 'FPR'])) and not (np.isnan(df.loc[i, 'ER'])) and not (np.isnan(df.loc[i, 'Density'])):
                    FPR = df.loc[i, 'FPR']
                    Accuracy = 1 - df.loc[i, 'ER']
                    Density = df.loc[i, 'Density']
                elif not (np.isnan(df.loc[i, 'TNR'])) and not (np.isnan(df.loc[i, 'Accuracy'])) and not (np.isnan(df.loc[i, 'Density'])):
                    FPR = 1 - df.loc[i, 'TNR']
                    Accuracy = df.loc[i, 'Accuracy']
                    Density = df.loc[i, 'Density']
                elif not (np.isnan(df.loc[i, 'TNR'])) and not (np.isnan(df.loc[i, 'ER'])) and not (np.isnan(df.loc[i, 'Density'])):
                    FPR = 1 - df.loc[i, 'TNR']
                    Accuracy = 1 - df.loc[i, 'ER']
                    Density = df.loc[i, 'Density']
                flag,result_TP,result_TN,result_FP,result_FN = self.fun12(FPR,Accuracy,Density)
                if flag == 0:
                    TP = result_TP
                    TN = result_TN
                    FP = result_FP
                    FN = result_FN
                else:
                    TP = np.nan
                    TN = np.nan
                    FP = np.nan
                    FN = np.nan
            elif  (not(np.isnan(df.loc[i,'FPR'])) and not(np.isnan(df.loc[i,'Precision'])) and not(np.isnan(df.loc[i,'Density'])))or(
                    not (np.isnan(df.loc[i, 'TNR'])) and not (np.isnan(df.loc[i, 'Precision'])) and not (np.isnan(df.loc[i, 'Density']))
            ):
                if not(np.isnan(df.loc[i,'FPR'])) and not(np.isnan(df.loc[i,'Precision'])) and not(np.isnan(df.loc[i,'Density'])):
                    FPR = df.loc[i,'FPR']
                    Precision = df.loc[i,'Precision']
                    Density = df.loc[i,'Density']
                elif not (np.isnan(df.loc[i, 'TNR'])) and not (np.isnan(df.loc[i, 'Precision'])) and not (np.isnan(df.loc[i, 'Density'])):
                    FPR = 1 - df.loc[i, 'TNR']
                    Precision = df.loc[i, 'Precision']
                    Density = df.loc[i, 'Density']
                flag,result_TP,result_TN,result_FP,result_FN = self.fun13(FPR,Precision,Density)
                if flag == 0:
                    TP = result_TP
                    TN = result_TN
                    FP = result_FP
                    FN = result_FN
                else:
                    TP = np.nan
                    TN = np.nan
                    FP = np.nan
                    FN = np.nan
            elif  (not(np.isnan(df.loc[i,'FPR'])) and not(np.isnan(df.loc[i,'FMeasure'])) and not(np.isnan(df.loc[i,'Density'])))or(
                    not (np.isnan(df.loc[i, 'TNR'])) and not (np.isnan(df.loc[i, 'FMeasure'])) and not (np.isnan(df.loc[i, 'Density']))
            ):
                if not(np.isnan(df.loc[i,'FPR'])) and not(np.isnan(df.loc[i,'FMeasure'])) and not(np.isnan(df.loc[i,'Density'])):
                    FPR = df.loc[i,'FPR']
                    FMeasure = df.loc[i,'FMeasure']
                    Density = df.loc[i,'Density']
                elif not (np.isnan(df.loc[i, 'TNR'])) and not (np.isnan(df.loc[i, 'FMeasure'])) and not (np.isnan(df.loc[i, 'Density'])):
                    FPR = 1 - df.loc[i, 'TNR']
                    FMeasure = df.loc[i, 'FMeasure']
                    Density = df.loc[i, 'Density']
                flag,result_TP,result_TN,result_FP,result_FN = self.fun14(FPR,FMeasure,Density)
                if flag == 0:
                    TP = result_TP
                    TN = result_TN
                    FP = result_FP
                    FN = result_FN
                else:
                    TP = np.nan
                    TN = np.nan
                    FP = np.nan
                    FN = np.nan
            elif  (not(np.isnan(df.loc[i,'Recall'])) and not(np.isnan(df.loc[i,'Accuracy'])) and not(np.isnan(df.loc[i,'Density'])))or(
                    not (np.isnan(df.loc[i, 'Recall'])) and not (np.isnan(df.loc[i, 'ER'])) and not (np.isnan(df.loc[i, 'Density'])))or(
                    not (np.isnan(df.loc[i, 'FNR'])) and not (np.isnan(df.loc[i, 'Accuracy'])) and not (np.isnan(df.loc[i, 'Density'])))or(
                    not (np.isnan(df.loc[i, 'FNR'])) and not (np.isnan(df.loc[i, 'ER'])) and not (np.isnan(df.loc[i, 'Density']))
            ):
                if not(np.isnan(df.loc[i,'Recall'])) and not(np.isnan(df.loc[i,'Accuracy'])) and not(np.isnan(df.loc[i,'Density'])):
                    Recall = df.loc[i,'Recall']
                    Accuracy = df.loc[i,'Accuracy']
                    Density = df.loc[i,'Density']
                elif not (np.isnan(df.loc[i, 'Recall'])) and not (np.isnan(df.loc[i, 'ER'])) and not (np.isnan(df.loc[i, 'Density'])):
                    Recall = df.loc[i, 'Recall']
                    Accuracy = 1 - df.loc[i, 'ER']
                    Density = df.loc[i, 'Density']
                elif  not (np.isnan(df.loc[i, 'FNR'])) and not (np.isnan(df.loc[i, 'Accuracy'])) and not (np.isnan(df.loc[i, 'Density'])):
                    Recall = 1 - df.loc[i, 'FNR']
                    Accuracy =  df.loc[i, 'Accuracy']
                    Density = df.loc[i, 'Density']
                elif not (np.isnan(df.loc[i, 'FNR'])) and not (np.isnan(df.loc[i, 'ER'])) and not (np.isnan(df.loc[i, 'Density'])):
                    Recall = 1 - df.loc[i, 'FNR']
                    Accuracy = 1 - df.loc[i, 'ER']
                    Density = df.loc[i, 'Density']
                flag, result_TP,result_TN,result_FP,result_FN = self.fun15(Recall,Accuracy,Density)
                if flag == 0:
                    TP = result_TP
                    TN = result_TN
                    FP = result_FP
                    FN = result_FN
                else:
                    TP = np.nan
                    TN = np.nan
                    FP = np.nan
                    FN = np.nan
            elif  (not(np.isnan(df.loc[i,'Recall'])) and not(np.isnan(df.loc[i,'Precision'])) and not(np.isnan(df.loc[i,'Density'])))or(
                    not (np.isnan(df.loc[i, 'FNR'])) and not (np.isnan(df.loc[i, 'Precision'])) and not (np.isnan(df.loc[i, 'Density']))
            ):
                if not(np.isnan(df.loc[i,'Recall'])) and not(np.isnan(df.loc[i,'Precision'])) and not(np.isnan(df.loc[i,'Density'])):
                    Recall = df.loc[i,'Recall']
                    Precision = df.loc[i,'Precision']
                    Density = df.loc[i,'Density']
                elif not (np.isnan(df.loc[i, 'FNR'])) and not (np.isnan(df.loc[i, 'Precision'])) and not (np.isnan(df.loc[i, 'Density'])):
                    Recall = 1 - df.loc[i, 'FNR']
                    Precision = df.loc[i, 'Precision']
                    Density = df.loc[i, 'Density']
                flag,result_TP,result_TN,result_FP,result_FN = self.fun16(Recall,Precision,Density)
                if flag == 0:
                    TP = result_TP
                    TN = result_TN
                    FP = result_FP
                    FN = result_FN
                else:
                    TP = np.nan
                    TN = np.nan
                    FP = np.nan
                    FN = np.nan
            elif (not(np.isnan(df.loc[i,'Recall'])) and not(np.isnan(df.loc[i,'FMeasure'])) and not(np.isnan(df.loc[i,'Density'])))or(
                    not (np.isnan(df.loc[i, 'FNR'])) and not (np.isnan(df.loc[i, 'FMeasure'])) and not (np.isnan(df.loc[i, 'Density']))
            ):
                if not(np.isnan(df.loc[i,'Recall'])) and not(np.isnan(df.loc[i,'FMeasure'])) and not(np.isnan(df.loc[i,'Density'])):
                    Recall = df.loc[i,'Recall']
                    FMeasure = df.loc[i,'FMeasure']
                    Density = df.loc[i,'Density']
                elif not (np.isnan(df.loc[i, 'Recall'])) and not (np.isnan(df.loc[i, 'FMeasure'])) and not (np.isnan(df.loc[i, 'Density'])):
                    Recall = 1 - df.loc[i, 'FNR']
                    FMeasure = df.loc[i, 'FMeasure']
                    Density = df.loc[i, 'Density']
                flag,result_TP,result_TN,result_FP,result_FN = self.fun17(Recall,FMeasure,Density)
                if flag == 0:
                    TP = result_TP
                    TN = result_TN
                    FP = result_FP
                    FN = result_FN
                else:
                    TP = np.nan
                    TN = np.nan
                    FP = np.nan
                    FN = np.nan
            elif  (not(np.isnan(df.loc[i,'Accuracy'])) and not(np.isnan(df.loc[i,'Precision'])) and not(np.isnan(df.loc[i,'Density'])))or(
                    not (np.isnan(df.loc[i, 'FNR'])) and not (np.isnan(df.loc[i, 'Precision'])) and not (np.isnan(df.loc[i, 'Density']))
            ):
                if not(np.isnan(df.loc[i,'Accuracy'])) and not(np.isnan(df.loc[i,'Precision'])) and not(np.isnan(df.loc[i,'Density'])):
                    Accuracy = df.loc[i,'Accuracy']
                    Precision = df.loc[i,'Precision']
                    Density = df.loc[i,'Density']
                elif not (np.isnan(df.loc[i, 'FNR'])) and not (np.isnan(df.loc[i, 'Precision'])) and not (np.isnan(df.loc[i, 'Density'])):
                    Accuracy = 1 - df.loc[i, 'FNR']
                    Precision = df.loc[i, 'Precision']
                    Density = df.loc[i, 'Density']
                flag,result_TP,result_TN,result_FP,result_FN = self.fun18(Accuracy,Precision,Density)
                if flag == 0:
                    TP = result_TP
                    TN = result_TN
                    FP = result_FP
                    FN = result_FN
                else:
                    TP = np.nan
                    TN = np.nan
                    FP = np.nan
                    FN = np.nan
            elif  (not(np.isnan(df.loc[i,'Accuracy']))and not(np.isnan(df.loc[i,'FMeasure'])) and not(np.isnan(df.loc[i,'Density'])))or(
                    not (np.isnan(df.loc[i, 'FNR'])) and not (np.isnan(df.loc[i, 'FMeasure'])) and not (np.isnan(df.loc[i, 'Density']))
            ):
                if not(np.isnan(df.loc[i,'Accuracy']))and not(np.isnan(df.loc[i,'FMeasure'])) and not(np.isnan(df.loc[i,'Density'])):
                    Accuracy = df.loc[i,'Accuracy']
                    FMeasure = df.loc[i,'FMeasure']
                    Density = df.loc[i,'Density']
                elif not (np.isnan(df.loc[i, 'FNR'])) and not (np.isnan(df.loc[i, 'FMeasure'])) and not (np.isnan(df.loc[i, 'Density'])):
                    Accuracy = 1 - df.loc[i, 'FNR']
                    FMeasure = df.loc[i, 'FMeasure']
                    Density = df.loc[i, 'Density']
                flag,result_TP,result_TN,result_FP,result_FN = self.fun19(Accuracy,FMeasure,Density)
                if flag == 0:
                    TP = result_TP
                    TN = result_TN
                    FP = result_FP
                    FN = result_FN
                else:
                    TP = np.nan
                    TN = np.nan
                    FP = np.nan
                    FN = np.nan
            elif  not(np.isnan(df.loc[i,'Precision'])) and not(np.isnan(df.loc[i,'FMeasure'])) and not(np.isnan(df.loc[i,'Density'])):
                flag, result_TP, result_TN, result_FP, result_FN = self.fun20(df.loc[i, 'Precision'],
                                                                                  df.loc[i, 'FMeasure'],
                                                                                  df.loc[i, 'Density'])
                if flag == 0:
                    TP = result_TP
                    TN = result_TN
                    FP = result_FP
                    FN = result_FN
                else:
                    TP = np.nan
                    TN = np.nan
                    FP = np.nan
                    FN = np.nan


            flag,FPR = self.fun_FPR(FP,TN)
            if flag == 0:
                pass
            else:
                FPR = np.nan
            flag,FNR = self.fun_FNR(TP,FN)
            if flag == 0:
                pass
            else:
                FNR = np.nan
            flag,TNR = self.fun_TNR(TN,FP)
            if flag == 0:
                pass
            else:
                TNR = np.nan
            flag,ER = self.fun_ER(TN,TP,FN,FP)
            if flag == 0:
                pass
            else:
                ER = np.nan
            flag,Recall = self.fun_Recall(TP,FN)
            if flag == 0:
                pass
            else:
                Recall = np.nan
            flag,Precision = self.fun_Precision(TP,FP)
            if flag == 0:
                pass
            else:
                Precision = np.nan
            flag,Accuracy = self.fun_Accuracy(TP,TN,FP,FN)
            if flag == 0:
                pass
            else:
                Accuracy = np.nan
            flag,FMeasure = self.fun_FMeasure(TP,FP,FN)
            if flag == 0:
                pass
            else:
                FMeasure = np.nan
            flag,MCC = self.fun_MCC(TP,TN,FP,FN)
            if flag == 0:
                pass
            else:
                MCC = np.nan
            flag,GMeasure = self.fun_GMeasure(TP,FN,TN,FP)
            if flag == 0:
                pass
            else:
                GMeasure = np.nan
            flag,GMean = self.fun_GMean(TP,FN,TN,FP)
            if flag == 0:
                pass
            else:
                GMean = np.nan
            flag,Balance = self.fun_Balance(TP,FN,FP,TN)
            if flag == 0:
                pass
            else:
                Balance = np.nan
            Density = self.fun_Density(TP,FN)
            data.append({"TP":round(TP,4),
                    'TN':round(TN,4),
                    'FP':round(FP,4),
                    'FN':round(FN,4),
                   'FPR':round(FPR,4),
                   'FNR':round(FNR,4),
                   'TNR':round(TNR,4),
                   'ER':round(ER,4),
                   'Recall':round(Recall,4),
                   'Precision':round(Precision,4),
                   'Accuracy':round(Accuracy,4),
                   'FMeasure':round(FMeasure,4),
                   'MCC':round(MCC,4),
                   'GMeasure':round(GMeasure,4),
                    'GMean':round(GMean,4),
                   'Balance':round(Balance,4),
                   'Density':round(Density,4)})

        df_output = pd.DataFrame(data,columns=["TP",
                'TN',
                'FP',
                'FN',
               'FPR',
               'FNR',
               'TNR',
               'ER',
               'Recall',
               'Precision',
               'Accuracy',
               'FMeasure',
               'MCC',
               'GMeasure',
               'GMean',
               'Balance',
               'Density'])
        try:
            df_output.to_excel(self.lineEdit_8.text()+"/output.xlsx")
        except PermissionError:
            QMessageBox.information(self,"文件拒绝访问","输出文件拒绝访问")


    def findOutputDir(self):
        dir = QFileDialog.getExistingDirectory(self,
                  "浏览",
                  self.cwd)  # 起始路径
        self.lineEdit_8.setText(dir)

    def findInputFilename(self):
        self.fileName,filetype= QFileDialog.getOpenFileName(self,
                                    "浏览",
                                    self.cwd,  # 起始路径
                                    "All Files (*);;Excel Files (*.xlsx)")  # 设置文件扩展名过滤,用双分号间隔
        self.lineEdit_7.setText(self.fileName)
        self.lineEdit_8.setText(os.path.dirname(self.fileName))

    def setThreshold(self):
        self.lineEdit_5.setReadOnly(False)
        self.lineEdit_6.setReadOnly(False)

    def getThresholdDefault(self):
        self.lineEdit_5.setText("0.05")
        self.lineEdit_6.setText("0.1")
        self.lineEdit_5.setReadOnly(True)
        self.lineEdit_6.setReadOnly(True)

    def getConfusionMatrix(self):
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        FPR = self.lineEdit_9.text()
        FNR = self.lineEdit_10.text()
        TNR = self.lineEdit_11.text()
        ER = self.lineEdit_12.text()
        Recall = self.lineEdit_13.text()
        Precision = self.lineEdit_14.text()
        Accuracy = self.lineEdit_15.text()
        FMeasure = self.lineEdit_16.text()
        MCC = self.lineEdit_17.text()
        GMeasure = self.lineEdit_18.text()
        GMean = self.lineEdit_19.text()
        Balance = self.lineEdit_20.text()
        Density = self.lineEdit_21.text()
        dictError = {}


    ## fun1
        if FPR == ''  and FNR == ''and TNR == '' and ER == ''and Recall == ''and Precision == ''and Accuracy == ''and FMeasure == ''and MCC == ''and GMeasure == ''and GMean == ''and Balance == ''and Density == '':
            QMessageBox.information(self,"错误","请在预测性能框内输入数字")
            pass
        else:
            if (FPR != '' and Recall != '' and Accuracy != '') or (FPR!='' and Recall!=''and ER!='')or (FPR!='' and FNR!=''and ER!='')or(FPR!='' and FNR!=''and Accuracy!='')or (
                    TNR != '' and Recall != '' and Accuracy != '')or(TNR!='' and Recall!=''and ER!='')or(TNR!='' and FNR!=''and ER!='')or (TNR!='' and FNR!=''and Accuracy!=''):
                if (FPR != '' and Recall != '' and Accuracy != ''):
                    FPR = float(FPR)
                    Recall = float(Recall)
                    Accuracy = float(Accuracy)
                    dictError["FPR,Recall,Accuracy"] = ""
                elif (FPR!='' and Recall!=''and ER!=''):
                    FPR = float(FPR)
                    Recall = float(Recall)
                    Accuracy = 1-float(ER)
                    dictError["FPR,Recall,ER"] = ""
                elif (FPR!='' and FNR!=''and ER!=''):
                    FPR = float(FPR)
                    Recall = 1- float(FNR)
                    Accuracy = 1 - float(ER)
                    dictError["FPR,FNR,ER"] = ""
                elif (FPR!='' and FNR!=''and Accuracy!=''):
                    FPR = float(FPR)
                    Recall = 1-float(FNR)
                    Accuracy = float(Accuracy)
                    dictError["FPR,FNR,Accuracy"] = ""
                elif TNR != '' and Recall != '' and Accuracy != '':
                    FPR = 1-float(TNR)
                    Recall = float(Recall)
                    Accuracy = float(Accuracy)
                    dictError["TNR,Recall,Accuracy"] = ""
                elif (TNR!='' and Recall!=''and ER!=''):
                    FPR = 1 - float(TNR)
                    Recall = float(Recall)
                    Accuracy = 1-float(ER)
                    dictError["TNR,Recall,ER"] = ""
                elif (TNR!='' and FNR!=''and ER!=''):
                    FPR = 1 - float(TNR)
                    Recall = 1-float(FNR)
                    Accuracy = 1 - float(ER)
                    dictError["TNR,FNR,ER"] = ""
                elif (TNR != '' and FNR != '' and Accuracy != ''):
                    FPR = 1 - float(TNR)
                    Recall = 1 - float(FNR)
                    Accuracy =float(Accuracy)
                    dictError["TNR,FNR,Accuracy"] = ""
                flag,result_TP, result_TN, result_FP, result_FN = self.fun1(FPR, Recall, Accuracy)
                if self.lineEdit.text() != '' and self.lineEdit_2.text() != '' and self.lineEdit_3.text() != '' and self.lineEdit_4.text() != '':
                    pass
                elif flag == 0:
                    self.lineEdit.setText(str(result_TP))
                    self.lineEdit_2.setText(str(result_FP))
                    self.lineEdit_3.setText(str(result_FN))
                    self.lineEdit_4.setText(str(result_TN))
                elif flag ==1:
                    dictError[list(dictError.keys())[-1]] = "d=N/N,但是无结果"
                elif flag == 2 :
                    dictError[list(dictError.keys())[-1]]= "d=N/0,表明原始数据有错误"
                elif flag == 3 :
                    dictError[list(dictError.keys())[-1]]="d=0,表明原始数据有错误"
                elif flag == 4:
                    dictError[list(dictError.keys())[-1]]="d=0/0,无法计算混淆矩阵"
                else:
                    dictError[list(dictError.keys())[-1]] ="原始数据有错误"

            ## fun2
            if (FPR != '' and Recall != ''and Precision != '')or(
                FPR != '' and FNR != ''and Precision != '')or(
                TNR != '' and Recall != '' and Precision != '')or(
                TNR != '' and FNR != '' and Precision != ''
            ):
                if (FPR != '' and Recall != ''and Precision != ''):
                    FPR = float(FPR)
                    Recall = float(Recall)
                    Precision = float(Precision)
                    dictError["FPR,Recall,Precision"] = ""
                elif (FPR != '' and FNR != ''and Precision != ''):
                    FPR = float(FPR)
                    Recall = 1-float(FNR)
                    Precision = float(Precision)
                    dictError["FPR,FNR,Precision"] = ""
                elif TNR != '' and Recall != '' and Precision != '':
                    FPR = 1-float(TNR)
                    Recall = float(Recall)
                    Precision = float(Precision)
                    dictError["FPR,Recall,Precision"] = ""
                elif TNR != '' and FNR != '' and Precision != '':
                    FPR = 1 - float(TNR)
                    Recall = 1-float(FNR)
                    Precision = float(Precision)
                    dictError["TNR,FNR,Precision"] = ""
                flag,result_TP,result_TN,result_FP,result_FN = self.fun2(FPR, Recall, Precision)
                if self.lineEdit.text() != '' and self.lineEdit_2.text() != '' and self.lineEdit_3.text() != '' and self.lineEdit_4.text() != '':
                    pass
                elif flag == 0:
                    self.lineEdit.setText(str(result_TP))
                    self.lineEdit_2.setText(str(result_FP))
                    self.lineEdit_3.setText(str(result_FN))
                    self.lineEdit_4.setText(str(result_TN))
                elif flag ==1:
                    dictError[list(dictError.keys())[-1]] = "d=N/N,但是无结果"
                elif flag == 2:
                    dictError[list(dictError.keys())[-1]]= "d=N/0,表明原始数据有错误"
                elif flag == 3:
                    dictError[list(dictError.keys())[-1]]="d=0,表明原始数据有错误"
                elif flag == 4:
                    dictError[list(dictError.keys())[-1]] ="d=0/0,无法计算混淆矩阵"
                else:
                    dictError[list(dictError.keys())[-1]] = "原始数据有错误"


    ## fun3
            if (FPR != '' and Recall != ''and FMeasure != '')or(
                FPR != '' and FNR != ''and FMeasure != '')or(
                TNR != '' and Recall != ''and FMeasure != '')or(
                TNR != '' and FNR != '' and FMeasure != ''
            ):
                if (FPR != '' and Recall != ''and FMeasure != ''):
                    FPR = float(FPR)
                    Recall = float(Recall)
                    FMeasure = float(FMeasure)
                    dictError["FPR,Recall,FMeasure"] = ""
                elif (FPR != '' and FNR != ''and FMeasure != ''):
                    FPR = float(FPR)
                    Recall = 1-float(FNR)
                    FMeasure = float(FMeasure)
                    dictError["FPR,FNR,FMeasure"] = ""
                elif (TNR != '' and Recall != ''and FMeasure != ''):
                    FPR = 1-float(TNR)
                    Recall = float(Recall)
                    FMeasure = float(FMeasure)
                    dictError["TNR,Recall,FMeasure"] = ""
                elif TNR != '' and FNR != '' and FMeasure != '':
                    FPR = 1 - float(TNR)
                    Recall = 1-float(FNR)
                    FMeasure = float(FMeasure)
                    dictError["TNR,FNR,FMeasure"] = ""
                flag,result_TP,result_TN,result_FP,result_FN = self.fun3(FPR, Recall, FMeasure)
                if self.lineEdit.text() != '' and self.lineEdit_2.text() != '' and self.lineEdit_3.text() != '' and self.lineEdit_4.text() != '':
                    pass
                elif flag == 0:
                    self.lineEdit.setText(str(result_TP))
                    self.lineEdit_2.setText(str(result_FP))
                    self.lineEdit_3.setText(str(result_FN))
                    self.lineEdit_4.setText(str(result_TN))
                elif flag ==1:
                    dictError[list(dictError.keys())[-1]] = "d=N/N,但是无结果"
                elif flag == 2:
                    dictError[list(dictError.keys())[-1]] = "d=N/0,表明原始数据有错误"
                elif flag == 3:
                    dictError[list(dictError.keys())[-1]] = "d=0,表明原始数据有错误"
                elif flag == 4:
                    dictError[list(dictError.keys())[-1]] = "d=0/0,无法计算混淆矩阵"
                else:
                    dictError[list(dictError.keys())[-1]] = "原始数据有错误"

            #fun4
            if (FPR != '' and Accuracy != '' and Precision != '')or(
                FPR != '' and ER != '' and Precision != '')or(
                TNR != '' and Accuracy != '' and Precision != '')or(
                TNR != '' and ER != '' and Precision != ''
            ):
                if FPR != '' and Accuracy != '' and Precision != '':
                    FPR = float(FPR)
                    Accuracy = float(Accuracy)
                    Precision = float(Precision)
                    dictError["FPR,Accuracy,Precision"] = ""
                elif FPR != '' and ER != '' and Precision != '':
                    FPR = float(FPR)
                    Accuracy = 1-float(ER)
                    Precision = float(Precision)
                    dictError["FPR,ER,Precision"] = ""
                elif TNR != '' and Accuracy != '' and Precision != '':
                    FPR = 1-float(TNR)
                    Accuracy = float(Accuracy)
                    Precision = float(Precision)
                    dictError["TNR,Accuracy,Precision"] = ""
                elif TNR != '' and ER != '' and Precision != '':
                    FPR = 1-float(TNR)
                    Accuracy = 1-float(ER)
                    Precision = float(Precision)
                    dictError["TNR,ER,Precision"] = ""
                flag,result_TP,result_TN,result_FP,result_FN = self.fun4(FPR, Accuracy, Precision)
                if self.lineEdit.text() != '' and self.lineEdit_2.text() != '' and self.lineEdit_3.text() != '' and self.lineEdit_4.text() != '':
                    pass
                elif flag == 0:
                    self.lineEdit.setText(str(result_TP))
                    self.lineEdit_2.setText(str(result_FP))
                    self.lineEdit_3.setText(str(result_FN))
                    self.lineEdit_4.setText(str(result_TN))
                elif flag ==1:
                    dictError[list(dictError.keys())[-1]] = "d=N/N,但是无结果"
                elif flag == 2:
                    dictError[list(dictError.keys())[-1]] = "d=N/0,表明原始数据有错误"
                elif flag == 3:
                    dictError[list(dictError.keys())[-1]] = "d=0,表明原始数据有错误"
                elif flag == 4:
                    dictError[list(dictError.keys())[-1]] = "d=0/0,无法计算混淆矩阵"
                else:
                    dictError[list(dictError.keys())[-1]] = "原始数据有错误"

            #fun 5
            if (FPR != '' and Accuracy != '' and FMeasure != '')or(
                FPR != '' and ER != '' and FMeasure != '')or(
                TNR != '' and Accuracy != '' and FMeasure != '')or(
                TNR != '' and ER != '' and FMeasure != ''
            ):
                if FPR != '' and Accuracy != '' and FMeasure != '':
                    FPR = float(FPR)
                    Accuracy = float(Accuracy)
                    FMeasure = float(FMeasure)
                    dictError["FPR,Accuracy,FMeasure"] = ""
                elif FPR != '' and ER != '' and FMeasure != '':
                    FPR = float(FPR)
                    Accuracy = 1-float(ER)
                    FMeasure = float(FMeasure)
                    dictError["FPR,ER,FMeasure"] = ""
                elif TNR != '' and Accuracy != '' and FMeasure != '':
                    FPR = 1-float(TNR)
                    Accuracy = float(Accuracy)
                    FMeasure = float(FMeasure)
                    dictError["TNR,Accuracy,FMeasure"] = ""
                elif TNR != '' and ER != '' and FMeasure != '':
                    FPR = 1 - float(TNR)
                    Accuracy = 1-float(ER)
                    FMeasure = float(FMeasure)
                    dictError["TNR,ER,FMeasure"] = ""
                flag,result_TP,result_TN,result_FP,result_FN = self.fun5(FPR, Accuracy, FMeasure)
                if self.lineEdit.text() != '' and self.lineEdit_2.text() != '' and self.lineEdit_3.text() != '' and self.lineEdit_4.text() != '':
                    pass
                elif flag == 0:
                    self.lineEdit.setText(str(result_TP))
                    self.lineEdit_2.setText(str(result_FP))
                    self.lineEdit_3.setText(str(result_FN))
                    self.lineEdit_4.setText(str(result_TN))
                elif flag ==1:
                    dictError[list(dictError.keys())[-1]] = "d=N/N,但是无结果"
                elif flag == 2:
                    dictError[list(dictError.keys())[-1]] = "d=N/0,表明原始数据有错误"
                elif flag == 3:
                    dictError[list(dictError.keys())[-1]] = "d=0,表明原始数据有错误"
                elif flag == 4:
                    dictError[list(dictError.keys())[-1]] = "d=0/0,无法计算混淆矩阵"
                else:
                    dictError[list(dictError.keys())[-1]] = "原始数据有错误"

            #fun 6
            if (FPR != '' and Precision != ''and FMeasure != '')or(
                TNR != '' and Precision != '' and FMeasure != ''
            ):
                if FPR != '' and Precision != ''and FMeasure != '':
                    FPR = float(FPR)
                    Precision = float(Precision)
                    FMeasure = float(FMeasure)
                    dictError["FPR,Precision,FMeasure"] = ""
                elif TNR != '' and Precision != '' and FMeasure != '':
                    FPR = 1-float(TNR)
                    Precision = float(Precision)
                    FMeasure = float(FMeasure)
                    dictError["TNR,Precision,FMeasure"] = ""
                flag,result_TP,result_TN,result_FP,result_FN = self.fun6(FPR, Precision, FMeasure)
                if self.lineEdit.text() != '' and self.lineEdit_2.text() != '' and self.lineEdit_3.text() != '' and self.lineEdit_4.text() != '':
                    pass
                elif flag == 0:
                    self.lineEdit.setText(str(result_TP))
                    self.lineEdit_2.setText(str(result_FP))
                    self.lineEdit_3.setText(str(result_FN))
                    self.lineEdit_4.setText(str(result_TN))
                elif flag ==1:
                    dictError[list(dictError.keys())[-1]] = "d=N/N,但是无结果"
                elif flag == 2:
                    dictError[list(dictError.keys())[-1]] = "d=N/0,表明原始数据有错误"
                elif flag ==3:
                    dictError[list(dictError.keys())[-1]] = "d=0,表明原始数据有错误"
                elif flag ==4:
                    dictError[list(dictError.keys())[-1]] = "d=0/0,无法计算混淆矩阵"
                else:
                    dictError[list(dictError.keys())[-1]] = "原始数据有错误"

            #fun7
            if (Recall != '' and Accuracy != ''and Precision != '')or(
                Recall != '' and ER != '' and Precision != '')or(
                FNR != '' and Accuracy != '' and Precision != '')or(
                FNR != '' and ER != '' and Precision != ''
            ):
                if  Recall != '' and Accuracy != ''and Precision != '':
                    Recall = float(Recall)
                    Accuracy = float(Accuracy)
                    Precision = float(Precision)
                    dictError["Recall,Accuracy,Precision"] = ""
                elif Recall != '' and ER != '' and Precision != '':
                    Recall = float(Recall)
                    Accuracy = 1-float(ER)
                    Precision = float(Precision)
                    dictError["Recall,ER,Precision"] = ""
                elif FNR != '' and Accuracy != '' and Precision != '':
                    Recall = 1-float(FNR)
                    Accuracy = float(Accuracy)
                    Precision = float(Precision)
                    dictError["FNR,Accuracy,Precision"] = ""
                elif FNR != '' and ER != '' and Precision != '':
                    Recall = 1 - float(FNR)
                    Accuracy = 1-float(ER)
                    Precision = float(Precision)
                    dictError["FNR,ER,Precision"] = ""
                flag,result_TP,result_TN,result_FP,result_FN = self.fun7(Recall, Accuracy, Precision)
                if self.lineEdit.text() != '' and self.lineEdit_2.text() != '' and self.lineEdit_3.text() != '' and self.lineEdit_4.text() != '':
                    pass
                elif flag == 0:
                    self.lineEdit.setText(str(result_TP))
                    self.lineEdit_2.setText(str(result_FP))
                    self.lineEdit_3.setText(str(result_FN))
                    self.lineEdit_4.setText(str(result_TN))
                elif flag ==1:
                    dictError[list(dictError.keys())[-1]] = "d=N/N,但是无结果"
                elif flag == 2:
                    dictError[list(dictError.keys())[-1]] = "d=N/0,表明原始数据有错误"
                elif flag == 3:
                    dictError[list(dictError.keys())[-1]] = "d=0,表明原始数据有错误"
                elif flag == 4:
                    dictError[list(dictError.keys())[-1]] = "d=0/0,无法计算混淆矩阵"
                else:
                    dictError[list(dictError.keys())[-1]] = "原始数据有错误"

            #fun 8
            if (Recall != '' and Accuracy != ''and FMeasure != '')or(
                Recall != '' and ER != '' and FMeasure != '')or(
                FNR != '' and Accuracy != '' and FMeasure != '')or(
                FNR != '' and ER != '' and FMeasure != ''
            ):
                if Recall != '' and Accuracy != ''and FMeasure != '':
                    Recall = float(Recall)
                    Accuracy = float(Accuracy)
                    FMeasure = float(FMeasure)
                    dictError["Recall,Accuracy,FMeasure"] = ""
                elif Recall != '' and ER != '' and FMeasure != '':
                    Recall = float(Recall)
                    Accuracy = 1- float(ER)
                    FMeasure = float(FMeasure)
                    dictError["Recall,ER,FMeasure"] = ""
                elif FNR != '' and Accuracy != '' and FMeasure != '':
                    Recall = 1-float(FNR)
                    Accuracy = float(Accuracy)
                    FMeasure = float(FMeasure)
                    dictError["FNR,Accuracy,FMeasure"] = ""
                elif FNR != '' and ER != '' and FMeasure != '':
                    Recall = 1-float(FNR)
                    Accuracy = 1-float(ER)
                    FMeasure = float(FMeasure)
                    dictError["FNR,ER,FMeasure"] = ""
                flag,result_TP,result_TN,result_FP,result_FN = self.fun8(Recall, Accuracy, FMeasure)
                if self.lineEdit.text() != '' and self.lineEdit_2.text() != '' and self.lineEdit_3.text() != '' and self.lineEdit_4.text() != '':
                    pass
                elif flag == 0:
                    self.lineEdit.setText(str(result_TP))
                    self.lineEdit_2.setText(str(result_FP))
                    self.lineEdit_3.setText(str(result_FN))
                    self.lineEdit_4.setText(str(result_TN))
                elif flag ==1:
                    dictError[list(dictError.keys())[-1]] = "d=N/N,但是无结果"
                elif flag == 2:
                    dictError[list(dictError.keys())[-1]] = "d=N/0,表明原始数据有错误"
                elif flag == 3:
                    dictError[list(dictError.keys())[-1]] = "d=0,表明原始数据有错误"
                elif flag == 4:
                    dictError[list(dictError.keys())[-1]] = "d=0/0,无法计算混淆矩阵"
                else:
                    dictError[list(dictError.keys())[-1]] = "原始数据有错误"

            # fun 9
            if (Precision != '' and Accuracy != '' and FMeasure != '')or(
                Precision != '' and ER != '' and FMeasure != ''):
                if Precision != '' and Accuracy != '' and FMeasure != '':
                    Precision = float(Precision)
                    Accuracy = float(Accuracy)
                    FMeasure = float(FMeasure)
                    dictError["Precision,Accuracy,FMeasure"] = ""
                elif Precision != '' and ER != '' and FMeasure != '':
                    Precision = float(Precision)
                    Accuracy = 1-float(ER)
                    FMeasure = float(FMeasure)
                    dictError["Precision,ER,FMeasure"] = ""
                flag,result_TP,result_TN,result_FP,result_FN = self.fun9(Precision, Accuracy, FMeasure)
                if self.lineEdit.text() != '' and self.lineEdit_2.text() != '' and self.lineEdit_3.text() != '' and self.lineEdit_4.text() != '':
                    pass
                elif flag == 0:
                    self.lineEdit.setText(str(result_TP))
                    self.lineEdit_2.setText(str(result_FP))
                    self.lineEdit_3.setText(str(result_FN))
                    self.lineEdit_4.setText(str(result_TN))
                elif flag ==1:
                    dictError[list(dictError.keys())[-1]] = "d=N/N,但是无结果"
                elif flag == 2:
                    dictError[list(dictError.keys())[-1]] = "d=N/0,表明原始数据有错误"
                elif flag == 3:
                    dictError[list(dictError.keys())[-1]] = "d=0,表明原始数据有错误"
                elif flag == 4:
                    dictError[list(dictError.keys())[-1]] = "d=0/0,无法计算混淆矩阵"
                else:
                    dictError[list(dictError.keys())[-1]] = "原始数据有错误"


            # 下面十种是两个参数求解
            #fun11
            if (FPR != '' and Recall != '' and Density != '')or(
                FPR != '' and FNR != '' and Density != '')or(
                TNR != '' and Recall != '' and Density != '')or(
                TNR != '' and FNR != '' and Density != ''
            ):
                if FPR != '' and Recall != '' and Density != '':
                    FPR = float(FPR)
                    Recall = float(Recall)
                    Density = float(Density)
                    dictError["FPR,Recall,Density"] = ""
                elif FPR != '' and FNR != '' and Density != '':
                    FPR = float(FPR)
                    Recall = 1-float(FNR)
                    Density = float(Density)
                elif TNR != '' and Recall != '' and Density != '':
                    FPR = 1-float(TNR)
                    Recall = float(Recall)
                    Density = float(Density)
                elif TNR != '' and FNR != '' and Density != '':
                    FPR = 1 - float(TNR)
                    Recall = 1-float(FNR)
                    Density = float(Density)
                flag,result_TP,result_TN,result_FP,result_FN = self.fun11(FPR, Recall, Density)
                if self.lineEdit.text() != '' and self.lineEdit_2.text() != '' and self.lineEdit_3.text() != '' and self.lineEdit_4.text() != '':
                    pass
                elif flag == 0:
                    self.lineEdit.setText(str(result_TP))
                    self.lineEdit_2.setText(str(result_FP))
                    self.lineEdit_3.setText(str(result_FN))
                    self.lineEdit_4.setText(str(result_TN))
                elif flag == 1:
                    dictError[list(dictError.keys())[-1]] = "d=N/N,但是无结果"

            #fun12
            if (FPR != '' and Accuracy != '' and Density != '')or(
                FPR != '' and FNR != '' and Density != '')or(
                TNR != '' and Accuracy != '' and Density != '')or(
                TNR != '' and FNR != '' and Density != ''
            ):
                if FPR != '' and Accuracy != '' and Density != '':
                    FPR = float(FPR)
                    Accuracy = float(Accuracy)
                    Density = float(Density)
                elif FPR != '' and FNR != '' and Density != '':
                    FPR = float(FPR)
                    Accuracy = 1-float(FNR)
                    Density = float(Density)
                elif TNR != '' and Accuracy != '' and Density != '':
                    FPR = 1-float(TNR)
                    Accuracy = float(Accuracy)
                    Density = float(Density)
                elif TNR != '' and FNR != '' and Density != '':
                    FPR = 1 - float(TNR)
                    Accuracy = 1 - float(FNR)
                    Density = float(Density)
                flag,result_TP,result_TN,result_FP,result_FN = self.fun12(FPR, Accuracy, Density)
                if self.lineEdit.text() != '' and self.lineEdit_2.text() != '' and self.lineEdit_3.text() != '' and self.lineEdit_4.text() != '':
                    pass
                elif flag == 0:
                    self.lineEdit.setText(str(result_TP))
                    self.lineEdit_2.setText(str(result_FP))
                    self.lineEdit_3.setText(str(result_FN))
                    self.lineEdit_4.setText(str(result_TN))
                elif flag == 1:
                    dictError[list(dictError.keys())[-1]] = "d=N/N,但是无结果"

            #fun 13
            if (FPR != '' and Precision != '' and Density != '')or(
                TNR != '' and Precision != '' and Density != ''
            ):
                if FPR != '' and Precision != '' and Density != '':
                    FPR = float(FPR)
                    Precision = float(Precision)
                    Density = float(Density)
                    dictError["FPR,Precision,Density"] = ""
                elif TNR != '' and Precision != '' and Density != '':
                    FPR = 1-float(TNR)
                    Precision = float(Precision)
                    Density = float(Density)
                    dictError["TNR,Precision,Density"] = ""
                flag,result_TP,result_TN,result_FP,result_FN = self.fun13(FPR, Precision, Density)
                if self.lineEdit.text() != '' and self.lineEdit_2.text() != '' and self.lineEdit_3.text() != '' and self.lineEdit_4.text() != '':
                    pass
                elif flag == 0:
                    self.lineEdit.setText(str(result_TP))
                    self.lineEdit_2.setText(str(result_FP))
                    self.lineEdit_3.setText(str(result_FN))
                    self.lineEdit_4.setText(str(result_TN))
                elif flag == 1:
                    dictError[list(dictError.keys())[-1]] = "d=N/N,但是无结果"
                elif flag == 2:
                    dictError[list(dictError.keys())[-1]] = "TP=N/0,表明原始数据有错误"
                elif flag == 3:
                    dictError[list(dictError.keys())[-1]] = "TP=0/0,表明原始数据有错误"
                else:
                    dictError[list(dictError.keys())[-1]] = "原始数据有错误"

            #fun14
            if (FPR != '' and FMeasure != '' and Density != '')or(
                TNR != '' and FMeasure != '' and Density != ''
            ):
                if FPR != '' and FMeasure != '' and Density != '':
                    FPR =float(FPR)
                    FMeasure = float(FMeasure)
                    Density = float(Density)
                elif TNR != '' and FMeasure != '' and Density != '':
                    FPR = 1-float(TNR)
                    FMeasure = float(FMeasure)
                    Density = float(Density)
                flag,result_TP,result_TN,result_FP,result_FN = self.fun14(FPR, FMeasure, Density)
                if self.lineEdit.text() != '' and self.lineEdit_2.text() != '' and self.lineEdit_3.text() != '' and self.lineEdit_4.text() != '':
                    pass
                elif flag == 0:
                    self.lineEdit.setText(str(result_TP))
                    self.lineEdit_2.setText(str(result_FP))
                    self.lineEdit_3.setText(str(result_FN))
                    self.lineEdit_4.setText(str(result_TN))
                elif flag == 1:
                    dictError[list(dictError.keys())[-1]] = "d=N/N,但是无结果"

            #fun15
            if (Recall != '' and Accuracy != '' and Density != '')or(
                Recall != '' and ER != '' and Density != '')or(
                FNR != '' and Accuracy != '' and Density != '')or(
                FNR != '' and ER != '' and Density != ''
            ):
                if Recall != '' and Accuracy != '' and Density != '':
                    Recall = float(Recall)
                    Accuracy = float(Accuracy)
                    Density =float(Density)
                elif Recall != '' and ER != '' and Density != '':
                    Recall = float(Recall)
                    Accuracy = 1-float(ER)
                    Density = float(Density)
                elif FNR != '' and Accuracy != '' and Density != '':
                    Recall = 1-float(FNR)
                    Accuracy = float(Accuracy)
                    Density = float(Density)
                elif FNR != '' and ER != '' and Density != '':
                    Recall = 1-float(FNR)
                    Accuracy = 1 - float(ER)
                    Density = float(Density)
                flag,result_TP,result_TN,result_FP,result_FN = self.fun15(Recall, Accuracy, Density)
                if self.lineEdit.text() != '' and self.lineEdit_2.text() != '' and self.lineEdit_3.text() != '' and self.lineEdit_4.text() != '':
                    pass
                elif flag == 0:
                    self.lineEdit.setText(str(result_TP))
                    self.lineEdit_2.setText(str(result_FP))
                    self.lineEdit_3.setText(str(result_FN))
                    self.lineEdit_4.setText(str(result_TN))
                elif flag == 1:
                    dictError[list(dictError.keys())[-1]] = "d=N/N,但是无结果"

            #fun16
            if (Recall != '' and Precision != '' and Density != '')or(
                FNR != '' and Precision != '' and Density != ''
            ):
                if Recall != '' and Precision != '' and Density != '':
                    Recall = float(Recall)
                    Precision = float(Precision)
                    Density = float(Density)
                    dictError["Recall,Precision,Density"] = ""
                elif FNR != '' and Precision != '' and Density != '':
                    Recall = 1-float(FNR)
                    Precision = float(Precision)
                    Density = float(Density)
                    dictError["FNR,Precision,Density"] = ""
                flag,result_TP,result_TN,result_FP,result_FN = self.fun16(Recall, Precision, Density)
                if self.lineEdit.text() != '' and self.lineEdit_2.text() != '' and self.lineEdit_3.text() != '' and self.lineEdit_4.text() != '':
                    pass
                elif flag == 0:
                    self.lineEdit.setText(str(result_TP))
                    self.lineEdit_2.setText(str(result_FP))
                    self.lineEdit_3.setText(str(result_FN))
                    self.lineEdit_4.setText(str(result_TN))
                elif flag == 1:
                    dictError[list(dictError.keys())[-1]] = "d=N/N,但是无结果"
                elif flag == 2:
                    dictError[list(dictError.keys())[-1]] = "FP=N/0,表明原始数据有错误"
                elif flag == 3:
                    dictError[list(dictError.keys())[-1]] = "FP=0/0,表明原始数据有错误"
                else:
                    dictError[list(dictError.keys())[-1]] = "原始数据有错误"

            #fun17
            if (Recall != '' and FMeasure != '' and Density != '')or(
                FNR != '' and FMeasure != '' and Density != ''
            ):
                if Recall != '' and FMeasure != '' and Density != '':
                    Recall = float(Recall)
                    FMeasure = float(FMeasure)
                    Density = float(Density)
                    dictError["Recall,FMeasure,Density"] = ""
                elif FNR != '' and FMeasure != '' and Density != '':
                    Recall = 1-float(FNR)
                    FMeasure = float(FMeasure)
                    Density = float(Density)
                    dictError["FNR,FMeasure,Density"] = ""
                flag,result_TP,result_TN,result_FP,result_FN = self.fun17(Recall, FMeasure, Density)
                if self.lineEdit.text() != '' and self.lineEdit_2.text() != '' and self.lineEdit_3.text() != '' and self.lineEdit_4.text() != '':
                    pass
                elif flag == 0:
                    self.lineEdit.setText(str(result_TP))
                    self.lineEdit_2.setText(str(result_FP))
                    self.lineEdit_3.setText(str(result_FN))
                    self.lineEdit_4.setText(str(result_TN))
                elif flag == 1:
                    dictError[list(dictError.keys())[-1]] = "d=N/N,但是无结果"
                elif flag == 2:
                    dictError[list(dictError.keys())[-1]] = "FP=N/0,表明原始数据有错误"
                elif flag == 3:
                    dictError[list(dictError.keys())[-1]] = "FP=0/0,表明原始数据有错误"
                else:
                    dictError[list(dictError.keys())[-1]] = "原始数据有错误"

            #fun18
            if (Accuracy != '' and Precision != '' and Density != '')or(
                ER != '' and Precision != '' and Density != ''
            ):
                if Accuracy != '' and Precision != '' and Density != '':
                    Accuracy = float(Accuracy)
                    Precision = float(Precision)
                    Density = float(Density)
                    dictError["Accuracy,Precision,Density"] = ""
                elif ER != '' and Precision != '' and Density != '':
                    Accuracy = 1-float(ER)
                    Precision = float(Precision)
                    Density = float(Density)
                    dictError["ER,Precision,Density"] = ""
                flag,result_TP,result_TN,result_FP,result_FN = self.fun18(Accuracy, Precision, Density)
                if self.lineEdit.text() != '' and self.lineEdit_2.text() != '' and self.lineEdit_3.text() != '' and self.lineEdit_4.text() != '':
                    pass
                elif flag == 0:
                    self.lineEdit.setText(str(result_TP))
                    self.lineEdit_2.setText(str(result_FP))
                    self.lineEdit_3.setText(str(result_FN))
                    self.lineEdit_4.setText(str(result_TN))
                elif flag == 1:
                    dictError[list(dictError.keys())[-1]] = "d=N/N,但是无结果"
                elif flag == 2:
                    dictError[list(dictError.keys())[-1]] = "TP=N/0,表明原始数据有错误"
                elif flag == 3:
                    dictError[list(dictError.keys())[-1]] = "TP=0/0,表明原始数据有错误"
                else:
                    dictError[list(dictError.keys())[-1]] = "原始数据有错误"

            #fun19
            if (Accuracy != '' and FMeasure != '' and Density != '')or(
                ER != '' and FMeasure != '' and Density != ''
            ):
                if Accuracy != '' and FMeasure != '' and Density != '':
                    Accuracy = float(Accuracy)
                    FMeasure = float(FMeasure)
                    Density = float(Density)
                    dictError["Accuracy,FMeasure,Density"] = ""
                elif ER != '' and FMeasure != '' and Density != '':
                    Accuracy = 1-float(ER)
                    FMeasure = float(FMeasure)
                    Density = float(Density)
                    dictError["ER,FMeasure,Density"] = ""
                flag,result_TP,result_TN,result_FP,result_FN = self.fun19(Accuracy, FMeasure, Density)
                if self.lineEdit.text() != '' and self.lineEdit_2.text() != '' and self.lineEdit_3.text() != '' and self.lineEdit_4.text() != '':
                    pass
                elif flag == 0:
                    self.lineEdit.setText(str(result_TP))
                    self.lineEdit_2.setText(str(result_FP))
                    self.lineEdit_3.setText(str(result_FN))
                    self.lineEdit_4.setText(str(result_TN))
                elif flag == 1:
                    dictError[list(dictError.keys())[-1]] = "TP=N/N,但是无结果"
                elif flag == 2:
                    dictError[list(dictError.keys())[-1]] = "TP=N/0,表明原始数据有错误"
                elif flag == 3:
                    dictError[list(dictError.keys())[-1]] = "TP=0/0,表明原始数据有错误"
                else:
                    dictError[list(dictError.keys())[-1]] = "原始数据有错误"

            #fun20
            if (Precision != '' and FMeasure != '' and Density != ''):
                dictError["Precision,FMeasure,Density"] = ""
                flag,result_TP,result_TN,result_FP,result_FN = self.fun20(Precision, FMeasure, Density)
                if self.lineEdit.text() != '' and self.lineEdit_2.text() != '' and self.lineEdit_3.text() != '' and self.lineEdit_4.text() != '':
                    pass
                elif flag == 0:
                    self.lineEdit.setText(str(result_TP))
                    self.lineEdit_2.setText(str(result_FP))
                    self.lineEdit_3.setText(str(result_FN))
                    self.lineEdit_4.setText(str(result_TN))
                elif flag == 1:
                    dictError[list(dictError.keys())[-1]] = "d=N/N,但是无结果"
                elif flag == 2:
                    dictError[list(dictError.keys())[-1]] = "FP=N/0,表明原始数据有错误"
                elif flag == 3:
                    dictError[list(dictError.keys())[-1]] = "FP=0/0,表明原始数据有错误"
                elif flag == 4:
                    dictError[list(dictError.keys())[-1]] = "TP=N/0,无法计算混淆矩阵"
                elif flag == 5:
                    dictError[list(dictError.keys())[-1]] = "TP=0/0,无法计算混淆矩阵"
                else:
                    dictError[list(dictError.keys())[-1]] = "原始数据有错误"
            #
            if self.lineEdit.text() == '' and self.lineEdit_2.text() == '' and self.lineEdit_3.text() == '' and self.lineEdit_4.text() == '':
                if dictError:
                    strMsg = ""
                    for key in dictError.keys():
                        strMsg = strMsg + "\n{}:{}".format(key,dictError[key])
                    QMessageBox.information(self,"",strMsg)
                else:
                    self.showMsg_nosolution()
            elif float(self.lineEdit.text()) < 0 or float(self.lineEdit_2.text())<0 or float(self.lineEdit_3.text())<0 or float(self.lineEdit_4.text())<0:
                self.label_49.setText("TP,TN,FP,FN的值均应在[0,1]之间")
            else:
                pass
    def getPerformance(self):
        self.lineEdit_22.clear()
        self.lineEdit_23.clear()
        self.lineEdit_24.clear()
        self.lineEdit_25.clear()
        self.lineEdit_26.clear()
        self.lineEdit_27.clear()
        self.lineEdit_28.clear()
        self.lineEdit_29.clear()
        self.lineEdit_30.clear()
        self.lineEdit_31.clear()
        self.lineEdit_32.clear()
        self.lineEdit_33.clear()
        self.lineEdit_34.clear()
        TP = self.lineEdit.text()
        FP = self.lineEdit_2.text()
        FN = self.lineEdit_3.text()
        TN = self.lineEdit_4.text()

        dictPerformanceError = {}
        try:
            TP = float(TP)
            FP = float(FP)
            FN = float(FN)
            TN = float(TN)
        except ValueError:
            QMessageBox.information(self,"错误","TP,FP,FN,TN应为数字且全部有值")
            return
        #FPR
        flag, FPR = self.fun_FPR(FP, TN)
        if flag == 0:
            self.lineEdit_23.setText(str(round(FPR,3)))
            if self.lineEdit_9.text() == '':
                self.lineEdit_23.setEnabled(False)
            self.label_36.clear()
            if self.lineEdit_9.text() != ''and self.lineEdit_23.text()!= '' and self.lineEdit_5.text()!='' and abs(
                    float(self.lineEdit_9.text()) - float(self.lineEdit_23.text())) > float(self.lineEdit_5.text()):
                self.label_36.setText("❌")
            elif float(self.lineEdit_23.text())<0 or float(self.lineEdit_23.text())>1:
                self.label_36.setText("FPR值应在[0,1]之间")
            elif self.lineEdit_9.text() != ''and self.lineEdit_23.text()!= '' and self.lineEdit_5.text()!='' and abs(
                    float(self.lineEdit_9.text()) - float(self.lineEdit_23.text())) > float(self.lineEdit_5.text()) and (float(self.lineEdit_23.text()) < 0 or float(self.lineEdit_23.text()) > 1):
                self.label_36.setText("❌  FPR值应在[0,1]之间 ")
        elif flag == 1:
            dictPerformanceError["FPR"] = "N/0"
        elif flag == 2:
            dictPerformanceError["FPR"] = "0/0"
        elif flag == 3:
            dictPerformanceError["FPR"] = "数据输入无效"

        #FNR
        flag,FNR = self.fun_FNR(TP, FN)
        if flag == 0:
            self.lineEdit_24.setText(str(round(FNR,3)))
            if self.lineEdit_10.text() == '':
                self.lineEdit_24.setEnabled(False)
            self.label_37.clear()
            if self.lineEdit_10.text() != ''and self.lineEdit_24.text()!= '' and self.lineEdit_5.text()!='' and abs(
                    float(self.lineEdit_10.text()) - float(self.lineEdit_24.text())) > float(self.lineEdit_5.text()):
                self.label_37.setText("❌")
            elif float(self.lineEdit_24.text())<0 or float(self.lineEdit_24.text())>1:
                self.label_37.setText("FNR值应在[0,1]之间")
            elif self.lineEdit_10.text() != ''and self.lineEdit_24.text()!= '' and self.lineEdit_5.text()!='' and abs(
                    float(self.lineEdit_10.text()) - float(self.lineEdit_24.text())) > float(self.lineEdit_5.text()) and float(self.lineEdit_24.text())<0 or float(self.lineEdit_24.text())>1:
                self.label_37.setText("❌  FNR值应在[0,1]之间 ")
        elif flag == 1:
            dictPerformanceError["FNR"] = "N/0"
        elif flag == 2:
            dictPerformanceError["FNR"] = "0/0"
        elif flag == 3:
            dictPerformanceError["FNR"] = "数据输入无效"

        # TNR
        flag,TNR = self.fun_TNR(TN, FP)
        if flag == 0:
            self.lineEdit_25.setText(str(round(TNR,3)))
            if self.lineEdit_11.text() == '':
                self.lineEdit_25.setEnabled(False)
            self.label_38.clear()
            if self.lineEdit_11.text() != '' and self.lineEdit_25.text()!= '' and self.lineEdit_5.text()!=''and abs(
                    float(self.lineEdit_11.text()) - float(self.lineEdit_25.text())) > float(self.lineEdit_5.text()):
                self.label_38.setText("❌")
            elif float(self.lineEdit_25.text()) < 0 or float(self.lineEdit_25.text()) > 1:
                    self.label_38.setText("TNR值应在[0,1]之间")
            elif self.lineEdit_11.text() != '' and self.lineEdit_25.text() != '' and self.lineEdit_5.text() != '' and abs(
                    float(self.lineEdit_11.text()) - float(self.lineEdit_25.text())) > float(
                self.lineEdit_5.text()) and float(self.lineEdit_25.text()) < 0 or float(self.lineEdit_25.text()) > 1:
                self.label_38.setText("❌  TNR值应在[0,1]之间 ")
        elif flag == 1:
            dictPerformanceError["TNR"] = "N/0"
        elif flag == 2:
            dictPerformanceError["TNR"] = "0/0"
        elif flag == 3:
            dictPerformanceError["ER"] = "数据输入无效"

        #ER
        flag,ER = self.fun_ER(TN, TP, FN, FP)
        if flag == 0:
            self.lineEdit_26.setText(str(round(ER,3)))
            if self.lineEdit_12.text() == '':
                self.lineEdit_26.setEnabled(False)
            self.label_39.clear()
            if self.lineEdit_12.text() != '' and self.lineEdit_26.text()!= '' and self.lineEdit_5.text()!=''and abs(
                    float(self.lineEdit_12.text()) - float(self.lineEdit_26.text())) > float(self.lineEdit_5.text()):
                self.label_39.setText("❌")
            elif float(self.lineEdit_26.text())<0 or float(self.lineEdit_26.text())>1:
                self.label_39.setText("ER值应在[0,1]之间")
            elif self.lineEdit_12.text() != ''and self.lineEdit_26.text()!= '' and self.lineEdit_5.text()!='' and abs(
                    float(self.lineEdit_12.text()) - float(self.lineEdit_26.text())) > float(self.lineEdit_5.text()) and float(self.lineEdit_26.text())<0 or float(self.lineEdit_26.text())>1:
                self.label_39.setText("❌  ER值应在[0,1]之间 ")
        elif flag == 1:
            dictPerformanceError["ER"] = "N/0"
        elif flag == 2:
            dictPerformanceError["ER"] = "0/0"
        elif flag == 3:
            dictPerformanceError["ER"] = "数据输入无效"


        #Recall
        flag,Recall = self.fun_Recall(TP, FN)
        if flag == 0:
            self.lineEdit_27.setText(str(round(Recall,3)))
            if self.lineEdit_13.text() == '':
                self.lineEdit_27.setEnabled(False)
            self.label_40.clear()
            if self.lineEdit_13.text() != '' and self.lineEdit_27.text()!= '' and self.lineEdit_5.text()!=''and abs(
                    float(self.lineEdit_13.text()) - float(self.lineEdit_27.text())) > float(self.lineEdit_5.text()):
                self.label_40.setText("❌")
            elif float(self.lineEdit_27.text())<0 or float(self.lineEdit_27.text())>1:
                self.label_40.setText("Recall值应在[0,1]之间")
            elif self.lineEdit_13.text() != ''and self.lineEdit_27.text()!= '' and self.lineEdit_5.text()!='' and abs(
                    float(self.lineEdit_13.text()) - float(self.lineEdit_27.text())) > float(self.lineEdit_5.text()) and float(self.lineEdit_27.text())<0 or float(self.lineEdit_27.text())>1:
                self.label_40.setText("❌  Recall值应在[0,1]之间 ")
        elif flag == 1:
            dictPerformanceError["Recall"] = "N/0"
        elif flag == 2:
            dictPerformanceError["Recall"] = "0/0"
        elif flag == 3:
            dictPerformanceError["Recall"] = "数据输入无效"

        #Performance
        flag ,Precision = self.fun_Precision(TP, FP)
        if flag == 0:
            self.lineEdit_28.setText(str(round(Precision,3)))
            if self.lineEdit_14.text() == '':
                self.lineEdit_28.setEnabled(False)
            self.label_41.clear()
            if self.lineEdit_14.text() != ''and self.lineEdit_28.text()!= '' and self.lineEdit_5.text()!='' and abs(float(self.lineEdit_14.text())-float(self.lineEdit_28.text()))>float(self.lineEdit_5.text()):
                self.label_41.setText("❌")
            elif float(self.lineEdit_28.text())<0 or float(self.lineEdit_28.text())>1:
                self.label_41.setText("Precision值应在[0,1]之间")
            elif self.lineEdit_14.text() != ''and self.lineEdit_28.text()!= '' and self.lineEdit_5.text()!='' and abs(
                    float(self.lineEdit_14.text()) - float(self.lineEdit_28.text())) > float(self.lineEdit_5.text()) and float(self.lineEdit_28.text())<0 or float(self.lineEdit_28.text())>1:
                self.label_41.setText("❌  Precision值应在[0,1]之间 ")
        elif flag == 1:
            dictPerformanceError["Precision"] = "N/0"
        elif flag == 2:
            dictPerformanceError["Precision"] = "0/0"
        elif flag == 3:
            dictPerformanceError["Precision"] = "数据输入无效"

        #Accuracy
        flag,Accuracy = self.fun_Accuracy(TP, TN, FP, FN)
        if flag == 0:
            self.lineEdit_29.setText(str(round(Accuracy,3)))
            if self.lineEdit_15.text() == '':
                self.lineEdit_29.setEnabled(False)
            self.label_42.clear()
            if self.lineEdit_15.text() != '' and self.lineEdit_29.text()!= '' and self.lineEdit_5.text()!=''and abs(
                    float(self.lineEdit_15.text()) - float(self.lineEdit_29.text())) > float(self.lineEdit_5.text()):
                self.label_42.setText("❌")
            elif float(self.lineEdit_29.text())<0 or float(self.lineEdit_29.text())>1:
                self.label_42.setText("Accuracy值应在[0,1]之间")
            elif self.lineEdit_15.text() != ''and self.lineEdit_29.text()!= '' and self.lineEdit_5.text()!='' and abs(
                    float(self.lineEdit_15.text()) - float(self.lineEdit_29.text())) > float(self.lineEdit_5.text()) and float(self.lineEdit_29.text())<0 or float(self.lineEdit_29.text())>1:
                self.label_42.setText("❌  Accuracy值应在[0,1]之间 ")
        elif flag == 1:
            dictPerformanceError["Accuracy"] = "N/0"
        elif flag == 2:
            dictPerformanceError["Accuracy"] = "0/0"
        elif flag == 3:
            dictPerformanceError["Accuracy"] = "数据输入无效"

        #FMeasure
        flag ,FMeasure = self.fun_FMeasure(TP, FP, FN)
        if flag == 0:
            self.lineEdit_30.setText(str(round(FMeasure,3)))
            if self.lineEdit_16.text() == '':
                self.lineEdit_30.setEnabled(False)
            self.label_43.clear()
            if self.lineEdit_16.text() != '' and self.lineEdit_30.text()!= '' and self.lineEdit_5.text()!=''and abs(
                    float(self.lineEdit_16.text()) - float(self.lineEdit_30.text())) > float(self.lineEdit_5.text()):
                self.label_43.setText("❌")
            elif float(self.lineEdit_30.text())<0 or float(self.lineEdit_30.text())>1:
                self.label_43.setText("FMeasure值应在[0,1]之间")
            elif self.lineEdit_16.text() != ''and self.lineEdit_30.text()!= '' and self.lineEdit_5.text()!='' and abs(
                    float(self.lineEdit_16.text()) - float(self.lineEdit_30.text())) > float(self.lineEdit_5.text()) and float(self.lineEdit_30.text())<0 or float(self.lineEdit_30.text())>1:
                self.label_43.setText("❌  FMeasure值应在[0,1]之间 ")
        elif flag == 1:
            dictPerformanceError["FMeasure"] = "N/0"
        elif flag == 2:
            dictPerformanceError["FMeasure"] = "0/0"
        elif flag == 3:
            dictPerformanceError["FMeasure"] = "Precision或Recall不可求"
        elif flag == 4:
            dictPerformanceError["FMeasure"] = "数据输入无效"

        #MCC
        flag,MCC = self.fun_MCC(TP, TN, FP, FN)
        if flag == 0:
            self.lineEdit_31.setText(str(round(MCC,3)))
            if self.lineEdit_17.text() == '':
                self.lineEdit_31.setEnabled(False)
            self.label_44.clear()
            if self.lineEdit_17.text() != '' and self.lineEdit_31.text()!= '' and self.lineEdit_5.text()!=''and abs(
                    float(self.lineEdit_17.text()) - float(self.lineEdit_31.text())) > float(self.lineEdit_5.text()):
                self.label_44.setText("❌")
            elif float(self.lineEdit_31.text())<-1 or float(self.lineEdit_31.text())>1:
                self.label_44.setText("MCC值应在[-1,1]之间")
            elif self.lineEdit_17.text() != ''and self.lineEdit_31.text()!= '' and self.lineEdit_5.text()!='' and abs(
                    float(self.lineEdit_17.text()) - float(self.lineEdit_31.text())) > float(self.lineEdit_5.text()) and float(self.lineEdit_31.text())<-1 or float(self.lineEdit_31.text())>1:
                self.label_44.setText("❌  MCC值应在[-1,1]之间 ")
        elif flag == 1:
            dictPerformanceError["MCC"] = "根号下出现负数"
        elif flag == 2:
            dictPerformanceError["MCC"] = "N/0"
        elif flag == 3:
            dictPerformanceError["MCC"] = "0/0"
        elif flag == 4:
            dictPerformanceError["MCC"] = "数据输入无效"

        #GMeasure
        flag,GMeasure = self.fun_GMeasure(TP, FN, TN, FP)
        if flag == 0:
            self.lineEdit_32.setText(str(round(GMeasure,3)))
            if self.lineEdit_18.text() == '':
                self.lineEdit_32.setEnabled(False)
            self.label_45.clear()
            if self.lineEdit_18.text() != '' and self.lineEdit_32.text()!= '' and self.lineEdit_5.text()!=''and abs(
                    float(self.lineEdit_18.text()) - float(self.lineEdit_32.text())) > float(self.lineEdit_5.text()):
                self.label_45.setText("❌")
            elif float(self.lineEdit_32.text())<0 or float(self.lineEdit_32.text())>1:
                self.label_45.setText("GMeasure值应在[0,1]之间")
            elif self.lineEdit_18.text() != ''and self.lineEdit_32.text()!= '' and self.lineEdit_5.text()!='' and abs(
                    float(self.lineEdit_18.text()) - float(self.lineEdit_32.text())) > float(self.lineEdit_5.text()) and float(self.lineEdit_32.text())<0 or float(self.lineEdit_32.text())>1:
                self.label_45.setText("❌  GMeasure值应在[0,1]之间 ")
        elif flag == 1:
            dictPerformanceError["GMeasure"] = "N/0"
        elif flag == 2:
            dictPerformanceError["GMeasure"] = "0/0"
        elif flag == 3:
            dictPerformanceError["GMeasure"] = "Recall或者TNR不可求"
        elif flag == 4:
            dictPerformanceError["GMeasure"] = "数据输入无效"

        #GMean
        flag,GMean = self.fun_GMean(TP, FN, TN, FP)
        if flag == 0:
            self.lineEdit_33.setText(str(round(GMean,3)))
            if self.lineEdit_19.text() == '':
                self.lineEdit_33.setEnabled(False)
            self.label_46.clear()
            if self.lineEdit_19.text() != '' and self.lineEdit_33.text()!= '' and self.lineEdit_5.text()!=''and abs(
                    float(self.lineEdit_19.text()) - float(self.lineEdit_33.text())) > float(self.lineEdit_5.text()):
                self.label_46.setText("❌")
            elif float(self.lineEdit_33.text())<0 or float(self.lineEdit_33.text())>1:
                self.label_46.setText("GMean值应在[0,1]之间")
            elif self.lineEdit_19.text() != ''and self.lineEdit_33.text()!= '' and self.lineEdit_5.text()!='' and abs(
                    float(self.lineEdit_19.text()) - float(self.lineEdit_33.text())) > float(self.lineEdit_5.text()) and float(self.lineEdit_33.text())<0 or float(self.lineEdit_33.text())>1:
                self.label_46.setText("❌  GMean值应在[0,1]之间 ")
        elif flag == 1:
            dictPerformanceError["GMean"] = "出现二次根号下负数"
        elif flag == 2:
            dictPerformanceError["GMean"] = "N/0"
        elif flag == 3:
            dictPerformanceError["GMean"] = "0/0"
        elif flag == 4:
            dictPerformanceError["GMean"] = "数据输入无效"


        #Balance
        flag,Balance = self.fun_Balance(TP, FN, FP, TN)
        if flag == 0:
            self.lineEdit_34.setText(str(round(Balance,3)))
            if self.lineEdit_20.text() == '':
                self.lineEdit_34.setEnabled(False)
            self.label_47.clear()
            if self.lineEdit_20.text() != '' and self.lineEdit_34.text()!= '' and self.lineEdit_5.text()!=''and abs(
                    float(self.lineEdit_20.text()) - float(self.lineEdit_34.text())) > float(self.lineEdit_5.text()):
                self.label_47.setText("❌")
            elif float(self.lineEdit_34.text())<0 or float(self.lineEdit_34.text())>1:
                self.label_47.setText("Balance值应在[0,1]之间")
            elif self.lineEdit_20.text() != ''and self.lineEdit_34.text()!= '' and self.lineEdit_5.text()!='' and abs(
                    float(self.lineEdit_20.text()) - float(self.lineEdit_34.text())) > float(self.lineEdit_5.text()) and float(self.lineEdit_34.text())<0 or float(self.lineEdit_34.text())>1:
                self.label_47.setText("❌  Balance值应在[0,1]之间")
        elif flag == 1:
            dictPerformanceError["Balance"] = "Recall或者FPR不可求"
        elif flag == 2:
            dictPerformanceError["Balance"] = "数据输入无效"

        #Density
        Density = self.fun_Density(TP, FN)
        self.lineEdit_22.setText(str(round(Density,3)))
        if self.lineEdit_21.text() == '':
            self.lineEdit_22.setEnabled(False)
        self.label_48.clear()
        if self.lineEdit_21.text() != '' and self.lineEdit_22.text()!= '' and self.lineEdit_6.text()!=''and abs(
                float(self.lineEdit_21.text()) - float(self.lineEdit_22.text())) > float(self.lineEdit_6.text()):
            self.label_48.setText("❌")
        elif float(self.lineEdit_22.text())<=0 :
            self.label_48.setText("Density值应大于0")
        elif self.lineEdit_21.text() != ''and self.lineEdit_22.text()!= '' and self.lineEdit_6.text()!='' and abs(
                float(self.lineEdit_21.text()) - float(self.lineEdit_22.text())) > float(self.lineEdit_6.text()) and float(self.lineEdit_22.text())<=0 :
            self.label_48.setText("❌  Density值应大于0")

        if dictPerformanceError:
            strMsg = ""
            for key in dictPerformanceError.keys():
                strMsg = strMsg + "\n{}:{}".format(key, dictPerformanceError[key])
            QMessageBox.information(self, "", strMsg)
        else:
            pass


    def showMsg_nosolution(self):
        reply = QMessageBox.about(self, "", "该组参数没有对应的混淆矩阵")

    #预测性能->混淆矩阵
    def fun1(self,FPR,r,a):
        FP, TP, FN, TN = symbols('FP,TP,FN,TN')
        flag = 0
        if abs(FPR + r-1) > 1e-6 and abs(FPR + a-1) > 1e-6:
            result = solve([FPR * (FP + TN) - FP,
                            r * (TP + FN) - TP,
                            a * (TP + TN + FP + FN) - (TP + TN),
                            TP + TN + FP + FN - 1],
                           [FP, TP, FN, TN])
            if isinstance(result, dict):
                result[TP] = round(result[TP], 3)
                result[TN] = round(result[TN], 3)
                result[FP] = round(result[FP], 3)
                result[FN] = round(result[FN], 3)
                return flag, result[TP], result[TN], result[FP], result[FN]
            else:
                flag = 1
                return flag, None, None, None, None
        elif abs(FPR + r-1)> 1e-6 and abs(FPR+a-1)<1e-6:
            flag = 2
            return flag,None,None,None,None
        elif abs(FPR+r-1)<1e-6 and abs(FPR+a-1)> 1e-6:
            flag = 3
            return flag,None,None,None,None
        elif abs(FPR+a-1)< 1e-6and abs(FPR+r-1) < 1e-6:
            flag = 4
            return flag,None,None,None,None
        else:
            flag = 5
            return flag,None,None,None,None


    def fun2(self,FPR,r,p):
        FP, TP, FN, TN = symbols('FP,TP,FN,TN')
        flag = 0
        if abs(p*FPR-0) > 1e-6 and abs(r*(1-p)+ p*FPR-0)> 1e-6:
            result = solve([FPR * (FP + TN) - FP,
                            r * (TP + FN) - TP,
                            p*(TP+FP)-TP,
                            TP + TN + FP + FN - 1],
                           [FP, TP, FN, TN])
            if isinstance(result, dict):
                result[TP] = round(result[TP], 3)
                result[TN] = round(result[TN], 3)
                result[FP] = round(result[FP], 3)
                result[FN] = round(result[FN], 3)
                return flag, result[TP], result[TN], result[FP], result[FN]
            else:
                flag = 1
                return flag, None, None, None, None
        elif abs(p*FPR-0)> 1e-6  and  abs(r*(1-p)+ p*FPR-0)<1e-6:
            flag = 2
            return flag,None,None,None,None
        elif abs(p*FPR-0)<1e-6  and  abs(r*(1-p)+ p*FPR-0)> 1e-6:
            flag = 3
            return flag,None,None,None,None
        elif abs(p*FPR-0)<1e-6 and abs(r*(1-p)+ p*FPR-0)<1e-6:
            flag =4
            return  flag,None, None,None, None
        else:
            flag = 5
            return flag,None, None,None, None

    def fun3(self,FPR, r, f1):
        FP, TP, FN, TN = symbols('FP,TP,FN,TN')
        flag = 0
        if abs(FPR*f1-0)> 1e-6 and abs(f1*(FPR+(1-r))+2*(1-f1-(1-r))-0)> 1e-6:
            result = solve([FPR * (FP + TN) - FP,
                            r * (TP + FN) - TP,
                            f1*(r+TP/(TP+FP))-2*r*(TP/(TP+FP)),
                            TP + TN + FP + FN - 1],
                           [FP, TP, FN, TN])
            if isinstance(result, dict):
                result[TP] = round(result[TP], 3)
                result[TN] = round(result[TN], 3)
                result[FP] = round(result[FP], 3)
                result[FN] = round(result[FN], 3)
                return flag, result[TP], result[TN], result[FP], result[FN]
            else:
                flag = 1
                return flag, None, None, None, None
        elif abs(FPR*f1-0)> 1e-6 and abs(f1*(FPR+(1-r))+2*(1-f1-(1-r))-0)<1e-6:
            flag = 2
            return flag, None, None, None, None
        elif abs(FPR*f1-0)<1e-6 and abs(f1*(FPR+(1-r))+2*(1-f1-(1-r))-0)> 1e-6:
            flag =3
            return flag, None, None, None, None
        elif abs(FPR*f1-0)<1e-6 and abs(f1*(FPR+(1-r))+2*(1-f1-(1-r))-0)<1e-6:
            flag =4
            return flag, None, None, None, None
        else:
            flag = 5
            return flag, None, None, None, None
    def fun4(self,FPR, a, p):
        FP, TP, FN, TN = symbols('FP,TP,FN,TN')
        flag = 0
        if abs((1-a)*(p-1)+FPR*(2*p-1)-0)> 1e-6 and abs((p-1)+FPR*(2*p-1)-0)> 1e-6:
            result = solve([FPR * (FP + TN) - FP,
                            a * (TP + TN + FP + FN) - (TP + TN),
                            p * (TP + FP) - TP,
                            TP + TN + FP + FN - 1],
                           [FP, TP, FN, TN])
            if isinstance(result, dict):
                result[TP] = round(result[TP], 3)
                result[TN] = round(result[TN], 3)
                result[FP] = round(result[FP], 3)
                result[FN] = round(result[FN], 3)
                return flag, result[TP], result[TN], result[FP], result[FN]
            else:
                flag = 1
                return flag, None, None, None, None
        elif abs((1-a)*(p-1)+FPR*(2*p-1)-0)> 1e-6 and abs((p-1)+FPR*(2*p-1)-0)<1e-6:
            flag = 2
            return flag, None, None, None, None
        elif abs((1-a)*(p-1)+FPR*(2*p-1)-0)< 1e-6 and abs((p-1)+FPR*(2*p-1)-0)>1e-6:
            flag = 3
            return flag, None, None, None, None
        elif abs((1-a)*(p-1)+FPR*(2*p-1)-0)<1e-6 and abs((p-1)+FPR*(2*p-1)-0)<1e-6:
            flag = 4
            return flag, None, None, None, None
        else:
            flag = 5
            return flag, None, None, None, None
    def fun5(self,FPR, a, F1):
        FP, TP, FN, TN = symbols('FP,TP,FN,TN')
        flag = 0
        if abs(F1*(1-a)+2*(1-a-FPR-F1*FPR)-0)> 1e-6 and abs((1-F1)*(1-FPR)-0)> 1e-6:
            result = solve([FPR * (FP + TN) - FP,
                            a * (TP + TN + FP + FN) - (TP + TN),
                            2 * (TP / (TP + FP)) * (TP / (TP + FN)) - F1*((TP / (TP + FP)) + (TP / (TP + FN))),
                            TP + TN + FP + FN - 1],
                           [FP, TP, FN, TN])
            if isinstance(result,dict):
                result[TP] = round(result[TP], 3)
                result[TN] = round(result[TN], 3)
                result[FP] = round(result[FP], 3)
                result[FN] = round(result[FN], 3)
                return flag,result[TP],result[TN],result[FP],result[FN]
            else:
                flag = 1
                return flag, None, None, None, None
        elif abs(F1*(1-a)+2*(1-a-FPR-F1*FPR)-0)> 1e-6 and abs((1-F1)*(1-FPR)-0)<1e-6:
            flag = 2
            return flag, None, None, None, None
        elif abs(F1*(1-a)+2*(1-a-FPR-F1*FPR)-0)<1e-6 and abs((1-F1)*(1-FPR)-0)> 1e-6:
            flag = 3
            return flag, None, None, None, None
        elif abs(F1*(1-a)+2*(1-a-FPR-F1*FPR)-0)<1e-6 and abs((1-F1)*(1-FPR)-0)<1e-6:
            flag = 4
            return flag, None, None, None, None
        else:
            flag = 5
            return flag, None, None, None, None

    def fun6(self,FPR, p, F1):
        FP, TP, FN, TN = symbols('FP,TP,FN,TN')
        flag = 0
        if abs(FPR*(F1 - 2*p)-0)> 1e-6 and abs(F1+FPR*(2*p-F1)-0)> 1e-6:
            result = solve([FPR * (FP + TN) - FP,
                            p * (TP + FP) - TP,
                            2 * p * (TP / (TP + FN)) - F1 * (p + (TP / (TP + FN))),
                            TP + TN + FP + FN - 1],
                           [FP, TP, FN, TN])
            if isinstance(result, dict):
                result[TP] = round(result[TP], 3)
                result[TN] = round(result[TN], 3)
                result[FP] = round(result[FP], 3)
                result[FN] = round(result[FN], 3)
                return flag, result[TP], result[TN], result[FP], result[FN]
            else:
                flag = 1
                return flag, None, None, None, None
        elif abs(FPR*(F1 - 2*p)-0)> 1e-6 and abs(F1+FPR*(2*p-F1)-0)<1e-6:
            flag = 2
            return flag, None, None, None, None
        elif abs(FPR*(F1 - 2*p)-0)<1e-6 and abs(F1+FPR*(2*p-F1)-0)> 1e-6:
            flag = 3
            return flag, None, None, None, None
        elif abs(FPR*(F1 - 2*p)-0)<1e-6 and abs(F1+FPR*(2*p-F1)-0)<1e-6:
            flag = 4
            return flag, None, None, None, None
        else:
            flag = 5
            return flag, None, None, None, None

    def fun7(self,r, a, p):
        FP, TP, FN, TN = symbols('FP,TP,FN,TN')
        flag = 0
        if abs(p*(a - 1)-0)> 1e-6 and abs(2*p*r - p - r-0)> 1e-6:
            result = solve([r * (TP + FN) - TP,
                            a * (TP + TN + FP + FN) - (TP + TN),
                            p * (TP + FP) - TP,
                            TP + TN + FP + FN - 1],
                           [FP, TP, FN, TN])
            if isinstance(result, dict):
                result[TP] = round(result[TP], 3)
                result[TN] = round(result[TN], 3)
                result[FP] = round(result[FP], 3)
                result[FN] = round(result[FN], 3)
                return flag, result[TP], result[TN], result[FP], result[FN]
            else:
                flag = 1
                return flag, None, None, None, None
        elif abs(p*(a - 1)-0)> 1e-6 and abs(2*p*r - p - r-0)<1e-6:
            flag = 2
            return flag, None, None, None, None
        elif abs(p*(a - 1)-0)<1e-6 and abs(2*p*r - p - r-0)> 1e-6:
            flag = 3
            return flag, None, None, None, None
        elif abs(p*(a - 1)-0)<1e-6 and abs(2*p*r - p - r-0)<1e-6:
            flag = 4
            return flag, None, None, None, None
        else:
            flag = 5
            return flag, None, None, None, None

    def fun8(self,r, a, F1):
        FP, TP, FN, TN = symbols('FP,TP,FN,TN')
        flag = 0
        if abs(F1*(a - 1) -0)> 1e-6 and abs(2*r*(F1 - 1)-0)> 1e-6:
            result = solve([r * (TP + FN) - TP,
                            a * (TP + TN + FP + FN) - (TP + TN),
                            F1 * (r + TP / (TP + FP)) - 2 * r * (TP / (TP + FP)),
                            TP + TN + FP + FN - 1],
                           [FP, TP, FN, TN])
            if isinstance(result, dict):
                result[TP] = round(result[TP], 3)
                result[TN] = round(result[TN], 3)
                result[FP] = round(result[FP], 3)
                result[FN] = round(result[FN], 3)
                return flag, result[TP], result[TN], result[FP], result[FN]
            else:
                flag = 1
                return flag, None, None, None, None
        elif abs(F1*(a - 1) -0)>1e-6 and abs(2*r*(F1 - 1)-0)< 1e-6:
            flag = 2
            return flag, None, None, None, None
        elif abs(F1*(a - 1)-0)<1e-6 and abs(2*r*(F1 - 1)-0)> 1e-6:
            flag = 3
            return flag, None, None, None, None
        elif abs(F1*(a - 1)-0)<1e-6 and abs(2*r*(F1 - 1)-0)<1e-6:
            flag = 4
            return flag, None, None, None, None
        else:
            flag = 5
            return flag, None, None, None, None

    def fun9(self,p, a, F1):
        FP, TP, FN, TN = symbols('FP,TP,FN,TN')
        flag = 0
        if abs((-F1*a + F1 + 2*a*p - 2*p)-0)> 1e-6 and abs((p*(F1 - 1))-0)> 1e-6:
            result = solve([a * (TP + TN + FP + FN) - (TP + TN),
                            p * (TP + FP) - TP,
                            2 * p * (TP / (TP + FN)) - F1 * (p + (TP / (TP + FN))),
                            TP + TN + FP + FN - 1],
                           [FP, TP, FN, TN])
            if isinstance(result, dict):
                result[TP] = round(result[TP], 3)
                result[TN] = round(result[TN], 3)
                result[FP] = round(result[FP], 3)
                result[FN] = round(result[FN], 3)
                return flag, result[TP], result[TN], result[FP], result[FN]
            else:
                flag = 1
                return flag, None, None, None, None
        elif abs((-F1*a/2 + F1/2 + a*p - p)-0)> 1e-6 and abs((p*(F1 - 1))-0)<1e-6:
            flag = 2
            return flag, None, None, None, None
        elif abs((-F1*a/2 + F1/2 + a*p - p)-0)<1e-6 and abs((p*(F1 - 1))-0)> 1e-6:
            flag = 3
            return flag, None, None, None, None
        elif abs((-F1*a/2 + F1/2 + a*p - p)-0)<1e-6 and abs((p*(F1 - 1))-0)<1e-6:
            flag = 4
            return flag, None, None, None, None
        else:
            flag = 5
            return flag, None, None, None, None

    """以下10种是两种参数求解混淆矩阵"""
    # 第一种FPR,r,d
    def fun11(self,FPR,r,d):
        FP, TP, FN, TN = symbols('FP TP FN TN')
        flag = 0
        result = solve([FPR * (FP + TN) - FP,
                        r * (TP + FN) - TP,
                        TP + FN - d,
                        FN + TN + TP + FP - 1],
                       [FP, TP, FN, TN])
        if isinstance(result, dict):
            result[TP] = round(result[TP], 3)
            result[TN] = round(result[TN], 3)
            result[FP] = round(result[FP], 3)
            result[FN] = round(result[FN], 3)
            return flag, result[TP], result[TN], result[FP], result[FN]
        else:
            flag = 1
            return flag, None, None, None, None
    # #FP: FPR*(-d*r + 1)/(FPR + 1),
    # #TP: d*r,
    # #FN: d*(-r + 1),
    # #TN: (-FPR + d*r*(FPR - 1) + 1)/(FPR + 1)

    # #第二种FPR,a,d
    def fun12(self,FPR, a, d):
        FP, TP, FN, TN = symbols('FP TP FN TN')
        flag = 0
        result = solve([FPR * (FP + TN) - FP,
                        (TP + TN) - a,
                        TP + FN - d,
                        FN + TN + TP + FP - 1],
                       [FP, TP, FN, TN])
        if isinstance(result, dict):
            result[TP] = round(result[TP], 3)
            result[TN] = round(result[TN], 3)
            result[FP] = round(result[FP], 3)
            result[FN] = round(result[FN], 3)
            return flag, result[TP], result[TN], result[FP], result[FN]
        else:
            flag = 1
            return flag, None, None, None, None
    # # FP: -a/2 + 1/2,
    # # TP: (FPR + a*(FPR + 1) - 1)/(2*FPR),
    # # FN: (2*FPR*d - FPR - a*(FPR + 1) + 1)/(2*FPR),
    # # TN: (-FPR + a*(FPR - 1) + 1)/(2*FPR)

    # #第三种FPR,p,d
    def fun13(self,FPR, p, d):
        FP, TP, FN, TN = symbols('FP TP FN TN')
        flag = 0
        if  abs(p - 1-0)> 1e-6:
            result = solve([FPR * (FP + TN) - FP,
                            p * (TP + FP) - TP,
                            TP + FN - d,
                            FN + TN + TP + FP - 1],
                           [FP, TP, FN, TN])
            if isinstance(result, dict):
                result[TP] = round(result[TP], 3)
                result[TN] = round(result[TN], 3)
                result[FP] = round(result[FP], 3)
                result[FN] = round(result[FN], 3)
                return flag, result[TP], result[TN], result[FP], result[FN]
            else:
                flag = 1
                return flag, None, None, None, None
        elif abs(FPR*p-0)> 1e-6 and abs(p - 1-0)<1e-6:#TP=N/0 表明原始值错误
            flag = 2
            return flag, None, None, None, None
        elif abs(FPR*p-0)<1e-6 and abs(p - 1-0)< 1e-6:#TP=0/0,表明原始值错误
            flag = 3
            return flag, None, None, None, None
        else:
            flag = 4
            return flag, None, None, None, None
    # #FP: FPR*(p - 1)/(-FPR + p - 1),
    # # TP: FPR*p/(FPR - p + 1),
    # # FN: (-FPR*d + FPR*p + d*p - d)/(-FPR + p - 1),
    # # TN: (-FPR*p + FPR + p - 1)/(-FPR + p - 1)

    # #第四种FPR,F1,d(不可算，F1需要p和r参数值)
    def fun14(self,FPR, F1, d):
        FP, TP, FN, TN = symbols('FP TP FN TN')
        flag = 0
        result = solve([FPR * (FP + TN) - FP,
                        F1 * (FP + 2 * TP + FN) - 2 * TP,
                        TP + FN - d,
                        FN + TN + TP + FP - 1],
                       [FP, TP, FN, TN])
        if isinstance(result, dict):
            result[TP] = round(result[TP], 3)
            result[TN] = round(result[TN], 3)
            result[FP] = round(result[FP], 3)
            result[FN] = round(result[FN], 3)
            return flag, result[TP], result[TN], result[FP], result[FN]
        else:
            flag = 1
            return flag, None, None, None, None
    # #FP: FPR*(F1*d + F1 - 2)/(F1 - 2*FPR - 2),
    # # TP: F1*(FPR*d + FPR + d)/(-F1 + 2*FPR + 2),
    # # FN: (F1*FPR*d + F1*FPR + 2*F1*d - 2*FPR*d - 2*d)/(F1 - 2*FPR - 2),
    # # TN: (-F1*FPR*d - F1*FPR + F1*d + F1 + 2*FPR - 2)/(F1 - 2*FPR - 2)

    # #第五种r ,a,d
    def fun15(self,r, a, d):
        FP, TP, FN, TN = symbols('FP TP FN TN')
        flag = 0
        result = solve([r * (TP + FN) - TP,
                        (TP + TN) - a,
                        TP + FN - d,
                        FN + TN + TP + FP - 1],
                       [FP, TP, FN, TN])
        if isinstance(result, dict):
            result[TP] = round(result[TP], 3)
            result[TN] = round(result[TN], 3)
            result[FP] = round(result[FP], 3)
            result[FN] = round(result[FN], 3)
            return flag, result[TP], result[TN], result[FP], result[FN]
        else:
            flag = 1
            return flag, None, None, None, None
    # #FP: -a/2 + 1/2,
    # # TP: d*r,
    # # FN: d*(-r + 1),
    # # TN: a - d*r

    # #第六种r p d
    def fun16(self,r, p, d):
        FP, TP, FN, TN = symbols('FP TP FN TN')
        flag=0
        if  abs(p-0)> 1e-6:
            result = solve([r * (TP + FN) - TP,
                            p * (TP + FP) - TP,
                            TP + FN - d,
                            FN + TN + TP + FP - 1],
                           [FP, TP, FN, TN])
            if isinstance(result, dict):
                result[TP] = round(result[TP], 3)
                result[TN] = round(result[TN], 3)
                result[FP] = round(result[FP], 3)
                result[FN] = round(result[FN], 3)
                return flag, result[TP], result[TN], result[FP], result[FN]
            else:
                flag = 1
                return flag, None, None, None, None
        elif abs(d*r*(1-p)-0)> 1e-6 and abs(p-0)< 1e-6:#FP
            flag = 2
            return flag, None, None, None, None
        elif abs(d*r*(1-p)-0)< 1e-6 and abs(p-0)<1e-6:
            flag = 3
            return flag, None, None, None, None
        else:
            flag = 4
            return flag, None, None, None, None
    # #FP: -d*r + d*r/p,
    # # TP: d*r,
    # # FN: d*(-r + 1),
    # # TN: d*r - 2*d*r/p + 1

    # #第七种r F1 d（不可算，F1需要依赖于p和r）
    def fun17(self,r, F1, d):
        FP, TP, FN, TN = symbols('FP TP FN TN')
        flag = 0
        if  abs(F1-0)> 1e-6:
            result = solve([r * (TP + FN) - TP,
                            F1 * (FP + 2 * TP + FN) - 2 * TP,
                            TP + FN - d,
                            FN + TN + TP + FP - 1],
                           [FP, TP, FN, TN])
            if isinstance(result, dict):
                result[TP] = round(result[TP], 3)
                result[TN] = round(result[TN], 3)
                result[FP] = round(result[FP], 3)
                result[FN] = round(result[FN], 3)
                return flag, result[TP], result[TN], result[FP], result[FN]
            else:
                flag = 1
                return flag, None, None, None, None
        elif abs(2*r-F1-r*F1-0)> 1e-6 and abs(F1-0)<1e-6:
            flag = 2
            return flag, None, None, None, None
        elif abs(2*r-F1-r*F1-0)<1e-6 and abs(F1-0)<1e-6:
            flag = 3
            return flag, None, None, None, None
        else:
            flag = 4
            return flag, None, None, None, None
    # # FP: -d*r - d + 2*d*r/F1,
    # # TP: d*r,
    # # FN: d*(-r + 1),
    # # TN: d*r + 2*d + 1 - 4*d*r/F1

    # #第八种a p d
    def fun18(self,a, p, d):
        FP, TP, FN, TN = symbols('FP TP FN TN')
        flag = 0
        if abs(2*p-1-0)> 1e-6:
            result = solve([(TP + TN) - a,
                            p * (TP + FP) - TP,
                            TP + FN - d,
                            FN + TN + TP + FP - 1],
                           [FP, TP, FN, TN])
            if isinstance(result, dict):
                result[TP] = round(result[TP], 3)
                result[TN] = round(result[TN], 3)
                result[FP] = round(result[FP], 3)
                result[FN] = round(result[FN], 3)
                return flag, result[TP], result[TN], result[FP], result[FN]
            else:
                flag = 1
                return flag, None, None, None, None
        elif abs((d-1+a)*p-0)> 1e-6 and abs(2*p-1-0)<1e-6:#TP
            flag = 2
            return flag, None, None, None, None
        elif abs((d-1+a)*p-0)<1e-6 and abs(2*p-1-0)<1e-6:
            flag = 3
            return flag, None, None, None, None
        else:
            flag = 4
            return flag, None, None, None, None
    # #FP: -a/2 + 1/2,
    # # TP: p*(a - 1)/(2*(p - 1)),
    # # FN: (-a*p + 2*d*(p - 1) + p)/(2*(p - 1)),
    # # TN: (a*(p - 2) + p)/(2*(p - 1))

    # #第九种a F1 d
    def fun19(self,a, F1, d):
        FP, TP, FN, TN = symbols('FP TP FN TN')
        flag = 0
        if abs((1-F1)-0)> 1e-6:
            result = solve([(TP + TN) - a,
                            F1 * (FP + 2 * TP + FN) - 2 * TP,
                            TP + FN - d,
                            FN + TN + TP + FP - 1],
                           [FP, TP, FN, TN])
            if isinstance(result, dict):
                result[TP] = round(result[TP], 3)
                result[TN] = round(result[TN], 3)
                result[FP] = round(result[FP], 3)
                result[FN] = round(result[FN], 3)
                return flag, result[TP], result[TN], result[FP], result[FN]
            else:
                flag = 1
                return flag, None, None, None, None
        elif abs(F1*(1-a)-0)> 1e-6 and abs((1-F1)-0)<1e-6:
            flag = 2
            return flag, None, None, None, None
        elif abs(F1*(1-a)-0)<1e-6 and abs((1-F1)-0)< 1e-6:
            flag = 3
            return flag, None, None, None, None
        else:
            flag = 4
            return flag, None, None, None, None
    # # FP: -a/2 + 1/2,
    # # TP: F1*(a - 2*d - 1)/(2*(F1 - 2)),
    # # FN: (-F1*a + F1 + 4*d*(F1 - 1))/(2*(F1 - 2)),
    # # TN: (2*F1*d + F1 + a*(F1 - 4))/(2*(F1 - 2))

    # #第十种p F1 d
    def fun20(self,p, F1, d):
        FP, TP, FN, TN = symbols('FP TP FN TN')
        flag = 0
        if  abs((2*p-F1)-0)> 1e-6 :#TP>0
            if p!=0:
                result = solve([p * (TP + FP) - TP,
                                F1 * (FP + 2 * TP + FN) - 2 * TP,
                                TP + FN - d,
                                FN + TN + TP + FP - 1],
                               [FP, TP, FN, TN])
                if isinstance(result, dict):
                    result[TP] = round(result[TP], 3)
                    result[TN] = round(result[TN], 3)
                    result[FP] = round(result[FP], 3)
                    result[FN] = round(result[FN], 3)
                    return flag, result[TP], result[TN], result[FP], result[FN]
                else:
                    flag = 1
                    return flag, None, None, None, None
            elif abs(d*p*F1-0)> 1e-6 and p==0 and p!=1:#FP=M/0
                flag = 2
                return flag, None, None, None, None
            elif (abs(d*p*F1-0)> 1e-6 and p==0 and p==1) or(abs(d*p*F1-0)<1e-6 and p==0):#FP=0/0
                flag = 3
                return flag, None, None, None, None
        elif abs(d*p*F1-0)> 1e-6 and  abs((2*p-F1)-0)<1e-6:#TP=N/0
            flag = 4
            return flag, None, None, None, None
        elif abs(d * p * F1-0)<1e-6 and abs((2 * p - F1)- 0)< 1e-6:#TP=0/0
            flag = 5
            return flag, None, None, None, None
        else:
            flag = 6
            return flag, None, None, None, None
    # # FP: F1*d*(p - 1)/(F1 - 2*p),
    # # TP: F1*d*p/(-F1 + 2*p),
    # # FN: d*(F1*p + F1 - 2*p)/(F1 - 2*p),
    # # TN: (F1*d*p - 2*F1*d - F1 + 2*p)/(-F1 + 2*p)

    #混淆矩阵->反求预测性能
    def fun_FPR(self,FP,TN):
        flag = 0
        if abs((FP+TN)-0)>1e-6:
            FPR = FP / (FP + TN)
            return flag,FPR
        elif FP!=0 and abs((FP+TN)-0)<1e-6:
            flag = 1
            return flag,None
        elif FP==0 and abs((FP+TN)-0)<1e-6:
            flag = 2
            return flag,None
        else:
            flag = 3
            return flag,None
    def fun_FNR(self,TP,FN):

        flag = 0
        if abs((TP+FN)-0)>1e-6:
            FNR = FN / (TP + FN)
            return flag,FNR
        elif FN!=0 and abs((TP+FN)-0)<1e-6:
            flag = 1
            return flag, None
        elif FN==0 and abs((TP+FN)-0)<1e-6:
            flag = 2
            return flag,None
        else:
            flag = 3
            return flag, None

    def fun_TNR(self,TN,FP):
        flag = 0
        if abs((TN+FP)-0)>1e-6:
            TNR = TN / (TN + FP)
            return flag,TNR
        elif TN!=0 and abs((TN+FP)-0)<1e-6:
            flag = 1
            return flag, None
        elif TN==0 and abs((TN+FP)-0)<1e-6:
            flag = 2
            return flag,None
        else:
            flag = 3
            return flag, None
    def fun_ER(self,TN,TP,FN,FP):
        flag = 0
        if abs((TP+TN+FP+FN) - 0) > 1e-6:
            ER = (FP + FN) / (TP + TN + FP + FN)
            return flag, ER
        elif abs(FP+FN-0)>1e-6 and abs((TP+TN+FP+FN) - 0) < 1e-6:
            flag = 1
            return flag, None
        elif abs(FP+FN-0)<1e-6 and abs((TP+TN+FP+FN) - 0) < 1e-6:
            flag = 2
            return flag, None
        else:
            flag = 3
            return flag, None

    def fun_Recall(self,TP,FN):
        flag = 0
        if abs((TP + FN) - 0) > 1e-6:
            Recall = TP / (TP + FN)
            return flag, Recall
        elif TP != 0 and abs((TP + FN) - 0) < 1e-6:
            flag = 1
            return flag, None
        elif TP == 0 and abs((TP + FN) - 0) < 1e-6:
            flag = 2
            return flag, None
        else:
            flag = 3
            return flag, None

    def fun_Precision(self,TP,FP):
        flag = 0
        if abs((TP + FP) - 0) > 1e-6:
            Precision = TP / (TP + FP)
            return flag, Precision
        elif TP != 0 and abs((TP + FP) - 0) < 1e-6:
            flag = 1
            return flag, None
        elif TP == 0 and abs((TP + FP) - 0) < 1e-6:
            flag = 2
            return flag, None
        else:
            flag = 3
            return flag, None

    def fun_Accuracy(self,TP,TN,FP,FN):
        flag = 0
        if abs((TP + TN + FP + FN) - 0) > 1e-6:
            Accuracy = (TN + TP) / (TP + TN + FP + FN)
            return flag, Accuracy
        elif abs(TN+TP - 0) > 1e-6 and abs((TP + TN + FP + FN) - 0) < 1e-6:
            flag = 1
            return flag, None
        elif abs(TN+TP - 0) < 1e-6 and abs((TP + TN + FP + FN) - 0) < 1e-6:
            flag = 2
            return flag, None
        else:
            flag = 3
            return flag, None

    def fun_FMeasure(self,TP,FP,FN):
        flag = 0
        if abs((TP + FP)-0) > 1e-6 and abs((TP + FN)-0)> 1e-6:
            Precision = TP/(TP + FP)
            Recall = TP/(TP + FN)
            if  abs((Precision+Recall) - 0) > 1e-6:
                FMeasure = 2 * Recall * Precision / (Precision + Recall)
                return flag, FMeasure
            elif abs(2*Recall*Precision - 0) > 1e-6 and abs((Precision+Recall) - 0) < 1e-6:
                flag = 1
                return flag, None
            elif abs(2*Recall*Precision - 0) < 1e-6 and abs((Precision+Recall) - 0) < 1e-6:
                flag = 2
                return flag, None
        elif abs((TP + FP)-0) < 1e-6 or abs((TP + FN)-0)< 1e-6:
            flag = 3
            return flag,None
        else:
            flag = 4
            return flag, None

    def fun_MCC(self,TP,TN,FP,FN):
        flag = 0
        if ((TP+FP)*(TP+FN)*(TN+FP)*(TN+FN))>0 and abs((((TP+FP)*(TP+FN)*(TN+FP)*(TN+FN))**0.5) - 0) > 1e-6:
            MCC = (TP * TN - FP * FN) / ((TP + FP) * (TP + FN) * (TN + FP) * (TN + FN)) ** 0.5
            return flag, MCC
        elif ((TP+FP)*(TP+FN)*(TN+FP)*(TN+FN))<0:
            flag = 1
            return flag,None
        elif abs(TP*TN-FP*FN - 0) > 1e-6 and abs(((TP+FP)*(TP+FN)*(TN+FP)*(TN+FN))**0.5 - 0) < 1e-6:
            flag = 2
            return flag, None
        elif abs(TP*TN-FP*FN - 0) < 1e-6 and abs(((TP+FP)*(TP+FN)*(TN+FP)*(TN+FN))**0.5 - 0)< 1e-6:
            flag = 3
            return flag, None
        else:
            flag = 4
            return flag, None

    def fun_GMeasure(self,TP,FN,TN,FP):
        flag = 0
        if abs((TP + FN)-0) > 1e-6 and abs((TP + FP)-0) > 1e-6:
            Recall = TP/(TP+FN)
            TNR = TN/(FP+TN)
            if abs(Recall+TNR - 0) > 1e-6:
                Recall = TP / (TP + FN)
                TNR = TN / (TN + FP)
                GMeasure = 2 * Recall * TNR / (Recall + TNR)
                return flag, GMeasure
            elif abs(2*Recall*TNR - 0) > 1e-6 and abs(Recall+TNR- 0) < 1e-6:
                flag = 1
                return flag, None
            elif abs(2*Recall*TNR - 0) < 1e-6 and abs(Recall+TNR- 0) < 1e-6:
                flag = 2
                return flag, None
        elif abs((TP + FN)-0) < 1e-6 or abs((TP + FP)-0) < 1e-6:
            flag = 3
            return flag ,None
        else:
            flag = 4
            return flag ,None

    def fun_GMean(self,TP,FN,TN,FP):
        flag = 0
        if abs((TP + FN)*(TN + FP)-0)>1e-6 and abs(TP*TN-0)>1e-6 and (TP*TN)/((TP + FN)*(TN + FP))>0:
            Recall = TP / (TP + FN)
            TNR = TN / (TN + FP)
            GMean = ((Recall * TNR)) ** 0.5
            return flag,GMean
        elif abs((TP + FN)*(TN + FP)-0)>1e-6 and abs(TP*TN-0)>1e-6 and (TP*TN)/((TP + FN)*(TN + FP))<0:
            flag = 1
            return flag,None
        elif abs(TP*TN-0)>1e-6 and abs((TP + FN)*(TN + FP)-0)<1e-6:
            flag = 2
            return flag, None
        elif abs(TP*TN-0)<1e-6 and abs((TP + FN)*(TN + FP)-0)<1e-6:
            flag = 3
            return flag, None
        else:
            flag = 4
            return flag, None

    def fun_Balance(self,TP,FN,FP,TN):
        flag = 0
        if abs((FP + TN)-0)>1e-6 and (TP + FN-0)>1e-6:
            Recall = TP / (TP + FN)
            FPR = FP / (FP + TN)
            Balance = 1-((0-FPR)**2+(1-Recall)**2)**0.5/2**0.5
            return flag,Balance
        elif abs((FP + TN)-0)<1e-6 or (TP + FN-0)<1e-6:
            flag = 1
            return flag,None
        else:
            flag = 2
            return flag, None

    def fun_Density(self,TP,FN):
        Density = TP+FN
        return Density

if __name__ == "__main__":

    #固定的，PyQt5程序都需要QApplication对象。sys.argv是命令行参数列表，确保程序可以双击运行
    app = QApplication(sys.argv)
    myWin = MyMainForm()
    #将窗口控件显示在屏幕上

    myWin.show()
    # font  = QFont("黑体")
    # ff = font.pointSize()
    # # font.setBold(True)
    # font.setPointSize(ff*90/72)
    # app.setFont(font)
    #程序运行，sys.exit方法确保程序完整退出。
    sys.exit(app.exec_())
