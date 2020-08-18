# PREREQUISITIES : webdriver for chrome / geckodriver for firefox (included in $PATH/PATH)
#                  GIT bash shell, properly set up with username and email
# In order for the login credentials not to be stored in the code itself, the creds are kept in:
# /path/to/script/py_user_pass.txt

# TODO : add support for spaces in the folder name (not tested = not supported for now)
# TODO : abort if folder already exists (in the bash script)

import sys
import os
from selenium import webdriver
from time import sleep

# reading login credentials, creating a local repo

credentials = open("../py_user_pass.txt", "r")
username = credentials.readline()
password = credentials.readline()
credentials.close()


# logging in (automated 'version' of the web browser will never leave a user logged in)

browser = webdriver.Firefox() # replace for your own browser...
browser.get('http://github.com/login')

button = browser.find_elements_by_xpath("//*[@id='login_field']")[0]
button.send_keys(username)
button = browser.find_elements_by_xpath("//*[@id='password']")[0]
button.send_keys(password)
button = browser.find_elements_by_xpath("//*[@id='password']")[0]
button = browser.find_elements_by_xpath("/html/body/div[3]/main/div/form/div[4]/input[9]")[0]
button.click()

# creating the repo

browser.get('http://github.com/new')
button = browser.find_elements_by_xpath("//*[@id='repository_name']")[0]
button.send_keys(str(sys.argv[1]))
button = browser.find_elements_by_xpath("//*[@id='repository_description']")[0]
button.send_keys("THIS IS AN AUTOMATED DESCRIPTION...")
button = browser.find_elements_by_xpath("/html/body/div[4]/main/div/form/div[4]/button")[0]
# wait for the 'create' button to unfreeze (TODO : loop while frozen)
sleep(2)
button.click()

# launching VSCode in the current working directory (OPTIONAL)
# browser.quit() # OPTIONAL
os.system('code .')




