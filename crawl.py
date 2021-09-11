from selenium import webdriver
from time import sleep
import tqdm

chrome_options = webdriver.chrome.options.Options()
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument('--disable-extensions')
chrome_options.add_argument("--disable-notifications");
chrome = webdriver.Chrome(executable_path='./chromedriver', options=chrome_options)
chrome.delete_all_cookies()

chrome.get("https://www.yangming.com/e-service/track_trace/track_trace_cargo_tracking.aspx")
sleep(2)
chrome.execute_script("window.scrollTo(0, document.body.scrollHeight);")
captcha_element = chrome.find_element_by_id('ContentPlaceHolder1_image_CAPTCHA')

CURRENT = 0

for i in tqdm.tqdm(range(10)): 
    # if i % 5 == 0:
    #     chrome.refresh()
    #     sleep(1)
    #     chrome.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #     captcha_element = chrome.find_element_by_id('ContentPlaceHolder1_image_CAPTCHA')
    captcha_element.click()
    sleep(0.1)
    captcha_element.screenshot("./data/test{0}.jpg".format(i+CURRENT))
    
chrome.close()