import sys, os
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.action_chains import ActionChains

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
browser = webdriver.Chrome(chromedriver_location)#, chrome_options=chrome_options)
#browser.implicitly_wait(page_delay)

browser.get(address_input)

#if .js-post-truncated present?
  #load all

try:
  browser.find_element_by_class_name("js-post-truncated").click()
except NoSuchElementException:
  print('All images loaded')

try:
  post_image_elements = []
  post_image_elements = browser.find_elements_by_class_name("post-image-container")
  actions = ActionChains(browser)

  print('Found {}'.format(len(post_image_elements.length))

  for element in post_image_elements:
    print('Moving to post-image with id: {}'.format(element.getAttribute("id")))
    actions.move_to_element(element).perform()

except NoSuchElementException:
  print('Images not found')