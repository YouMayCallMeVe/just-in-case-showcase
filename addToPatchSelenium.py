from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
import time
import pyautogui
import os
import sys
import googleExport

def waitForLoadId(itemId, driver):
  DELAY = 60
  try:
      myElem = WebDriverWait(driver, DELAY).until(EC.presence_of_element_located((By.ID, itemId)))
      print("Page is ready!")
  except TimeoutException:
      print("Loading took too much time!")
      sys.exit(1)
      
def waitForLoadXPATH(path, driver):
  DELAY = 60
  try:
      myElem = WebDriverWait(driver, DELAY).until(EC.presence_of_element_located((By.XPATH, path)))
      print("Page is ready!")
  except TimeoutException:
      print("Loading took too much time!")
      sys.exit(1)
      
def waitForLoadClass(path, driver):
  DELAY = 60
  try:
      myElem = WebDriverWait(driver, DELAY).until(EC.presence_of_element_located((By.CLASS_NAME, path)))
      print("Page is ready!")
  except TimeoutException:
      print("Loading took too much time!")
      sys.exit(1)
      
def waitForLoadXPATHHidden(path, x, driver):
  DELAY = 10
  if x > DELAY:
    sys.exit(1)
  DELAY = DELAY # seconds
  try:
      myElem = WebDriverWait(driver, DELAY).until(EC.presence_of_element_located((By.XPATH, path)))
      time.sleep(2)
      waitForLoadXPATHHidden(path, x+1, driver)
  except TimeoutException:
      print("The item is gone now")

#print(googleExport.getValues())
def run(items):
  driver = webdriver.Chrome("chromedriver.exe")
  driver.get('https://mcriss-cdsdev.appiancloud.com/suite/design/lQBY7b8XyEG3sHPiDxlu8ZrV8LENAU_SQ5oJCUwg_freLRs2IulV4fLo--rXPlSQnPvVn5G5ay5rLhFVaH_juNa3rlpvXP4eG-1dzZZJpGoHs2L5LQ')
  username = driver.find_element_by_id('un')
  username.send_keys("bdumont@chenega.com")
  password = driver.find_element_by_id('pw')
  password.send_keys("BSwimmer15!!")
  submit = driver.find_element_by_xpath('//input[@type="submit" and @value="Sign In"]')
  submit.click()
  waitForLoadId('a23ae63c8846e3f0f41f8a50e77f07b8', driver)

  # for each user story 
  # for each item in user story
  for item in items:
    searchBox = driver.find_element_by_id('a23ae63c8846e3f0f41f8a50e77f07b8')
    searchBox.send_keys(item)
    # SEARCH BUTTON
    search = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div/div/div[1]/div/div/div[1]/div[2]/div/div/button')
    search.click()
    # SELECT ALL CHECKBOX
    waitForLoadXPATH('//*[contains(text(), "Search results for ")]', driver)
    waitForLoadXPATH('/html/body/div[1]/div[1]/div/div/div/div/div[3]/div/div/div[3]/div[2]/div/div[1]/table/thead/tr/th[1]/div/div/div/label', driver)
    select = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div/div/div[3]/div/div/div[3]/div[2]/div/div[1]/table/thead/tr/th[1]')
    select.click()
    # ADD TO PATCH
    waitForLoadXPATH('//*[contains(text(), "Add to Patch")]', driver)
    addToPatch = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div/div/div[3]/div/div/div[1]/div/div[2]/div/div[1]/div/div[3]/button')
    addToPatch.click()
    # CHECK FOR ADD TO PATCH TO VANISH
    waitForLoadXPATHHidden('//*[contains(text(), "Add to Patch")]', 0, driver)
    searchBox = driver.find_element_by_id('a23ae63c8846e3f0f41f8a50e77f07b8')
    searchBox.clear()
    waitForLoadXPATHHidden('//*[contains(text(), "Search results for ")]', 0, driver)
  # EXPORT PATCH
  waitForLoadXPATH('//*[contains(text(), "Export Patch")]', driver)
  export = driver.find_element_by_xpath('//*[contains(text(), "Export Patch")]')
  export.click()
  waitForLoadXPATH('//*[contains(text(), "Clear Patch Contents")]', driver)
  export = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div[3]/div/div/div[2]/div/div/button')
  export.click()
  waitForLoadXPATH('//*[contains(text(), "Download package")]', driver)
  export = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div[2]/div/div[2]/div/div/div/div/div/div/div[1]/div[2]/div/p/a')
  export.click()
  time.sleep(15)


  

  