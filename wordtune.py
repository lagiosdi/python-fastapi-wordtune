import os
import time
import requests
from bs4 import BeautifulSoup
from copy import deepcopy
import random

##Token
token = 'wordtune'

class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'
    
class CRAWLER(object):
    def __init__(self):
        self.baseUrl = ''
        self.obj = {'search_text':'','result_text':''}
        self.postHeaders = {
            'content-type': 'application/json',
            'sec-fetch-site':'same-site',
            'origin' : 'https://www.wordtune.com',
            'referer' :'https://www.wordtune.com/',
            'userid':'deviceId-eUFiY1MTh_pT0AKb3mCsdt',
            # 'x-wordtune-origin':'https://www.wordtune.com',
            'User-Agent':
                'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36',
            'Accept':
                '*/*',
        }
        self.session = requests.session()
        self.domain = 'wordrtune'
        #self.obj = deepcopy(get_obj())
        self.iserror = False
        self.allJobs=[]
        self.proxy={
        'http': 'http://testhc:testhc@dc.us-pr.oxylabs.io:30000' ,#+ prx,
        'https': 'http://testhc:testhc@dc.us-pr.oxylabs.io:30000'#+ prx
    }

    def post_request(self, url,data):
        mycount = 0
        while True:
            try:
                res = self.session.post(url, headers=self.postHeaders,json=data,proxies=self.proxy)
                if res.status_code == 200:
                    return True, res
                time.sleep(random.randint(1,3))
            except Exception as e:
                print(e)
            print("Trying again to fetch data")
            mycount = mycount + 1
            if mycount > 3:
                break
        return False, False

    def process_logic(self,search_data):
        try:
            newurl = 'https://api.wordtune.com/rewrite-limited'
            search_texts=str(search_data).strip().split('. ')
            for search_text in search_texts:
                data = {"action":"REWRITE","text":str(search_text).strip(),"draftId":"lpDemoDraft-deviceId-jcrSCkTdlpE3arAMdc9Myz-1664273882431","start":0,"end":len(search_text),"selection":{"wholeText":str(search_text).strip(),"start":0,"end":len(search_text)}}
                isloaded, res = self.post_request(newurl,data)
                if isloaded:
                    data=res.json()
                    item={
                        'search_text':search_text,
                        'result_text':data['suggestions']
                    }
                    self.allJobs.append(item)

    
                #print(style.GREEN + str(result_data) +style.RESET)
            
        except Exception as e:
            print(e)
        return self.allJobs
       
       
        
          


if __name__ == "__main__":
    scraper = CRAWLER()
    scraper.process_logic("hello. hii")
    print(scraper.allJobs)