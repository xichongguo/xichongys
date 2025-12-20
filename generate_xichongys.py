import requests
import json
import sys
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"
}

urls_to_try = [
    "http://cdn.qiaoji8.com/tvbox.json",
    "https://cdn.qiaoji8.com/tvbox.json"
]

data = None
for url in urls_to_try:
    try:
        print(f"尝试拉取: {url}")
        if url.startswith("https"):
            resp = requests.get(url, headers=headers, timeout=10, verify=False)
        else:
            resp = requests.get(url, headers=headers, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        print("✅ 拉取成功！")
        break
    except Exception as e:
        print(f"❌ 失败: {e}")
        continue

if data is None:
    print("所有链接均无法拉取配置，请检查网络或源是否失效。")
    sys.exit(1)

# 添加直播源
new_live_url = "https://gh-proxy.com/https://raw.githubusercontent.com/xichongguo/live-stream/refs/heads/main/live/current.m3u8"
if "lives" not in data:
    data["lives"] = []
data["lives"].append({
    "group": "自定义",
    "channels": [{"name": "GitHub直播源", "urls": [new_live_url]}]
})

with open("xichongys.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("✅ 已生成 xichongys.json")
