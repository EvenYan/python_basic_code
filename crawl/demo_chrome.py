import os
import subprocess
from selenium import webdriver

# 定位到当前文件的父目录
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 用命令打开Chrome浏览器
# 先将程序的执行目录切换到Chrome的安装目录
os.chdir("C:\\Program Files (x86)\\Google\\Chrome\\Application")
# 用os.system执行命令会阻塞程序，导致后续代码无法执行，故使用Popen代替
# os.system('chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\selenum\AutomationProfile"')
# 利用命令行打开Chrome浏览器
subprocess.Popen('chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\selenum\AutomationProfile"', stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# 将程序空间切换到当前文件的父目录
os.chdir(BASE_DIR)


# 利用Selenium接管Chrome
option = webdriver.ChromeOptions()
# 这里配置的IP和端口，是前面执行命令的时候指定的
option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome(os.path.join(BASE_DIR, 'chromedriver.exe'), chrome_options=option)
print("..."*20)

driver.get("http://www.baidu.com")
