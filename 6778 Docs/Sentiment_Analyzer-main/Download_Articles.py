from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

options = webdriver.ChromeOptions()

# Github credentials
username = "username"
password = "password"

# 'American Express', 'Honeywell', 'Coca-Cola', 'Goldman Sachs', 'Cisco', 'Chevron', 'Caterpillar', 'Boeing', 'Apple', 'Amgen', '3M',  'Dow', 'Home Depot', 'IBM', 'Intel', , 'JPMorgan Chase', "McDonald's", 'Merck', 'Microsoft', 'Nike', 'Procter & Gamble', 'Salesforce', 'Travelers', 'UnitedHealth', 'Verizon', 'Visa', 'Walgreens Boots Alliance', 'Walmart', 'Walt Disney'

companies = ['Amgen']


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

    # first date
    driver.find_element(By.XPATH, "//*[@id=\"3bJgkgk\"]/ln-gns-searchbox/lng-searchbox/div[1]/date-selector/lng-search-options-menu/div[2]/div/custom-date-range-selector/div[3]/calendarfield/div/input").send_keys(Keys.COMMAND, "a")
    driver.find_element(By.XPATH, "//*[@id=\"3bJgkgk\"]/ln-gns-searchbox/lng-searchbox/div[1]/date-selector/lng-search-options-menu/div[2]/div/custom-date-range-selector/div[3]/calendarfield/div/input").send_keys("07/15/2022")

    # second date
    driver.find_element(By.XPATH, "//*[@id=\"3bJgkgk\"]/ln-gns-searchbox/lng-searchbox/div[1]/date-selector/lng-search-options-menu/div[2]/div/custom-date-range-selector/div[4]/calendarfield/div/input").send_keys(Keys.COMMAND, "a")
    driver.find_element(By.XPATH, "//*[@id=\"3bJgkgk\"]/ln-gns-searchbox/lng-searchbox/div[1]/date-selector/lng-search-options-menu/div[2]/div/custom-date-range-selector/div[4]/calendarfield/div/input").send_keys("08/15/2022")

    # apply date selection
    driver.find_element(By.XPATH, "//*[@id=\"3bJgkgk\"]/ln-gns-searchbox/lng-searchbox/div[1]/date-selector/lng-search-options-menu/div[2]/div/custom-date-range-selector/input").click()


    # change to 'news'
    driver.find_element(By.XPATH, "//*[@id=\"3bJgkgk\"]/ln-gns-searchbox/lng-searchbox/div[1]/filter-selector/lng-search-options-menu/div/button").click()
    driver.find_element(By.XPATH, "//*[@id=\"3bJgkgk\"]/ln-gns-searchbox/lng-searchbox/div[1]/filter-selector/lng-search-options-menu/div[2]/div/div/filter-selector-node[1]/label/span").click()

    # click search button
    driver.find_element(By.XPATH, "//*[@id=\"3bJgkgk\"]/ln-gns-searchbox/lng-searchbox/div[1]/lng-search-button").click()
    time.sleep(0.5)
    # Select Articles 1-10

    driver.find_element(By.XPATH, "//*[@id='content']/div[2]/form/div[2]/ol/li[2]/label/input").click()
    driver.find_element(By.XPATH, "//*[@id='content']/div[2]/form/div[2]/ol/li[4]/label/input").click()
    time.sleep(0.25)
    driver.find_element(By.XPATH, "//*[@id='content']/div[2]/form/div[2]/ol/li[6]/label/input").click()
    driver.find_element(By.XPATH, "//*[@id='content']/div[2]/form/div[2]/ol/li[8]/label/input").click()
    driver.find_element(By.XPATH, "//*[@id='content']/div[2]/form/div[2]/ol/li[10]/label/input").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//*[@id='content']/div[2]/form/div[2]/ol/li[12]/label/input").click()
    driver.find_element(By.XPATH, "//*[@id='content']/div[2]/form/div[2]/ol/li[14]/label/input").click()
    driver.find_element(By.XPATH, "//*[@id='content']/div[2]/form/div[2]/ol/li[16]/label/input").click()
    time.sleep(0.25)
    driver.find_element(By.XPATH, "//*[@id='content']/div[2]/form/div[2]/ol/li[18]/label/input").click()
    driver.find_element(By.XPATH, "//*[@id='content']/div[2]/form/div[2]/ol/li[20]/label/input").click()

    time.sleep(2)

    # click download button
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

    driver.find_element(By.ID, "FileName").send_keys(str(company_name))



    # Download

    driver.find_element(By.XPATH, "/html/body/aside/footer/div/button[1]").click()
    time.sleep(15)


    # close the driver


for company in companies:
    company_name = company
    download_articles(company_name)