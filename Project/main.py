
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
import urllib.request

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

def closeModal() :
    closeButton = driver.find_element(By.ID, "close-popup")
    closeButton.click()
    global scrollPosition
    scrollPosition += 100
    driver.execute_script("window.scrollTo(0,{})".format(scrollPosition))

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
time.sleep(5)
lectureName = driver.find_element(By.CSS_SELECTOR,".col-sm-8.grid8").get_attribute("innerHTML")
allVideos = driver.find_elements(By.CSS_SELECTOR,".btn.btn-xs.btn-info")
for video in allVideos:
    video.click()
    time.sleep(2)
    try:
        videoFile = driver.find_element(By.TAG_NAME,"a").get_attribute("href")
        videoName = driver.find_element(By.CSS_SELECTOR,"td[title='Başlangıç Zamanı']").get_attribute("innerHTML")
        videoName = lectureName.strip() + " " + videoName.split(" ")[0]+".mp4"          
        urllib.request.urlretrieve(videoFile,videoName)       #Video download process
        closeModal()
    except:
        closeModal()
    

        
    