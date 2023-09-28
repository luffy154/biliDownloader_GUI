# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'bilidsetting.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from UI import images_dl_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(620, 613)
        icon = QIcon()
        icon.addFile(u":/Icon/images/bilidownloader.ico", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet(u"*{\n"
"	font: 14px \"Microsoft YaHei\";\n"
"	color:rgb(0, 0, 0);\n"
"}\n"
"/* \u4e3b\u4f53\u989c\u8272\n"
".QWidget#centralwidget{\n"
"	background-color: rgb(156, 156, 156);\n"
"	border-radius:20px;\n"
"} */\n"
"QLabel{\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
".QWidget#mainwidget{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius:20px;\n"
"}\n"
"\n"
"/* \u7f16\u8f91\u6846\u6837\u5f0f */\n"
"QLineEdit{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 15px;\n"
"	border: 2px solid rgb(255, 153, 153);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"}\n"
"QLineEdit:hover{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(255, 238, 238);\n"
"}\n"
"\n"
"/* \u6309\u94ae\u6837\u5f0f */\n"
"QPushButton[flat=\"false\"]{\n"
"	background-color: rgb(255, 153, 153);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 15px;\n"
"	font: 15px \"Microsoft YaHei\";\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop"
                        ":0 rgba(255, 153, 153, 255), stop:1 rgba(255, 136, 136, 255));\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(190, 115, 115, 255), stop:1 rgba(255, 153, 153, 255));\n"
"}\n"
"QPushButton#btnclose{\n"
"	background-color: rgb(255, 102, 102);\n"
"	border-radius:8px;\n"
"}\n"
"QPushButton#btnclose:pressed{\n"
"	background-color: rgb(200, 80, 80);\n"
"}\n"
"QPushButton#btnmax{\n"
"	background-color: rgb(255, 255, 102);\n"
"	border-radius:8px;\n"
"}\n"
"QPushButton#btnmax:pressed{\n"
"	background-color: rgb(195, 195, 78);\n"
"}\n"
"QPushButton#btnmin{\n"
"	background-color: rgb(153, 204, 102);\n"
"	border-radius:8px;\n"
"}\n"
"QPushButton#btnmin:pressed{\n"
"	background-color: rgb(126, 168, 83);\n"
"}\n"
"\n"
"/* \u8fdb\u5ea6\u6761\u6837\u5f0f */\n"
"QProgressBar{\n"
"	border: 2px solid rgb(255, 153, 153);\n"
"	height: 10px;\n"
"	background-color: rgb(255, 255, 255);\n"
"	font: 16px \"Microsoft YaHei\";\n"
"	border-radius:6px;\n"
"	color: rgb(0, "
                        "0, 0);\n"
"}\n"
"QProgressBar::chunk{\n"
"	background-color: rgb(255, 204, 153);\n"
"	border-radius:6px;\n"
"}\n"
"\n"
"/* \u9009\u62e9\u8868\u6837\u5f0f */\n"
"QListWidget{\n"
"	border: 2px solid rgb(255, 153, 153);\n"
"	border-radius:15px;\n"
"	padding: 5px;\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"QListWidget::item{\n"
"	border: 1px dashed rgb(255, 204, 153);\n"
"	border-radius: 5px;\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"QListWidget::item:hover{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(255, 204, 153);\n"
"}\n"
"QListWidget::item:focus{\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"/* \u9009\u62e9\u6846\u6837\u5f0f */\n"
"QComboBox{\n"
"	border-radius: 15px;\n"
"	border: 2px solid rgb(255, 153, 153);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"QComboBox:hover{\n"
"	color: rgb(0, 0, 0);\n"
"	background: rgb(255, 238, 238)\n"
"}\n"
"QComboBox QAbstractItemView{\n"
"	bo"
                        "rder: 2px solid rgb(255, 153, 153);\n"
"	selection-background-color: rgb(255, 204, 153)\n"
"}\n"
"QComboBox::drop-down {\n"
"     subcontrol-origin: padding;\n"
"     subcontrol- position :  top  left;\n"
"     width :  28px ;\n"
"     border: none;\n"
"}\n"
"QComboBox::down-arrow{\n"
"	image: url(:/combo/images/dd.png);\n"
"}\n"
"QComboBox::down-arrow:hover{\n"
"	image: url(:/combo/images/dd1.png);\n"
"}\n"
"QComboBox::down-arrow:pressed{\n"
"	image: url(:/combo/images/dd2.png);\n"
"}\n"
"\n"
"/* \u6587\u672c\u6846\u6837\u5f0f */\n"
"QPlainTextEdit{\n"
"	border-radius: 15px;\n"
"	border: 2px solid rgb(255, 153, 153);\n"
"	padding: 5px;\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* Title Frame\u6837\u5f0f */\n"
"QFrame#title{\n"
"	background-image: url(:/title/images/title.png);\n"
"	border: none;\n"
"}\n"
"\n"
"/* \u5206\u7ec4\u6846\u6837\u5f0f */\n"
"QGroupBox{\n"
"	border: 2px solid rgb(255, 153, 153);\n"
"	border-radius: 15px;\n"
"	margin-top: 2ex;\n"
"}\n"
"QGroupB"
                        "ox::title{\n"
"	subcontrol-origin: margin;\n"
"	subcontrol-position: top center;\n"
"	padding: 0 3px;\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"/* \u7ec4\u5408\u6846\u6837\u5f0f */\n"
"QCheckBox{\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"\n"
"/* \u6811\u5f62\u6846\u6837\u5f0f */\n"
"QTreeWidget{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(255, 153, 153);\n"
"	border-radius: 15px;\n"
"	padding: 5px;\n"
"}\n"
"QTreeWidget::item{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 1px dashed rgb(255, 204, 153);\n"
"	border-radius: 5px;\n"
"}\n"
"QTreeWidget::item:hover{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(255, 204, 153);\n"
"}\n"
"")
        self.mainwidget = QWidget(Form)
        self.mainwidget.setObjectName(u"mainwidget")
        self.mainwidget.setGeometry(QRect(40, 40, 531, 531))
        self.btnmax = QPushButton(self.mainwidget)
        self.btnmax.setObjectName(u"btnmax")
        self.btnmax.setGeometry(QRect(460, 20, 16, 16))
        self.btnmax.setFlat(True)
        self.btnclose = QPushButton(self.mainwidget)
        self.btnclose.setObjectName(u"btnclose")
        self.btnclose.setGeometry(QRect(490, 20, 16, 16))
        self.btnclose.setFlat(True)
        self.btnmin = QPushButton(self.mainwidget)
        self.btnmin.setObjectName(u"btnmin")
        self.btnmin.setGeometry(QRect(430, 20, 16, 16))
        self.btnmin.setFlat(True)
        self.label = QLabel(self.mainwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 10, 111, 41))
        font = QFont()
        font.setFamily(u"\u5fae\u8f6f\u96c5\u9ed1")
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(QFont.Normal)
        self.label.setFont(font)
        self.label.setStyleSheet(u"*{\n"
"	font: 18px \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"}\n"
"")
        self.groupBox = QGroupBox(self.mainwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(30, 260, 471, 121))
        self.btn_cleanplain = QPushButton(self.groupBox)
        self.btn_cleanplain.setObjectName(u"btn_cleanplain")
        self.btn_cleanplain.setGeometry(QRect(340, 30, 111, 31))
        self.edit_cookies = QPlainTextEdit(self.groupBox)
        self.edit_cookies.setObjectName(u"edit_cookies")
        self.edit_cookies.setGeometry(QRect(20, 30, 311, 71))
        self.btn_wherecookie = QPushButton(self.groupBox)
        self.btn_wherecookie.setObjectName(u"btn_wherecookie")
        self.btn_wherecookie.setGeometry(QRect(340, 70, 111, 31))
        self.groupBox_2 = QGroupBox(self.mainwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(30, 50, 471, 201))
        self.lineEdit = QLineEdit(self.groupBox_2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(90, 30, 361, 31))
        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 30, 72, 31))
        self.btn_testProxy = QPushButton(self.groupBox_2)
        self.btn_testProxy.setObjectName(u"btn_testProxy")
        self.btn_testProxy.setGeometry(QRect(360, 150, 93, 31))
        self.cb_useProxy = QCheckBox(self.groupBox_2)
        self.cb_useProxy.setObjectName(u"cb_useProxy")
        self.cb_useProxy.setGeometry(QRect(20, 70, 101, 31))
        self.btn_huseProxy = QPushButton(self.groupBox_2)
        self.btn_huseProxy.setObjectName(u"btn_huseProxy")
        self.btn_huseProxy.setGeometry(QRect(280, 70, 171, 31))
        self.lineEdit_test = QLineEdit(self.groupBox_2)
        self.lineEdit_test.setObjectName(u"lineEdit_test")
        self.lineEdit_test.setEnabled(True)
        self.lineEdit_test.setGeometry(QRect(20, 150, 331, 31))
        self.lineEdit_test.setStyleSheet(u"/* \u7f16\u8f91\u6846\u6837\u5f0f */\n"
"QLineEdit{\n"
"	border-radius: 15px;\n"
"	border: 2px solid rgb(255, 153, 153);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"}")
        self.lineEdit_test.setAlignment(Qt.AlignCenter)
        self.lineEdit_test.setReadOnly(True)
        self.cb_useAuth = QCheckBox(self.groupBox_2)
        self.cb_useAuth.setObjectName(u"cb_useAuth")
        self.cb_useAuth.setGeometry(QRect(120, 70, 151, 31))
        self.le_AuthUsr = QLineEdit(self.groupBox_2)
        self.le_AuthUsr.setObjectName(u"le_AuthUsr")
        self.le_AuthUsr.setEnabled(False)
        self.le_AuthUsr.setGeometry(QRect(90, 110, 151, 31))
        self.le_AuthUsr.setAlignment(Qt.AlignCenter)
        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 110, 72, 31))
        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(260, 110, 31, 31))
        self.le_AuthPwd = QLineEdit(self.groupBox_2)
        self.le_AuthPwd.setObjectName(u"le_AuthPwd")
        self.le_AuthPwd.setEnabled(False)
        self.le_AuthPwd.setGeometry(QRect(300, 110, 151, 31))
        self.le_AuthPwd.setEchoMode(QLineEdit.Password)
        self.le_AuthPwd.setAlignment(Qt.AlignCenter)
        self.btn_editconfig = QPushButton(self.mainwidget)
        self.btn_editconfig.setObjectName(u"btn_editconfig")
        self.btn_editconfig.setGeometry(QRect(200, 480, 141, 31))
        self.btn_cancel = QPushButton(self.mainwidget)
        self.btn_cancel.setObjectName(u"btn_cancel")
        self.btn_cancel.setGeometry(QRect(360, 480, 141, 31))
        self.groupBox_3 = QGroupBox(self.mainwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(30, 390, 471, 81))
        self.label_3 = QLabel(self.groupBox_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 30, 91, 31))
        self.label_4 = QLabel(self.groupBox_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(270, 30, 71, 31))
        self.dl_err = QSpinBox(self.groupBox_3)
        self.dl_err.setObjectName(u"dl_err")
        self.dl_err.setGeometry(QRect(130, 30, 81, 31))
        self.dl_err.setMinimum(0)
        self.dl_err.setValue(3)
        self.chunk_size = QSpinBox(self.groupBox_3)
        self.chunk_size.setObjectName(u"chunk_size")
        self.chunk_size.setGeometry(QRect(350, 30, 81, 31))
        self.chunk_size.setMinimum(128)
        self.chunk_size.setMaximum(4096)
        self.chunk_size.setValue(1024)

        self.retranslateUi(Form)
        self.btnclose.clicked.connect(Form.close)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u9ad8\u7ea7\u8bbe\u7f6e", None))
        self.btnmax.setText("")
        self.btnclose.setText("")
        self.btnmin.setText("")
        self.label.setText(QCoreApplication.translate("Form", u"\u9ad8\u7ea7\u8bbe\u7f6e", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"Cookie\u4fee\u6539", None))
        self.btn_cleanplain.setText(QCoreApplication.translate("Form", u"\u6e05\u7a7a", None))
        self.edit_cookies.setPlaceholderText(QCoreApplication.translate("Form", u"\u8bf7\u5728\u6b64\u8f93\u5165\u60a8\u5728\u6d4f\u89c8\u5668\u4e2d\u590d\u5236\u7684Cookie", None))
        self.btn_wherecookie.setText(QCoreApplication.translate("Form", u"Cookie\u5728\u54ea\uff1f", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"\u4ee3\u7406\u8bbe\u7f6e", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"\u8f93\u5165\u4ee3\u7406\u5730\u5740", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u4ee3\u7406\u5730\u5740", None))
        self.btn_testProxy.setText(QCoreApplication.translate("Form", u"\u6d4b\u8bd5\u4ee3\u7406", None))
        self.cb_useProxy.setText(QCoreApplication.translate("Form", u"\u4f7f\u7528\u4ee3\u7406", None))
        self.btn_huseProxy.setText(QCoreApplication.translate("Form", u"\u5982\u4f55\u4f7f\u7528\u4ee3\u7406\uff1f", None))
        self.lineEdit_test.setText(QCoreApplication.translate("Form", u"\u6d4b\u8bd5\u72b6\u6001\uff1a\u672a\u6d4b\u8bd5", None))
        self.cb_useAuth.setText(QCoreApplication.translate("Form", u"\u4f7f\u7528\u4ee3\u7406\u8eab\u4efd\u9a8c\u8bc1", None))
        self.le_AuthUsr.setPlaceholderText(QCoreApplication.translate("Form", u"\u8f93\u5165\u767b\u5f55\u7528\u6237\u540d", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u767b\u5f55\u540d\u79f0", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u5bc6\u7801", None))
        self.le_AuthPwd.setPlaceholderText(QCoreApplication.translate("Form", u"\u8f93\u5165\u767b\u5f55\u9a8c\u8bc1\u5bc6\u7801", None))
        self.btn_editconfig.setText(QCoreApplication.translate("Form", u"\u786e\u5b9a\u8bbe\u7f6e", None))
        self.btn_cancel.setText(QCoreApplication.translate("Form", u"\u53d6\u6d88\u8bbe\u7f6e", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Form", u"\u4e0b\u8f7d\u8bbe\u7f6e", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u4e0b\u8f7d\u91cd\u8bd5\u6b21\u6570", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u6570\u636e\u5305\u5927\u5c0f", None))
    # retranslateUi

