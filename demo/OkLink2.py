import requests
import time
import subprocess
from functools import partial
subprocess.Popen = partial(subprocess.Popen, encoding="utf-8")

import execjs

cookies = {
    'aliyungf_tc': '690c5f0112d0e7eee3993bdf001cc247eb34a9e38e8809c15e21305c10729a6e',
    'locale': 'zh_CN',
    'browserVersionLevel': 'v5.6ad2a8e37c01',
    'devId': '085fec3c-767b-4a70-a3bd-d3eb2eba6cdb',
    'okg.currentMedia': 'lg',
    '_monitor_extras': '{"deviceId":"92LMw6vsi4u1pXyAYf-mdc","eventId":7,"sequenceNumber":7}',
    'amp_d77757': 'jHpkFHBPDio2WbJDSul0xM...1hgsth36s.1hgstjl97.6.0.6',
    'ok-ses-id': 'yFifSvmLtrAsyn+xIhlS7Ufj51SjZDnlBO71p1IRH0pAZPJobR+NsxSl5aFvTa0Ar/n/MnwSqeScv6PL2uNvQ1K85Leru5LLmhBEB4rrZw7269o4MvSGFNAn6DmTBPpw',
}

#自定义页数
page_num = 2

with open('./OkLink.js', 'r', encoding='UTF-8') as file:
	result = file.read()
#获取加密参数
api_key = execjs.compile(result).call('getApiKey')

headers = {
    'authority': 'www.oklink.com',
    'accept': 'application/json',
    'accept-language': 'zh-CN,zh;q=0.9',
    'app-type': 'web',
    # 'cookie': 'aliyungf_tc=690c5f0112d0e7eee3993bdf001cc247eb34a9e38e8809c15e21305c10729a6e; locale=zh_CN; browserVersionLevel=v5.6ad2a8e37c01; devId=085fec3c-767b-4a70-a3bd-d3eb2eba6cdb; okg.currentMedia=lg; _monitor_extras={"deviceId":"92LMw6vsi4u1pXyAYf-mdc","eventId":7,"sequenceNumber":7}; amp_d77757=jHpkFHBPDio2WbJDSul0xM...1hgsth36s.1hgstjl97.6.0.6; ok-ses-id=yFifSvmLtrAsyn+xIhlS7Ufj51SjZDnlBO71p1IRH0pAZPJobR+NsxSl5aFvTa0Ar/n/MnwSqeScv6PL2uNvQ1K85Leru5LLmhBEB4rrZw7269o4MvSGFNAn6DmTBPpw',
    'devid': '085fec3c-767b-4a70-a3bd-d3eb2eba6cdb',
    'referer': f'https://www.oklink.com/cn/btc/tx-list/page/{page_num}',
    'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'x-apikey': f'{api_key}',
    'x-cdn': 'https://static.oklink.com',
    'x-locale': 'zh_CN',
    'x-site-info': '{}',
    'x-utc': '8',
    'x-zkdex-env': '0',
}

#当前时间戳
time_stamp = int(round(time.time() * 1000))
#每页条数
limit = 1
#其实查询位置
offset =  ((page_num -1),0)[(page_num -1) < 0 ] * limit


#带参数请求是拼接url，不带参数直接请求是传body
#sort=realTransferValue,desc 排序
#value=1 区间起始值
#valueUpperLimit=2 区间结束值
response = requests.get(
    f'https://www.oklink.com/api/explorer/v1/btc/transactionsNoRestrict?t={time_stamp}&offset={offset}&txType=&limit={limit}&curType=&sort=realTransferValue,desc&value=1&valueUpperLimit=2',
    cookies=cookies,
    headers=headers,
)

print(response.text)