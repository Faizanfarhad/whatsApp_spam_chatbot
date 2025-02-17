from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time,random

def open_whatsApp():
    options = webdriver.ChromeOptions()
    options.add_argument('--user-data-dir=./chrome-data')
    driver = webdriver.Chrome(options=options)
    driver.get('https://web.whatsapp.com/')
    input("Scan the QR code : ")
    return driver
def send_messgae(driver,contact_number,message):
    try:
        search_box = driver.find_element(By.XPATH, "//div[@contenteditable='true']")
        search_box.send_keys(contact_number)
        search_box.send_keys(Keys.ENTER)
        time.sleep(2)
        
        message_box = driver.find_element(By.XPATH, "//div[@contenteditable='true' and @data-tab='10']")
        message_box.send_keys(message)
        message_box.send_keys(Keys.ENTER)
        print(f'Message sended to : {contact_number}')
    except Exception  as e:
        print("Error : ",e)
if __name__ == '__main__':
    driver = open_whatsApp()
    
    contact_number = input("Enter your contact number : ")
    message = input("Enter your message (q to quit)  : ")
    while True:
        if message == 'q':
            driver.quit()
            break
        send_messgae(driver,contact_number,message)
        time.sleep(30)