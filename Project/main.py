import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
import urllib.request
# from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
    time.sleep(3)
    # closeButton=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button.close")))
    closeButton = driver.find_element(By.CSS_SELECTOR,"button.close")
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
# wait = WebDriverWait(driver, 10)

datafromfile=["https://online.yildiz.edu.tr/?transaction=LMS.EDU.LessonProgram.ViewOnlineLessonProgramForStudent/36484"]
login("<your e-mail adress>","<password>")
# wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"li.active a")))
time.sleep(3)
for DOWNLOAD_URL in datafromfile:
    scrollPosition = 0
    driver.get(DOWNLOAD_URL)
    # wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,".btn.btn-xs.btn-info")))
    time.sleep(3)
    lectureName = driver.find_element(By.CSS_SELECTOR,".col-sm-8.grid8").get_attribute("innerHTML") #look
    allVideos = driver.find_elements(By.CSS_SELECTOR,".btn.btn-xs.btn-info")
    for video in allVideos:
        try:
            time.sleep(3)
            # wait.until_not(EC.element_to_be_clickable((By.CSS_SELECTOR,"button.close")))
            video.click()
            time.sleep(3)
            # wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button.close")))
            videoFile = driver.find_elements(By.XPATH,"//a[starts-with(text(),'İzle')]")
            print(videoFile)
            print(len(videoFile))
            if (len(videoFile)>1):
                idx=0
                for v in videoFile:
                    idx+=1
                    videoFile= v.get_attribute("href")
                    videoName = driver.find_element(By.CSS_SELECTOR,"td[title='Başlangıç Zamanı']").get_attribute("innerHTML") #look
                    videoName = lectureName.strip() + " " + videoName.split(" ")[0]+ "_({})".format(idx)+".mp4"  
                    print(videoName+" Basladı") 
                    time.sleep(5)
                    # urllib.request.urlretrieve(videoFile,videoName)       #Video download process              
                closeModal()
                idx=0
            else:
                videoFile = videoFile[0].get_attribute("href")
                videoName = driver.find_element(By.CSS_SELECTOR,"td[title='Başlangıç Zamanı']").get_attribute("innerHTML") #look
                print(videoName+"Basladı")
                videoName = lectureName.strip() + " " + videoName.split(" ")[0]+".mp4"   
                time.sleep(5)
                # urllib.request.urlretrieve(videoFile,videoName)       #Video download process
                closeModal()
        except:
            try :
                closeModal()
            except:
                driver.close()

        