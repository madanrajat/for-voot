import os
from datetime import datetime
os.system("pip3 install -r requirements.txt")
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import random
from webdriver_manager.firefox import GeckoDriverManager
try:
    os.system("pip3 install PyVirtualDisplay==1.3.2")
except:
    pass
from pyvirtualdisplay import Display
import time
import random
import requests
options = webdriver.ChromeOptions()
mobile_emulation = {
    "deviceMetrics": { "width": 375, "height": 812, "pixelRatio": 3.0 },
    "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19"
}
options.add_experimental_option("mobileEmulation", mobile_emulation)
options.add_argument("----start-maximized")
options.add_argument("--window-size=1440,789")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
if os.name=="posix":
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    #options.add_argument("--window-size=1420,1080")
    display = Display(visible=0, size=(1420,1080))
    display.start()
    pass
for i in range(0,10000):
    try:
        uas=["Mozilla/5.0 (iPhone; CPU iPhone OS 8_0_2 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12A366 Safari/600.1.4",
        "Mozilla/5.0 (Linux; U; Android 2.2; en-us; Sprint APA9292KT Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 8_0_2 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12A366 Safari/600.1.4",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1",
        "Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; SCH-I535 Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
        "Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36"]
        ua=random.choice(uas)
        options.add_argument(f"user-agent={ua}")
        driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)
        driver.implicitly_wait(30)
        driver.get('chrome://settings/')
        driver.execute_script('chrome.settingsPrivate.setDefaultZoom(0.33);') #keep # at begining to remove zoom settings
        driver.get("https://superadme.com/tracker/click.php?key=kkucznljx7faov7r07c2")
        print("clicking episode")
        time.sleep(10)
        driver.refresh()
        print(f"Sleeping till {time.ctime(time.time()+120)}")
        time.sleep(60)
        #watch one episode for 30 seconds
        print("clicking episode")
        driver.refresh()
        print("clicking episode 12345")
        print(f"Sleeping till {time.ctime(time.time()+30)}")
        time.sleep(10)
        ############################################
        driver.quit()
    except:
        try:
            driver.quit()
        except:
            pass