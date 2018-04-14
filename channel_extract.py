from bs4 import BeautifulSoup
import requests

start_url = "http://wh.58.com/sale.shtml"
url = "http://wh.58.com/"

def get_channeel_urls(url):
    wb_data = requests.get(start_url)
    soup = BeautifulSoup(wb_data.text,"lxml")
    links = soup.select("#ymenu-side > ul > li > ul > li > b > a")
    for link in links:
        page_url = url.split("/sale.shtml")[0]+link.get("href")
        print(page_url)
get_channeel_urls(start_url)


channel_list = """
http://wh.58.com/shouji/
http://wh.58.com/tongxunyw/
http://wh.58.com/danche/
http://wh.58.com/diandongche/
http://wh.58.com/fzixingche/
http://wh.58.com/sanlunche/
http://wh.58.com/peijianzhuangbei/
http://wh.58.com/diannao/
http://wh.58.com/bijiben/
http://wh.58.com/pbdn/
http://wh.58.com/diannaopeijian/
http://wh.58.com/zhoubianshebei/
http://wh.58.com/shuma/
http://wh.58.com/shumaxiangji/
http://wh.58.com/mpsanmpsi/
http://wh.58.com/youxiji/
http://wh.58.com/ershoukongtiao/
http://wh.58.com/dianshiji/
http://wh.58.com/xiyiji/
http://wh.58.com/bingxiang/
http://wh.58.com/jiadian/
http://wh.58.com/binggui/
http://wh.58.com/chuang/
http://wh.58.com/ershoujiaju/
http://wh.58.com/yingyou/
http://wh.58.com/yingeryongpin/
http://wh.58.com/muyingweiyang/
http://wh.58.com/muyingtongchuang/
http://wh.58.com/yunfuyongpin/
http://wh.58.com/fushi/
http://wh.58.com/nanzhuang/
http://wh.58.com/fsxiemao/
http://wh.58.com/xiangbao/
http://wh.58.com/meirong/
http://wh.58.com/yishu/
http://wh.58.com/shufahuihua/
http://wh.58.com/zhubaoshipin/
http://wh.58.com/yuqi/
http://wh.58.com/tushu/
http://wh.58.com/tushubook/
http://wh.58.com/wenti/
http://wh.58.com/yundongfushi/
http://wh.58.com/jianshenqixie/
http://wh.58.com/huju/
http://wh.58.com/qiulei/
http://wh.58.com/yueqi/
http://wh.58.com/bangongshebei/
http://wh.58.com/diannaohaocai/
http://wh.58.com/bangongjiaju/
http://wh.58.com/ershoushebei/
http://wh.58.com/chengren/
http://wh.58.com/nvyongpin/
http://wh.58.com/qinglvqingqu/
http://wh.58.com/qingquneiyi/
http://wh.58.com/chengren/
http://wh.58.com/xiaoyuan/
http://wh.58.com/ershouqiugou/
http://wh.58.com/tiaozao/
http://wh.58.com/tiaozao/
http://wh.58.com/tiaozao/


"""
