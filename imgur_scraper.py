import sys, os
import time
import urllib
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

address_input = raw_input("Address: ")
chromedriver_location = './assets/chromedriver'
driver = webdriver.Chrome(chromedriver_location)
driver.get(address_input)

try:
  driver.find_element_by_class_name("js-post-truncated").click()
except NoSuchElementException:
  print('All images loaded')

try:
  post_image_elements = []
  image_address_hash = {}
  last_element_id = ""
  
  #imgur wont load all images when you load the page just the ~5 closest to your viewing area
  #we scroll to the last one repeatedly to keep the images loading
  while True: #python doesnt have a do..while loop?
    post_image_elements = driver.find_elements_by_class_name("post-image-container")

    for element in post_image_elements:
      image_id = element.get_attribute("id")
      image_source = element.find_element_by_css_selector("img").get_attribute("src")
      if image_address_hash.has_key(image_id):
        pass
        #print('image id {} already saved'.format(image_id))
      else:
        image_address_hash[image_id] = image_source
        print('[{}] -> {}'.format(image_id, image_source))
        #download image
        urllib.urlretrieve(image_source, "./images/" + image_source.split('/')[-1])
        

    last_element = post_image_elements[-1]
    new_last_element_id = last_element.get_attribute("id")

    print('Moving to post-image with id: {}'.format(last_element_id))
    driver.execute_script("arguments[0].scrollIntoView();", last_element)
    time.sleep(0.5)

    if new_last_element_id == last_element_id:
      print('End of list!')
      print('{} images found'.format(len(image_address_hash)))
      break
    else:
      last_element_id = new_last_element_id

except NoSuchElementException:
  print('Images not found')
