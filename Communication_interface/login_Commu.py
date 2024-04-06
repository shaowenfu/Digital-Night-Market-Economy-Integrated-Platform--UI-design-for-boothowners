import requests
from PyQt5.QtWidgets import QMessageBox

from utils.encode_json import parse_json_string


# from UIview_codes import MainWindow_p1
def login_request(self, username, password_hash):
    url = "http://yspt.fun:8080/Login/Merchant"
    headers = {"Accept": "application/json"}
    data = {"account": username, "passHash": password_hash}
    print("开始发送请求。。。")
    # self.switch_to_MainWindow.emit()
    try:
        response = requests.post(url, headers=headers, data=data)
        print(response)
        # 获取 Response 对象的内容
        content = response.content.decode('utf-8')
        print(content)
        # 调用函数并获取返回值
        result = parse_json_string(content)
        # 检查返回值中是否包含 "error" 键，如果包含则说明解析或数据提取出错
        if "error" in result:
            print("解析错误:", result["error"])
        else:
            # 输出解析成功后的数据
            print("Code:", result["code"])
            print("Message:", result["msg"])
            print("User ID:", result["user_id"])
            print("Username:", result["username"])
            print("Password Hash:", result["pass_hash"])
            print("Token:", result["token"])
            Token = result["token"]

        response.raise_for_status()
        print(response)
        if result["msg"] == "用户名或密码错误":
            # 登录失败，弹出提示框
            QMessageBox.warning(self, '登录失败', '账号或密码错误，请重新输入！')
            # 清空输入框
            self.account_edit.clear()
            self.password_edit.clear()
        else:
            print("登录成功！")
            # 发送打开主窗口关闭登录窗口页面的信号
            self.switch_to_MainWindow.emit(Token)

    except requests.exceptions.RequestException as e:
        print(f"发生错误{e}")
