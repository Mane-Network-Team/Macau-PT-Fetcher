from selenium import webdriver
from datetime import datetime, timedelta
from urllib.parse import quote
import time,sys

def run(Hide = False):
    print('[UM]',end='')
    sys.stdout.flush()

    chrome_options = webdriver.ChromeOptions()
    if Hide :
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        prefs = {"profile.managed_default_content_settings.images":2}
        chrome_options.add_experimental_option("prefs",prefs)

    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://isw.um.edu.mo/sjv/browseAdvertisements.do?event=filter&locale=E&faculty=&jobNature=&typeOfRecruit=&typeOfJob=#")

    all_list = driver.find_elements_by_xpath('//*[@id="main_table"]//a')
    all_list = [x.get_attribute("href") for x in all_list]
    
    def get_contact(url):
        driver.get(url)
        all_td = driver.find_elements_by_xpath('//*[@id="main_table"]/tbody//td')
        all_text = ""   
        for y in all_td:
            all_text += y.text.strip() + '\r\n'
        return [url,all_text]
    
    save_list = []
    for x in all_list:
        save_list.append(get_contact(x))
        print('.',end='')
        sys.stdout.flush()
    print('')
    
    # Date Save
    files = open('mane.md','a+')
    files.writelines('\r\n')
    files.writelines("## 澳门大学 職位空缺"+ '\r\n')
    files.writelines('\r\n')
    for x,y in save_list:
        x = "https://manesec.com/jump.php?j=" + quote(str(x),safe='')
        files.writelines("### 正在招聘  [OPEN SOURCE LINK]("+x+")"+ '\r\n')
        files.writelines('```mane'+ '\r\n')
        files.writelines(y + '\r\n')
        files.writelines('```'+ '\r\n')
    files.close()
    driver.quit()