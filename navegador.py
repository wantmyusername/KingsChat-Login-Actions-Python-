from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC  
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import Select 
from selenium.common.exceptions import NoSuchElementException  
import time
import urllib
import csv
import random

def Configurar():
    
    profile = webdriver.FirefoxProfile()
    profile.set_preference("permissions.default.image", 2)
    return webdriver.Firefox(firefox_profile=profile)


f = open('Names.csv')
archiveC = "Comentarios.txt"
oLike = "OFF"     # ON or OFF
oShare = "OFF"    # ON or OFF
oComment = "OFF"  # ON or OFF


lines = csv.reader(f)
driver = Configurar()
for line in lines:
    post = random.choice(list(open("Post.txt")))
    status  = random.choice(list(open("Status.txt")))
    try:
            driver.get("https://web.kingsch.at/")
            element = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "login"))
                )
            driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/div/form/div[2]/input').send_keys(line[0])
    	    driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/div/form/div[3]/div/input').send_keys(line[1])
            Login = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/div/form/div[4]/div/button')
    	    Login.click()
    	    element = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div[2]/div/div[2]/div[1]/div/div[2]/div/div'))
                )
            driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div[2]/div/div[1]/div/div/div[1]/textarea').send_keys(status)
            Postear = driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div[2]/div/div[1]/div/div/div[2]/div[2]/div')
            Postear.click()
            time.sleep(2)
    	    driver.get(post)
            element = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="q-app"]/div/div[2]/div/div[1]/div/div[4]/div[2]/i'))
                )
            if oShare == "ON":
                element = driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div[1]/div/div[4]/div[2]/i')
                driver.execute_script("arguments[0].click();", element)
                element = WebDriverWait(driver, 20).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="q-app"]/div/div[2]/div/div[1]/div/div[4]/div[3]/div[1]'))
                    )
                element = driver.find_element_by_xpath('//*[@id="q-app"]/div/div[2]/div/div[1]/div/div[4]/div[3]/div[1]')
                driver.execute_script("arguments[0].click();", element)
            if oLike == "ON":
                Like = driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div[1]/div/div[4]/div[1]/i')
                Like.click()
            time.sleep(1)
            if oComment == "ON":    
                driver.find_element_by_xpath(' /html/body/div/div/div[2]/div/div[2]/div/div[1]/textarea').send_keys(random.choice(list(open(archiveC))))
                Enviar = driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div[2]/div/div[2]/div')
                Enviar.click()
            time.sleep(1)
            driver.delete_all_cookies()
    except Exception as e :
            driver.delete_all_cookies()
            print e
            driver = Configurar()
