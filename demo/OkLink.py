import requests
import time


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


headers = {
    'authority': 'www.oklink.com',
    'accept': 'application/json',
    'accept-language': 'zh-CN,zh;q=0.9',
    'app-type': 'web',
    # 'cookie': 'aliyungf_tc=95ab5bfc81e2065bfc99cf0f022f71bde028c22d75b35109a0161ce39f22dd09; locale=zh_CN; browserVersionLevel=v5.6ad2a8e37c01; devId=ed501d50-d802-4cb7-92cf-b27bb611cf7b; okg.currentMedia=xl; ok-ses-id=0nSYH+lMSXkFirYOhRTBnaUkuVorbfa9acflfBFRLNG9lBBq45SZjAHh6BHbW+M930qGlBkdD0sY9B7GdN440CWLHosNo4uSlbU/KnArRrTdnKP4P8hiyluoiOmNRbhw; _monitor_extras={"deviceId":"YDUQ0LhDXNv7wfZTEjEZ2b","eventId":39,"sequenceNumber":39}; amp_d77757=liKzEtcuv9e6uZVT5VXe6_...1hgsg1b7v.1hgshome4.16.0.16',
    'devid': 'ed501d50-d802-4cb7-92cf-b27bb611cf7b',
    'referer': f'https://www.oklink.com/cn/btc/tx-list/page/{page_num}',
    'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'x-apikey': 'LWIzMWUtNDU0Ny05Mjk5LWI2ZDA3Yjc2MzFhYmEyYzkwM2NjfDI4MTI4NzYzMjM0MDUyNzU=',
    'x-cdn': 'https://static.oklink.com',
    'x-locale': 'zh_CN',
    'x-site-info': '{}',
    'x-utc': '8',
    'x-zkdex-env': '0',
}

#当前时间戳
time_stamp = int(round(time.time() * 1000))
limit = 20
offset =  ((page_num -1),0)[(page_num -1) < 0 ] * limit

response = requests.get(
    f'https://www.oklink.com/api/explorer/v1/btc/transactionsNoRestrict?t={time_stamp}&offset={offset}&txType=&limit={limit}&curType=&sort=realTransferValue,desc&value=1&valueUpperLimit=2',
    cookies=cookies,
    headers=headers,
)

print(response.text)