from selenium import webdriver
from datetime import datetime, timedelta
import time,sys

begin_date = datetime.today() - timedelta(days=30)
begin_date = begin_date.date()

def Run(Hide = False):
    chrome_options = webdriver.ChromeOptions()
    if Hide :
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        prefs = {"profile.managed_default_content_settings.images":2}
        chrome_options.add_experimental_option("prefs",prefs)

    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.fastfindjob.com/jobList?searchJobStr=&ctotal=408&searchJobType=0&total=8&careerType=2&sortType=1&pageSize=30")
    time.sleep(5)
    all_list = driver.find_elements_by_class_name("search-job-item row no-gutters")

    print(len(all_list))

    def fetch_selection_contact(elem):
        title = driver.find_elements_by_xpath(".//h3")[0]
        coom = driver.find_elements_by_xpath(".//h3")[1]
        print (title)
        print (coom)

        
    def fetch_contact(url):
        pass
    
    for x in all_list:
        fetch_selection_contact(x)