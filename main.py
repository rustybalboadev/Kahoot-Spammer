from selenium import webdriver
from selenium.common.exceptions import TimeoutException, UnexpectedAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from uuid import uuid4
import time
import random

game_code = input("what is the game code? ")
numB = int(input("How many bots do you want? "))
nameB = input("What name do you want the bots to have? ")
time_in_game = int(input("How long do you want the bots to be in the game? (Use minutes) "))
time_in_seconds = (time_in_game*60)
times = 0
co = Options()
co.add_argument("--headless")
co.add_argument("test-type")
co.add_argument("--js-flags=--expose-gc")
co.add_argument("--enable-precise-memory-info")
co.add_argument("--disable-default-apps")
driver = webdriver.Chrome(options=co)
tab = 0
amount = 0
def get_name(nameB):
    split_uuid = str(uuid4()).split('-')
    name = nameB
    return str(name + split_uuid[0])
def add_bot():
    global amount, numB, element, tab
    wait = WebDriverWait(driver, 10)
    name = get_name(nameB)
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[tab])
    driver.get("https://kahoot.it")
    driver.execute_script("window.alert = function() {};")
    element = wait.until(EC.element_to_be_clickable((By.ID, 'game-input')))
    inputGID = driver.find_element_by_id("game-input")
    inputGID.send_keys(game_code)
    inputGID.submit()
    element = wait.until(EC.element_to_be_clickable((By.ID, 'nickname')))
    inputNID = driver.find_element_by_id("nickname")
    inputNID.send_keys(name)
    inputNID.submit()
    time.sleep(1)
    amount += 1
    tab += 1
    print("Added bot {}".format(name))

while amount < numB:
    try:
        add_bot()
    except TimeoutException:
        add_bot()
while times < time_in_seconds:
    time.sleep(1)
    times += 1
    print("it's been {} seconds".format(times))
driver.quit()