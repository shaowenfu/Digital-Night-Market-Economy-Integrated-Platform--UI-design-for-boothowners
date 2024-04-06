import requests
def get_order_data(Token):
    # 使用函数
    token = Token
    headers = {'token': token}
    # 发送 GET 请求
    response = requests.get('http://yspt.fun:8080/Merchant/select/Order', headers=headers)
    # 检查响应状态码
    if response.status_code == 200:
        return response
    else:
        print('请求失败:', response.status_code)
    return response
