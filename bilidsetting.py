# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bilidsetting.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(604, 349)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icon/images/bilidownloader.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("*{\n"
"    font: 9pt \"Microsoft YaHei\";\n"
"}\n"
"/* 主体颜色\n"
".QWidget#centralwidget{\n"
"    background-color: rgb(156, 156, 156);\n"
"    border-radius:20px;\n"
"} */\n"
".QWidget#mainwidget{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius:20px;\n"
"}\n"
"\n"
"/* 编辑框样式 */\n"
"QLineEdit{\n"
"    border-radius: 15px;\n"
"    border: 2px solid rgb(255, 153, 153);\n"
"    padding-left: 5px;\n"
"    padding-right: 27px;\n"
"}\n"
"QLineEdit:hover{\n"
"    background-color: rgb(255, 238, 238);\n"
"}\n"
"\n"
"/* 按钮样式 */\n"
"QPushButton[flat=\"false\"]{\n"
"    background-color: rgb(255, 153, 153);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 15px;\n"
"    font: 9pt \"Microsoft YaHei\";\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 153, 153, 255), stop:1 rgba(255, 136, 136, 255));\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(190, 115, 115, 255), stop:1 rgba(255, 153, 153, 255));\n"
"}\n"
"QPushButton#btnclose{\n"
"    background-color: rgb(255, 102, 102);\n"
"    border-radius:8px;\n"
"}\n"
"QPushButton#btnclose:pressed{\n"
"    background-color: rgb(200, 80, 80);\n"
"}\n"
"QPushButton#btnmax{\n"
"    background-color: rgb(255, 255, 102);\n"
"    border-radius:8px;\n"
"}\n"
"QPushButton#btnmax:pressed{\n"
"    background-color: rgb(195, 195, 78);\n"
"}\n"
"QPushButton#btnmin{\n"
"    background-color: rgb(153, 204, 102);\n"
"    border-radius:8px;\n"
"}\n"
"QPushButton#btnmin:pressed{\n"
"    background-color: rgb(126, 168, 83);\n"
"}\n"
"\n"
"/* 进度条样式 */\n"
"QProgressBar{\n"
"    border: 2px solid rgb(255, 153, 153);\n"
"    height: 10px;\n"
"    background-color: rgb(255, 255, 255);\n"
"    font: 10pt \"Microsoft YaHei\";\n"
"    border-radius:6px;\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"QProgressBar::chunk{\n"
"    background-color: rgb(255, 204, 153);\n"
"    border-radius:6px;\n"
"}\n"
"\n"
"/* 选择表样式 */\n"
"QListWidget{\n"
"    border: 2px solid rgb(255, 153, 153);\n"
"    border-radius:15px;\n"
"    padding: 5px;\n"
"}\n"
"QListWidget::item{\n"
"    border: 1px dashed rgb(255, 204, 153);\n"
"    border-radius: 5px\n"
"}\n"
"QListWidget::item:hover{\n"
"    background-color: rgb(255, 204, 153);\n"
"}\n"
"QListWidget::item:focus{\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"/* 选择框样式 */\n"
"QComboBox{\n"
"    border-radius: 15px;\n"
"    border: 2px solid rgb(255, 153, 153);\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"}\n"
"QComboBox:hover{\n"
"    background: rgb(255, 238, 238)\n"
"}\n"
"QComboBox QAbstractItemView{\n"
"    border: 2px solid rgb(255, 153, 153);\n"
"    selection-background-color: rgb(255, 204, 153)\n"
"}\n"
"QComboBox::drop-down {\n"
"     subcontrol-origin: padding;\n"
"     subcontrol- position :  top  left;\n"
"     width :  28px ;\n"
"     border: none;\n"
"}\n"
"QComboBox::down-arrow{\n"
"    image: url(:/combo/images/dd.png);\n"
"}\n"
"QComboBox::down-arrow:hover{\n"
"    image: url(:/combo/images/dd1.png);\n"
"}\n"
"QComboBox::down-arrow:pressed{\n"
"    image: url(:/combo/images/dd2.png);\n"
"}\n"
"\n"
"/* 文本框样式 */\n"
"QPlainTextEdit{\n"
"    border-radius: 15px;\n"
"    border: 2px solid rgb(255, 153, 153);\n"
"    padding: 5px;\n"
"}\n"
"\n"
"/* Title Frame样式 */\n"
"QFrame#title{\n"
"    background-image: url(:/title/images/title.png);\n"
"}\n"
"\n"
"/* 分组框样式 */\n"
"QGroupBox{\n"
"    border: 2px solid rgb(255, 153, 153);\n"
"    border-radius: 15px;\n"
"    margin-top: 2ex;\n"
"}\n"
"QGroupBox::title{\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding: 0 3px;\n"
"}\n"
"\n"
"/* 组合框样式 */\n"
"/*QCheckBox{}*/\n"
"QFrame#title{\n"
"    border: none\n"
"}")
        self.mainwidget = QtWidgets.QWidget(Form)
        self.mainwidget.setGeometry(QtCore.QRect(70, 50, 471, 231))
        self.mainwidget.setObjectName("mainwidget")
        self.btnmax = QtWidgets.QPushButton(self.mainwidget)
        self.btnmax.setGeometry(QtCore.QRect(400, 20, 16, 16))
        self.btnmax.setText("")
        self.btnmax.setFlat(True)
        self.btnmax.setObjectName("btnmax")
        self.btnclose = QtWidgets.QPushButton(self.mainwidget)
        self.btnclose.setGeometry(QtCore.QRect(430, 20, 16, 16))
        self.btnclose.setText("")
        self.btnclose.setFlat(True)
        self.btnclose.setObjectName("btnclose")
        self.btnmin = QtWidgets.QPushButton(self.mainwidget)
        self.btnmin.setGeometry(QtCore.QRect(370, 20, 16, 16))
        self.btnmin.setText("")
        self.btnmin.setFlat(True)
        self.btnmin.setObjectName("btnmin")
        self.label = QtWidgets.QLabel(self.mainwidget)
        self.label.setGeometry(QtCore.QRect(30, 10, 111, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label.setFont(font)
        self.label.setStyleSheet("*{\n"
"    font: 75 10pt \"微软雅黑\";\n"
"}\n"
"")
        self.label.setObjectName("label")
        self.edit_cookies = QtWidgets.QPlainTextEdit(self.mainwidget)
        self.edit_cookies.setGeometry(QtCore.QRect(30, 60, 411, 101))
        self.edit_cookies.setObjectName("edit_cookies")
        self.btn_editcookie = QtWidgets.QPushButton(self.mainwidget)
        self.btn_editcookie.setGeometry(QtCore.QRect(30, 180, 111, 31))
        self.btn_editcookie.setObjectName("btn_editcookie")
        self.btn_wherecookie = QtWidgets.QPushButton(self.mainwidget)
        self.btn_wherecookie.setGeometry(QtCore.QRect(180, 180, 111, 31))
        self.btn_wherecookie.setObjectName("btn_wherecookie")
        self.btn_cleanplain = QtWidgets.QPushButton(self.mainwidget)
        self.btn_cleanplain.setGeometry(QtCore.QRect(330, 180, 111, 31))
        self.btn_cleanplain.setObjectName("btn_cleanplain")

        self.retranslateUi(Form)
        self.btnclose.clicked.connect(Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "修改Cookie"))
        self.label.setText(_translate("Form", "修改Cookie"))
        self.edit_cookies.setPlaceholderText(_translate("Form", "请在此输入您在浏览器中复制的Cookie"))
        self.btn_editcookie.setText(_translate("Form", "修改Cookie"))
        self.btn_wherecookie.setText(_translate("Form", "Cookie在哪？"))
        self.btn_cleanplain.setText(_translate("Form", "清空"))
import images_dl_rc
