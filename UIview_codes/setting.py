from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QWidget, QCheckBox, QSlider, QPushButton, QComboBox, QHBoxLayout


class Window5(QWidget):
    def __init__(self):
        super(Window5, self).__init__()
        # 设置整体布局
        self.main_layout = QVBoxLayout(self)

        # 创建标题栏
        self.create_title_bar()

        # 创建设置项
        self.create_settings()

    def create_title_bar(self):
        title_widget = QWidget(self)
        title_widget.setStyleSheet("background-color: #70a7ad;")  # 使用绿色，你可以根据需要调整颜色

        # 创建标题标签
        title_label = QLabel("设置", title_widget)
        title_label.setStyleSheet("background-color: #333; color: white; font-weight: bold;")  # 使用深灰色背景，白色字体
        title_label.setAlignment(Qt.AlignCenter)

        # 将标题标签放置在标题栏中央
        title_layout = QVBoxLayout(title_widget)
        title_layout.addWidget(title_label, alignment=Qt.AlignCenter)

        # 将标题栏添加到整体布局
        self.main_layout.addWidget(title_widget)

    def create_settings(self):
        # 创建设置项垂直布局
        settings_layout = QVBoxLayout()

        layout1 = QHBoxLayout()
        # 示例设置项1：夜间模式
        night_mode_label = QLabel("夜间模式")
        night_mode_checkbox = QCheckBox(self)
        layout1.addWidget(night_mode_label)
        layout1.addWidget(night_mode_checkbox)
        settings_layout.addLayout(layout1)

        layout2 = QHBoxLayout()
        # 示例设置项2：音效开关
        sound_label = QLabel("音效")
        sound_checkbox = QCheckBox(self)
        layout2.addWidget(sound_label)
        layout2.addWidget(sound_checkbox)
        settings_layout.addLayout(layout2)

        layout3 = QHBoxLayout()
        # 示例设置项3：亮度调节
        brightness_label = QLabel("屏幕亮度")
        brightness_slider = QSlider(Qt.Horizontal)
        layout3.addWidget(brightness_label)
        layout3.addWidget(brightness_slider)
        settings_layout.addLayout(layout3)

        layout4 = QHBoxLayout()
        # 示例设置项4：推送通知
        notifications_label = QLabel("推送通知")
        notifications_checkbox = QCheckBox(self)
        layout4.addWidget(notifications_label)
        layout4.addWidget(notifications_checkbox)
        settings_layout.addLayout(layout4)

        # 示例设置项5：字体大小
        font_size_label = QLabel("字体大小")
        font_size_slider = QSlider(Qt.Horizontal)
        settings_layout.addWidget(font_size_label)
        settings_layout.addWidget(font_size_slider)

        # 示例设置项6：语言选择
        language_label = QLabel("语言选择")
        language_combobox = QComboBox()
        language_combobox.addItems(["中文", "English"])
        settings_layout.addWidget(language_label)
        settings_layout.addWidget(language_combobox)

        layout5 = QHBoxLayout()
        # 示例设置项7：自动更新
        auto_update_label = QLabel("自动更新")
        auto_update_checkbox = QCheckBox(self)
        layout5.addWidget(auto_update_label)
        layout5.addWidget(auto_update_checkbox)
        settings_layout.addLayout(layout5)

        layout6 = QHBoxLayout()
        # 示例设置项8：主题颜色
        theme_color_label = QLabel("主题颜色")
        theme_color_combobox = QComboBox()
        theme_color_combobox.addItems(["蓝色", "绿色", "红色"])
        layout6.addWidget(theme_color_label)
        layout6.addWidget(theme_color_combobox)
        settings_layout.addLayout(layout6)

        # 示例设置项9：存储空间清理
        clean_storage_button = QPushButton("清理存储空间")
        clean_storage_button.setStyleSheet("background-color:#f7b634")
        settings_layout.addWidget(clean_storage_button)

        # 示例设置项10：关于我们
        about_us_button = QPushButton("关于我们")
        about_us_button.setStyleSheet("background-color:#f7b634")
        settings_layout.addWidget(about_us_button)

        # 将设置项添加到整体布局
        self.main_layout.addLayout(settings_layout)

