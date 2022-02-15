import requests, re, time

link = input(' -Nhap link bai viet : ')
while True:
  cookies = {
      '_ga': 'GA1.2.1275925754.1644917587',
      '_gid': 'GA1.2.794375241.1644917587',
      'XSRF-TOKEN': 'eyJpdiI6IjlpN0lqVFFSZmhlTkdCbDlnYllRRkE9PSIsInZhbHVlIjoiRnZ5am91V0szR2NLVnlyc2hhQWt0cng3WDBLL1k1OGV1LzMvODdlbnZaUW1CbDZaOHlPYzBGdE9TUFVlZW1BUGszTXpoelMwK0xya0RTOGQxb2VpZkhHMktSUkpGcVQwUzdzOE4zVS9OTVNTWUhhN3lHeEs4UUM1dmdlS094UVEiLCJtYWMiOiJjNjJlMTNiOWY2NjRhNmZjYzY5YjNiZmI4NTc4ZTY5NmMxNWU4MGE2NTgyN2JmYzQ2ZDQ0YWRiYzM5M2ExMzlhIiwidGFnIjoiIn0%3D',
      'rpwliker_session': 'eyJpdiI6IlBhOWVCOFdBeWhhbkM5ZzZCbnBPc2c9PSIsInZhbHVlIjoiNXJSeWdJSE1OS1Ivb1pPZWxSd1JSWnZBRk9ScXd3ZFYyYm9uSG1weDBOb1dkUjFDWldLSzF3UGhJMVVOWE9xcVJMeUhEa3hraW1IWjdVTnJ4U1NyWktBbkUvczNJamgvemRVRUhnNExjai9HZEhHa3V5VjNNK1BxVnFBelBIYW0iLCJtYWMiOiIwMzZmNjc1NmNmN2FmZjFhZTIyMDMxY2ZmMDBjZTlkMzU3ZjliZGM4MGM3M2Q0OTNmMzMxMmQzNTZjMDM0YWUwIiwidGFnIjoiIn0%3D',
  }

  headers = {
      'authority': 'rpwliker.com',
      'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
      'content-type': 'application/x-www-form-urlencoded',
      'x-csrf-token': 'JeqNOIf0k1nwlnByeLkcpbwNfQj4qFz55pWK7amz',
      'sec-ch-ua-mobile': '?0',
      'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36',
      'sec-ch-ua-platform': '"Windows"',
      'accept': '*/*',
      'origin': 'https://rpwliker.com',
      'sec-fetch-site': 'same-origin',
      'sec-fetch-mode': 'cors',
      'sec-fetch-dest': 'empty',
      'referer': 'https://rpwliker.com/facebook/posts',
      'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
  }
# https://m.facebook.com/story.php?story_fbid=1383848268710463&id=100012559095862
  data = {
    'is_from_local':'0',
    'is_from_old_account':'0',
    'reaction_type[]':'like',
    'reaction_type[]':'love',
    'post_link':(link),
    'quantity':'100',
  }

  response = requests.post('https://rpwliker.com/facebook/autoreaction', headers=headers, cookies=cookies, data=data)
  print (response.text)
  t = time.sleep(1203)
