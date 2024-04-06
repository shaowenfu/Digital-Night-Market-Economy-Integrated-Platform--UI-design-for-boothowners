# 文化社区
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QStackedLayout, QLabel, QHBoxLayout, \
    QScrollArea

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel

class Window4(QWidget):
    def __init__(self):
        super().__init__()
        # 整体布局
        main_layout = QVBoxLayout(self)
        main_layout.setSpacing(0)

        # 标题栏
        title_widget = QWidget()
        title_widget.setStyleSheet("background-color: #a2d934")
        title_layout = QVBoxLayout(title_widget)
        title_label = QLabel("文化社区")
        title_label.setStyleSheet("background-color: #a2d934; color: black; font-weight: bold;")
        title_label.setAlignment(Qt.AlignCenter)
        title_layout.addWidget(title_label)
        main_layout.addWidget(title_widget)

        # 信息栏
        info_layout = QHBoxLayout()

        # 顾客评论区
        feedback_widget = QWidget()
        feedback_widget.setStyleSheet("background-color: #cccccc")
        feedback_layout = QVBoxLayout(feedback_widget)

        feedback_title = QLabel("顾客评论")
        feedback_title.setStyleSheet("background-color:#fdeb3b; color: black; font-weight: bold;")
        feedback_layout.addWidget(feedback_title)

        feedback_scroll_area = QScrollArea()
        self.feedback_scroll_content = QWidget()
        feedback_scroll_layout = QVBoxLayout(self.feedback_scroll_content)

        # 示例评论框
        for i in range(5):
            feedback_box = self.create_feedback_box(f"顾客{i + 1}", f"好吃，爱吃{i + 1}")
            feedback_scroll_layout.addWidget(feedback_box)

        feedback_scroll_area.setWidget(self.feedback_scroll_content)
        feedback_layout.addWidget(feedback_scroll_area)

        feedback_button = QPushButton("文化社区")
        feedback_button.clicked.connect(self.add_feedback)
        feedback_layout.addWidget(feedback_button)

        info_layout.addWidget(feedback_widget)

        # 评分统计区
        rating_widget = QWidget()
        rating_widget.setStyleSheet("background-color: #70a7ad")
        rating_layout = QVBoxLayout(rating_widget)

        rating_title = QLabel("顾客评分")
        rating_title.setStyleSheet("background-color:#fdeb3b; color: black; font-weight: bold;")
        rating_layout.addWidget(rating_title)

        # 示例评分条
        for category in ["服务态度", "食品口味", "性价比"]:
            rating_bar = self.create_rating_bar(category)
            rating_layout.addWidget(rating_bar)

        info_layout.addWidget(rating_widget)

        main_layout.addLayout(info_layout)

    def create_feedback_box(self, customer_name, comment):
        feedback_box = QWidget()
        feedback_layout = QHBoxLayout(feedback_box)

        customer_info_label = QLabel(f"{customer_name}:")
        comment_label = QLabel(comment)

        feedback_layout.addWidget(customer_info_label)
        feedback_layout.addWidget(comment_label)

        return feedback_box

    def create_rating_bar(self, category):
        rating_bar = QWidget()
        rating_layout = QHBoxLayout(rating_bar)

        category_label = QLabel(category)
        stars_label = QLabel("⭐⭐⭐⭐⭐")

        rating_layout.addWidget(category_label)
        rating_layout.addWidget(stars_label)

        return rating_bar

    def add_feedback(self):
        # 在点击“顾客评论”按钮时调用这个函数，用于补充新增评论
        # 在这里添加获取新评论的逻辑，并更新UI
        new_feedback_box = self.create_feedback_box("新顾客", "新评论")
        self.feedback_scroll_content.layout().addWidget(new_feedback_box)
        self.update()