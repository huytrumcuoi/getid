import requests

cookies = {
    'inpl_mobile': 'd',
    '_ga': 'GA1.2.1361258199.1642774234',
    '_gid': 'GA1.2.1432168543.1642774234',
    '_gcl_au': '1.1.1479034815.1642774234',
    '__gfp_64b': '8ZfBPhysZlplTeaimQFqbGzVqcbaeZ0Zbzm1008oUID.l7|1642774246',
    'inpl_mail_device_type': 'nonMobileDevice%7C0%7C0%7C7%7Cd1628',
    'inpl_mail_cac': '1',
    'loginAppPromo': '1',
    'CSID': 'f8c3ad3c6c909c10324b4c1ffdc60424',
    '_abd_hash': '0011',
    '__adb_aid': '7435a406-8b93-4450-9a18-59aec9773f33',
    '_abd_st': '1',
}

headers = {
    'authority': 'konto-pocztowe.interia.pl',
    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
    'content-type': 'application/json',
    'accept': 'application/json; q=1.0, text/*; q=0.8, */*; q=0.1',
    'cache-control': 'no-cache',
    'x-requested-with': 'XMLHttpRequest',
    'x-app-fcrtkn': 'rgwG3J3cGwB2Lmum0JsZUue6hPTTPadXIMbEGmWTfJE',
    'sec-ch-ua-platform': '"Windows"',
    'origin': 'https://konto-pocztowe.interia.pl',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://konto-pocztowe.interia.pl/',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
}

data = '{"user":{"name":"dsdsd","surname":"dsdtnf","birthDate":"1999-9-22","gender":"M","login":"josh","domain":"interia.pl","password":"Lamgiahuy@123","rePassword":"Lamgiahuy@123","type":0,"agreementHazard":1},"agreement":{"versionList":["41","40","90","49"],"bundleId":17},"captcha":"03AGdBq25vF_hm-kZKcBHM9f2H7AhSvbsB2KV4drulMQLWu-1cS3OZkLBN4rRZVYfI_I35X8JoJ1Io-NxYN_mKYqgi8duRYSrxvo37FhGslXIksD8dHpKL872A5C76x7MnyZ1z145BowXTxSP8KpSgcmP6hc_PoA7EN1oljhyXP3dww7yf7sdcmxmpCdGQiFgT_mJVfZz4YEcD9gRm_jpdTb5Dxu-7fUDbEv6hro88pnScihIWQPndu26vJefnWy74G_qjzNCbCXoYxQUPJvScv5bQmgARAbD8GQ5txFHkZNDjkq9TgR_uEzZmnBy1Uk8ZPT1xj1lkrD7NVyByD_0-8QExYIQAwScbkO4fZqdhtmSexcwfbs1kS6lUCwzSWL5vfIXt-RlyjFlSqtDAG7jAGM8PEzITfpws4k7BHBzveTDn0pYLu7nAIeWHL0CJnmG5Nm4if3tPPj0zNLw8IEEJ8shIXAD0UZPMUA"}'

response = requests.post('https://konto-pocztowe.interia.pl/account', headers=headers, cookies=cookies, data=data)
print(response.content)
