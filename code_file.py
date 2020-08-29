from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
#from personal import user_info
import time

def login(driver):
    username = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
    username.send_keys(user_info.user)
    password = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
    password.send_keys(user_info.psw)
    login_button = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div')
    login_button.click()
    time.sleep(3)

def account_page(driver):
    not_now = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
    not_now.click()
    time.sleep(3)
    notifications = driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
    notifications.click()
    print('Account Page Open Successful!')
    time.sleep(2)

def message_profile(driver):
    account_search = input('')
    send_message_link = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[2]/a')
    send_message_link.click()
    time.sleep(2)
    message_button = driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div/button')
    message_button.click()
    time.sleep(1)
    find_person = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div[1]/div/div[2]/input')
    find_person.send_keys(account_search)
    time.sleep(2)
    click_person = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div[2]/div[1]/div/div[3]/button')
    click_person.click()
    time.sleep(2)
    next_link = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[1]/div/div[2]/div/button')
    next_link.click()
    time.sleep(2)
    message_box = driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
    user_input = input('')
    message_box.send_keys(user_input+Keys.ENTER)
    print("Message Sent Successfully!")

def add_people(driver, person_of_interest):
    find_person = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
    find_person.send_keys(person_of_interest)
    time.sleep(2)
    click_person = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div[2]/div/a[1]/div')
    click_person.click()
    time.sleep(5)
    follow_person = driver.find_element_by_xpath('//button[text()="Follow"]')
    follow_person.click()
    time.sleep(2)

def comment_posts(driver):
    find_account = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/section/div/div[3]/div/article[1]/header/div[2]/div[1]/div/span/a')
    time.sleep(1)
    find_account.click()
    time.sleep(2)
    first_post = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[3]/article/div[1]/div/div[1]/div[1]')
    time.sleep(1)
    first_post.click()
    time.sleep(2)
    now_comment = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/textarea')
    time.sleep(1)
    now_comment.click()
    entry = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div[1]/form/textarea')
    entry.send_keys("RIP Boseman <3" + Keys.ENTER)
    print("Comment Posted Succesfully!")

def main():
    path = "/Users/jon/chromedriver" #find local path for chromedriver 
    driver = webdriver.Chrome(path)

    driver.get("https://www.instagram.com/")
    time.sleep(3)

    print(driver.title)
    print("Running Login...")
    login(driver)

    print('Opening account page...')
    account_page(driver)

    print("Finding account...")
    #message_profile(driver) 

    comment_posts(driver)

    time.sleep(100)
    driver.close()

main()

