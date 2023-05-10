from bs4 import BeautifulSoup
import selenium.webdriver as webdriver
from Usuario import Usuario

url = f'https://www.instagram.com/marissol_mfernandes7/'
driver = webdriver.Chrome()
driver.get(url)
soup = BeautifulSoup(driver.page_source, features="html.parser")
# nome = soup.find('h2', class_='x1lliihq x1plvlek xryxfnj x1n2onr6 x193iq5w xeuugli x1fj9vlw x13faqbe x1vvkbs x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x1i0vuye x1ms8i2q xo1l8bm x5n08af x10wh9bi x1wdrske x8viiok x18hxmgj').text
dados = []
for x in soup.findAll('span', {'class': '_ac2a'}):
  print(x.text)
