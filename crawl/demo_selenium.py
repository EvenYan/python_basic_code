from selenium import webdriver
import time

# driver = webdriver.Chrome('/home/even/Documents/Python_Basic/chapter05/chromedriver')  # Optional argument, if not specified will search path.
option = webdriver.ChromeOptions()
# option.add_argument('headless')

# chrome浏览器
driver = webdriver.Chrome('chromedriver.exe', chrome_options=option)
# driver = webdriver.Chrome('./chromedriver', chrome_options=option)

# Firefox浏览器,驱动为geckodriver,在/root/Downloads目录中
# driver = webdriver.Firefox(executable_path="/root/Downloads/geckodriver")


# 百度搜索python
# driver.get('http://www.baidu.com')
# # Let the user actually see something!
# time.sleep(5)
# search_box = driver.find_element_by_id('kw')
# search_box.send_keys('python')
# search_box.submit()
# time.sleep(3)
# ret = driver.find_element_by_id("container")
# print(ret.text)
# time.sleep(3)
# driver.quit()

# ret1 = driver.find_element_by_id("3")
# print(ret1.text)


# driver.get("https://weibo.com/login.php")
# time.sleep(3)
# username = driver.find_element_by_id("loginname")
# username.send_keys("100")
# password = driver.find_element_by_class_name("W_input")
# password.send_keys("111")


# 登录微博
driver.get("https://passport.weibo.cn/signin/login")
time.sleep(5)
driver.find_element_by_xpath('//*[@id="loginName"]').send_keys('18126740721')
driver.find_element_by_xpath('//*[@id="loginPassword"]').send_keys('1qaz@WSX')
# username.send_keys('18126740721')
time.sleep(3)
# passwd.send_keys('1qaz@WSX')

driver.find_element_by_xpath('//*[@id="loginAction"]').click()

# //*[@id="app"]/div[1]/div[1]/div[1]/div[1]
time.sleep(5)
driver.find_element_by_xpath('//*[@id="embed-captcha"]/div/div[2]/div[1]/div[3]/span[1]').click()
time.sleep(5)

driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div[1]/div[1]').click()
time.sleep(5)
ret = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div[2]/div[2]/div/h3/span')
print(ret.text)

# time.sleep(3)


# Let the user actually see something!
# time.sleep(5)
# driver.quit()

# option = webdriver.ChromeOptions()
# option.add_argument('headless')
# driver = webdriver.Chrome(chrome_options=option)
# # driver = webdriver.Chrome()
# # driver = webdriver.PhantomJS()
# driver.get('https://www.baidu.com/')
# print('打开浏览器')
# print(driver.title)
# driver.find_element_by_id('kw').send_keys('测试')
# print('关闭')
# driver.quit()
# print('测试完成')
