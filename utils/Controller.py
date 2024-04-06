# 控制器页面
from PyQt5.QtCore import pyqtSignal

from Fuction_codes.Login_fuction import Login_fuc
from UIview_codes.MainWindow_UI import MainWindow_UI
class Controller:
    def __init__(self):
        pass
    # 跳转到 login 窗口
    def show_login(self):
        self.login = Login_fuc()
        self.login.switch_to_MainWindow.connect(lambda Token:self.show_MainWindow(Token))
        # 从文件中加载样式表，并指定编码为utf-8
        style_file = open('qss_file/login_qss.css', 'r', encoding='utf-8')
        self.style = style_file.read()
        style_file.close()
        self.login.show()

    # 跳转到 operate 窗口, 注意关闭原页面
    def show_MainWindow(self,Token):
        self.mainWindow = MainWindow_UI(Token)
        # self.mainWindow.set_param(Token)
        self.login.close()
        # style_file = open('qss_file/MainWindow_qss.css', 'r', encoding='utf-8')
        # self.style = style_file.read()
        # style_file.close()
        self.mainWindow.show()
