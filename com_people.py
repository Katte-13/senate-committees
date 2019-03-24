# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 11:42:09 2019

@author: Cătălina Popescu 
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
start = time.time()


"""Comisia juridică, de numiri, disciplină, imunităţi şi validări"""
page = requests.get('https://www.senat.ro/ComponentaComisii.aspx?Zi=&ComisieID=7A441D78-C24F-4DE6-BB15-2B86F93AD14F')
page = page.text
soup = BeautifulSoup(page, 'lxml')

item = {}
juridica = ['Comisia juridică, de numiri, disciplină, imunităţi şi validări']

table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl02_ListViewMembri_ctrl0_ctl01_Td1")
td = table.find('a', target="_blank")
juridica.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl03_ListViewMembri_ctrl0_ctl01_Td1")
td = table.find('a', target="_blank")
juridica.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl04_ListViewMembri_ctrl0_ctl01_Td1")
td = table.find('a', target="_blank")
juridica.append(td.text.strip())

    
table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl0_ctl01_Td1")
td = table.find('a', target="_blank")
juridica.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl0_ctl03_Td1")
td = table.find('a', target="_blank")
juridica.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl0_ctl05_Td1")
td = table.find('a', target="_blank")
juridica.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl0_ctl07_Td1")
td = table.find('a', target="_blank")
juridica.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl1_ctl01_Td1")
td = table.find('a', target="_blank")
juridica.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl1_ctl03_Td1")
td = table.find('a', target="_blank")
juridica.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl1_ctl05_Td1")
td = table.find('a', target="_blank")
juridica.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl1_ctl07_Td1")
td = table.find('a', target="_blank")
juridica.append(td.text.strip())


"""Comisia pentru Constituționalitate"""
page = requests.get('https://senat.ro/ComponentaComisii.aspx?Zi=&ComisieID=8074EFF5-8B26-4D62-979A-CF69B4C81868')
# extract the content
page = page.text
# create a soup object
soup = BeautifulSoup(page, 'lxml')

const = ['Comisia pentru constituţionalitate']

table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl02_ListViewMembri_ctrl0_ctl01_Td1")
td = table.find('a', target="_blank")
const.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl03_ListViewMembri_ctrl0_ctl01_Td1")
td = table.find('a', target="_blank")
const.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl04_ListViewMembri_ctrl0_ctl01_Td1")
td = table.find('a', target="_blank")
const.append(td.text.strip())
    

table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl0_ctl01_Td1")
td = table.find('a', target="_blank")
const.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl0_ctl03_Td1")
td = table.find('a', target="_blank")
const.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl0_ctl05_Td1")
td = table.find('a', target="_blank")
const.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl0_ctl07_Td1")
td = table.find('a', target="_blank")
const.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl1_ctl01_Td1")
td = table.find('a', target="_blank")
const.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl1_ctl03_Td1")
td = table.find('a', target="_blank")
const.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl1_ctl05_Td1")
td = table.find('a', target="_blank")
const.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl1_ctl07_Td1")
td = table.find('a', target="_blank")
const.append(td.text.strip())


"""Comisia pentru buget, finanţe, activitate bancară şi piaţă de capital"""
page = requests.get('https://www.senat.ro/ComponentaComisii.aspx?Zi=&ComisieID=25E13BB6-CBFC-4F67-9F6B-467E3EEC365E')
# extract the content
page = page.text
# create a soup object
soup = BeautifulSoup(page, 'lxml')

buget = ['Comisia pentru buget, finanţe, activitate bancară şi piaţă de capital']

table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl02_ListViewMembri_ctrl0_ctl01_Td1")
td = table.find('a', target="_blank")
buget.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl03_ListViewMembri_ctrl0_ctl01_Td1")
td = table.find('a', target="_blank")
buget.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl04_ListViewMembri_ctrl0_ctl01_Td1")
td = table.find('a', target="_blank")
buget.append(td.text.strip())
    

table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl0_ctl01_Td1")
td = table.find('a', target="_blank")
buget.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl0_ctl03_Td1")
td = table.find('a', target="_blank")
buget.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl0_ctl05_Td1")
td = table.find('a', target="_blank")
buget.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl0_ctl07_Td1")
td = table.find('a', target="_blank")
buget.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl1_ctl01_Td1")
td = table.find('a', target="_blank")
buget.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl1_ctl03_Td1")
td = table.find('a', target="_blank")
buget.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl1_ctl05_Td1")
td = table.find('a', target="_blank")
buget.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl1_ctl07_Td1")
td = table.find('a', target="_blank")
buget.append(td.text.strip())


"""Comisia pentru Politică Externă"""
page = requests.get('https://www.senat.ro/ComponentaComisii.aspx?Zi=&ComisieID=4E3C4984-ABAA-4778-B4D0-BBAFA944AC67')
# extract the content
page = page.text
# create a soup object
soup = BeautifulSoup(page, 'lxml')

pol = ['Comisia pentru politică externă']

table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl02_ListViewMembri_ctrl0_ctl01_Td1")
td = table.find('a', target="_blank")
pol.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl03_ListViewMembri_ctrl0_ctl01_Td1")
td = table.find('a', target="_blank")
pol.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl04_ListViewMembri_ctrl0_ctl01_Td1")
td = table.find('a', target="_blank")
pol.append(td.text.strip())
    

table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl0_ctl01_Td1")
td = table.find('a', target="_blank")
pol.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl0_ctl03_Td1")
td = table.find('a', target="_blank")
pol.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl0_ctl05_Td1")
td = table.find('a', target="_blank")
pol.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl0_ctl07_Td1")
td = table.find('a', target="_blank")
pol.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl1_ctl01_Td1")
td = table.find('a', target="_blank")
pol.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl1_ctl03_Td1")
td = table.find('a', target="_blank")
pol.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl1_ctl05_Td1")
td = table.find('a', target="_blank")
pol.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl1_ctl07_Td1")
td = table.find('a', target="_blank")
pol.append(td.text.strip())

"""Comisia pentru apărare, ordine publică şi siguranţă naţională"""
page = requests.get('https://www.senat.ro/ComponentaComisii.aspx?Zi=&ComisieID=F3E4672C-E333-44E0-B781-70D7F273EE1C')
# extract the content
page = page.text
# create a soup object
soup = BeautifulSoup(page, 'lxml')

aparare = ['Comisia pentru apărare, ordine publică şi siguranţă naţională']

table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl02_ListViewMembri_ctrl0_ctl01_Td1")
td = table.find('a', target="_blank")
aparare.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl03_ListViewMembri_ctrl0_ctl01_Td1")
td = table.find('a', target="_blank")
aparare.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl04_ListViewMembri_ctrl0_ctl01_Td1")
td = table.find('a', target="_blank")
aparare.append(td.text.strip())
    

table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl0_ctl01_Td1")
td = table.find('a', target="_blank")
aparare.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl0_ctl03_Td1")
td = table.find('a', target="_blank")
aparare.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl0_ctl05_Td1")
td = table.find('a', target="_blank")
aparare.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl0_ctl07_Td1")
td = table.find('a', target="_blank")
aparare.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl1_ctl01_Td1")
td = table.find('a', target="_blank")
aparare.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl1_ctl03_Td1")
td = table.find('a', target="_blank")
aparare.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl1_ctl05_Td1")
td = table.find('a', target="_blank")
aparare.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl1_ctl07_Td1")
td = table.find('a', target="_blank")
aparare.append(td.text.strip())


"""Comisia pentru afaceri europene"""
page = requests.get('https://www.senat.ro/ComponentaComisii.aspx?Zi=&ComisieID=57E2FD36-D898-4FD1-A435-832D05FACC0A')
# extract the content
page = page.text
# create a soup object
soup = BeautifulSoup(page, 'lxml')

af_eu = ['Comisia pentru afaceri europene']

table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl02_ListViewMembri_ctrl0_ctl01_Td1")
td = table.find('a', target="_blank")
af_eu.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl03_ListViewMembri_ctrl0_ctl01_Td1")
td = table.find('a', target="_blank")
af_eu.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl04_ListViewMembri_ctrl0_ctl01_Td1")
td = table.find('a', target="_blank")
af_eu.append(td.text.strip())
    

table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl0_ctl01_Td1")
td = table.find('a', target="_blank")
af_eu.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl0_ctl03_Td1")
td = table.find('a', target="_blank")
af_eu.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl0_ctl05_Td1")
td = table.find('a', target="_blank")
af_eu.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl0_ctl07_Td1")
td = table.find('a', target="_blank")
af_eu.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl1_ctl01_Td1")
td = table.find('a', target="_blank")
af_eu.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl1_ctl03_Td1")
td = table.find('a', target="_blank")
af_eu.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl1_ctl05_Td1")
td = table.find('a', target="_blank")
af_eu.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl1_ctl07_Td1")
td = table.find('a', target="_blank")
af_eu.append(td.text.strip())


"""Comisia economică, industrii şi servicii"""
page = requests.get('https://www.senat.ro/ComponentaComisii.aspx?Zi=&ComisieID=31F15C69-ED51-42A1-95CC-C74A2B745038')
# extract the content
page = page.text
# create a soup object
soup = BeautifulSoup(page, 'lxml')

econ = ['Comisia economică, industrii şi servicii']

table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl02_ListViewMembri_ctrl0_ctl01_Td1")
td = table.find('a', target="_blank")
econ.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl03_ListViewMembri_ctrl0_ctl01_Td1")
td = table.find('a', target="_blank")
econ.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl04_ListViewMembri_ctrl0_ctl01_Td1")
td = table.find('a', target="_blank")
econ.append(td.text.strip())
    

table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl0_ctl01_Td1")
td = table.find('a', target="_blank")
econ.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl0_ctl03_Td1")
td = table.find('a', target="_blank")
econ.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl0_ctl05_Td1")
td = table.find('a', target="_blank")
econ.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl0_ctl07_Td1")
td = table.find('a', target="_blank")
econ.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl1_ctl01_Td1")
td = table.find('a', target="_blank")
econ.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl1_ctl03_Td1")
td = table.find('a', target="_blank")
econ.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl1_ctl05_Td1")
td = table.find('a', target="_blank")
econ.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl1_ctl07_Td1")
td = table.find('a', target="_blank")
econ.append(td.text.strip())


"""Comisia pentru agricultură, industrie alimentară si dezvoltare rurală"""
page = requests.get('https://www.senat.ro/ComponentaComisii.aspx?Zi=&ComisieID=888E8480-1EE7-451D-A899-6F2607CC2ACF')
# extract the content
page = page.text
# create a soup object
soup = BeautifulSoup(page, 'lxml')

agric = ['Comisia pentru agricultură, industrie alimentară si dezvoltare rurală']

table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl02_ListViewMembri_ctrl0_ctl01_Td1")
td = table.find('a', target="_blank")
agric.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl03_ListViewMembri_ctrl0_ctl01_Td1")
td = table.find('a', target="_blank")
agric.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl04_ListViewMembri_ctrl0_ctl01_Td1")
td = table.find('a', target="_blank")
agric.append(td.text.strip())
    

table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl0_ctl01_Td1")
td = table.find('a', target="_blank")
agric.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl0_ctl03_Td1")
td = table.find('a', target="_blank")
agric.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl0_ctl05_Td1")
td = table.find('a', target="_blank")
agric.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl0_ctl07_Td1")
td = table.find('a', target="_blank")
agric.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl1_ctl01_Td1")
td = table.find('a', target="_blank")
agric.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl1_ctl03_Td1")
td = table.find('a', target="_blank")
agric.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl1_ctl05_Td1")
td = table.find('a', target="_blank")
agric.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl1_ctl07_Td1")
td = table.find('a', target="_blank")
agric.append(td.text.strip())


"""Comisia pentru ape, păduri, pescuit și fond cinegetic"""
page = requests.get('https://www.senat.ro/ComponentaComisii.aspx?Zi=&ComisieID=360CEE7F-1F4D-453D-A9E3-D36DA6CDAEA0')
# extract the content
page = page.text
# create a soup object
soup = BeautifulSoup(page, 'lxml')

ape = ['Comisia pentru ape, păduri, pescuit și fond cinegetic']

table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl02_ListViewMembri_ctrl0_ctl01_Td1")
td = table.find('a', target="_blank")
ape.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl03_ListViewMembri_ctrl0_ctl01_Td1")
td = table.find('a', target="_blank")
ape.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl04_ListViewMembri_ctrl0_ctl01_Td1")
td = table.find('a', target="_blank")
ape.append(td.text.strip())
    

table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl0_ctl01_Td1")
td = table.find('a', target="_blank")
ape.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl0_ctl03_Td1")
td = table.find('a', target="_blank")
ape.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl0_ctl05_Td1")
td = table.find('a', target="_blank")
ape.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl0_ctl07_Td1")
td = table.find('a', target="_blank")
ape.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl1_ctl01_Td1")
td = table.find('a', target="_blank")
ape.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl1_ctl03_Td1")
td = table.find('a', target="_blank")
ape.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl1_ctl05_Td1")
td = table.find('a', target="_blank")
ape.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl1_ctl07_Td1")
td = table.find('a', target="_blank")
ape.append(td.text.strip())


"""Comisia pentru administraţie publică"""
page = requests.get('https://www.senat.ro/ComponentaComisii.aspx?Zi=&ComisieID=E23BFEAE-B405-4E9B-B2B3-2C0EA1EE3815')
# extract the content
page = page.text
# create a soup object
soup = BeautifulSoup(page, 'lxml')

admin = ['Comisia pentru administraţie publică']

table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl02_ListViewMembri_ctrl0_ctl01_Td1")
td = table.find('a', target="_blank")
admin.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl03_ListViewMembri_ctrl0_ctl01_Td1")
td = table.find('a', target="_blank")
admin.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl04_ListViewMembri_ctrl0_ctl01_Td1")
td = table.find('a', target="_blank")
admin.append(td.text.strip())
    

table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl0_ctl01_Td1")
td = table.find('a', target="_blank")
admin.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl0_ctl03_Td1")
td = table.find('a', target="_blank")
admin.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl0_ctl05_Td1")
td = table.find('a', target="_blank")
admin.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl0_ctl07_Td1")
td = table.find('a', target="_blank")
admin.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl1_ctl01_Td1")
td = table.find('a', target="_blank")
admin.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl1_ctl03_Td1")
td = table.find('a', target="_blank")
admin.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl1_ctl05_Td1")
td = table.find('a', target="_blank")
admin.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl1_ctl07_Td1")
td = table.find('a', target="_blank")
admin.append(td.text.strip())


"""Comisia pentru muncă, familie şi protecţie socială"""
page = requests.get('https://www.senat.ro/ComponentaComisii.aspx?Zi=&ComisieID=4F9E64DA-E812-4770-83E7-EB54572C084C')
# extract the content
page = page.text
# create a soup object
soup = BeautifulSoup(page, 'lxml')

munca = ['Comisia pentru muncă, familie şi protecţie socială']

table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl02_ListViewMembri_ctrl0_ctl01_Td1")
td = table.find('a', target="_blank")
munca.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl03_ListViewMembri_ctrl0_ctl01_Td1")
td = table.find('a', target="_blank")
munca.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl04_ListViewMembri_ctrl0_ctl01_Td1")
td = table.find('a', target="_blank")
munca.append(td.text.strip())
    

table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl0_ctl01_Td1")
td = table.find('a', target="_blank")
munca.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl0_ctl03_Td1")
td = table.find('a', target="_blank")
munca.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl0_ctl05_Td1")
td = table.find('a', target="_blank")
munca.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl0_ctl07_Td1")
td = table.find('a', target="_blank")
munca.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl1_ctl01_Td1")
td = table.find('a', target="_blank")
munca.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl1_ctl03_Td1")
td = table.find('a', target="_blank")
munca.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl1_ctl05_Td1")
td = table.find('a', target="_blank")
munca.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl1_ctl07_Td1")
td = table.find('a', target="_blank")
munca.append(td.text.strip())


"""Comisia pentru învăţământ, ştiinţă, tineret şi sport"""
page = requests.get('https://www.senat.ro/ComponentaComisii.aspx?Zi=&ComisieID=BA6A4F49-A7C8-49A0-BE0D-83CC79AA1B71')
# extract the content
page = page.text
# create a soup object
soup = BeautifulSoup(page, 'lxml')

educ = ['Comisia pentru învăţământ, ştiinţă, tineret şi sport']

table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl02_ListViewMembri_ctrl0_ctl01_Td1")
td = table.find('a', target="_blank")
educ.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl03_ListViewMembri_ctrl0_ctl01_Td1")
td = table.find('a', target="_blank")
educ.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl04_ListViewMembri_ctrl0_ctl01_Td1")
td = table.find('a', target="_blank")
educ.append(td.text.strip())
    

table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl0_ctl01_Td1")
td = table.find('a', target="_blank")
educ.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl0_ctl03_Td1")
td = table.find('a', target="_blank")
educ.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl0_ctl05_Td1")
td = table.find('a', target="_blank")
educ.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl0_ctl07_Td1")
td = table.find('a', target="_blank")
educ.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl1_ctl01_Td1")
td = table.find('a', target="_blank")
educ.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl1_ctl03_Td1")
td = table.find('a', target="_blank")
educ.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl1_ctl05_Td1")
td = table.find('a', target="_blank")
educ.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl1_ctl07_Td1")
td = table.find('a', target="_blank")
educ.append(td.text.strip())


"""Comisia pentru sănătate publică"""
page = requests.get('https://www.senat.ro/ComponentaComisii.aspx?Zi=&ComisieID=D0CE6E28-28E6-4D52-A1C4-A5995F4F02C9')
# extract the content
page = page.text
# create a soup object
soup = BeautifulSoup(page, 'lxml')

sanatate = ['Comisia pentru sănătate publică']

table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl02_ListViewMembri_ctrl0_ctl01_Td1")
td = table.find('a', target="_blank")
sanatate.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl03_ListViewMembri_ctrl0_ctl01_Td1")
td = table.find('a', target="_blank")
sanatate.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl04_ListViewMembri_ctrl0_ctl01_Td1")
td = table.find('a', target="_blank")
sanatate.append(td.text.strip())
    

table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl0_ctl01_Td1")
td = table.find('a', target="_blank")
sanatate.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl0_ctl03_Td1")
td = table.find('a', target="_blank")
sanatate.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl0_ctl05_Td1")
td = table.find('a', target="_blank")
sanatate.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl0_ctl07_Td1")
td = table.find('a', target="_blank")
sanatate.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl1_ctl01_Td1")
td = table.find('a', target="_blank")
sanatate.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl1_ctl03_Td1")
td = table.find('a', target="_blank")
sanatate.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl1_ctl05_Td1")
td = table.find('a', target="_blank")
sanatate.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl1_ctl07_Td1")
td = table.find('a', target="_blank")
sanatate.append(td.text.strip())


"""Comisia pentru cultură şi media"""
page = requests.get('https://www.senat.ro/ComponentaComisii.aspx?Zi=&ComisieID=47a390a9-689e-46fd-85a3-5dd1c5ad8f0a')
# extract the content
page = page.text
# create a soup object
soup = BeautifulSoup(page, 'lxml')

cult = ['Comisia pentru cultură şi media']

table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl02_ListViewMembri_ctrl0_ctl01_Td1")
td = table.find('a', target="_blank")
cult.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl03_ListViewMembri_ctrl0_ctl01_Td1")
td = table.find('a', target="_blank")
cult.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl04_ListViewMembri_ctrl0_ctl01_Td1")
td = table.find('a', target="_blank")
cult.append(td.text.strip())
    

table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl0_ctl01_Td1")
td = table.find('a', target="_blank")
cult.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl0_ctl03_Td1")
td = table.find('a', target="_blank")
cult.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl0_ctl05_Td1")
td = table.find('a', target="_blank")
cult.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl0_ctl07_Td1")
td = table.find('a', target="_blank")
cult.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl1_ctl01_Td1")
td = table.find('a', target="_blank")
cult.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl1_ctl03_Td1")
td = table.find('a', target="_blank")
cult.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl1_ctl05_Td1")
td = table.find('a', target="_blank")
cult.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl1_ctl07_Td1")
td = table.find('a', target="_blank")
cult.append(td.text.strip())


"""Comisia pentru transporturi şi infrastructură"""
page = requests.get('https://www.senat.ro/ComponentaComisii.aspx?Zi=&ComisieID=13BC9365-960B-40CA-8186-7B8FED65F20B')
# extract the content
page = page.text
# create a soup object
soup = BeautifulSoup(page, 'lxml')

trans = ['Comisia pentru transporturi şi infrastructură']

table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl02_ListViewMembri_ctrl0_ctl01_Td1")
td = table.find('a', target="_blank")
trans.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl03_ListViewMembri_ctrl0_ctl01_Td1")
td = table.find('a', target="_blank")
trans.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl04_ListViewMembri_ctrl0_ctl01_Td1")
td = table.find('a', target="_blank")
trans.append(td.text.strip())
    

table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl0_ctl01_Td1")
td = table.find('a', target="_blank")
trans.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl0_ctl03_Td1")
td = table.find('a', target="_blank")
trans.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl0_ctl05_Td1")
td = table.find('a', target="_blank")
trans.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl0_ctl07_Td1")
td = table.find('a', target="_blank")
trans.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl1_ctl01_Td1")
td = table.find('a', target="_blank")
trans.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl1_ctl03_Td1")
td = table.find('a', target="_blank")
trans.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl1_ctl05_Td1")
td = table.find('a', target="_blank")
trans.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl1_ctl07_Td1")
td = table.find('a', target="_blank")
trans.append(td.text.strip())


"""Comisia pentru energie, infrastructură energetică și resurse minerale"""
page = requests.get('https://www.senat.ro/ComponentaComisii.aspx?Zi=&ComisieID=954E4F88-2BAD-4A31-AE22-9719E636BAD5')
# extract the content
page = page.text
# create a soup object
soup = BeautifulSoup(page, 'lxml')

energ = ['Comisia pentru energie, infrastructură energetică și resurse minerale']

table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl02_ListViewMembri_ctrl0_ctl01_Td1")
td = table.find('a', target="_blank")
energ.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl03_ListViewMembri_ctrl0_ctl01_Td1")
td = table.find('a', target="_blank")
energ.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl04_ListViewMembri_ctrl0_ctl01_Td1")
td = table.find('a', target="_blank")
energ.append(td.text.strip())
    

table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl0_ctl01_Td1")
td = table.find('a', target="_blank")
energ.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl0_ctl03_Td1")
td = table.find('a', target="_blank")
energ.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl0_ctl05_Td1")
td = table.find('a', target="_blank")
energ.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl0_ctl07_Td1")
td = table.find('a', target="_blank")
energ.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl1_ctl01_Td1")
td = table.find('a', target="_blank")
energ.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl1_ctl03_Td1")
td = table.find('a', target="_blank")
energ.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl1_ctl05_Td1")
td = table.find('a', target="_blank")
energ.append(td.text.strip())

energ.append('None')


"""Comisia pentru comunicații și tehnologia informației"""
page = requests.get('https://www.senat.ro/ComponentaComisii.aspx?Zi=&ComisieID=4717DF8D-0243-4711-9101-F4FB10B5C410')
# extract the content
page = page.text
# create a soup object
soup = BeautifulSoup(page, 'lxml')

it = ['Comisia pentru comunicații și tehnologia informației']

table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl02_ListViewMembri_ctrl0_ctl01_Td1")
td = table.find('a', target="_blank")
it.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl03_ListViewMembri_ctrl0_ctl01_Td1")
td = table.find('a', target="_blank")
it.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl04_ListViewMembri_ctrl0_ctl01_Td1")
td = table.find('a', target="_blank")
it.append(td.text.strip())
    

table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl0_ctl01_Td1")
td = table.find('a', target="_blank")
it.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl0_ctl03_Td1")
td = table.find('a', target="_blank")
it.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl0_ctl05_Td1")
td = table.find('a', target="_blank")
it.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl0_ctl07_Td1")
td = table.find('a', target="_blank")
it.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl1_ctl01_Td1")
td = table.find('a', target="_blank")
it.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl1_ctl03_Td1")
td = table.find('a', target="_blank")
it.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl1_ctl05_Td1")
td = table.find('a', target="_blank")
it.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl1_ctl07_Td1")
td = table.find('a', target="_blank")
it.append(td.text.strip())


"""Comisia pentru drepturile omului, egalitate de șanse, culte şi minorităţi"""
page = requests.get('https://www.senat.ro/ComponentaComisii.aspx?Zi=&ComisieID=57D70A5F-F421-45B7-B355-E11AE37CA421')
# extract the content
page = page.text
# create a soup object
soup = BeautifulSoup(page, 'lxml')

culte = ['Comisia pentru drepturile omului, egalitate de șanse, culte şi minorităţi']

table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl02_ListViewMembri_ctrl0_ctl01_Td1")
td = table.find('a', target="_blank")
culte.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl03_ListViewMembri_ctrl0_ctl01_Td1")
td = table.find('a', target="_blank")
culte.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl04_ListViewMembri_ctrl0_ctl01_Td1")
td = table.find('a', target="_blank")
culte.append(td.text.strip())
    

table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl0_ctl01_Td1")
td = table.find('a', target="_blank")
culte.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl0_ctl03_Td1")
td = table.find('a', target="_blank")
culte.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl0_ctl05_Td1")
td = table.find('a', target="_blank")
culte.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl0_ctl07_Td1")
td = table.find('a', target="_blank")
culte.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl1_ctl01_Td1")
td = table.find('a', target="_blank")
culte.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl1_ctl03_Td1")
td = table.find('a', target="_blank")
culte.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl1_ctl05_Td1")
td = table.find('a', target="_blank")
culte.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl1_ctl07_Td1")
td = table.find('a', target="_blank")
culte.append(td.text.strip())


"""Comisia pentru comunitățile de români din afara țării"""
page = requests.get('https://www.senat.ro/ComponentaComisii.aspx?Zi=&ComisieID=DE080A9D-3785-409E-8A4A-48E0B87A3EB8')
# extract the content
page = page.text
# create a soup object
soup = BeautifulSoup(page, 'lxml')

diaspora = ['Comisia pentru comunitățile de români din afara țării']

table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl02_ListViewMembri_ctrl0_ctl01_Td1")
td = table.find('a', target="_blank")
diaspora.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl03_ListViewMembri_ctrl0_ctl01_Td1")
td = table.find('a', target="_blank")
diaspora.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl04_ListViewMembri_ctrl0_ctl01_Td1")
td = table.find('a', target="_blank")
diaspora.append(td.text.strip())
    

table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl0_ctl01_Td1")
td = table.find('a', target="_blank")
diaspora.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl0_ctl03_Td1")
td = table.find('a', target="_blank")
diaspora.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl0_ctl05_Td1")
td = table.find('a', target="_blank")
diaspora.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl0_ctl07_Td1")
td = table.find('a', target="_blank")
diaspora.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl1_ctl01_Td1")
td = table.find('a', target="_blank")
diaspora.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl1_ctl03_Td1")
td = table.find('a', target="_blank")
diaspora.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl1_ctl05_Td1")
td = table.find('a', target="_blank")
diaspora.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl1_ctl07_Td1")
td = table.find('a', target="_blank")
diaspora.append(td.text.strip())


"""Comisia pentru mediu"""
page = requests.get('https://www.senat.ro/ComponentaComisii.aspx?Zi=&ComisieID=53089913-1E10-4762-82AC-51EDCFA54F66')
# extract the content
page = page.text
# create a soup object
soup = BeautifulSoup(page, 'lxml')

mediu = ['Comisia pentru mediu']

table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl02_ListViewMembri_ctrl0_ctl01_Td1")
td = table.find('a', target="_blank")
mediu.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl03_ListViewMembri_ctrl0_ctl01_Td1")
td = table.find('a', target="_blank")
mediu.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl04_ListViewMembri_ctrl0_ctl01_Td1")
td = table.find('a', target="_blank")
mediu.append(td.text.strip())
    

table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl0_ctl01_Td1")
td = table.find('a', target="_blank")
mediu.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl0_ctl03_Td1")
td = table.find('a', target="_blank")
mediu.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl0_ctl05_Td1")
td = table.find('a', target="_blank")
mediu.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl0_ctl07_Td1")
td = table.find('a', target="_blank")
mediu.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl1_ctl01_Td1")
td = table.find('a', target="_blank")
mediu.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl1_ctl03_Td1")
td = table.find('a', target="_blank")
mediu.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl1_ctl05_Td1")
td = table.find('a', target="_blank")
mediu.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl1_ctl07_Td1")
td = table.find('a', target="_blank")
mediu.append(td.text.strip())


"""Comisia pentru cercetarea abuzurilor, combaterea corupției și petiții"""
page = requests.get('https://www.senat.ro/ComponentaComisii.aspx?Zi=&ComisieID=18D49556-70FC-42AB-B19F-FCF3CD107A07')
# extract the content
page = page.text
# create a soup object
soup = BeautifulSoup(page, 'lxml')

abuz = ['Comisia pentru cercetarea abuzurilor, combaterea corupției și petiții']

table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl02_ListViewMembri_ctrl0_ctl01_Td1")
td = table.find('a', target="_blank")
abuz.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl03_ListViewMembri_ctrl0_ctl01_Td1")
td = table.find('a', target="_blank")
abuz.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl04_ListViewMembri_ctrl0_ctl01_Td1")
td = table.find('a', target="_blank")
abuz.append(td.text.strip())
    

table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl0_ctl01_Td1")
td = table.find('a', target="_blank")
abuz.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl0_ctl03_Td1")
td = table.find('a', target="_blank")
abuz.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl0_ctl05_Td1")
td = table.find('a', target="_blank")
abuz.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl0_ctl07_Td1")
td = table.find('a', target="_blank")
abuz.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl1_ctl01_Td1")
td = table.find('a', target="_blank")
abuz.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl1_ctl03_Td1")
td = table.find('a', target="_blank")
abuz.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl1_ctl05_Td1")
td = table.find('a', target="_blank")
abuz.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl1_ctl07_Td1")
td = table.find('a', target="_blank")
abuz.append(td.text.strip())


"""Comisia pentru regulament"""
page = requests.get('https://www.senat.ro/ComponentaComisii.aspx?Zi=&ComisieID=540E0916-EEFF-4E01-A700-8E3ABD2C3F0F')
# extract the content
page = page.text
# create a soup object
soup = BeautifulSoup(page, 'lxml')

regul = ['Comisia pentru regulament']

table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl02_ListViewMembri_ctrl0_ctl01_Td1")
td = table.find('a', target="_blank")
regul.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl03_ListViewMembri_ctrl0_ctl01_Td1")
td = table.find('a', target="_blank")
regul.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl04_ListViewMembri_ctrl0_ctl01_Td1")
td = table.find('a', target="_blank")
regul.append(td.text.strip())
    

table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl0_ctl01_Td1")
td = table.find('a', target="_blank")
regul.append(td.text.strip())


table = soup.find('td', id="ctl00_B_Center_GridViewMembri_ctl05_ListViewMembri_ctrl0_ctl03_Td1")
td = table.find('a', target="_blank")
regul.append(td.text.strip())
empty = ['None', 'None', 'None', 'None', 'None', 'None']
regul.extend(empty)


com_jur = {juridica[0]:juridica[1:] for x in juridica}
item.update(com_jur)

com_const = {const[0]:const[1:] for x in const}
item.update(com_const)

com_buget = {buget[0]:buget[1:] for x in buget}
item.update(com_buget)

com_pol = {pol[0]:pol[1:] for x in pol}
item.update(com_pol)

com_aparare = {aparare[0]:aparare[1:] for x in aparare}
item.update(com_aparare)

com_af_eu = {af_eu[0]:af_eu[1:] for x in af_eu}
item.update(com_af_eu)

com_econ = {econ[0]:econ[1:] for x in econ}
item.update(com_econ)

com_agric = {agric[0]:agric[1:] for x in agric}
item.update(com_agric)

com_ape = {ape[0]:ape[1:] for x in ape}
item.update(com_ape)

com_munca = {munca[0]:munca[1:] for x in munca}
item.update(com_munca)

com_educ = {educ[0]:educ[1:] for x in educ}
item.update(com_educ)

com_sanatate = {sanatate[0]:sanatate[1:] for x in sanatate}
item.update(com_sanatate)

com_cult = {cult[0]:cult[1:] for x in cult}
item.update(com_cult)

com_trans = {trans[0]:trans[1:] for x in trans}
item.update(com_trans)

com_energ = {energ[0]:energ[1:] for x in energ}
item.update(com_energ)

com_it = {it[0]:it[1:] for x in it}
item.update(com_it)

com_culte = {culte[0]:culte[1:] for x in culte}
item.update(com_culte)

com_diaspora = {diaspora[0]:diaspora[1:] for x in diaspora}
item.update(com_diaspora)

com_mediu = {mediu[0]:mediu[1:] for x in mediu}
item.update(com_mediu)

com_abuz = {abuz[0]:abuz[1:] for x in abuz}
item.update(com_abuz)

com_regul = {regul[0]:regul[1:] for x in regul}
item.update(com_regul)

 
df = pd.DataFrame(item)
df.to_csv('comisii.csv', encoding='utf-8-sig')

  
end = time.time()
print(end-start)