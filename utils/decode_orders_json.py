import json
from Communication_interface.get_orders import get_order_data
def parse_orders_json(json_string):
    try:
        # 处理 UTF-8 BOM
        if json_string.startswith('\ufeff'):
            json_string = json_string[1:]

        # 解析 JSON
        data = json.loads(json_string)

        # 提取有用信息
        orders = []
        for order_data in data.get("data", []):
            order_id = order_data.get("orderId")
            status = order_data.get("status")
            openid = order_data.get("openid")
            merchant_id = order_data.get("merchantId")
            order_infos = json.loads(order_data.get("orderInfos", "[]"))

            order = {
                "orderId": order_id,
                "status": status,
                "openid": openid,
                "merchantId": merchant_id,
                "orderInfos": order_infos
            }

            orders.append(order)

        return orders

    except json.JSONDecodeError as e:
        print(f"JSON 解析错误: {e}")
        return []

# # 示例用法
# json_string = """{
#     "code": "200",
#     "msg": "请求成功",
#     "data": [
#         {"orderId": 8, "status": 0, "openid": "ogzmY5QfMWIxPs4iNRwS69gRImnI", "merchantId": 1, "orderInfos": {\"id\": 1, \"num\": 2, \"conf\": \"备注1\", \"inId\": 2, \"name\": \"豪华手抓饼\"}},
#         {"orderId": 9, "status": 0, "openid": "ogzmY5QfMWIxPs4iNRwS69gRImnI", "merchantId": 1, "orderInfos": {\"id\": 2, \"num\": 1, \"conf\": \"备注2\", \"inId\": 1, \"name\": \"基础手抓饼\"}}
#     ]
# }"""
token_value = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIxIiwiZXhwIjoxNzA2Njc5NzE2fQ.ceP521vYjsD4EJ_T5DmqS52wOKFyvH5Xi9m5EQnodGA"
result = get_order_data(token_value)
print(result)
orders = parse_orders_json(result)
print(orders)
