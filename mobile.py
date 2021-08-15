import mechanize
from bs4 import BeautifulSoup
url="https://findandtrace.com/trace-mobile-number-location"
brow= mechanize.Browser()
brow.set_handle_robots(False) #make  false bcs some website doesn't allow to scrab data
brow.open(url)
brow.select_form(name="trace")
brow['mobilenumber']=str(input("enter the mobile number: "))
result=brow.submit()
soup=BeautifulSoup(result.read(),'html.parser')
table_extr=soup.find_all('table',class_='shop_table')
#print(len(table_extr))
data_extracted= table_extr[0].find('tfoot')
count=0
for tr in data_extracted:
    count += 1
    if count in (1,4,6,8):
        continue
    th=tr.find('th')
    td=tr.find('td')
    print(th.text)
    print(td.text)

data_extracted= table_extr[1].find('tfoot')
counnt=0
for tr in data_extracted:
    counnt += 1
    if counnt in (2,8,10,12,14,16,20,22,24,26):
        th=tr.find('th')
        td=tr.find("td")
        print(th.text)
        print(td.text)











