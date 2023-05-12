import time
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from flask import Flask, jsonify

from Usuario import Usuario


url = "https://twitter.com/"
usuario = "diojorange"
driver = webdriver.Chrome()
driver.get(f"{url}{usuario}")
time.sleep(5)
soup = BeautifulSoup(driver.page_source, features="html.parser")
# Pegar dados
arroba = soup.find('div',class_="css-901oao css-1hf3ou5 r-14j79pv r-18u37iz r-1qd0xha r-1wvb978 r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-qvutc0").text # ok
nome = soup.find('div',class_="css-901oao r-1awozwy r-18jsvk2 r-6koalj r-1qd0xha r-adyw6z r-1vr29t4 r-135wba7 r-bcqeeo r-1udh08x r-qvutc0").text # ok
tweets = soup.find('div',class_="css-901oao css-1hf3ou5 r-14j79pv r-1qd0xha r-n6v787 r-16dba41 r-1cwl3u0 r-bcqeeo r-qvutc0").text # ok
seguidores = soup.find('a', {'href' : '/diojorange/followers', 'class' : 'css-4rbku5 css-18t94o4 css-901oao r-18jsvk2 r-1loqt21 r-1qd0xha r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-qvutc0'}).text.replace('Seguidores','').strip() #ok
seguindo = soup.find('span',class_="css-901oao css-16my406 r-18jsvk2 r-poiln3 r-1b43r93 r-b88u0q r-1cwl3u0 r-bcqeeo r-qvutc0").text # ok

usuario = Usuario(arroba,nome,tweets,seguidores,seguindo)
print(usuario)











# app = Flask(__name__)
# @app.route('/')
# def homepage():
#     return 'Hello World!'
# @app.route('/usuarios')
# def iniciar():
#   result = {}
#   for url in listaUsuarios:
#      usuario = scrapper.iniciarBusca(url)
#      result.__setitem__(url, usuario)
#   return jsonify(result)
# app.run()
