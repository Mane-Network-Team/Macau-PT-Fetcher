from selenium import webdriver
from datetime import datetime, timedelta
from urllib.parse import quote
import time,sys

def run(Hide = False):
    print('[jobscallme]',end='')
    sys.stdout.flush()

    chrome_options = webdriver.ChromeOptions()
    if Hide :
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        prefs = {"profile.managed_default_content_settings.images":2}
        chrome_options.add_experimental_option("prefs",prefs)

    driver = webdriver.Chrome(options=chrome_options)
    driver.get("http://www.jobscall.me/freelance")

    all_list = driver.find_elements_by_xpath('//*[@class="summary-title"]//a')
    all_list = [x.get_attribute("href") for x in all_list]
    
    def get_contact(url):
        driver.get(url)
        try:
            driver.execute_script("document.getElementsByClassName('form-wrapper')[0].remove()")
        except:
            pass
        head_line = driver.find_element_by_xpath('//*[@class="entry-title"]').text.strip()
        all_td = driver.find_elements_by_xpath('//*[@class="entry-content"]')
        all_text = head_line + "\r\n"   
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
    files.writelines("## jobscall.me 澳門好工作 - 澳門最高瀏覽量的綜合招聘網站"+ '\r\n')
    files.writelines('\r\n')
    for x,y in save_list:
        x = "https://manesec.com/jump.php?j=" + quote(str(x),safe='')
        files.writelines("### 正在招聘  [OPEN SOURCE LINK]("+x+")"+ '\r\n')
        files.writelines('```mane'+ '\r\n')
        files.writelines(y + '\r\n')
        files.writelines('```'+ '\r\n')
    files.close()
    driver.quit()