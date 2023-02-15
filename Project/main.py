
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
import urllib.request
from bs4 import BeautifulSoup

def login(USERNAME,PASS,URL):
    driver.get(URL)
    e_mail = driver.find_element(By.ID,"Data_Mail")
    e_mail.send_keys(USERNAME)
    e_mail.send_keys(Keys.TAB)
    password = driver.find_element(By.ID,"Data_Password")
    password.send_keys(PASS)
    button = driver.find_element(By.CSS_SELECTOR,".btn.btn-primary.mt-2")
    button.click()
    time.sleep(3)


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
service = Service("./chromedriver")
driver = webdriver.Chrome(options= chrome_options,service=service)
driver.maximize_window()
scrollPosition = 0

login("<your e-mail adress>","<password>.","<Login URL>")

DOWNLOAD_ADRESS = "<The page URL you want download>"
driver.get(DOWNLOAD_ADRESS)
time.sleep(2)
allVideos = driver.find_elements(By.CSS_SELECTOR,".btn.btn-xs.btn-info")
for video in allVideos:
    video.click()
    time.sleep(2)
    pageSource = driver.page_source
    soup = BeautifulSoup(pageSource, 'html.parser')
    videoNotFound = soup.find('td', {'colspan':"5"})
    if (videoNotFound == None):
        element = driver.find_element(By.TAG_NAME,"a").get_attribute("href")
        videoName = driver.find_element(By.CSS_SELECTOR,"td[title='Başlangıç Zamanı']").get_attribute("innerHTML")
        videoName = videoName.split(" ")[0]+".mp4"          
        urllib.request.urlretrieve(element,videoName)       #Video download process
    closeModal = driver.find_element(By.ID,"close-popup")
    closeModal.click()
    scrollPosition += 100
    driver.execute_script("window.scrollTo(0,{})".format(scrollPosition))
    

        
    