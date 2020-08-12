from selenium import webdriver
from datetime import datetime, timedelta
from urllib.parse import quote
import time,sys

begin_date = datetime.today() - timedelta(days=30)
begin_date = begin_date.date()

def Run(Hide = False):
    print('[Fast Find Job]',end='')
    sys.stdout.flush()
    chrome_options = webdriver.ChromeOptions()
    if Hide :
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        prefs = {"profile.managed_default_content_settings.images":2}
        chrome_options.add_experimental_option("prefs",prefs)

    driver = webdriver.Chrome(options=chrome_options)

    driver.get("https://www.fastfindjob.com/jobList?searchJobStr=&ctotal=411&searchJobType=0&total=9&careerType=2&sortType=1")

    time.sleep(5)

    card_list = driver.find_elements_by_xpath('//*[@class="search-job-item row no-gutters"]')

    def get_card_body(elem):
        card_title = elem.find_element_by_xpath('.//*[@class="col-lg-7 job-item-l"]//*[@class="p-top"]').text
        card_comm = elem.find_element_by_xpath('.//*[@class="col-lg-5 job-item-r"]//*[@class="p-top"]').text
        card_date = elem.find_element_by_xpath('.//*[@class="col-lg-5 job-item-r"]//*[@class="p-mid"]').text
        card_date = card_date.replace('最後更新於','')
        card_date = datetime.strptime(card_date, "%Y-%m-%d").date()
        card_url = elem.find_element_by_xpath('.//*[@class="col-lg-7 job-item-l"]//*[@class="p-top"]//a').get_attribute("href")
        return [card_title,card_comm,card_date,card_url]

    def get_insite_contact(url):
        driver.get(url)
        time.sleep(2)
        return driver.find_element_by_xpath('//*[@class="col-lg-8 job-content-l"]').text

    return_list = []
    for x in card_list:
        return_list.append(get_card_body(x))

    # Date Save
    files = open('mane.md','a+')
    files.writelines("## 快搵工 Fast Find Job - 澳門菁英求職第一選擇"+ '\r\n')

    for card_title,card_comm,card_date,card_url in return_list:
        if (card_date<begin_date):
            continue
        save_url = "https://manesec.com/jump.php?j=" + quote(str(card_url),safe='')
        files.writelines("### "+str(card_date) + "  [OPEN SOURCE LINK]("+save_url+")"+ '\r\n')

        files.writelines('```mane'+ '\r\n')
        files.writelines(card_title + '\r\n')
        files.writelines(card_comm + '\r\n')
        files.writelines(get_insite_contact(card_url) + '\r\n')
        files.writelines('```'+ '\r\n')

        print('.',end='')
        sys.stdout.flush()

    files.close()
    driver.quit()

    print()
