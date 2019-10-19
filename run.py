from selenium import webdriver
from selenium.webdriver.support import expected_conditions as e_co
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import glob
import platform
from tools import login, spam
from cli import spam_info, login_info

# SEARCHING FOR USER-DATA-DIR
files = glob.glob("./User_Data")

if "./User_Data" not in files:
    print("\033[91m {}\033[00m" .format("Whoops! User_Data directory not found :( \n Enter login data!"))
    login_inf = login_info()
else:
    pass
print("\033[91m {}\033[00m" .format('Enter spam details!'))
# USER INPUTS
spam_r = spam_info()
# DRIVER CONFIGS AND DECLARATIONS
if platform.system().lower() == 'linux':
    options = webdriver.ChromeOptions()
    options.add_argument('--user-data-dir=./User_Data')
    options.add_argument("--disable-notifications")
    driver = webdriver.Chrome('chromedriver', options=options)
    wait = WebDriverWait(driver, 40)

if "./User_Data" not in files:

    # login_inf = login_info()
    login(driver, wait, e_co, By, username=login_inf['username'], password=login_inf['password'])
else:
    pass
spam(driver, wait, e_co, By, count=spam_r['count'], inp=spam_r['contact'], msg=spam_r['msg'])