from turtle import title
from webbrowser import Chrome
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import os
import undetected_chromedriver as uc
import ssl
import certifi
from selenium.webdriver.common.keys import Keys
from datetime import date
ssl._create_default_https_context = ssl._create_unverified_context

if __name__ == '__main__':
    sciezka = Service('chrome/chromedriver')
    chrome_options = Options()
    chrome_options.headless = True
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
    chrome_options.add_argument('user-agent={0}'.format(user_agent))
    driver = webdriver.Chrome(chrome_options=chrome_options, service=sciezka)
    # czeka 30 sekund i ponawia wyszukiwanie poszczególnege elementu
    driver.implicitly_wait(30)
    driver.get("https://www.messenger.com/")

    driver.find_element(
        By.XPATH, '/html/body/div[2]/div[2]/div/div/div/div/div[3]/button[2]').click()

    #driver.find_element(
      #  By.XPATH, '//*[@id="email"]').send_keys('//login//')
    #driver.find_element(
        #By.XPATH, '//*[@id="pass"]').send_keys('//Hasło//', Keys.TAB, Keys.ENTER)
    time.sleep(1)
    driver.find_element(
        By.XPATH, '//*[@id="pass"]').send_keys(Keys.ENTER)
    driver.find_element(
        By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div/div/div/div/label/input').click()
    driver.find_element(
        By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div/div/div/div/label/input').send_keys('Norbert Ziółkowski')
    driver.find_element(
        By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div/div/div/div/label/input').send_keys('Norbert Ziółkowski')
    driver.find_element(
        By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div/div[1]/ul/li[1]/ul/li[2]/div/a/div').click()
    today = date.today()
    # dd/mm/YY
    Data = today.strftime("%d/%m/%Y")
    driver.find_element(
        By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div[2]/div[4]/div[2]/div/div/div[1]/p').send_keys(Data, Keys.ENTER)

    time.sleep(5)
    # PB = driver.find_element(
    #     By.XPATH, '/html/body/div[11]/div/div/div[1]/div[1]/div/a[1]/div').text
    # ON = driver.find_element(
    #     By.XPATH, '/html/body/div[11]/div/div/div[1]/div[1]/div/a[3]/div').text
    # LPG = driver.find_element(
    #     By.XPATH, '/html/body/div[11]/div/div/div[1]/div[1]/div/a[5]/div').text
    # print("95: "+PB+"\nON: "+ON+"\nLPG: "+LPG+"")
    # driver.close()

    # sciezka = Service('chrome/chromedriver')
    # chrome_options1 = Options()
    # chrome_options1.headless = True
    # user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
    # chrome_options1.add_argument('user-agent={0}'.format(user_agent))
    # driver = webdriver.Chrome(chrome_options=chrome_options1, service=sciezka)

    # driver = uc.Chrome()
    # driver.delete_all_cookies()

    # driver.implicitly_wait(30)
    # driver.get(
    #     "https://docs.google.com/spreadsheets/d/1sO0vWYq-Hqfp-l8hRRgugk1RVeY9u3q8zS7837K6EF4/edit#gid=649173132")
    # driver.find_element(
    #     By.XPATH, '//*[@id="identifierId"]').send_keys('aleks4409ryhu440@gmail.com', Keys.ENTER)

    # driver.find_element(
    #     By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input').send_keys('Moje2imie', Keys.ENTER)
    # driver.find_element(
    #     By.ID, ':4h').click()

    # today = date.today()
    # # dd/mm/YY
    # Data = today.strftime("%d/%m/%Y")
    # print("Data =", Data)
    # time.sleep(4)
    # driver.find_element(
    #     By.ID, 't-name-box').click()

    # driver.find_element(
    #     By.ID, 't-name-box').send_keys('G11', Keys.ENTER, Keys.BACKSPACE, Data, Keys.ENTER)
    # driver.find_element(
    #     By.ID, 't-name-box').send_keys('G12', Keys.ENTER, Keys.BACKSPACE, ON, Keys.ENTER)
    # driver.find_element(
    #     By.ID, 't-name-box').send_keys('G13', Keys.ENTER, Keys.BACKSPACE, PB, Keys.ENTER)
    # driver.find_element(
    #     By.ID, 't-name-box').send_keys('G14', Keys.ENTER, Keys.BACKSPACE, LPG, Keys.ENTER)

    quit()
