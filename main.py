# -*- encoding:utf-8 -*-
# --------------------------------------------------------------------
# Communication_interface 存放通信接口类，用于向后端发送请求和查询信息
# Function_codes文件夹里存放每个界面具体逻辑的实现，包括加载样式表，与后端交互操作
# imgs文件夹存放页面图片
# qss_file文件夹存放每个页面的样式表
# UIview_codes存放页面的设计
# utils 存放工具类

# 运行入口
import sys
import pygame
from PyQt5.QtWidgets import QApplication
from utils.Controller import Controller


def main():
    app = QApplication(sys.argv)
    controller = Controller() # 控制器实例
    controller.show_login() # 默认展示的是 hello 页面
    pygame.init()
    info= pygame.display.Info()
    pygame.quit()
    print(f"Screen Size:{info.current_w}*{info.current_h}")
    # 应用样式表
    app.setStyleSheet(controller.style)

    sys.exit(app.exec_())
if __name__ == "__main__":
    main()
