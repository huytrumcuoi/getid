import requests

cookies = {
    '__cf_bm': 'j9BXs4kVLMF3EF2Z_P5CLMxLm5Xziwcu4SH_bYywzno-1641571508-0-AQWorOxz0QMRZY6E+dKA9NxTGSxVM6uQ+HxSrJeySHYMIFoRdXdt+HTmQwOs90CcCH09S7ric47L5RaQ1Nq3apkjXN6+HWVNBnxy+xdsjC9RCAgrzhi2B+1mC5PFcpwLRQ==',
    'XSRF-TOKEN': 'eyJpdiI6ImxuK1RkbHRlK0huM2lXRzRjS2JKOXc9PSIsInZhbHVlIjoiWVBJWGVCaVpscUpUTEM0ZEE5SzNXWlpqNVZKK1d6YkNtWTNHV3VDeEw5UTNLTlJTU2NFekdSU3hlZVBXMmJFSCIsIm1hYyI6IjY3ODM4YzI5ZjU4MTI2ZWY3ZWE1YmEzNjNhOGZmNGU2NjNkNjg5NDVmNmY0ZThkNjhjZWNhZjQ3MWNiOTc1ZWMifQ%3D%3D',
    'laravel_session': 'eyJpdiI6ImVGQS9pSVBJY25vS1pkYVR6Z29EZHc9PSIsInZhbHVlIjoicHlUZksySEszUlk5Uy95MHlmQTBzZ2JsUHJIdFljd1NOaWdJa3ZhQjhIV3hsKzBHRUcvaUdZY0ZyNmJFWFNoaCIsIm1hYyI6IjBiNjBhY2U4NDhkMjFlZDhmYzgwNDY3NDBmN2EzNjViOGI1ZWRjOWMzY2JkMGZmNDNiNGQ3NzM2ODY2MWMxYjkifQ%3D%3D',
}

headers = {
    'authority': 'likevietsub.com',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'upgrade-insecure-requests': '1',
    'origin': 'https://likevietsub.com',
    'content-type': 'application/x-www-form-urlencoded',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': 'https://likevietsub.com/dang-nhap',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
}

data = 'username=lamgiahuy123&site_id=35&password=huyhuy229'

response = requests.post('https://likevietsub.com/login', headers=headers, cookies=cookies, data=data)
print(response.content)
