from selenium import webdriver
from datetime import datetime, timedelta
from urllib.parse import quote
import time,sys

def run(Hide = False):
    print('[job853]',end='')
    sys.stdout.flush()

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--host-resolver-rules=MAP *.cnzz.com 127.0.0.1')
    if Hide :
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        prefs = {"profile.managed_default_content_settings.images":2}
        chrome_options.add_experimental_option("prefs",prefs)

    driver = webdriver.Chrome(options=chrome_options)
    driver.get("http://www.job853.com/Personal/CorpJob_Lists.aspx?page=1")

    # click one month and PT

    driver.find_element_by_xpath('//*[@id="Search1_D_isResh"]/option[2]').click()
    driver.find_element_by_xpath('//*[@id="Search1_Jobkind"]/option[3]').click()
    driver.find_element_by_xpath('//*[@id="Search1_iB_Search"]').click()

    all_list = []
    for x in range(1,4):
        driver.get("http://www.job853.com/Personal/CorpJob_Lists.aspx?page="+str(x))
        all_lists = driver.find_elements_by_xpath('//table[8]//a')
        for y in all_lists:
            href_links = y.get_attribute("href")
            if href_links.find("JobInfo.aspx")!=-1:
                href_links = href_links.replace("Personal","Mobile").replace("bid","id")
                all_list.append(href_links)
        print('.',end='')
        sys.stdout.flush()
    print('>',end='')
    sys.stdout.flush()
    def get_contact(url):
        driver.get(url)
        all_text = driver.find_element_by_id('L_JobName').text.strip() + '\r\n'
        all_text += driver.find_element_by_class_name('jobinfo').text.strip() + '\r\n'
        all_text += driver.find_element_by_id('L_Requirement').text.strip() + '\r\n'
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
    files.writelines("## 澳門人才網 job853.com"+ '\r\n')
    files.writelines('\r\n')
    for x,y in save_list:
        x = "https://manesec.com/jump.php?j=" + quote(str(x),safe='')
        files.writelines("### 正在招聘  [OPEN SOURCE LINK]("+x+")"+ '\r\n')
        files.writelines('```mane'+ '\r\n')
        files.writelines(y + '\r\n')
        files.writelines('```'+ '\r\n')
    files.close()
    driver.quit()