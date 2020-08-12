# 澳門兼職情報站 Macau Part-Time Jobs Station
# https://www.facebook.com/pg/MacauPartTimeJobsStation/posts/?ref=page_internal 
# https://www.facebook.com/MacauPartTimeJobsStation/posts_to_page?ref=page_internal

from selenium import webdriver
from datetime import datetime, timedelta
from urllib.parse import quote
import time

begin_date = datetime.today() - timedelta(days=30)
begin_date = begin_date.date()
#print("Set Begin Date : %s " % begin_date)

def run(Hide = False):
    print("[FB-MPTJS]")
    chrome_options = webdriver.ChromeOptions()
    if Hide:
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        #prefs = {"profile.managed_default_content_settings.images":2}
        #chrome_options.add_experimental_option("prefs",prefs)

    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.facebook.com/pg/MacauPartTimeJobsStation/posts/?ref=page_internal")

    # remove pagelet_growth_expanding_cta
    time.sleep(1)
    driver.execute_script('document.getElementById("pagelet_growth_expanding_cta").innerHTML = "";')

    # scoll botton
    for x in range(10):
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
        time.sleep(2)
        
    # see all
    try:
        driver.execute_script('for(var i=0;i<=1000;i++){document.getElementsByClassName("see_more_link_inner")[i].click()};')
    except:
        pass

    # get poster
    poster = driver.find_elements_by_xpath('//*[@id="pagelet_timeline_main_column"]//*[@data-visualcompletion="ignore-dynamic"]')

    def Get_Times_contact(elem):
        times = elem.find_element_by_xpath('.//*[@class="fsm fwn fcg"]//abbr')
        times = TimeTitle_Date(times.get_attribute('title'))
        contact = elem.find_element_by_xpath('.//*[@data-testid="post_message"]').text
        link = elem.find_element_by_xpath('.//*[@class="fsm fwn fcg"]//a').get_attribute('href')
        link = link.split('?',1)[0]
        return [times,contact,link]

    del poster[-1]
    comb = []
    for x in poster:
        comb.append(Get_Times_contact(x))
        
    # Date Save
    files = open('mane.md','a+')
    files.writelines("## 澳門兼職情報站 Macau Part-Time Jobs Station"+ '\r\n')
    for x,y,z in comb:
        if (x<begin_date):
            continue
        z = "https://manesec.com/jump.php?j=" + quote(str(z),safe='')
        files.writelines("### "+str(x) + "  [OPEN SOURCE LINK]("+z+")"+ '\r\n')
        files.writelines('```mane'+ '\r\n')
        files.writelines(y + '\r\n')
        files.writelines('```'+ '\r\n')
    files.close()
    driver.quit()


def TimeTitle_Date(fb_date):
    dd = fb_date
    dd = dd.split(',',1)[1].strip()

    Month = {"January":1,"February":2,"March":3,"April":4,"May":5,"June":6,"July":7,"August":8,"September":9,"October":10,"November":11,"December":12}
    for x in Month:
        dd = dd.replace(x,str(Month[x]))
    
    dd = dd.split('at')[0].strip()
    dd = datetime.strptime(dd, "%m %d, %Y").date()
    return dd

def run_vister(Hide=False):
    print("[FB-MPTJS-VISTER]")
    chrome_options = webdriver.ChromeOptions()
    if Hide:
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        #prefs = {"profile.managed_default_content_settings.images":2}
        #chrome_options.add_experimental_option("prefs",prefs)

    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.facebook.com/pg/MacauPartTimeJobsStation/posts/?ref=page_internal")
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div[1]/div/div[2]/div/div/div[1]/a').click()
    time.sleep(5)
    
    # see all
    try:
        driver.execute_script('for(var i=0;i<=1000;i++){document.getElementsByClassName("see_more_link_inner")[i].click()};')
    except:
        pass

    # get poster
    poster = driver.find_elements_by_xpath('//*[@id="pages_posts_to_page_pagelet"]/div')

    def Get_Times_contact_Link_from_vister(elem):
        times = elem.find_element_by_xpath('.//abbr')
        times = TimeTitle_Date(times.get_attribute('title'))
        contact = elem.find_element_by_xpath('.//div[@data-testid="post_message"]').text
        link = elem.find_element_by_xpath('.//*[@class="fsm fwn fcg"]/a').get_attribute('href')
        return [times,contact,link]

    del poster[-1]
    comb = []
    for x in poster:
        comb.append(Get_Times_contact_Link_from_vister(x))

    # Date Save
    files = open('mane.md','a+')
    files.writelines("## 澳門兼職情報站 Macau Part-Time Jobs Station Visitor Posts"+ '\r\n')
    for x,y,z in comb:
        if (x<begin_date):
            continue
        z = "https://manesec.com/jump.php?j=" + quote(str(z),safe='')
        files.writelines("### "+str(x) + "  [OPEN SOURCE LINK]("+z+")"+ '\r\n')
        files.writelines('```mane'+ '\r\n')
        files.writelines(y + '\r\n')
        files.writelines('```'+ '\r\n')
    files.close()
    driver.quit()
