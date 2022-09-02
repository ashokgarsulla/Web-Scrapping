import requests
from bs4 import BeautifulSoup as bs
import csv
import re
URL = 'https://www.geeksforgeeks.org/page/'
for page in range(1, 15):
    req = requests.get(URL + str(page) + '/')
    soup = bs(req.content, 'html.parser')

    titles = soup.find_all('div', attrs={'class', 'head'})
    titles_list = []
    
    for i in titles:
        if i.find("a") is not None:
            print(i.find("a").get('href'))
    # for link in titles.find_all('a',attrs={'href': re.compile("^https://")}):
    # # display the actual urls
    #     print(link.get('href'))  
    

    count = 1
    for title in titles:
        d = {}
        d['Title Number'] = f'Title {count}'
        d['Title Name'] = title.text
        if title.find("a") is not None:
            d['Title link'] = title.find("a").get('href')
        count += 1
        titles_list.append(d)

   
    filename = 'titles3.csv'
    with open(filename, 'w', newline='') as f:
        w = csv.DictWriter(f,['Title Number','Title Name','Title link'])
        w.writeheader()
        
        w.writerows(titles_list)
