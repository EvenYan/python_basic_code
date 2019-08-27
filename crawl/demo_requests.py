import requests

# User-Agent
header = {"User-Agent":"Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_8;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50"}

r = requests.get('https://api.github.com/user', auth=('1014934663@qq.com', '733@755go'), headers=header)

print(r.status_code)
print(r.headers['content-type'])
print(r.text)
print(r.json())


# data = {"wd": "java"}
# ret = requests.get(url="http://www.baidu.com/s?", params=data)
