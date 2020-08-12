from selenium import webdriver
from datetime import datetime, timedelta
from urllib.parse import quote
import time,sys

begin_date = datetime.today() - timedelta(days=30)
begin_date = begin_date.date()
#print("Set Begin Date : %s " % begin_date)

def Run(Hide = False):
    print('[SunCareer]',end='')
    sys.stdout.flush()
    chrome_options = webdriver.ChromeOptions()
    if Hide :
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        prefs = {"profile.managed_default_content_settings.images":2}
        chrome_options.add_experimental_option("prefs",prefs)

    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.sun-career.com/parttime")
    lists = driver.find_elements_by_xpath("//tr")
    del lists[0]

    def process_time(days):
        return datetime.strptime(days, "%Y-%m-%d").date()

    def get_contact(elem):
        left_bd = elem.find_elements_by_xpath("./td/a")
        title = "招聘人员：" + left_bd[0].text
        comm = "公司："+ left_bd[1].text
        tdd = elem.find_elements_by_xpath("./td")
        area = "地区：" + tdd[1].text
        menory= "MOP：" + tdd[2].text
        types = "类型：" + tdd[3].text
        date = process_time(tdd[4].text)
        url = left_bd[0].get_attribute("href")
        return [title,comm,area,menory,types,date,url]

    def get_inside_contact(url):
        driver.get(url)
        return driver.find_element_by_xpath('//*[@class="container-gray-border job-content"]').text

    fetch_cont = [get_contact(x) for x in lists]

    # Date Save
    files = open('mane.md','a+')
    files.writelines("## 澳門筍工網"+ '\r\n')

    for title,comm,area,menory,types,date,url in fetch_cont:
        if (date<begin_date):
            continue
        save_url = "https://manesec.com/jump.php?j=" + quote(str(url),safe='')
        files.writelines("### "+str(date) + "  [OPEN SOURCE LINK]("+save_url+")"+ '\r\n')
        files.writelines('```mane'+ '\r\n')
        files.writelines(title + '\r\n')
        files.writelines(comm + '\r\n')
        files.writelines(get_inside_contact(url) + '\r\n')
        files.writelines('```'+ '\r\n')

        print('.',end='')
        sys.stdout.flush()
    print()
    files.close()
    driver.quit()
