from selenium import webdriver
from datetime import datetime, timedelta
import time,sys

begin_date = datetime.today() - timedelta(days=30)
begin_date = begin_date.date()
#print("Set Begin Date : %s " % begin_date)

def Run(Hide = False):
    print('[Hello Job]',end='')
    sys.stdout.flush()
    chrome_options = webdriver.ChromeOptions()
    if Hide :
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        prefs = {"profile.managed_default_content_settings.images":2}
        chrome_options.add_experimental_option("prefs",prefs)

    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://wecarehappyjobs.hello-jobs.com/position.html?text=&fids=-1&sids=2")

    for x in range(10):
        time.sleep(2)
        driver.execute_script('document.getElementsByClassName("nui-scroll wj_list_box __list_box")[0].scrollTop = 30000')
        print('.',end='')
        sys.stdout.flush()
    def process_time(days):
        return datetime.strptime(days, "%d/%m/%Y").date()

    def get_contact(elem):
        title ="招聘人员：" +  elem.find_element_by_xpath('.//*[@class="ellipsis"]').text
        com = "公司："+ elem.find_element_by_xpath('.//*[@class="wji_name ellipsis"]').text
        types = "类型：" + elem.find_element_by_xpath('.//*[@class="flex-item ellipsis"]').text
        times = process_time(elem.find_element_by_xpath('.//*[@class="wji_time"]').text)
        url = "https://wecarehappyjobs.hello-jobs.com" + elem.find_element_by_xpath('.//*[@class="wji_btn open"]').get_attribute("aiu_link")
        return [times,title,com,types,url]

    all_contact = driver.find_elements_by_xpath('//*[@class="wj_item"]')

    return_contact = [get_contact(x) for x in all_contact]
    print('>',end='')

    def Fetch_all_contact(url):
        driver.get(url)
        print('.',end='')
        sys.stdout.flush()
        return driver.find_element_by_class_name("pdl_context").text

    # Date Save
    files = open('mane.txt','a+')
    files.writelines('\n')
    files.writelines("#"*18 + " @Mane " + "#"*19+ '\n')
    files.writelines("  隨心搵好工 – WeCare Happy Jobs隨心好工  "+ '\n')
    files.writelines("#"*44+ '\n')
    files.writelines('\n')
    for times,title,com,types,url in return_contact:
        if (times < begin_date):
            continue
        files.writelines("=============== ["+str(times) + "] ==============="+ '\n')
        files.writelines(title + '\n')
        files.writelines(com + '\n')
        files.writelines(types + '\n' + Fetch_all_contact(url) + '\n')
        files.writelines("-"*44+ '\n')
        files.writelines(url + '\n')
    files.close()
    driver.quit()
    print('')