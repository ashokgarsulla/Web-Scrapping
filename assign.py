import requests
from bs4 import BeautifulSoup as bs
import csv
import datetime
URL = 'https://www.theverge.com/archives/'
# soup = bs(requests.get(URL).content,'html.parser')
# MAX_page = soup.find("span",class_="c-pagination__text").text
# print(MAX_page.strip())
# print(MAX_page.strip())
# x = MAX_page.strip()
# print(x[30:32],"working")
# print(len(MAX_page))
count = 1
for page in range(1, 16):
    req = requests.get(URL + str(page))
    soup = bs(req.content, 'html.parser')

    titles = soup.find_all('div', attrs={'class', 'c-entry-box--compact__body'})
    titles_list = []
    
    # for i in titles:
    #     if i.find("a") is not None:
    #         # print(i.find("a").get('href'))
    #         pass
    # # for link in titles.find_all('a',attrs={'href': re.compile("^https://")}):
    # # # display the actual urls
    # #     print(link.get('href'))  
    

    
    for title in titles:
        d = {}
        d['id'] = count
        if title.find("a") is not None:
            d['URL'] = title.find("a").get('href')
        d['headline'] = title.find('h2').text
        if title.find("span",class_="c-byline__author-name") is not None:
            d['author'] = title.find("span",class_="c-byline__author-name").text
        d['date'] = title.find("time",class_="c-byline__item").get('datetime').replace("-","/")[0:10]
        count += 1
        titles_list.append(d)
        # print(titles_list)

    filename = str(datetime.date.today()).replace("-","")+"_verge"+".csv"
    with open(filename, 'a', newline='') as f:
        w = csv.DictWriter(f,['id','URL','headline','author','date'])
        # w.writeheader()
        w.writerows(titles_list)
