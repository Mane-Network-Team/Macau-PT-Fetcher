from selenium import webdriver
from datetime import datetime, timedelta
from urllib.parse import quote
import time,sys

begin_date = datetime.today() - timedelta(days=30)
begin_date = begin_date.date()

def Run(Hide = False):
    print('[Must edu]',end='')
    sys.stdout.flush()
    chrome_options = webdriver.ChromeOptions()
    if Hide :
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        prefs = {"profile.managed_default_content_settings.images":2}
        chrome_options.add_experimental_option("prefs",prefs)

    driver = webdriver.Chrome(options=chrome_options)

    driver.get("https://www.must.edu.mo/cecp/student/job?limit=50&limitstart=0")

    card_list = driver.find_elements_by_xpath('//*[@class="category"]//li')

    def get_card_body(elem):
        card_title = elem.find_element_by_xpath('.//a').text
        card_date = elem.find_element_by_xpath('.//em').text
        card_date = datetime.strptime(card_date, "%Y年%m月%d日").date()
        card_url = elem.find_element_by_xpath('.//a').get_attribute("href")
        return [card_title,card_date,card_url]

    def get_insite_contact(url):
        driver.get(url)
        return driver.find_element_by_xpath('//*[@class="article-content clearfix"]').text

    return_list = []
    for x in card_list:
        return_list.append(get_card_body(x))

    # Date Save
    files = open('mane.md','a+')
    files.writelines("## 澳门科技大学 職位空缺"+ '\r\n')

    for card_title,card_date,card_url in return_list:
        if (card_date<begin_date):
            continue
        if (card_title.find("兼職")==-1):
            continue
        save_url = "https://manesec.com/jump.php?j=" + quote(str(card_url),safe='')
        files.writelines("### "+str(card_date) + "  [OPEN SOURCE LINK]("+save_url+")"+ '\r\n')

        files.writelines('```mane'+ '\r\n')
        files.writelines(card_title + '\r\n')
        files.writelines(get_insite_contact(card_url) + '\r\n')
        files.writelines('```'+ '\r\n')

        print('.',end='')
        sys.stdout.flush()

    files.close()
    driver.quit()

    print()
    