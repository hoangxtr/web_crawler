from selenium import webdriver
from time import sleep

def login_fb(chrome):
    chrome.get("http://facebook.com")
    email = chrome.find_element_by_id("email")
    password = chrome.find_element_by_id('pass')

    email.send_keys("hcmut232k@gmail.com")
    password.send_keys("hoangpr023\n")

chrome_options = webdriver.chrome.options.Options()
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument('--disable-extensions')
chrome_options.add_argument("--disable-notifications");
chrome = webdriver.Chrome(executable_path='./chromedriver', options=chrome_options)

login_fb(chrome)
sleep(1)
chrome.get("https://www.facebook.com/groups/anuongdulich/permalink/2317578395038764/?__cft__[0]=AZXt-vnJ9-KoMnVcMVZY-ANXolQFUturkUhwVwXcH-fEFTTMltgsTm_kNJxTyOAkeKcBGP86TIx3ZsfXH0cOaoY08YW7dd3fWq5kN8nga2wu9jxpzuMhk2V4BD_6Ob4SJjI-PiC0nMZ962wdIeuj0L37cYag8_Fz2OJZ2cNVqTbGk8Nn7yAcBQtYksT4nD-wMFs&__tn__=%2CO%2CP-R")
sleep(4)

btn_comment_mode = chrome.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[4]/div/div/div/div/div/div/div[1]/div/div/div/div/div/div/div/div/div/div/div[2]/div/div[4]/div/div/div[2]/div[2]/div/div/span")
btn_comment_mode.click()
sleep(1)

btn_all_comment = chrome.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[2]/div/div/div[1]/div[1]/div/div/div[1]/div/div[1]/div/div[3]")
btn_all_comment.click()


sleep(5)
chrome.close()