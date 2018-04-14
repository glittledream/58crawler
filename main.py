from multiprocessing import Pool
from channel_extract import channel_list
from page_parding import get_itemlinks,get_info,sheet_line

def get_all_links_from(channel):
    for num in range(1,101):
        get_itemlinks(channel,num)


if __name__=="__main__":
    pool = Pool()
    # pool.map(get_all_links_from,channel_list.split())
    pool.map(get_info,[i['url'] for i in sheet_line.find()])
    pool.close()
    pool.join()
