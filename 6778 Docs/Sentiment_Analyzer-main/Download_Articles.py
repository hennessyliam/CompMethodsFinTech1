from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

options = webdriver.ChromeOptions()

# LexisNexus credentials
username = ""
password = ""


companies = ['3M Co', 'American Express Co', 'Amgen Inc', 'Apple Inc', 'Boeing Co', 'Caterpillar Inc', 'Chevron Corp', 'Cisco Systems Inc', 'Coca-Cola Co', 'Dow Inc', 'Goldman Sachs Group Inc', 'Honeywell International Inc', 'Intel Corp', 'International Business Machines Corp', 'JPMorgan Chase & Co', "McDonald's Corp", 'Merck & Co Inc', 'Microsoft Corp', 'Nike Inc', 'Procter & Gamble Co', 'Salesforce Inc', 'Travelers Companies Inc', 'UnitedHealth Group Inc', 'Verizon Communications Inc', 'Visa Inc', 'Walgreens Boots Alliance Inc', 'Walmart Inc', 'Walt Disney Co', 'Home Depot', 'Johnson Johnson']


def download_articles(company_name):
    # Initialize the Chrome driver
    driver = webdriver.Chrome(options=Options())
    # Head to Nexis login page
    driver.get("https://guides.ucf.edu/database/LNA")

    # Maximize window and wait
    driver.maximize_window()


    # Login
    driver.find_element("id", "userNameInput").send_keys(username)
    driver.find_element("id", "passwordInput").send_keys(password)
    driver.find_element("id","submitButton").click()

    time.sleep(3)

    # New URL
    #print(driver.current_url)
    driver.get(driver.current_url)

    # Select type in company name

    driver.find_element(By.XPATH, "//*[@id=\"3bJgkgk\"]/ln-gns-searchbox/lng-searchbox/div[1]/lng-search-input/div/div/lng-expanding-textarea").send_keys(str(company_name))

    time.sleep(0.5)

    # Select date range
    # date range button
    driver.find_element(By.XPATH, "//*[@id=\"3bJgkgk\"]/ln-gns-searchbox/lng-searchbox/div[1]/date-selector/lng-search-options-menu/div/button").click()
    driver.find_element(By.XPATH, "//*[@id=\"3bJgkgk\"]/ln-gns-searchbox/lng-searchbox/div[1]/date-selector/lng-search-options-menu/div[2]/div/ul/li[9]/button/span[1]").click()
    time.sleep(0.5)

    # first date
    driver.find_element(By.XPATH, "//*[@id=\"3bJgkgk\"]/ln-gns-searchbox/lng-searchbox/div[1]/date-selector/lng-search-options-menu/div[2]/div/custom-date-range-selector/div[3]/calendarfield/div/input").send_keys(Keys.COMMAND, "a")
    driver.find_element(By.XPATH, "//*[@id=\"3bJgkgk\"]/ln-gns-searchbox/lng-searchbox/div[1]/date-selector/lng-search-options-menu/div[2]/div/custom-date-range-selector/div[3]/calendarfield/div/input").send_keys("07/15/2022")
    
    # second date
    driver.find_element(By.XPATH, "//*[@id=\"3bJgkgk\"]/ln-gns-searchbox/lng-searchbox/div[1]/date-selector/lng-search-options-menu/div[2]/div/custom-date-range-selector/div[4]/calendarfield/div/input").send_keys(Keys.COMMAND, "a")
    driver.find_element(By.XPATH, "//*[@id=\"3bJgkgk\"]/ln-gns-searchbox/lng-searchbox/div[1]/date-selector/lng-search-options-menu/div[2]/div/custom-date-range-selector/div[4]/calendarfield/div/input").send_keys("08/15/2022")

    # apply date selection
    driver.find_element(By.XPATH, "//*[@id=\"3bJgkgk\"]/ln-gns-searchbox/lng-searchbox/div[1]/date-selector/lng-search-options-menu/div[2]/div/custom-date-range-selector/input").click()


    # change to 'news', then 'newspaper
    driver.find_element(By.XPATH, "//*[@id=\"3bJgkgk\"]/ln-gns-searchbox/lng-searchbox/div[1]/filter-selector/lng-search-options-menu/div/button").click()
    driver.find_element(By.XPATH, "//*[@id=\"3bJgkgk\"]/ln-gns-searchbox/lng-searchbox/div[1]/filter-selector/lng-search-options-menu/div[2]/div/div/filter-selector-node[1]/label/span").click()
    time.sleep(0.25)
    driver.find_element(By.XPATH, "//input[@data-track='Newspapers']").click()
    time.sleep(0.25)

    # click search button
    driver.find_element(By.XPATH, "//*[@id=\"3bJgkgk\"]/ln-gns-searchbox/lng-searchbox/div[1]/lng-search-button").click()
    time.sleep(3)
    
    # language selection:
    # language button 
    driver.find_element(By.XPATH, "//*[@id=\"podfiltersbuttonlanguage\"]").click()
    time.sleep(3)
    # choose english language
    english = driver.find_element(By.CSS_SELECTOR, "[data-filtertype=\"language\"][data-value=\"English\"]")
    english.find_element(By.XPATH,'..').click()
    time.sleep(3)

    # change geo location:
    # geo location button
    driver.find_element(By.XPATH, "//*[@id=\"podfiltersbuttonen-geography-news\"]").click()
    time.sleep(3)
    # choose North America
    try:

        driver.find_element(By.CSS_SELECTOR, "ul[aria-labelledby='podfiltersbuttonen-geography-news'] li[class='more'] button[type='button']").click()
        time.sleep(0.5)
        north_america = driver.find_element(By.CSS_SELECTOR, "[data-filtertype=\"en-geography-news\"][data-value=\"North America\"]")
        north_america.find_element(By.XPATH,'..').click()

    except:
        north_america = driver.find_element(By.CSS_SELECTOR, "[data-filtertype=\"en-geography-news\"][data-value=\"North America\"]")
        north_america.find_element(By.XPATH,'..').click()
    
    time.sleep(3)

    # change subject:
    # subject button
    driver.find_element(By.XPATH, "//*[@id=\"podfiltersbuttonen-subject\"]").click()
    time.sleep(3)
    # choose business news
    business_news = driver.find_element(By.CSS_SELECTOR, "[data-filtertype=\"en-subject\"][data-value=\"Business News\"]")
    business_news.find_element(By.XPATH,'..').click()
    time.sleep(3)

    # box_list from values 2 - 20 interval 2
    box_list = [2,4,6,8,10,12,14,16,18,20]
    
    # Select Articles 1-10
    for i in box_list:

        try:

            driver.find_element(By.XPATH, "//*[@id='content']/div[2]/form/div[2]/ol/li["+ str(i) +"]/label/input").is_displayed()
            driver.find_element(By.XPATH, "//*[@id='content']/div[2]/form/div[2]/ol/li["+ str(i) +"]/label/input").click()
            time.sleep(0.5)

        except:
            break
    
    # click download button
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='results-list-toolbar-gvs']/ul[1]/li[4]/ul/li[3]/button/span[1]").click()
    time.sleep(2)

    # choose format 
    # .docx
    #driver.find_element(By.ID, "Docx").click()
    # PDF
    #driver.find_element(By.ID, "PDF").click()
    # .rtf
    driver.find_element(By.ID, "Rtf").click()

    time.sleep(2)

    # name file name of company

    driver.find_element(By.ID, "FileName").send_keys(Keys.COMMAND, "a")

    driver.find_element(By.ID, "FileName").clear()
    if company_name == "McDonald's Corp":
        driver.find_element(By.ID, "FileName").send_keys("McDonalds Corp")
    else:
        driver.find_element(By.ID, "FileName").send_keys(str(company_name))

    time.sleep(0.25)

    # Download

    driver.find_element(By.XPATH, "/html/body/aside/footer/div/button[1]").click()
    time.sleep(12)


    # close the driver


for company in companies:
    company_name = company
    download_articles(company_name)