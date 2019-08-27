import time
import random

import requests
from lxml import etree
from flask import Flask, jsonify, render_template


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/home")
def index():
    return "Welcome"


@app.route("/get_data")
def get_data():
    car_list, sale_list = get_fund_data()
    return jsonify({"car_list": car_list, "sale_list": sale_list})


def get_fund_data():
    # 构造请求头中的UA，突破低级的的爬虫
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"} 

    fund_name_list = []
    fund_incr_list = []

    for i in range(10):
        # 每爬取网页一次随机休眠（5s内)
        time.sleep(random.randrange(5))
        # 将基金代码格式化为六位数的字符串
        str_i = "%06d" % i    
        # 构造基金的详情页
        url = "http://fund.eastmoney.com/" + str(str_i) + ".html"
        # 发送http request请求，并获取网页数据
        response = requests.get(url, headers=headers)
        try:
            # 将网页数据解码为字符串
            print("*"*100)
            # print(response.text[400:500])
            # print(response.content)
            # content = response.content.decode()
            content = response.content
        except Exception as e:
            print(e)
            continue

        # 利用lxml解析数据
        mytree = etree.HTML(content)
        # 抓取当日基金价格
        # price = mytree.xpath('//*[@id="body"]/div[12]/div/div/div[2]/div[1]/div[1]/dl[2]/dd[1]/span[1]/text()')
        # 抓取当日基金涨幅的估值
        price_increase = mytree.xpath('//*[@id="body"]/div[12]/div/div/div[2]/div[1]/div[1]/dl[1]/dd[1]/dl[3]/span[2]/text()')
        # 抓取基金名称
        fund_name = mytree.xpath('//*[@id="body"]/div[12]/div/div/div[1]/div[1]/div/text()')
        print("#"*100)
        print(fund_name)
        print(price_increase)

        # 抓取的信息有可能为空或者产生异常
        try:
            # 将抓取到的基金信息追加到fund_list列表
            fund_name_list.append(fund_name[0])
            fund_incr_list.append(float(price_increase[0][:-1]))
            print(fund_name[0] + ":" + price_increase[0])
        except Exception as e:
            print(e)
            continue
    return fund_name_list, fund_incr_list


@app.route("/get_car_data")
def get_car_data():
    """从指定网页的汽车销量排行榜爬取top销量的汽车信息
    """
    response = requests.get('https://db.auto.sohu.com/carsales/', headers=headers)
    mytree = etree.HTML(response.content)
    # print(response.content.decode("utf-8"))
    car_list = mytree.xpath("//*[@id='ucon_11']/ol[1]/li/a/text()")
    sale_list = mytree.xpath("//*[@id='ucon_11']/ol[1]/li/span/text()")
    print(car_list)
    print(sale_list)
    return jsonify({"car_list": car_list, "sale_list": sale_list})


if __name__ == "__main__":
    app.run(port="5000")
