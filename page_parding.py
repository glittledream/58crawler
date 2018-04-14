from bs4 import BeautifulSoup
import requests
import time
import pymongo
import random
host = "localhost"
port = 27017
client = pymongo.MongoClient("localhost",27017)
test_url = client["test_url"]
sheet_line = test_url["sheet_line"]
tongchenguser = sheet_line["tongchenguser"]
"""#jingzhun > tbody > tr:nth-child(2) > td.t.t_b > a"""
def get_itemlinks(channel,pages,personal=0):
    itemviews = "{}{}/pn{}/".format(channel,str(personal),str(pages))
    data = requests.get(itemviews)
    time.sleep(2)
    soup = BeautifulSoup(data.text,"lxml")
    if soup.find("td","t"):
        for link in soup.select("td.t a.t"):
            item_link = link.get("href").split("?")[0]
            sheet_line.insert_one({"url":item_link})
            print(item_link)
    else:
        pass


proxy_list=[

]

def get_info(url):
    proxy=random.choice(proxy_list)
    proxies={"http":proxy}
    wb_data = requests.get(url,proxies=proxies,time=6)
    time.sleep(2)
    soup = BeautifulSoup(wb_data.text,"lxml")
    no_longer_exist = '404' in soup.find('script', type="text/javascript")
    if no_longer_exist:
      pass
    # else:
    elif soup.find("div",attrs={"class":"intro_top"}):
        title = soup.select("h1.info_titile")[0].text
        price = soup.select(" div.price_li > span > i")[0].text
        date = soup.select("span.look_time")[0].text
        area = soup.select(" div.palce_li > span > i")[0].text
        tongchenguser.insert_one({"title":title,"price":price,"date":date,"area":area})
        print({"title":title,"price":price,"date":date,"area":area})
    else:
        print("抓取失败")

get_info("http://zhuanzhuan.58.com/detail/757220292444733444z.shtml")
# sum=0
# for k in sheet_line.remove({"url":"http://jump.zhineng.58.com/jump"}):
#     print(k)




"""
http://zhuanzhuan.58.com/detail/972370084660133895z.shtml
http://zhuanzhuan.58.com/detail/972796861597777932z.shtml
http://zhuanzhuan.58.com/detail/973440544315752456z.shtml
http://zhuanzhuan.58.com/detail/973427564249760268z.shtml
http://zhuanzhuan.58.com/detail/972355987200049158z.shtml
http://zhuanzhuan.58.com/detail/972354126892236808z.shtml
http://zhuanzhuan.58.com/detail/971729732955766790z.shtml
http://zhuanzhuan.58.com/detail/971367677641605132z.shtml
http://zhuanzhuan.58.com/detail/970862268645261320z.shtml
http://zhuanzhuan.58.com/detail/970860137126985740z.shtml
http://zhuanzhuan.58.com/detail/973118898381340679z.shtml
http://zhuanzhuan.58.com/detail/970481532295135238z.shtml
http://zhuanzhuan.58.com/detail/969602394344275976z.shtml
http://zhuanzhuan.58.com/detail/973631225165004806z.shtml
http://zhuanzhuan.58.com/detail/969204286170365961z.shtml
http://zhuanzhuan.58.com/detail/906098614290710536z.shtml
http://zhuanzhuan.58.com/detail/963324815688253449z.shtml
http://zhuanzhuan.58.com/detail/908630587217575947z.shtml
http://zhuanzhuan.58.com/detail/930634913507049480z.shtml
http://zhuanzhuan.58.com/detail/941658633274425864z.shtml
http://zhuanzhuan.58.com/detail/943008890543882246z.shtml
http://zhuanzhuan.58.com/detail/952050177743306758z.shtml
http://zhuanzhuan.58.com/detail/945844130395570182z.shtml
http://zhuanzhuan.58.com/detail/915062264096276491z.shtml
http://zhuanzhuan.58.com/detail/932447097066766343z.shtml
"""