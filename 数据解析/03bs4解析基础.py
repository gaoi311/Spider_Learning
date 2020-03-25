from bs4 import BeautifulSoup

f = open("test.html", "r", encoding="utf-8")
soup = BeautifulSoup(f, "lxml")
# print(soup.find_all('div'))
# print(soup.select('.tang'))
print(soup.select('.tang > ul > li > a')[0]['href'])