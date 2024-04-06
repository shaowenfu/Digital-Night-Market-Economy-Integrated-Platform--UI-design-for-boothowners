# 订单界面
from PyQt5.QtCore import QFile, QTextStream

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from UIview_codes.orders_inside.Notice_Widget import NoticeWidget
from UIview_codes.orders_inside.Order_list import OrderViewWidget


# 窗口一订单页面
class Window1(QWidget):
    def __init__(self,Token):
        self.Token = Token
        super().__init__()
        # 定义上方通知栏
        # 创建通知栏
        notice_widget = NoticeWidget(self)
        notice_widget.setStyleSheet("background-color: orange;margin:0px;padding:0px")
        # 创建订单列表
        widget_orders = OrderViewWidget(self.Token)

        orders_layout2 = QVBoxLayout(self)
        orders_layout2.setSpacing(0)  # 设置垂直布局的间距为0
        orders_layout2.addWidget(notice_widget)
        orders_layout2.addWidget(widget_orders)
        orders_layout2.setContentsMargins(0, 0, 0, 0)
        # 应用样式表
        style_file = QFile('qss_file/Window1.css')
        if style_file.open(QFile.ReadOnly | QFile.Text):
            stream = QTextStream(style_file)
            self.setStyleSheet(stream.readAll())
            style_file.close()

