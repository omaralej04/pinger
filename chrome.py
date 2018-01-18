# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support import ui
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time
from selenium.common.exceptions import NoSuchElementException
from notification import send_message
from datetime import datetime

print "[",datetime.now().strftime("%I:%M:%S %p"),"]","Iniciando!!!"

#insert path to chromedriver.exe
driver = webdriver.Chrome('C:\Users\chromedriver.exe')

def page_is_loaded(driver):
    return driver.find_element_by_tag_name("body") != None

def login_page():
    print "[",datetime.now().strftime("%I:%M:%S %p"),"]","Accesando Pagina"
    driver.get("https://tramites.saime.gob.ve/index.php?r=site/login")
    wait = ui.WebDriverWait(driver, 10)
    wait.until(page_is_loaded)
    print "[",datetime.now().strftime("%I:%M:%S %p"),"]","llenando LoginForm_username"
    email_field = driver.find_element_by_id("LoginForm_username")

    #insert your username in the page
    email_field.send_keys("user@user.user")
    print "[",datetime.now().strftime("%I:%M:%S %p"),"]","llenando LoginForm_password"
    password_field = driver.find_element_by_id("LoginForm_password")
    
    #insert password in the page
    password_field.send_keys("password")
    print "[",datetime.now().strftime("%I:%M:%S %p"),"]","Enter Key"
    password_field.send_keys(Keys.RETURN)

def travel():
    wait = ui.WebDriverWait(driver, 10)
    wait.until(page_is_loaded)

    # Hover mechanics
    element_to_hover_over = driver.find_element_by_class_name("menu_pasaporte")
    hover = ActionChains(driver).move_to_element(element_to_hover_over)
    print "[",datetime.now().strftime("%I:%M:%S %p"),"]","Hovering en menu_pasaporte"
    hover.perform()

    link_field = driver.find_element_by_xpath('//*[@id="yw0"]/li[3]/ul/li[2]/a')
    time.sleep(2)
    print "[",datetime.now().strftime("%I:%M:%S %p"),"]","Click en link_field"
    link_field.click()

def check_availability():
    element_to_hover_over = driver.find_element_by_xpath("//*[@id='pago-form']/input[5]")
    hover = ActionChains(driver).move_to_element(element_to_hover_over)
    print "[",datetime.now().strftime("%I:%M:%S %p"),"]","Hovering en Formulario"
    hover.perform()
    agilizar_field = element_to_hover_over
    time.sleep(2)
    print "[",datetime.now().strftime("%I:%M:%S %p"),"]","Click en Formulario"
    agilizar_field.click()

def check_exists_by_xpath(xpath):
    try:
        print "[",datetime.now().strftime("%I:%M:%S %p"),"]","Revisando si se encuentra el mensaje de error"
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        print "[",datetime.now().strftime("%I:%M:%S %p"),"]","No Aparece el mensaje de error"
        return True
    print "[",datetime.now().strftime("%I:%M:%S %p"),"]","Aparece el mensaje de error"
    return False

def loop():
    check_availability()
    time.sleep(2)
    if check_exists_by_xpath('//*[@id="yw0"]/div'):
        print "[",datetime.now().strftime("%I:%M:%S %p"),"]","No se ha encontrado el mensaje"
        send_message(True)
        time.sleep(600)
        loop()
    else:
        print "[",datetime.now().strftime("%I:%M:%S %p"),"]","Se ha encontrado el mensaje"
        send_message(False)
        time.sleep(600)
        loop()

def initialize():
    print "[",datetime.now().strftime("%I:%M:%S %p"),"]","Loggin' in"
    login_page()
    print "[",datetime.now().strftime("%I:%M:%S %p"),"]","Travelin' to Hanamura"
    travel()
    time.sleep(2)
    print "[",datetime.now().strftime("%I:%M:%S %p"),"]","Amigo quedan arepas?"
    check_availability()
    time.sleep(2)
    if check_exists_by_xpath('//*[@id="yw0"]/div'):
        print "[",datetime.now().strftime("%I:%M:%S %p"),"]","No se ha encontrado el mensaje"
        send_message(True)
        time.sleep(600)
        loop()
    else:
        print "[",datetime.now().strftime("%I:%M:%S %p"),"]","Se ha encontrado el mensaje"
        send_message(False)
        time.sleep(600)
        loop()

initialize()
