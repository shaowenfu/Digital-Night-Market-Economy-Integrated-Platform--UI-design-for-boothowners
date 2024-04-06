import sys
import os
from PyQt5.QtCore import QFile, QTextStream
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QStackedLayout
from UIview_codes.orders import Window1
from UIview_codes.shop_booth import Window2
from UIview_codes.environment import Window3
from UIview_codes.cultural_neighbor import Window4
from UIview_codes.setting import Window5


class MainWindow_UI(QWidget):
    def __init__(self,Token):
        self.Token = Token
        super().__init__()
        self.create_stacked_layout()
        self.init_ui()

    # def set_param(self, Token):
    #     self.Token = Token

    def create_stacked_layout(self):
        self.stacked_layout = QStackedLayout()
        win1 = Window1(self.Token)
        win2 = Window2()
        win3 = Window3()
        win4 = Window4()
        win5 = Window5()
        for win in [win1, win2, win3, win4, win5]:
            win.setContentsMargins(0, 0, 0, 0)
            win.setFixedSize(924,600)
            self.stacked_layout.addWidget(win)
        self.stacked_layout.setSpacing(0)

    def init_ui(self):
        self.setFixedSize(1024, 600)
        container = QHBoxLayout()
        container.setSpacing(0)

        widget_content = QWidget()
        widget_content.setObjectName("widget_content")
        widget_content.setLayout(self.stacked_layout)
        widget_content.setContentsMargins(0, 0, 0, 0)
        widget_content.setFixedSize(924, 600)

        widget_list = QWidget()
        widget_list.setObjectName("widget_list")
        widget_list.setFixedSize(100, 600)
        widget_list.setContentsMargins(0, 0, 0, 0)
        list_layout = QVBoxLayout()
        widget_list.setLayout(list_layout)
        btn_press1 = QPushButton("订单管理")
        btn_press2 = QPushButton("商铺管理")
        btn_press3 = QPushButton("环境数据")
        btn_press4 = QPushButton("文化社区")
        btn_press5 = QPushButton("设置")
        for btn in [btn_press1, btn_press2, btn_press3, btn_press4, btn_press5]:
            btn.setStyleSheet("padding: 0; margin: 0; border: none;color:black")
            list_layout.addWidget(btn)
            btn.clicked.connect(self.on_button_clicked)

        container.addWidget(widget_list)
        container.addWidget(widget_content)
        self.setLayout(container)

        # 通过绝对路径加载样式表
        style_path = os.path.abspath('E:\\all_workspace\pyQt_projects\DaChuang4\qss_file\widget_List_qss.css')
        style_file = QFile(style_path)
        if style_file.open(QFile.ReadOnly | QFile.Text):
            style_stream = QTextStream(style_file)
            self.setStyleSheet(style_stream.readAll())
            style_file.close()

    def on_button_clicked(self):
        sender = self.sender()
        if sender.text() == "订单管理":
            self.stacked_layout.setCurrentIndex(0)
        elif sender.text() == "商铺管理":
            self.stacked_layout.setCurrentIndex(1)
        elif sender.text() == "环境数据":
            self.stacked_layout.setCurrentIndex(2)
        elif sender.text() == "文化社区":
            self.stacked_layout.setCurrentIndex(3)
        elif sender.text() == "设置":
            self.stacked_layout.setCurrentIndex(4)
