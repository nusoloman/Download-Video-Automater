import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
import urllib.request


def login(USERNAME,PASS):
    driver.get("https://online.yildiz.edu.tr/Account/Login?ReturnUrl=%2f")
    e_mail = driver.find_element(By.ID,"Data_Mail")
    e_mail.send_keys(USERNAME)
    e_mail.send_keys(Keys.TAB)
    password = driver.find_element(By.ID,"Data_Password")
    password.send_keys(PASS)
    button = driver.find_element(By.CSS_SELECTOR,".btn.btn-primary.mt-2")
    button.click()

def closeModal() :
    wait_until("button.close")
    closeButton = driver.find_element(By.CSS_SELECTOR,"button.close")
    closeButton.click()
    global scrollPosition
    scrollPosition += 100
    driver.execute_script("window.scrollTo(0,{})".format(scrollPosition))


def wait_until(locator, timeout=10, period=0.5):    # This function used for blocking misclick.
  mustend = time.time() + timeout
  while time.time() < mustend:
    try:
        element = driver.find_element(By.CSS_SELECTOR,locator)
        if(element.is_displayed()): return True
        time.sleep(period)
    except:
        time.sleep(period)
  return False


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
service = Service("./chromedriver")
driver = webdriver.Chrome(options= chrome_options,service=service)
driver.maximize_window()
scrollPosition = 0

lessonsUrls=["<First lesson's URL you want to download>","<Second lesson's URL you want to download ...>"]
login("<your e-mail adress>","<password>")


wait_until("li.active a")
for DOWNLOAD_URL in lessonsUrls:
    scrollPosition = 0
    driver.get(DOWNLOAD_URL)
    try: 
        lectureName = driver.find_element(By.CSS_SELECTOR,".col-sm-8.grid8").get_attribute("innerHTML") #look
        allVideos = driver.find_elements(By.CSS_SELECTOR,".btn.btn-xs.btn-info")
    except:
        wait_until(".col-sm-8.grid8")
        wait_until(".btn.btn-xs.btn-info")
        lectureName = driver.find_element(By.CSS_SELECTOR,".col-sm-8.grid8").get_attribute("innerHTML") #look
        allVideos = driver.find_elements(By.CSS_SELECTOR,".btn.btn-xs.btn-info")
                    
    for video in allVideos:
        try:
            wait_until("button.close")
            video.click()
            wait_until("button.close")
            videoFile = driver.find_elements(By.XPATH,"//a[starts-with(text(),'İzle')]")
            if (len(videoFile)>1):
                idx=0
                for v in videoFile:
                    idx+=1
                    videoFile= v.get_attribute("href")
                    videoName = driver.find_element(By.CSS_SELECTOR,"td[title='Başlangıç Zamanı']").get_attribute("innerHTML") #look
                    videoName = lectureName.strip() + " " + videoName.split(" ")[0]+ "_({})".format(idx)+".mp4"  
                    urllib.request.urlretrieve(videoFile,videoName)       #Video download process              
                closeModal()
                idx=0
            else:
                videoFile = videoFile[0].get_attribute("href")
                videoName = driver.find_element(By.CSS_SELECTOR,"td[title='Başlangıç Zamanı']").get_attribute("innerHTML") #look
                videoName = lectureName.strip() + " " + videoName.split(" ")[0]+".mp4"   
                urllib.request.urlretrieve(videoFile,videoName)       #Video download process
                closeModal()
        except:
            try :
                closeModal()
            except:
                driver.close()

        