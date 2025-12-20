import requests
import json
import sys

url = "https://cdn.qiaoji8.com/tvbox.json"  # 优先尝试 HTTPS

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"
}

try:
    print("正在拉取配置...")
    response = requests.get(url, headers=headers, timeout=15)
    response.raise_for_status()  # 检查 HTTP 错误

    # 尝试解析 JSON
    data = response.json()
    print("✅ 配置拉取成功！")

except requests.exceptions.RequestException as e:
    print(f"❌ 网络请求失败: {e}")
    sys.exit(1)

except json.JSONDecodeError:
    print("❌ 返回内容不是有效的 JSON！响应预览：")
    print(response.text[:300])
    sys.exit(1)

# 添加直播源
new_live_url = "https://gh-proxy.com/https://raw.githubusercontent.com/xichongguo/live-stream/refs/heads/main/live/current.m3u8"

if "lives" not in data:
    data["lives"] = []

data["lives"].append({
    "group": "自定义",
    "channels": [{
        "name": "GitHub直播源",
        "urls": [new_live_url]
    }]
})

# 保存为 xichongys.json
try:
    with open("xichongys.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print("✅ 已成功保存为 xichongys.json")
except Exception as e:
    print(f"❌ 保存文件失败: {e}")
