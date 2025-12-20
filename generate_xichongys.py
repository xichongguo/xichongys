import requests
import json

# 原始 JSON 地址
url = "http://cdn.qiaoji8.com/tvbox.json"

# 获取原始 JSON 内容
response = requests.get(url)
response.raise_for_status()  # 确保请求成功
data = response.json()

# 要添加的直播源
new_live_url = "https://gh-proxy.com/https://raw.githubusercontent.com/xichongguo/live-stream/refs/heads/main/live/current.m3u8"

# 确保 lives 存在
if "lives" not in data:
    data["lives"] = []

# 添加新的直播源（按你的结构，放在 channels 里，group 可自定义）
new_channel = {
    "group": "自定义",
    "channels": [
        {
            "name": "GitHub直播源",
            "urls": [new_live_url]
        }
    ]
}

# 将新直播源追加到 lives 列表
data["lives"].append(new_channel)

# 保持原格式输出（确保 key 顺序、缩进等尽量一致）
# 注意：Python 3.7+ dict 默认有序，若原文件有特定顺序，建议用原始 key 顺序处理（此处简化）
output_json = json.dumps(data, ensure_ascii=False, indent=2)

# 保存到文件（可选）
with open("tvbox_modified.json", "w", encoding="utf-8") as f:
    f.write(output_json)

# 或者直接打印
print(output_json)
