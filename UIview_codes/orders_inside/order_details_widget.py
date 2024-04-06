import json

import requests
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget, QPushButton, QHBoxLayout, QGridLayout


class OrderDetailsPage(QWidget):
    def __init__(self, order, Token):
        self.Token = Token
        super().__init__()
        self.order_done = order
        # 解析订单数据
        customer_name = "Sherwen"
        order_time = "17:54"
        order_id = order['orderId']
        # 初始化order_content为空字符串
        order_content = ""
        # 将每个obj2小组的内容放在同一行
        obj_array = json.loads(order['orderInfos'])
        for obj2 in obj_array:
            content_line = f"   id: {obj2['id']}  {obj2['name']}*{obj2['num']}份 \n 备注: {obj2['conf']}\n"
            order_content = order_content + content_line

        # 设置整体布局
        main_layout = QVBoxLayout(self)
        main_layout.setSpacing(0)
        main_layout.setContentsMargins(0, 0, 0, 0)
        self.setFixedSize(370, 510)
        self.setStyleSheet("background-color: #70a7ad;")

        # 标题栏
        title_label = QLabel("订单详情")
        title_label.setStyleSheet("background-color: grey; color: white; font-size: 20px;")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setFixedSize(370, 56)
        title_label.setContentsMargins(0, 0, 0, 0)
        main_layout.addWidget(title_label)

        # 顾客信息标签
        customer_info_label = QLabel(f"顾客信息：{customer_name}")
        customer_info_label.setStyleSheet("font-size: 20px;color:white;padding-left:15px;padding-top:10px;")
        customer_info_label.setAlignment(Qt.AlignLeft)
        main_layout.addWidget(customer_info_label)

        # 订单信息标签
        customer_info_label = QLabel(f"订单编号：{order_id}")
        customer_info_label.setStyleSheet("font-size: 20px;color:white;padding-left:15px;")
        customer_info_label.setAlignment(Qt.AlignLeft)
        main_layout.addWidget(customer_info_label)

        # 下单时间标签
        customer_info_label = QLabel(f"下单时间：{order_time}")
        customer_info_label.setStyleSheet("font-size: 20px;color:white;padding-left:15px;")
        customer_info_label.setAlignment(Qt.AlignLeft)
        main_layout.addWidget(customer_info_label)

        # 订单内容标签
        order_content_label = QLabel(f"订单内容：\n{order_content}")
        order_content_label.setStyleSheet("font-size: 20px;color:white;padding-left:15px;")
        order_content_label.setAlignment(Qt.AlignLeft)
        order_content_label.setFixedSize(370, 200)
        order_content_label.setWordWrap(True)
        main_layout.addWidget(order_content_label)

        # 预计完成时间选择框
        due_time_widget = QWidget()
        due_time_widget.setFixedSize(370, 100)
        due_time_widget.setStyleSheet("background-color: #F5C18E;")

        due_time_layout = QHBoxLayout(due_time_widget)
        due_time_layout.setContentsMargins(0, 0, 0, 0)
        label_due_time = QLabel("预计\n完成\n时间")
        label_due_time.setContentsMargins(0, 0, 0, 0)
        label_due_time.setStyleSheet("background-color: #5E9BE0; font-size: 20px;padding-top:15px;color:white;")
        label_due_time.setAlignment(Qt.AlignLeft)
        label_due_time.setFixedSize(50, 150)

        grid_layout = QGridLayout()
        grid_layout.setSpacing(0)

        # 设置四个按钮，每个按钮点击时将 due_time 置为相应数字
        time_options = [3, 5, 10, 15]
        for i, time_option in enumerate(time_options):
            button = QPushButton(f"{time_option}分钟")
            button.setStyleSheet("background-color: grey; font-size: 15px;height:25px")
            button.clicked.connect(lambda _, t=time_option: self.set_due_time(t))
            grid_layout.addWidget(button, i // 2, i % 2)

        btn_report = QPushButton("上报")
        btn_report.setStyleSheet("background-color: #BFE077; font-size: 20px;")
        btn_report.clicked.connect(self.report_due_time)

        due_time_layout.addWidget(label_due_time)
        due_time_layout.addLayout(grid_layout)
        due_time_layout.addWidget(btn_report)
        due_time_layout.setContentsMargins(0, 0, 0, 0)

        main_layout.addWidget(due_time_widget)

        # 水平布局
        button_layout = QHBoxLayout()
        button_layout.setContentsMargins(0, 0, 0, 0)

        # 联系顾客按钮
        btn_contact_customer = QPushButton("联系顾客")
        btn_contact_customer.setContentsMargins(0, 0, 0, 0)
        btn_contact_customer.setStyleSheet("background-color: #A5D63F; font-size: 25px;")
        btn_contact_customer.clicked.connect(self.contact_customer)

        # 更新订单按钮
        btn_update_order = QPushButton("完成订单")
        btn_update_order.setStyleSheet("background-color: #FFBEB0; font-size: 25px;")
        btn_update_order.clicked.connect(lambda Token: self.done_order(self.Token))

        button_layout.addWidget(btn_contact_customer)
        button_layout.addWidget(btn_update_order)

        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)

    def set_due_time(self, time):
        # 处理设置预计完成时间的逻辑
        pass

    def report_due_time(self):
        # 处理上报预计完成时间的逻辑
        pass

    def contact_customer(self):
        # 处理联系顾客的逻辑
        pass

    def done_order(self, token):
        print('这里是token：', token)
        print('这里是order:',self.order_done)
        url = "http://yspt.fun:8080/Merchant/update/Order/complish"
        headers = {
            "token": token,
            "content-type": "application/json"
        }
        response = requests.post(url, json=self.order_done, headers=headers)

        print(response.text)

        # 检查响应状态码
        if response.status_code == 200:
            # 使用 response.json() 解析 JSON 字符串
            response_data = response.json()
            # 获取并打印 msg 字段的值
            msg_value = response_data['msg']
            print(msg_value)
        else:
            print('请求失败:', response.status_code)
        # # 处理更新订单的逻辑
        # # 使用函数
        # # token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIxIiwiZXhwIjoxNzA4ODc3OTQ0fQ.d-l48TiKhb5uRg03jOpaRb4ZYAVi_UrYX67fXZdAzsI'
        #
        # # 检查响应状态码
        # if response.status_code == 200:
        #     # 解析 JSON 字符串
        #     response_data = json.loads(response)
        #     # 获取并打印 msg 字段的值
        #     msg_value = response_data['msg']
        #     print(msg_value)
        # else:
        #     print('请求失败:', response.status_code)
        # pass
