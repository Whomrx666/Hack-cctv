
#!/usr/bin/env python3
#-*- coding: utf-8 -*-
#github.com/Whomrx666/Hack-cctv

import requests, re , colorama ,random
from requests.structures import CaseInsensitiveDict
colorama.init()

url = "http://www.insecam.org/en/jsoncountries/"

headers = CaseInsensitiveDict()
headers["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
headers["Cache-Control"] = "max-age=0"
headers["Connection"] = "keep-alive"
headers["Host"] = "www.insecam.org"
headers["Upgrade-Insecure-Requests"] = "1"
headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"


resp = requests.get(url, headers=headers)

data = resp.json()
countries = data['countries']

yellow = '\033[1;33m'
blue = '\033[1;34m'
green = '\033[1;32m'
red = '\033[1;91m'
print(f"""
{blue}
 
 __    __       ___       ______  __  ___      ______   ______ .___________.____    ____ 
|  |  |  |     /   \     /      ||  |/  /     /      | /      ||           |\   \  /   / 
|  |__|  |    /  ^  \   |  ,----'|  '  /     |  ,----'|  ,----'`---|  |----` \   \/   /  
|   __   |   /  /_\  \  |  |     |    <      |  |     |  |         |  |       \      /   
|  |  |  |  /  _____  \ |  `----.|  .  \     |  `----.|  `----.    |  |        \    /    
|__|  |__| /__/     \__\ \______||__|\__\     \______| \______|    |__|         \__/                                                                                                   
\033[1;31m                                                                </> CODED BY MR.X </> \033[1;31m\033[1;37m""")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              

       
for key, value in countries.items():
    print(f'Code : ({key}) - {value["country"]} / ({value["count"]})  ')
    print("")



try:
   

    country = input("Code(##) : ")
    res = requests.get(
        f"http://www.insecam.org/en/bycountry/{country}", headers=headers
    )
    last_page = re.findall(r'pagenavigator\("\?page=", (\d+)', res.text)[0]

    for page in range(int(last_page)):
        res = requests.get(
            f"http://www.insecam.org/en/bycountry/{country}/?page={page}",
            headers=headers
        )
        find_ip = re.findall(r"http://\d+.\d+.\d+.\d+:\d+", res.text)
    
        with open(f'{country}.txt', 'w') as f:
          for ip in find_ip:
              print("")
              print("\033[1;31m", ip)
              f.write(f'{ip}\n')
except:
    pass
finally:
    print("\033[1;37m")
    print('\033[37mSave File :'+country+'.txt')

    exit()

