# 环境数据界面
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QStackedLayout, QLabel, QSizePolicy, \
    QHBoxLayout

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton
from PyQt5.QtGui import QPixmap, QFont, QIcon
from PyQt5.QtCore import QTimer, Qt


class Window3(QWidget):
    def __init__(self):
        super().__init__()

        # 整体垂直布局
        main_layout = QVBoxLayout(self)

        # 标题栏
        title_widget = QWidget()
        title_widget.setStyleSheet("background-color: #a2d934")
        title_layout = QVBoxLayout(title_widget)

        title_label = QLabel("环境数据展示")
        title_label.setStyleSheet("background-color: #fdeb3b; color: black; font-weight: bold; font-size: 18px")
        title_label.setAlignment(Qt.AlignCenter)
        title_layout.addWidget(title_label)

        main_layout.addWidget(title_widget,1)

        # 信息栏
        info_layout = QHBoxLayout()

        # 传感器数据展示区
        sensor_widget = QWidget()
        sensor_layout = QVBoxLayout(sensor_widget)

        sensor_data_labels = ["温度：", "湿度：", "可燃性气体浓度："]
        sensor_values = ["20°", "45%", "5%"]
        i=1
        for label, value in zip(sensor_data_labels, sensor_values):
            sensor_row_layout = QHBoxLayout()

            icon_label = QLabel()
            icon_label.setFixedSize(50, 50)
            if i==1:
                icon_label.setPixmap(QIcon("icon1.png").pixmap(50, 50))  # 使用你的图标文件路径
            elif i==2:
                icon_label.setPixmap(QIcon("icon2.png").pixmap(50, 50))  # 使用你的图标文件路径
            else:
                icon_label.setPixmap(QIcon("icon3.png").pixmap(50, 50))  # 使用你的图标文件路径
            i = i+1
            label1 = QLabel(label)
            label2 = QLabel(value)

            sensor_row_layout.addWidget(icon_label)
            sensor_row_layout.addWidget(label1)
            sensor_row_layout.addWidget(label2)

            sensor_layout.addLayout(sensor_row_layout)

        refresh_button = QPushButton("刷新")
        refresh_button.clicked.connect(self.read_sensor_data)

        sensor_layout.addWidget(refresh_button)

        info_layout.addWidget(sensor_widget)

        # 天气预报信息区
        weather_widget = QWidget()
        weather_widget.setStyleSheet("background-color: #70a7ad")
        self.weather_layout = QVBoxLayout(weather_widget)

        weather_title = QLabel("天气预报")
        weather_title.setStyleSheet("background-color: grey; color: black; font-weight: bold; font-size: 18px")
        weather_title.setAlignment(Qt.AlignCenter)
        self.weather_layout.addWidget(weather_title)

        # 添加天气预报数据的展示，这里需要使用接口获取数据并展示
        self.update_weather_info()  # 初始化时更新天气信息
        # 添加 QLabel 到布局中
        info_layout.addLayout(self.weather_layout)

        info_layout.addWidget(weather_widget)

        main_layout.addLayout(info_layout,5)

        self.setWindowTitle('Environment Display')
        self.setGeometry(100, 100, 800, 600)

    def read_sensor_data(self):
        # 这里编写读取传感器数据的逻辑，更新相应的 QLabel 的文本
        pass
    def update_weather_info(self):
        weather_data_list = [
            {"time": "21:00", "weather": "晴"},
            {"time": "08:30", "weather": "多云"},
            {"time": "15:45", "weather": "雨"},
            {"time": "12:00", "weather": "阴"},
            {"time": "18:20", "weather": "雪"},
        ]

        # 清空天气布局中的所有控件
        for i in reversed(range(self.weather_layout.count())):
            self.weather_layout.itemAt(i).widget().setParent(None)

        # 重新添加天气信息
        for data in weather_data_list:
            time_label = QLabel(f"时间：{data['time']}")
            weather_label = QLabel(f"天气：{data['weather']}")

            # 这里可以设置 QLabel 的样式，例如背景颜色、字体大小等
            time_label.setStyleSheet("background-color: #29DDE3; font-size: 16px;")
            weather_label.setStyleSheet("background-color: #29DDE3; font-size: 16px;")

            # 将 QLabel 添加到天气布局中
            self.weather_layout.addWidget(time_label)
            self.weather_layout.addWidget(weather_label)