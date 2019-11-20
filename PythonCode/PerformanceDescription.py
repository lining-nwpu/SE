import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QLabel
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
class Dialog(QDialog):
    """
    对话框类
    """

    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)

        # 设置对话框的标题及大小
        self.setWindowTitle('性能指标说明')
        self.resize(400,400)
        self.setMinimumSize(QtCore.QSize(400, 400))
        self.setMaximumSize(QtCore.QSize(400, 400))
        # 设置窗口为模态，用户只有关闭弹窗后，才能关闭主界面
        self.setWindowModality(Qt.ApplicationModal)
        self.label = QLabel(self)
        self.label.setGeometry(QtCore.QRect(20,20,370,370))
        self.label.setObjectName("label")
