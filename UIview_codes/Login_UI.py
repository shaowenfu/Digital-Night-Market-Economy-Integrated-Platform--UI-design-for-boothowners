from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget


class Login_MainWindow(QWidget):
    switch_to_MainWindow = pyqtSignal(str)  # 跳转信号

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 480)
        # 创建文本浏览器部件
        self.textBrowser = QtWidgets.QTextBrowser(self)
        self.textBrowser.setGeometry(QtCore.QRect(10, 10, 320, 470))
        self.textBrowser.setObjectName("textBrowser")

        # 创建分割线
        self.line = QtWidgets.QFrame(MainWindow)
        self.line.setGeometry(QtCore.QRect(330, 0, 2, 480))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        # 创建标签和用户名输入框
        self.name = QtWidgets.QLabel(MainWindow)
        self.name.setGeometry(QtCore.QRect(360, 50, 150, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.name.setFont(font)
        self.name.setObjectName("name")

        self.account_edit = QtWidgets.QLineEdit(MainWindow)
        self.account_edit.setGeometry(QtCore.QRect(500, 50, 240, 50))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.account_edit.setFont(font)
        self.account_edit.setObjectName("account_edit")

        # 创建标签和密码输入框
        self.code = QtWidgets.QLabel(MainWindow)
        self.code.setGeometry(QtCore.QRect(360, 150, 150, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.code.setFont(font)
        self.code.setObjectName("code")

        self.password_edit = QtWidgets.QLineEdit(MainWindow)
        self.password_edit.setGeometry(QtCore.QRect(500, 150, 240, 50))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.password_edit.setFont(font)
        self.password_edit.setObjectName("line_code")

        # 创建登录和忘记密码按钮
        self.pushButton_login = QtWidgets.QPushButton(MainWindow)
        self.pushButton_login.setGeometry(QtCore.QRect(470, 250, 220, 60))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_login.setFont(font)
        self.pushButton_login.setObjectName("pushButton_login")

        self.pushButton_help = QtWidgets.QPushButton(MainWindow)
        self.pushButton_help.setGeometry(QtCore.QRect(470, 340, 220, 60))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_help.setFont(font)
        self.pushButton_help.setObjectName("pushButton_help")

        # 设置UI文本
        self.retranslateUi(MainWindow)

        # 连接槽函数
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "登录窗口"))
        # 设置图标
        MainWindow.setWindowIcon(QIcon('E:\\all_workspace\pyQt_projects\DaChuang2\imgs\login.png'))
        user_agreement_text = """
        <h2>用户协议</h2>
        <p>欢迎使用本软件。在使用本软件之前，请您务必仔细阅读并同意以下用户协议：</p>
        <p>1. 本软件的所有权和运营权归开发者所有。</p>
        <p>2. 您可以免费使用本软件，但不得对其进行任何形式的修改、翻译、反向工程等。</p>
        <p>3. 在使用本软件过程中，您需遵守国家法律法规，不得用于非法用途。</p>
        <p>4. 本软件不对用户使用过程中产生的数据丢失负责。</p>
        <p>5. 本用户协议可能会根据软件版本更新而进行调整，请您在使用前查阅最新版本。</p>
        """

        self.textBrowser.setHtml(_translate("MainWindow", user_agreement_text))
        self.name.setText(_translate("MainWindow", "用户名："))
        self.code.setText(_translate("MainWindow", "  密码："))
        self.pushButton_login.setText(_translate("MainWindow", "登录"))
        self.pushButton_help.setText(_translate("MainWindow", "忘记密码？"))