#importing all the necessary libaries
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time


PATH = "C:\\Users\\oubelkas fatima\\Documents\\chromeDriverSelenium\\chromedriver.exe"
driver = webdriver.Chrome(PATH)

# defining the webdriver and config
chrome_options = webdriver.ChromeOptions()

# !!! blocking browser notifications !!!
prefs = {"profile.default_content_setting_values.notifications" : 2} 
chrome_options.add_experimental_option("prefs", prefs)

# starting in maximized window
chrome_options.add_argument("start-maximized")

chrome_options.add_argument("--disable-default-apps")
""" driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="C:\\Users\\taha_\\Downloads\\chromedriver_win32\\chromedriver.exe") """


driver.get('https://www.linkedin.com/login')
driver.maximize_window()
time.sleep(2)

driver.find_element_by_id('username').clear()
driver.find_element_by_id('username').send_keys('email')
driver.find_element_by_id('password').send_keys('password')
driver.find_element_by_xpath("//button[contains(text(),'S’identifier')]").click()
time.sleep(2)

def myFunction(Ingénieur, filiere):
    driver.get('https://www.linkedin.com/school/institut-national-des-postes-et-telecommunications/people/')
    time.sleep(3)
    search_but = driver.find_element_by_id("people-search-keywords")
    search_but.click()
    search_but.send_keys(filiere)
    search_but.send_keys(Keys.ENTER)
    start_year = driver.find_element_by_xpath("//input[@id='people-search-year-start']")
    start_year.send_keys('2018')
    start_year.send_keys(Keys.ENTER)

    end_year = driver.find_element_by_xpath("//input[@id='people-search-year-end']")
    end_year.send_keys('2021')
    end_year.send_keys(Keys.ENTER)
    time.sleep(4)
    
    Ingénieur =[]
    for i in range(1,35):
        laureat = driver.find_element_by_xpath("//body[1]/div[6]/div[3]/div[1]/div[2]/div[1]/div[2]/main[1]/div[2]/div[1]/div[2]/div[1]/div[1]/ul[1]/li["+str(i)+"]/section[1]/div[1]/div[1]/div[2]/div[1]/a[1]").get_attribute('href')
        Ingénieur.append(laureat)
        
    Ingénieur
    
    careers = []
    entreprises = []
    for laureat in Ingénieur:
        career = ""
        driver.get(laureat)
        time.sleep(2)
        try:
            elem = driver.find_element_by_xpath("//body[1]/div[6]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/main[1]/section[1]/div[2]/div[2]/div[1]")

            career = elem.find_element_by_class_name("text-body-medium").text
        except Exception as e:
            elem = driver.find_element_by_xpath("//body[1]/div[5]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/main[1]/section[1]/div[2]/div[2]/div[1]")
            career = elem.find_element_by_class_name("text-body-medium").text
        careers.append(career)
        
    careers
    
    for laureat in Ingénieur:
        entreprise = ""
        driver.get(laureat)
        time.sleep(4)
        try:
            entreprise = driver.find_element_by_xpath("//body[1]/div[6]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/main[1]/section[1]/div[2]/div[2]/div[2]/span[1]").text
        except Exception as e:
            print(e)
        entreprises.append(entreprise)
    
    
    entreprises
    
    with open(Ingénieur, 'w', encoding="utf-8") as file:
        file.write("laureat_amoa; entreprises\n")

    for i in range(34) :
        with open(Ingénieur, 'a', encoding="utf-8") as file:
            file.write(careers[i]+ " , "+entreprises[i]+"\n")
            
            
            