import requests
from bs4 import BeautifulSoup
import csv

search_product = input('masukkan produk yang di cari : ')
page = [range]
url = 'https://www.tokopedia.com/search?navsource=home&page={}&q={}&st=product'.format(page,search_product)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
data = []
for page in range(1,10):
    req = requests.get(url, headers = headers) 
    soup = BeautifulSoup(req.text, 'html.parser')
    product = soup.find_all('div', 'pcv3__container css-1bd8ct')
    for it in product:
        product_name = it.find('div', 'css-1f4mp12').text
        product_price = it.find('div', 'css-rhd610').text.replace('Rp','').replace(' ','').replace('.','').replace('  ','')
        try : product_sold = it.find('span', 'css-1kgbcz0').text.replace('Terjual ','').replace(' rb','00').replace(',','')
        except : product_sold = ''
        try : product_rate = it.find('span', 'css-etd83i').text
        except : product_rate = ''
        data.append([product_name,product_price,product_sold,product_rate]) 

header_csv = ['produk','harga','terjual','rating']
writer = csv.writer(open('tokopedia_{}_scraping.csv'.format(search_product),'w',newline=''))
writer.writerow(header_csv)

for d in data: writer.writerow(d)