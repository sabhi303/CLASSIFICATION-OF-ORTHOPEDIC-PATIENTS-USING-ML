import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
class TestcaseDemo(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		print("setting up data")
		global driver

		chromedriver = "C:/Users/Abhijeet/Desktop/miniproj/chromedriver.exe"
		driver = webdriver.Chrome(chromedriver)
		driver.get("http://127.0.0.1:8000/")
		driver.maximize_window()
	def test_1loginValid(self):
		print("Testing  Valid login in execution")
		driver.find_element_by_name('userid').send_keys('dsa@a.c')
		driver.find_element_by_name('password').send_keys('pass')
		signbutton = driver.find_element_by_name('signbut')
		time.sleep(6)
		signbutton.click()

	def test_2logout(self):
		print("Testing logout ")
		time.sleep(6)

		link=driver.find_element_by_partial_link_text('LOGOUT')
		link.click()
	
	def test_3loginInvalid(self):
		time.sleep(10)
		
		print("Testing InValid login in execution")
		driver.find_element_by_name('userid').send_keys('abc@a.c')
		driver.find_element_by_name('password').send_keys('abc')
		signbutton = driver.find_element_by_name('signbut')
		signbutton.click()
		time.sleep(10)

	def test_4loginValid(self):
		print("Testing Valid login in execution")
		driver.find_element_by_name('userid').send_keys('dsa@a.c')
		driver.find_element_by_name('password').send_keys('pass')
		signbutton = driver.find_element_by_name('signbut')
		signbutton.click()
		time.sleep(10)

	def test_5knnresult(self):
		print("Checking KNN Result")
		time.sleep(10)

		driver.find_element_by_name('pelinc').send_keys('10')
		driver.find_element_by_name('pelti').send_keys('10')
		driver.find_element_by_name('lumlor').send_keys('10')
		driver.find_element_by_name('sacral').send_keys('10')
		driver.find_element_by_name('pelrad').send_keys('10')
		driver.find_element_by_name('degree').send_keys('10')
		knn = driver.find_element_by_name('knn')
		time.sleep(6)
		knn.click()
		time.sleep(10)

	def test_6naiveresult(self):
		print("Checking Naive Bayes Result")
		# driver.find_element_by_name('pelinc').send_keys('10')
		# driver.find_element_by_name('pelti').send_keys('10')
		# driver.find_element_by_name('lumlor').send_keys('10')
		# driver.find_element_by_name('sacral').send_keys('10')
		# driver.find_element_by_name('pelrad').send_keys('10')
		# driver.find_element_by_name('degree').send_keys('10')
		naive = driver.find_element_by_name('naive')
		time.sleep(5)
		naive.click()
		time.sleep(10)
	

	def test_7logout(self):
		print("Testing logout ")
		link=driver.find_element_by_partial_link_text('LOGOUT')
		link.click()
		
	@classmethod
	def tearDownClass(cls):
		print("tearDown execution")
		time.sleep(10)
		driver.quit()


unittest.main()