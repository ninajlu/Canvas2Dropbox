from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
import sys

def download(address):
	#print 'Number of arguments:', len(sys.argv), 'arguments.'
	#sys.argv.pop(0)
	#print 'Number of arguments:', len(sys.argv), 'arguments.'
	#for arg in sys.argv:

	browser = webdriver.Chrome() # Get local session of firefox
	print address
	browser.get(address) # Load page
	#assert "Yahoo!" in browser.title
	#elem = browser.find_element_by_name("p") # Find the query box
	#elem.send_keys("seleniumhq" + Keys.RETURN)
	time.sleep(5) # Let the page load, will be added to the API
	#try:
	 #   browser.find_element_by_xpath("//a[contains(@href,'http://seleniumhq.org')]")
	#except NoSuchElementException:
	#    assert 0, "can't find seleniumhq"
	browser.close()