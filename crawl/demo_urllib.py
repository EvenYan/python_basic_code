from urllib.request import urlopen
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

print(BASE_DIR)

url = "http://www.baidu.com/"

response = urlopen(url)
with open(os.path.join(BASE_DIR, 'test.html'), 'wb') as f:
    # print(response.read())
    f.write(response.read())

# print(response.read().decode())
