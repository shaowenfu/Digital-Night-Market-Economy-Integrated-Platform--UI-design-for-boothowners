from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel
from PyQt5.QtCore import QFile, QTextStream, QTimer, Qt
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt

class NoticeWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # 设置通知栏大小
        self.setFixedSize(924, 80)

        # 创建水平布局
        notice_layout = QHBoxLayout()

        # 创建显示图片的Label
        label_pic = QLabel()
        pixmap = QPixmap("imgs/notice.png")
        label_pic.setPixmap(pixmap)
        label_pic.setFixedSize(40, 40)
        label_pic.setScaledContents(True)  # 让图片自适应label大小

        # 将图片Label添加到水平布局
        notice_layout.addWidget(label_pic)

        # 设置滚屏播放
        self.labelpro = "请各位商家遵守夜市的规章制度，正确经营，保障夜市良好面貌!!!!!!!"
        self.nPos = 0
        self.label = QLabel(self.labelpro)
        self.label.setAlignment(Qt.AlignTop)
        self.label.setWordWrap(True)
        font = QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color:#e2dbe3; color:black;")
        self.label.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)

        notice_layout.addWidget(self.label)

        # 将水平布局添加到widget_notice中
        self.setLayout(notice_layout)
