import json
import sys
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QScrollArea
from UIview_codes.orders_inside.order_details_widget import OrderDetailsPage
from Communication_interface.get_orders import get_order_data


class OrderViewWidget(QWidget):
    def __init__(self,Token):
        self.Token = Token
        super().__init__()

        # 设置整体大小
        self.setFixedSize(924, 510)
        self.setStyleSheet("background-color:#cccccc")

        # 创建OrderDetailsPage实例
        self.order_details_page = None
        order_data = {"orderId": 1, "status": 1, "openid": "user123", "merchantId": "m123",
                      "orderInfos": '[{"id": 101, "num": 2, "conf": "A", "inId": "in123", "name": "item1"}]'}
        self.widget_details = OrderDetailsPage(order_data, self.Token)

        self.overall_layout = QHBoxLayout(self)
        self.overall_layout.setSpacing(0)
        self.overall_layout.setContentsMargins(0, 0, 0, 0)

        # 创建垂直布局
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)

        # 创建Scroll Area
        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)

        # 创建订单列表区域
        self.order_list_widget = QWidget(self)
        self.order_list_layout = QVBoxLayout(self.order_list_widget)
        self.order_list_layout.setSpacing(0)

        # 创建定时器，每隔一段时间刷新订单列表
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.refresh_orders)
        self.timer.start(5000)  # 5秒刷新一次

        # 初始化订单列表
        self.refresh_orders()
        # 设置Scroll Area的 Widget
        scroll_area.setWidget(self.order_list_widget)

        # 将Scroll Area添加到垂直布局
        main_layout.addWidget(scroll_area)
        self.overall_layout.addLayout(main_layout)
        self.overall_layout.addWidget(self.widget_details)

    def create_order_widget(self, order_data):
        # 创建水平布局
        order_layout = QHBoxLayout()
        order_layout.setSpacing(0)

        # 创建左侧垂直布局
        left_layout = QVBoxLayout()
        left_layout.setSpacing(0)

        # 订单编号标签
        label_order_id = QLabel(f"订单编号：\n{order_data['orderId']}")
        label_order_id.setStyleSheet("background-color: #FFC300; font-size: 14px; padding-left:5px")
        label_order_id.setFixedSize(75, 44)
        left_layout.addWidget(label_order_id)

        # 订单数量标签
        label_order_num = QLabel(f"订单数量：\n{len(json.loads(order_data['orderInfos']))}组")
        label_order_num.setStyleSheet("background-color: #FFEB3B; font-size: 14px; padding-left:5px")
        label_order_num.setFixedSize(75, 44)
        left_layout.addWidget(label_order_num)

        # 将左侧垂直布局添加到水平布局
        order_layout.addLayout(left_layout)

        # 订单内容展示区
        order_content_widget = QLabel()
        order_content_widget.setWordWrap(True)
        order_content_widget.setFixedSize(300,88)
        order_content_widget.setStyleSheet("background-color:#F5FF3B; font-size: 18px;padding-top:5px")

        # 将每个obj2小组的内容放在同一行
        obj_array = json.loads(order_data['orderInfos'])
        for obj2 in obj_array:
            content_line = f"   id: {obj2['id']}  {obj2['name']}*{obj2['num']}份 \n"
            order_content_widget.setText(order_content_widget.text() + content_line)

        # 将订单内容展示区添加到水平布局
        order_layout.addWidget(order_content_widget, stretch=376)

        # 订单详情按钮
        btn_detailed_order = QPushButton("订单\n详情")
        btn_detailed_order.setFixedSize(58, 88)
        btn_detailed_order.setStyleSheet("background-color: #A5D63F; font-size: 20px;")
        btn_detailed_order.clicked.connect(lambda: self.show_order_details(order_data))
        order_layout.addWidget(btn_detailed_order, stretch=58)

        # 将整个订单水平布局添加到垂直布局中
        order_widget = QWidget()
        order_widget.setLayout(order_layout)
        order_widget.setStyleSheet("background-color:#cccccc")

        return order_widget

    def remove_order(self, order_layout):
        # 获取按钮所在的订单布局，然后从父布局中删除该订单
        order_widget = order_layout.parentWidget()
        order_widget.setParent(None)

    # 槽函数：处理订单详情按钮点击事件
    def show_order_details(self, order_data):
        # 如果已经存在OrderDetailsPage实例，先关闭它
        if self.widget_details:
            self.widget_details.close()

        # 创建新的OrderDetailsPage实例
        self.widget_details = OrderDetailsPage(order_data,self.Token)
        # 添加到水平布局的右侧
        self.overall_layout.addWidget(self.widget_details)

    def refresh_orders(self):
        response = get_order_data(self.Token)
        # 清空之前的订单列表
        for i in reversed(range(self.order_list_widget.layout().count())):
            self.order_list_widget.layout().itemAt(i).widget().setParent(None)
        response_data = response.json()
        json_content = response_data
        # print('code:', json_content['code'])
        # print('msg:', json_content['msg'])
        # print('data:', json_content['data'])
        # print('\n')
        for obj in json_content['data']:
            print('orderId:', obj['orderId'])
            print('status:', obj['status'])
        #     print('openid:', obj['openid'])
        #     print('merchantId:', obj['merchantId'])
        #     obj_array = json.loads(obj['orderInfos'])
        #     for obj2 in obj_array:
        #         print('   id:', obj2['id'])
        #         print('   num:', obj2['num'])
        #         print('   conf:', obj2['conf'])
        #         print('   inId:', obj2['inId'])
        #         print('   name:', obj2['name'])
        #         print('\n')

        # response_data = {
        #     "code": 200,
        #     "msg": "Success",
        #     "data": [
        #         {
        #             "orderId": 1,
        #             "status": 1,
        #             "openid": "user123",
        #             "merchantId": "m123",
        #             "orderInfos": '[{"id": 101, "num": 2, "conf": "A", "inId": "in123", "name": "item1"}, {"id": 102, "num": 3, "conf": "B", "inId": "in124", "name": "item2"}]'
        #         },
        #         {
        #             "orderId": 2,
        #             "status": 0,
        #             "openid": "user456",
        #             "merchantId": "m124",
        #             "orderInfos": '[{"id": 201, "num": 1, "conf": "C", "inId": "in125", "name": "item3"}]'
        #         },
        #         # Add more orders...
        #     ]
        # }

        # 过滤出status为3的订单
        filtered_orders = [order for order in response_data["data"] if order["status"] == 0]
        # 添加新订单到订单列表
        for order in filtered_orders:
            order_widget = self.create_order_widget(order)
            order_widget.setFixedSize(500, 100)
            self.order_list_widget.layout().addWidget(order_widget)


