import requests

cookies = {
    '_ga': 'GA1.2.435690909.1627458049',
    '_gid': 'GA1.2.785264039.1641650072',
}

headers = {
    'authority': 'autofb.pro',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
    'accept': 'application/json, text/plain, */*',
    'content-type': 'application/json',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
    'origin': 'https://autofb.pro',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://autofb.pro/',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
}

data = '{"username":"lamgiahuy123","password":"lamgiahuy"}'

response = requests.post('https://autofb.pro/api/auth', headers=headers, cookies=cookies, data=data)
print(response.content)
