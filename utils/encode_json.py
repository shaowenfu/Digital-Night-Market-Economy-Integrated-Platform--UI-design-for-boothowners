# 解析接收到的json串
import json

def parse_json_string(json_string):
    try:
        # 解析 JSON 字符串
        data = json.loads(json_string)

        # 获取特定字段的值
        code = data.get("code")
        msg = data.get("msg")
        user_data = data.get("data", {})

        if msg == "用户名或密码错误":
            return {
                "code": code,
                "msg": msg,
                "user_id": user_data,
                "username": None,
                "pass_hash": None,
                "token": None
            }

        if code and msg and user_data:
            user_id = user_data.get("id")
            username = user_data.get("usename")  # 注意这里是 "usename" 而不是 "username"
            pass_hash = user_data.get("pass_hash")
            token = user_data.get("token")

            return {
                "code": code,
                "msg": msg,
                "user_id": user_id,
                "username": username,
                "pass_hash": pass_hash,
                "token": token
            }
        else:
            return {"error": "Invalid JSON format"}

    except json.JSONDecodeError as e:
        return {"error": f"JSON 解析错误: {str(e)}"}