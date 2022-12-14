import urllib3
import xlwt
from bs4 import BeautifulSoup

word = input('Enter the word: ')

keywords = []
relatedSearches = []

session = urllib3.PoolManager()
request = session.request('GET', f'https://www.google.com/search?q={word}')
content = BeautifulSoup(request.data, 'html.parser')

for i in content.find_all('div', {'class': 'BNeawe s3v9rd AP7Wnd lRVwie'}):
    keywords.append(i.text)

excel = xlwt.Workbook()
sh = excel.add_sheet('my data')

for j in range(len(keywords)):
    req = session.request('GET', f'https://www.google.com/search?q={keywords[j]}')
    cont = BeautifulSoup(req.data, 'html.parser')
    sh.write(j, 0, keywords[j])
    items = cont.find_all('div', {'class': 'BNeawe s3v9rd AP7Wnd lRVwie'})

    for i in range(len(items)):
        relatedSearches.append(items[i].text)
        sh.write(j, i+1, items[i].text)


print('Success, view the keywords.xls file.')
excel.save('keywords.xls')
