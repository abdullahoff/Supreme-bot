# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.




from selenium import webdriver
from selenium.webdriver.common.keys import  Keys
import time
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)


name = "abdullah theone"
email = "abdullah@live.ca"
tel = "647 745 1234"
address = "14 MONEY st"
zip = "L6Y 4Z7"
city = "brampton"
cardnumber = "314"
CVV = "123"


#driver.get('https://www.supremenewyork.com/shop/shirts/x3b8lmz9v')
driver.get('https://www.supremenewyork.com/shop/jackets/yvus8kftm')
driver.find_element_by_xpath('//*[@id="add-remove-buttons"]/input').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="cart"]/a[2]').click()
driver.find_element_by_xpath('//*[@id="order_billing_name"]').send_keys(name)
driver.find_element_by_xpath('//*[@id="order_email"]').send_keys(email)
driver.find_element_by_xpath('//*[@id="order_tel"]').send_keys(tel)

driver.find_element_by_xpath('//*[@id="bo"]').send_keys(address)
#country
driver.find_element_by_xpath('//*[@id="order_billing_country"]/option[2]').click()
#province
driver.find_element_by_xpath('//*[@id="order_billing_state"]/option[10]').click()

driver.find_element_by_xpath('//*[@id="order_billing_zip"]').send_keys(zip)
driver.find_element_by_xpath('//*[@id="order_billing_city"]').send_keys(city)
driver.find_element_by_xpath('//*[@id="rnsnckrn"]').send_keys(cardnumber)
driver.find_element_by_xpath('//*[@id="orcer"]').send_keys(CVV)

#terms
driver.find_element_by_xpath('//*[@id="cart-cc"]/fieldset/p/label/div/ins').click()

#process payment
driver.find_element_by_xpath('//*[@id="pay"]/input').click()