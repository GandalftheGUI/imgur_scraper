import sys, os
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.action_chains import ActionChains
import time

address_input = raw_input("Address: ")

chromedriver_location = './assets/chromedriver'
# chrome_options = Options()
# chrome_options.add_argument('--dns-prefetch-disable')
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--lang=en-US')

# chrome_prefs = {
#     'intl.accept_languages': 'en-US'
# }
#chrome_options.add_experimental_option('prefs', chrome_prefs)
driver = webdriver.Chrome(chromedriver_location)#, chrome_options=chrome_options)
#driver.implicitly_wait(page_delay)

driver.get(address_input)

#if .js-post-truncated present?
  #load all

try:
  driver.find_element_by_class_name("js-post-truncated").click()
except NoSuchElementException:
  print('All images loaded')

try:
  post_image_elements = []
  last_element_id = ""

  
  actions = ActionChains(driver)

  
  while True:
    post_image_elements = driver.find_elements_by_class_name("post-image-container")
    last_element = post_image_elements[-1]
    new_last_element_id = last_element.get_attribute("id")

    print('Moving to post-image with id: {}'.format(last_element_id))
    driver.execute_script("arguments[0].scrollIntoView();", last_element)
    time.sleep(2)
    
    if new_last_element_id == last_element_id:
      print('End of list!')
      break
    else:
      last_element_id = new_last_element_id


  #print('Found {}'.format(len(post_image_elements)))
  #for element in post_image_elements:
  #actions.move_to_element(last_element).perform()
  


except NoSuchElementException:
  print('Images not found')