# 店铺管理界面
import os
import sys

from PyQt5.QtCore import QFile, QTextStream, Qt, pyqtSlot
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QStackedLayout, QLabel, \
    QTableWidget, QScrollArea, QTableWidgetItem

from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout

class Window2(QWidget):
    def __init__(self):
        super().__init__()

        # 整体布局
        layout = QHBoxLayout(self)
        widget_flow = InformationDisplay()
        widget_flow.setStyleSheet("background-color:#e2dbe3")
        widget_storage = InventoryManagement()
        widget_storage.setStyleSheet("background-color:#cccccc")
        layout.addWidget(widget_flow,3)
        layout.addWidget(widget_storage,2)
        layout.setSpacing(0)

        #  流水窗口部分布局
        layout_flow = QVBoxLayout(widget_flow)
        #  标题标签
        title_flow = QLabel("流水信息")
        title_flow.setStyleSheet("background-color:#70a7ad;font-size:18px;color:white")
        #  列表标题

class InformationDisplay(QWidget):
    def __init__(self):
        super().__init__()

        # 设置整体背景颜色
        self.setStyleSheet("background-color: #A5D63F;")

        # 垂直布局
        main_layout = QVBoxLayout()
        # 第一部分：标题
        title_label = QLabel("流水信息")
        title_label.setStyleSheet("background-color: #cccccc; color:black; font-size: 30px;padding:10px")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setCursor(Qt.PointingHandCursor)  # 设置鼠标样式为手型
        title_label.mousePressEvent = self.on_title_label_clicked  # 绑定点击事件
        main_layout.addWidget(title_label)

        # 第二部分：列表信息标题
        headers = ["订单编号", "操作名称", "时间", "订单金额", "顾客信息"]
        # header_layout = QHBoxLayout()
        # for header in headers:
        #     label = QLabel(header)
        #     label.setStyleSheet("background-color: #FF5733; color: black; font-weight: bold; padding: 5px;")
        #     header_layout.addWidget(label)
        # main_layout.addLayout(header_layout)

        # 第三部分：流水信息表格
        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(len(headers))
        self.table_widget.setHorizontalHeaderLabels(headers)

        # 设置滚动区域
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(self.table_widget)

        main_layout.addWidget(scroll_area)
        self.setLayout(main_layout)

    def add_row(self, data):
        row_position = self.table_widget.rowCount()
        self.table_widget.insertRow(row_position)

        for col, value in enumerate(data):
            item = QTableWidgetItem(str(value))
            self.table_widget.setItem(row_position, col, item)
    # 点击事件：添加新行
    @pyqtSlot()
    def on_title_label_clicked(self, event):
        # 在这里添加你希望执行的点击事件逻辑
        data=get_data_from_server()
        self.add_row(data)
        print("Title Label Clicked!")

class InventoryManagement(QWidget):
    def __init__(self):
        super().__init__()

        # 设置整体背景颜色
        self.setStyleSheet("background-color: #FFEB3B;")

        # 垂直布局
        main_layout = QVBoxLayout()

        # 第一部分：标题
        title_label = QLabel("库存管理")
        title_label.setStyleSheet("background-color: #cccccc; color:black; font-size: 30px;padding:10px")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setCursor(Qt.PointingHandCursor)  # 设置鼠标样式为手型
        title_label.mousePressEvent = self.on_title_label_clicked  # 绑定点击事件
        main_layout.addWidget(title_label)

        # 第二部分：列表信息标题
        headers = ["原料名称", "当前库存量", "状态"]
        header_layout = QHBoxLayout()
        for header in headers:
            label = QLabel(header)
            label.setStyleSheet("background-color: #43CF7C; color: black; font-weight: bold; padding: 5px;")
            header_layout.addWidget(label)
        main_layout.addLayout(header_layout)

        # 第三部分：具体库存信息
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_widget = QWidget()
        self.scroll_layout = QVBoxLayout(self.scroll_widget)
        self.scroll_area.setWidget(self.scroll_widget)
        main_layout.addWidget(self.scroll_area)

        self.setLayout(main_layout)

    @pyqtSlot()
    def on_title_label_clicked(self, event):
        # 模拟向服务器查询信息的函数，实际情况需要根据实际需求修改
        data = self.fetch_data_from_server()
        self.update_inventory_data(data)

    def fetch_data_from_server(self):
        # 示例数据
        example_data = [
            {"name": "生鸡腿", "present_Storage": "3箱", "status": "overpacked"},
            {"name": "新鲜蔬菜", "present_Storage": "15包", "status": "full"},
            {"name": "牛奶", "present_Storage": "10瓶", "status": "normal"},
            {"name": "面粉", "present_Storage": "2袋", "status": "tense"},
            {"name": "冰激凌", "present_Storage": "0箱", "status": "run_out"},
            {"name": "冰激凌", "present_Storage": "0箱", "status": "run_out"},
            {"name": "冰激凌", "present_Storage": "0箱", "status": "run_out"},
            {"name": "冰激凌", "present_Storage": "0箱", "status": "run_out"},
            {"name": "冰激凌", "present_Storage": "0箱", "status": "run_out"},
            {"name": "冰激凌", "present_Storage": "0箱", "status": "run_out"},
            {"name": "冰激凌", "present_Storage": "0箱", "status": "run_out"},
            {"name": "冰激凌", "present_Storage": "0箱", "status": "run_out"},

        ]
        return example_data
        # 模拟从服务器获取数据的逻辑，实际情况需要根据实际需求修改
        try:
            response = requests.get("https://example.com/inventory_data")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data from server: {e}")
            return []

    def update_inventory_data(self, data):
        # 清空之前的数据
        for i in reversed(range(self.scroll_layout.count())):
            widgetToRemove = self.scroll_layout.itemAt(i).widget()
            self.scroll_layout.removeWidget(widgetToRemove)
            widgetToRemove.setParent(None)

        # 添加新数据
        for item in data:
            widget = self.create_inventory_item_widget(item)
            self.scroll_layout.addWidget(widget)

    def create_inventory_item_widget(self, item):
        # 创建一个库存信息框
        widget = QWidget()
        widget.setStyleSheet("background-color: #2A82E4;")

        # 设置信息框内的水平布局
        layout = QHBoxLayout(widget)

        # 根据status设置不同的背景颜色
        status_color_map = {
            "overpacked": "#4ea3c3",
            "full": "#46cc83",
            "normal": "#fdeb3b",
            "tense": "#ffc203",
            "run_out": "#f25d33"
        }
        status = item.get("status", "normal")
        status_color = status_color_map.get(status, "#FFEB3B")

        # 添加信息框内的字段内容
        for field in ["name", "present_Storage", "status"]:
            label = QLabel(str(item.get(field, "")))
            label.setStyleSheet(f"background-color: {status_color}; padding: 5px;")
            layout.addWidget(label)

        return widget

import requests

def get_data_from_server():
    # 模拟添加数据
    data = ["00120313", "取消订单", "18:54", "118￥", "Sherwen"]
    return data
    try:
        # 替换为您的服务器URL
        url = "https://example.com/api/get_data"

        # 发起GET请求
        response = requests.get(url)

        # 检查请求是否成功
        if response.status_code == 200:
            # 返回获取到的数据，这里假设服务器返回的是JSON格式数据
            return response.json()
        else:
            print(f"Failed to fetch data. Status Code: {response.status_code}")
    except Exception as e:
        print(f"Error during request: {e}")

# 使用示例
data = get_data_from_server()
if data:
    print(data)