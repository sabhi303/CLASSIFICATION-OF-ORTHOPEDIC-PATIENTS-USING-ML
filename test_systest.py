
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
from os import system, name

def clear(): 
    if name == 'nt': 
        _ = system('cls')

class TestSystest():
  passed = 0
  def setup_method(self):
    chromedriver = "C:/Users/Abhijeet/Desktop/miniproj/chromedriver.exe"
    self.driver = webdriver.Chrome(chromedriver)
    # self.vars = {}
  
  def teardown_method(self):
    self.driver.quit()
  
  def test_systest(self):
    self.driver.get("http://127.0.0.1:8000/")
    self.driver.set_window_size(1552, 880)

    clear()
    print("\n")
    print("*"*34)
    print("*"*7," SELENIUM TESTING ","*"*7 )
    print("*"*34,"\n\n")

    #login credentials.. 
    try:
      print("TESTING LOGIN ...",end="\t")
      
      self.driver.find_element(By.ID, "username").click()
      self.driver.find_element(By.ID, "username").send_keys("s@v.c")
      time.sleep(1)
      self.driver.find_element(By.ID, "password").click()
      self.driver.find_element(By.ID, "password").send_keys("sam")
      time.sleep(1)
      self.driver.find_element(By.NAME, "signbut").click()
      time.sleep(2)

      print("Ok!\n\n")
      self.passed += 1
    except:
      print("Failed!\n\n")
      

    try:
      print("TESTING LOGOUT ...",end="\t")

      self.driver.find_element(By.LINK_TEXT, "LOGOUT").click()
      time.sleep(1)

      print("Ok!\n\n")
      self.passed += 1
    except:
      print("Failed!\n\n")
    

    try:
      print("LOGGING AGAIN...",end="\t")

      self.driver.find_element(By.ID, "username").click()
      self.driver.find_element(By.ID, "username").send_keys("s@v.c")
      time.sleep(1)
      self.driver.find_element(By.ID, "password").click()
      self.driver.find_element(By.ID, "password").send_keys("sam")
      time.sleep(1)
      self.driver.find_element(By.NAME, "signbut").click()
      time.sleep(2)

      print("Ok!\n\n")
      self.passed += 1
    except:
      print("Failed!\n\n")


    try: 
      print("INSERTING VALUES[1]...",end="\t")
      
      self.driver.find_element(By.ID, "pelinc").click()
      self.driver.find_element(By.ID, "pelinc").send_keys("30")
      time.sleep(1)
      self.driver.find_element(By.ID, "pelti").send_keys("10")
      time.sleep(1)
      self.driver.find_element(By.ID, "lumlor").send_keys("10")
      time.sleep(1)
      self.driver.find_element(By.ID, "sacral").send_keys("15")
      time.sleep(1)
      self.driver.find_element(By.ID, "pelrad").send_keys("100")
      time.sleep(1)
      self.driver.find_element(By.ID, "degree").send_keys("100")
      time.sleep(2)

      print("Ok!\n\n")
      self.passed += 1
    except:
      print("Failed!\n\n")

    try:
      print("KNN TESTING [1]...",end="\t")

      self.driver.find_element(By.NAME, "knn").click()
      time.sleep(2)
      
      print("Ok!\n\n")
      self.passed += 1
    except:
      print("Failed!\n\n")

    try:
      print("NB TESTING[1]...",end="\t")
      self.driver.find_element(By.NAME, "naive").click()
      time.sleep(2)
      
      print("Ok!\n\n")
      self.passed += 1
    except:
      print("Failed!\n\n")

    try:
      print("RESETTING BODY...",end="\t")
     
      element = self.driver.find_element(By.NAME, "naive")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()
      element = self.driver.find_element(By.CSS_SELECTOR, "body")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()
      time.sleep(1) 

      print("Ok!\n\n")
      self.passed += 1
    except:
      print("Failed!\n\n")
    
    try: 
      print("INSERTING VALUES[2]...",end="\t")

      self.driver.find_element(By.ID, "pelinc").click()
      self.driver.find_element(By.ID, "pelinc").send_keys("33")
      time.sleep(1)
      self.driver.find_element(By.ID, "pelti").send_keys("5")
      self.driver.find_element(By.ID, "lumlor").send_keys("36")
      time.sleep(1)
      self.driver.find_element(By.ID, "sacral").send_keys("21")
      time.sleep(1)
      self.driver.find_element(By.ID, "pelrad").send_keys("127")
      time.sleep(1)
      self.driver.find_element(By.ID, "degree").send_keys("7")
      time.sleep(2)

      print("Ok!\n\n")
      self.passed += 1
    except:
      print("Failed!\n\n")

    try:
      print("KNN TESTING [2]...",end="\t")
      
      self.driver.find_element(By.NAME, "knn").click()
      time.sleep(1)

      print("Ok!\n\n")
      self.passed += 1
    except:
      print("Failed!\n\n")

    try:
      print("RESETTING BODY...",end="\t")

      element = self.driver.find_element(By.NAME, "knn")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()
      element = self.driver.find_element(By.CSS_SELECTOR, "body")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()
      time.sleep(2)

      print("Ok!\n\n")
      self.passed += 1
    except:
      print("Failed!\n\n")

    try:
      print("NB TESTING [2]...",end="\t")
    
      self.driver.find_element(By.NAME, "naive").click()
      time.sleep(1)
    
      print("Ok!\n\n")
      self.passed += 1
    except:
      print("Failed!\n\n")
    
    try:
      print("TESTING LOGOUT ...",end="\t")
      
      self.driver.find_element(By.LINK_TEXT, "LOGOUT").click()
      time.sleep(1)
      
      print("Ok!\n\n")
      self.passed += 1
    except:
      print("Failed!\n\n")
    
    print("\n")
    print("*"*34)
    print(" ",self.passed,"OUT OF 12 TEST CASES PASSED" )
    print("*"*34,"\n\n")
    

  
test = TestSystest()  #object creation

#method calls
test.setup_method()   #setup driver
test.test_systest()   #perform testcases
test.teardown_method()  #quit testing