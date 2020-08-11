from selenium import webdriver
from datetime import datetime, timedelta
import time,sys

begin_date = datetime.today() - timedelta(days=30)
begin_date = begin_date.date()
#print("Set Begin Date : %s " % begin_date)

def Run(Hide = False):
    print('[MacauHR]',end='')
    sys.stdout.flush()
    chrome_options = webdriver.ChromeOptions()
    if Hide :
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        prefs = {"profile.managed_default_content_settings.images":2}
        chrome_options.add_experimental_option("prefs",prefs)

    driver = webdriver.Chrome(options=chrome_options)

    fetch_contact = []
    
    def process_time(days):
        return datetime.strptime(days, "%Y-%m-%d").date()

    def fetch_list(page):
        driver.get("https://macauhr.com/allJobs?pageNum="+str(page))
        time.sleep(3)
        contact = driver.find_elements_by_xpath('//*[@class="pc-mode"]')
        
        del contact[0]
        for x in contact:
            types = x.find_element_by_xpath('.//*[@class="ribbon"]').text
            title = x.find_element_by_xpath('.//*[@class="job-search-text"]/a').text
            comm = x.find_element_by_xpath('.//*[@class="job-search-text"]/span').text
            date = process_time(x.find_element_by_xpath('.//*[@class="job-search-time"]/span').text)
            url = x.find_element_by_xpath('.//*[@class="job-search-text"]/a').get_attribute("href")
            fetch_contact.append([title,types,comm,date,url])
            
    for y in range(1,6):
        fetch_list(y)
        print('.',end='')
        sys.stdout.flush()
    print('>',end='')

    def fetch_url_contact(url):
        try:
            driver.get(url)
            tagg = driver.find_elements_by_xpath('//*[@class="job-tag-table"]//td')
            tagg_contact = ""
            for z in tagg:
                m = z.text.strip()
                if m.find(':') ==-1:
                    m = m + '\r\n'
                tagg_contact += m
                
            tagg_contact += driver.find_element_by_xpath('//*[@class="group-job-description"]').text
            return tagg_contact
        except :
            return ""


    # Date Save
    files = open('mane.md','a+')
    files.writelines("## 澳門首選搵工網站"+ '\r\n')

    for title,types,comm,date,url in fetch_contact:
        if (date<begin_date):
            continue
        files.writelines("### "+str(date) + "  [OPEN SOURCE LINK]("+url+")"+ '\r\n')
        files.writelines('```mane'+ '\r\n')
        files.writelines(title + '\r\n')
        files.writelines(types + '\r\n')
        files.writelines(comm + '\r\n')
        files.writelines(fetch_url_contact(url) + '\r\n')
        files.writelines('```'+ '\r\n')
        print('.',end='')
        sys.stdout.flush()
    print()
    files.close()
    driver.quit()
