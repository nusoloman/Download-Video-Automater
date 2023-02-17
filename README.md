# Video İndirme Otomasyonu
Yıldız Teknik Üniversitesi online video sisteminin videolarını otomatik olarak indiren bir koddur. Yüzyüze katılımı artırmak amacıyla online sistemin kapatılması  ihtimaline karşın, sistemdeki tüm  videoları hızlı bir şekilde cihazınıza depolayabilirsiniz. Kod çalışmaya başladığı andan itibaren bilgisayarınıza dokunmadan bir kahve molası verebilirsiniz, o sizin için belirttiğiniz tüm videoları indirecektir...  

## Gereksinimler

* Python
* Selenium
* Chromedriver.exe

## Kurulum

1. Python'u indirip kurduktan sonra selenium paketini indirmelisiniz. Selenium indirmek için : https://www.selenium.dev/downloads/ 
2. Kendi Chrome sürümünüze uygun chromewebdriver'larınızı kurmalısınız. Bu kod için dizinde verilen driver 110.0.5481.97 sürümü içindir. 
3. Chrome sürümünü öğrenmek için --> Chome'da sağ üstteki 3 nooktaya basın --> Yardım --> Google Chrome Hakkında --> "110.0.5481.97" 
4. Sürümünüzü öğrendikten sonra https://chromedriver.chromium.org/downloads linki üzerinden kendi sürümünüze uygun driver'ı indirin ve kurun. Execution dosyasını kod ile aynı klasör dizininde saklayın!

## Kullanım

1. Kodun içerisinde bir login() fonksiyonu var, bu fonksiyona sisteme giriş yapmanızı sağlayacak e-mail ve şifre bilgilerinizi girmelisiniz.
2. lessonsUrls[] adlı dizinin içine indirmek istediğiniz tüm derslerin linklerini yazın.
3. Kendinize bir kahve yapın ve gerçekten faydalandıysanız bana bir teşekkür mesajı atın 


# Download-Video-Automater
It is a code that automatically downloads the videos of Yıldız Technical University online video system. In case the online system is shut down in order to increase face-to-face participation, you can quickly store all the videos in the system on your device. From the moment the code starts working, you can take a coffee break without touching your computer, it will download all the videos for you... 

## Requirements

* Python
* Selenium
* Chromedriver.exe


## Setup

1. After downloading and installing Python, you must download the selenium package. To download Selenium: https://www.selenium.dev/downloads/
2. You should install your chromewebdrivers suitable for your own version of Chrome. The driver given in the directory for this code is for version 110.0.5481.97.
3. To find out the version of Chrome --> Click the 3 dots at the top right of Chome --> Help --> About Google Chrome --> "110.0.5481.97"
4. After learning your version, download and install the appropriate driver for your version via the link https://chromedriver.chromium.org/downloads. Store the execution file in the same folder directory as the code!

## Usage

1. There is a login() function in the code, in this function you must enter your e-mail and password information to log in to the system.
2. In the array named lessonsUrls[], write the links of all the lessons you want to download. 
3. Make yourself a coffee and text me a thank you if you really benefited
