import requests
"""
execjs执行js编码错误的解决方法（UnicodeDecodeError: ‘gbk‘ codec can‘t decode byte 0xad in position 20: illegal ）
在导入execjs之前加上下列三行代码即可
"""
import subprocess
from functools import partial
subprocess.Popen = partial(subprocess.Popen, encoding="utf-8")

import execjs
import json

cookies = {
    'btoken': '606N0E858QMT0NEDPJJO57JRD7PMA99B',
    'Hm_lvt_42317524c1662a500d12d3784dbea0f8': '1701688413',
    'hy_data_2020_id': '18c34888da3c0f-078d05d4bc918c-26031051-2710825-18c34888da415f5',
    'hy_data_2020_js_sdk': '%7B%22distinct_id%22%3A%2218c34888da3c0f-078d05d4bc918c-26031051-2710825-18c34888da415f5%22%2C%22site_id%22%3A211%2C%22user_company%22%3A105%2C%22props%22%3A%7B%7D%2C%22device_id%22%3A%2218c34888da3c0f-078d05d4bc918c-26031051-2710825-18c34888da415f5%22%7D',
    'sajssdk_2020_cross_new_user': '1',
    'Hm_lpvt_42317524c1662a500d12d3784dbea0f8': '1701693414',
}

headers = {
    'authority': 'www.xiniudata.com',
    'accept': 'application/json',
    'accept-language': 'zh-CN,zh;q=0.9',
    'content-type': 'application/json',
    # 'cookie': 'btoken=606N0E858QMT0NEDPJJO57JRD7PMA99B; Hm_lvt_42317524c1662a500d12d3784dbea0f8=1701688413; hy_data_2020_id=18c34888da3c0f-078d05d4bc918c-26031051-2710825-18c34888da415f5; hy_data_2020_js_sdk=%7B%22distinct_id%22%3A%2218c34888da3c0f-078d05d4bc918c-26031051-2710825-18c34888da415f5%22%2C%22site_id%22%3A211%2C%22user_company%22%3A105%2C%22props%22%3A%7B%7D%2C%22device_id%22%3A%2218c34888da3c0f-078d05d4bc918c-26031051-2710825-18c34888da415f5%22%7D; sajssdk_2020_cross_new_user=1; Hm_lpvt_42317524c1662a500d12d3784dbea0f8=1701693414',
    'origin': 'https://www.xiniudata.com',
    'referer': 'https://www.xiniudata.com/industry/newest?from=data',
    'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
}

#自定义请求数据,sort不能变
l = {
    "sort": 1,
    "start": 0,
    "limit": 1
}

with open('./蜗牛数据.js', 'r', encoding='UTF-8') as file:
	result = file.read()
#获取加密参数
payload = execjs.compile(result).call('payload',l)
sig = execjs.compile(result).call('sign',payload)

json_data = {
    'payload': 'LBc3V0I6ZGB5bXsxTCQnPRBuBhgbPj1fJDpwd2c4',
    'sig': 'AB2D2E90A3EB1D3FA47D058D3C35DCD6',
    'v': 1,
}
json_data['payload'] = payload
json_data['sig'] = sig

response = requests.post(
    'https://www.xiniudata.com/api2/service/x_service/person_industry_list/list_industries_by_sort',
    cookies=cookies,
    headers=headers,
    json=json_data,
)

# print(response.text)

json_obj = json.loads(response.text)
# print(json_obj)
# print(type(json_obj))

d = json_obj["d"]
#解密返回结果
re = execjs.compile(result).call('de',d)
print(re)