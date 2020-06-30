import requests, selenium, webbrowser, time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get('https://play2048.co/')
res = requests.get('https://play2048.co/')
soup = BeautifulSoup(res.text,'html.parser')

html_elem = browser.find_element_by_tag_name('html')
while True:
    html_elem.send_keys(Keys.UP)
    game_over = soup.find_all(class_ = 'game-over')
    if game_over:
        break
    time.sleep(0.5)
    html_elem.send_keys(Keys.LEFT)
    game_over = soup.find_all(class_ = 'game-over')
    if game_over:
        break
    time.sleep(0.5)
    html_elem.send_keys(Keys.DOWN)
    game_over = soup.find_all(class_ ='game-over')
    if game_over:
        break
    time.sleep(0.5)
    html_elem.send_keys(Keys.RIGHT)
    game_over = soup.find_all(class_ = 'game-over')
    if game_over:
        break
    time.sleep(0.5)
