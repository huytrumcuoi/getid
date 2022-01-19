import requests
import random
from bs4 import BeautifulSoup as bs
import traceback


proxies = []

file = open("proxy.txt").readlines()
for f in file:
  line_proxy = f.strip("\n")
  proxies.append(line_proxy)


url = "http://httpbin.org/ip"


for i in range(len(proxies)):
    #printing req number
    print("Request Number : " + str(i+1))
    proxy = proxies[i]
    try:
        response = requests.get(url, proxies = {"http":proxy, "https":proxy})
        print(response.json())
    except:
        # if the proxy Ip is pre occupied
        print("Not Available")

