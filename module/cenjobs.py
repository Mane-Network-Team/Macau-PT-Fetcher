from selenium import webdriver
from datetime import datetime, timedelta
from urllib.parse import quote
import time,sys

begin_date = datetime.today() - timedelta(days=30)
begin_date = begin_date.date()

def Run(Hide = False):
    print('[Cenjobs]',end='')
    sys.stdout.flush()
    chrome_options = webdriver.ChromeOptions()
    if Hide :
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        prefs = {"profile.managed_default_content_settings.images":2}
        chrome_options.add_experimental_option("prefs",prefs)

    driver = webdriver.Chrome(options=chrome_options)

    driver.get("https://www.cenjobs.com/jobs/?searchId=1597238241.5478&action=refine&EmploymentType[multi_like][]=1251")

    card_list = driver.find_elements_by_xpath('//*[@class="media well listing-item listing-item__jobs  "]')

    def get_card_body(elem):
        card_title = elem.find_element_by_xpath('.//*[@class="media-heading listing-item__title"]').text
        card_comm = elem.find_element_by_xpath('.//*[@class="listing-item__info--item listing-item__info--item-company"]').text
        card_date = elem.find_element_by_xpath('.//*[@class="listing-item__date"]').text
        card_date = datetime.strptime(card_date, "%d/%m/%Y").date()
        card_url = elem.find_element_by_xpath('.//*[@class="media-heading listing-item__title"]//a').get_attribute("href")
        return [card_title,card_comm,card_date,card_url]

    def get_insite_contact(url):
        driver.get(url)
        return driver.find_element_by_xpath('//*[@class="pull-left details-body__left"]').text

    return_list = []
    for x in card_list:
        return_list.append(get_card_body(x))

    # Date Save
    files = open('mane.md','a+')
    files.writelines("## No.1 澳門招聘指南 CENJOBS.COM"+ '\r\n')

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
    