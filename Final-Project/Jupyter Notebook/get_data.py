from bs4 import BeautifulSoup
import requests
from time import sleep
from random import randint
import pandas as pd
import os
import json
import tqdm

urls = pd.read_csv('courseraUrls.csv',delimiter = ';')
url_list = list(urls['link-href'])

for ix,url in enumerate(tqdm.tqdm(url_list[1264:]),start=1264):
    response = requests.get(url)
    #print(response.status_code)
#     pickle.dump(str(response.content,'utf-8'), open('./raw_data/{}.pkl'.format(str(ix)), 'w'))
    with open('./raw_data_txt/{}.txt'.format(str(ix)), 'wb') as f:
        f.write(response.content)
    wait_time=randint(1,3)
    sleep(wait_time)
