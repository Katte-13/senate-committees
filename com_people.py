# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 17:03:36 2019

@author: Catalina Popescu
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

start = time.time()


page = requests.get('https://www.senat.ro/EnumComisii.aspx?Permanenta=1')
soup = BeautifulSoup(page.text, 'lxml')


linkuri_comisii = soup.find('div', {'class':"link-list-arrow d-inline-block"})
linkuri_comisii = linkuri_comisii.find_all('a')
linkuri_comisii = [x.get("href").replace("Comisie_new.aspx", "ComponentaComisii.aspx") for x in linkuri_comisii]

componenta = {}

for link in linkuri_comisii:
    comisie = requests.get(f"https://www.senat.ro/{link}")
    comisie = BeautifulSoup(comisie.text, 'lxml')
    
    nume_comisie = comisie.find('div', {'class':"col-md-12 section-title"}).text.strip()

    senatori = comisie.find('div', {'class':"p-box-grey"}).find_all('a', target="_blank")
    senatori_text = [x.text.strip() for x in senatori]
    senatori_lung = senatori_text + ['none']*abs(12-len(senatori))
    componenta[nume_comisie] = senatori_lung
    print(len(senatori_lung))
           
df = pd.DataFrame(componenta)
df.to_csv('comisii.csv', encoding='utf-8-sig')
  
end = time.time()
print(end-start)
