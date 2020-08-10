from selenium import webdriver
from datetime import datetime, timedelta
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
            all_text += y.text.strip() + '\n'
        return [url,all_text]
    
    save_list = []
    for x in all_list:
        save_list.append(get_contact(x))
        print('.',end='')
        sys.stdout.flush()
    print('')
    
    # Date Save
    files = open('mane.txt','a+')
    files.writelines('\n')
    files.writelines("#"*18 + " @Mane " + "#"*19+ '\n')
    files.writelines("             澳门大学 職位空缺"+ '\n')
    files.writelines("#"*44+ '\n')
    files.writelines('\n')
    for x,y in save_list:
        files.writelines("="*44+ '\n')
        files.writelines(y + '\n')
        files.writelines("-"*44+ '\n')
        files.writelines(x + '\n')
    files.close()
    driver.quit()