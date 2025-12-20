import requests
import json

# 原始 JSON 地址
url = "http://cdn.qiaoji8.com/tvbox.json"

# 获取原始 JSON 内容
response = requests.get(url)
response.raise_for_status()  # 如果请求失败会抛出异常
data = response.json()

# 要添加的直播源
new_live_url = "https://gh-proxy.com/https://raw.githubusercontent.com/xichongguo/live-stream/refs/heads/main/live/current.m3u8"

# 确保 lives 字段存在（如果不存在则初始化为空列表）
if "lives" not in data:
    data["lives"] = []

# 构造新的直播频道条目
new_channel = {
    "group": "自定义",
    "channels": [
        {
            "name": "GitHub直播源",
            "urls": [new_live_url]
        }
    ]
}

# 将新条目追加到 lives 列表中
data["lives"].append(new_channel)

# 格式化输出（保留中文、缩进，尽量贴近原格式）
output_json = json.dumps(data, ensure_ascii=False, indent=2)

# 保存为 xichongys.json
with open("xichongys.json", "w", encoding="utf-8") as f:
    f.write(output_json)

print("✅ 已成功生成文件：xichongys.json")
