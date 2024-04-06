# 登录页面的逻辑实现
from UIview_codes.Login_UI import Login_MainWindow
from PyQt5.QtWidgets import QMainWindow
from Communication_interface.login_Commu import login_request
from utils.sha256_hash import sha256_hash

class Login_fuc(Login_MainWindow, QMainWindow):
    def __init__(self):
        super(Login_fuc, self).__init__()
        self.setupUi(self)
        # 绑定按钮点击函数
        self.pushButton_login.clicked.connect(self.login_button_clicked)

    def login_button_clicked(self):
        # 具体登录逻辑实现
        username = self.account_edit.text()
        password = self.password_edit.text()
        res = sha256_hash(password)
        print("输入密码的hash值为：",res)
        # 调用通信接口，发送登录请求
        login_request(self,username, res)