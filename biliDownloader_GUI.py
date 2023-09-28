from etc import *
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt
from BiliModule.Main import MainWindow


######################################################################
# 程序入口
QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
app = QApplication(sys.argv)
MainWindow = MainWindow()
MainWindow.show()
sys.exit(app.exec_())
