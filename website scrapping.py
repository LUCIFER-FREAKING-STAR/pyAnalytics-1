import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from urllib.request import urlopen
from bs4 import BeautifulSoup
url = "http://www.hubertiming.com/results/2017GPTR10K"
html=urlopen(url)
soup = BeautifulSoup(html,'lxml')
type(soup)
title = soup.title
print(title)
text=soup.get_text()
print(text)
soup.find_all('a')
soup.find_all('table')
soup.find_all('tr')
soup.find_all('th')
soup.find_all('td')
all_links=soup.find_all('a')
print(all_links)
for link in all_links:
    print(link.get("href"))
rows = soup.find_all('tr')
print(rows[:10])
for row in rows:
    row_td = row.find_all('td')
print(row_td)
type(row_td)