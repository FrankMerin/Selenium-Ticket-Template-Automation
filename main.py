# chrome.exe must be set as a path varible 

# launch chrome from CMD with: chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\selenum\ChromeProfile"
# if you run without a path, it will use your normal cache and browser info
# however if you intend to keep more than 1 chrome browser running, a path will be nesassary
# this assumes you will manually sign in prior to using the script


from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait




chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
# Change chrome driver path accordingly
chrome_driver = "C:\\Users\\user\\Downloads\\chromedriver_win32\\chromedriver.exe" 
driver = webdriver.Chrome(chrome_driver, options=chrome_options)


def createTicket():
    driver.execute_script("window.open('https://ipcenter.ipsoft.com/IPradar/open.htm?client=ipsoft','new window')") # modify for specific client
    driver.switch_to_window(driver.window_handles[-1])
    # Queue
    ipimQueue = Select(driver.find_element_by_id('ipimQueue'))
    ipimQueue.select_by_visible_text('IPsoft-helpdesk')
    # Delete Requestor default
    newRequestor = WebDriverWait (driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="newRequestor"]')))
    newRequestor.clear()
    # Subject (sample text)
    description = driver.find_element_by_xpath('//*[@id="description"]')
    description.send_keys('Password Reset')
    # Status
    status = Select(driver.find_element_by_xpath('//*[@id="status"]'))
    status.select_by_visible_text('Resolved')
    # Body (sample text)
    post = driver.find_element_by_xpath('//*[@id="post"]')
    post.send_keys(
        """Hello,
Thank you for calling the helpdesk.

You've called for assistance with:
Password Reset

Next steps and resolution:
Resolved

We were happy to assist you today. Please do not hesitate to contact us at 123-456-7890 if you have any further questions or concerns.

--
Best,

Frank Merin
""")





createTicket()