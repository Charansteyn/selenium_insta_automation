import autoit
import requests
from time import sleep
import urllib
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

mobile_emulation = {
   "deviceMetrics": { "width": 360, "height": 640, "pixelRatio": 3.0 },
   "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19" }
chrome_options = Options()
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
driver = webdriver.Chrome(chrome_options = chrome_options)
main_url = "https://www.instagram.com"
driver.get(main_url)


driver.refresh()

#cross
x = driver.find_element_by_xpath('//*[@id="react-root"]/section/div[2]/div/p[2]/div/button/span').click()
sleep(3)

#login click
button_login = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div/div/div/div[3]/button[1]').click()
sleep(3)

#username and password click

username = "" #Enter your username
password = "" #Enter your passwor
caption = " k8s "
path="" #path of the file.
def login():
    login_button = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]')
    login_button.click()
    sleep(3)
    username_input = driver.find_element_by_xpath("//input[@name='username']")
    username_input.send_keys(username)
    password_input = driver.find_element_by_xpath("//input[@name='password']")
    password_input.send_keys(password)
    password_input.submit()
login()
sleep(4)


not_now = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/button').click()
sleep(5)


cancel = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]').click()
sleep(3)


#second_cancel = driver.find_element_by_xpath('//*[@id="react-root"]/section/div[3]/div/p[2]/div/button/span')
sleep(3)

#working till here

#click share

new_post_btn = driver.find_element_by_xpath("//div[@role='menuitem']").click()
sleep(1.5)
autoit.win_active("Open") 
sleep(2)
autoit.control_send("Open","Edit1",path) 
sleep(1.5)
autoit.control_send("Open","Edit1","{ENTER}")

sleep(2)

next_btn = driver.find_element_by_xpath("//button[contains(text(),'Next')]").click()

sleep(3)

caption_field = driver.find_element_by_xpath('//*[@id="react-root"]/section/div[2]/section[1]/div[1]/textarea')
caption_field.send_keys(caption)

share_btn = driver.find_element_by_xpath("//button[contains(text(),'Share')]").click()

sleep(25)
