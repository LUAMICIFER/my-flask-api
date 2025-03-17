# import os
# import time
# import pickle
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains
# import requests
# from bs4 import BeautifulSoup
# os.environ['PATH'] += r"/home/advik/python/selenium/chromedriver_linux64 (1)"
# driver = webdriver.Firefox()
# driver.get("https://internshala.com/jobs")
# driver.maximize_window()
# time.sleep(2)
# driver.find_element(By.ID,'close_popup').click()
# logintoggle = driver.find_element(By.XPATH,"/html/body/div[1]/div[19]/div/nav/div[3]/ul/li[4]/a").click()
# login = driver.find_element(By.ID,'header_login_modal_button').click()
# # login = driver.find_element(By.CLASS_NAME,'login-cta').click()
# email = driver.find_element(By.ID,'modal_email').send_keys("music.addict3052@gmail.com")
# password = driver.find_element(By.ID,'modal_password').send_keys("_YzicJ*4hf7bDmU")
# submit = driver.find_element(By.ID,'modal_login_submit').click()
# htm= driver.page_source
# soup = BeautifulSoup(htm,"html.parser")


# last_height = driver.execute_script("return document.body.scrollHeight")

# while True:
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(2)  # Wait for new content to load
    
#     new_height = driver.execute_script("return document.body.scrollHeight")
#     if new_height == last_height:  # Stop if no more content loads
#         break
#     last_height = new_height



# job_title_elements = soup.find_all("a", class_="job-title-href")    
# job_titles = [element.text.strip() for element in job_title_elements]
# print(job_titles)
# print("\n")

# internlinks = []
# for a_tag in soup.find_all("a", class_="job-title-href", href=True):
#     full_link = "https://internshala.com" + a_tag["href"]  # Convert relative URL to absolute
#     internlinks.append(full_link)
# print(internlinks)
# print("\n")

# image_elements = soup.find_all("div", class_="internship_logo") #Changed to div, as that is the tag that holds the image.

# image_links = []
# for element in image_elements:
#     img_tag = element.find("img") #find the img tag inside the div.
#     if img_tag and 'src' in img_tag.attrs: #check to see if the img tag and src attribute exists.
#         image_links.append(img_tag["src"])
# print(image_links)

# # for _ in range(25):  # Adjust range as needed
# #     driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
# #     time.sleep(2)  # Give time for new content to load

# # Now extract all company names
# company_elements = driver.find_elements(By.CLASS_NAME, "company-name")
# company_names = [element.text.strip() for element in company_elements]

# print(company_names)  # Should print all loaded names
# location = driver.find_elements(By.CSS_SELECTOR, ".row-1-item.locations")

# # Extract text from each parent element
# text_list = [element.text.strip() for element in location]
# print(text_list)
import os
import time
import pickle
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

os.environ['PATH'] += r"/home/advik/python/selenium/chromedriver_linux64 (1)"
driver = webdriver.Firefox()
driver.get("https://internshala.com/jobs")
driver.maximize_window()
time.sleep(2)

# Close popup if exists
try:
    driver.find_element(By.ID, 'close_popup').click()
except:
    pass
hover = driver.find_element(By.ID,'select_category_chosen').click()
writer = driver.find_element(By.XPATH,'/html/body/div[1]/div[22]/div[3]/div/div[4]/div[1]/div/div/div/form[1]/div[1]/div/div[1]/ul/li/input').send_keys("android")
time.sleep(1)
choosen = driver.find_element(By.CLASS_NAME,'active-result').click()
# search =driver.find_element(By.CLASS_NAME,"chosen-search-input default")
# search.send_keys("android")
# # Login
# driver.find_element(By.XPATH, "/html/body/div[1]/div[19]/div/nav/div[3]/ul/li[4]/a").click()
# driver.find_element(By.ID, 'header_login_modal_button').click()
# driver.find_element(By.ID, 'modal_email').send_keys("music.addict3052@gmail.com")
# driver.find_element(By.ID, 'modal_password').send_keys("_YzicJ*4hf7bDmU")
# driver.find_element(By.ID, 'modal_login_submit').click()

# # Scroll to load all jobs
# last_height = driver.execute_script("return document.body.scrollHeight")
# while True:
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(2)
#     new_height = driver.execute_script("return document.body.scrollHeight")
#     if new_height == last_height:
#         break
#     last_height = new_height

# # Get the updated HTML after scrolling
# html = driver.page_source
# soup = BeautifulSoup(html, "html.parser")

# # Extract Job Titles
# job_titles = [element.text.strip() for element in soup.find_all("a", class_="job-title-href")]

# # Extract Job Links
# job_links = ["https://internshala.com" + a["href"] for a in soup.find_all("a", class_="job-title-href", href=True)]

# # Extract Image Links
# image_links = []
# for div in soup.find_all("div", class_="internship_logo"):
#     img = div.find("img")
#     image_links.append(img["src"] if img and "src" in img.attrs else None)

# # Extract Company Names
# # company_names = [element.text.strip() for element in driver.find_elements(By.CLASS_NAME, "company-name")]
# company_elements = driver.find_elements(By.CLASS_NAME, "company-name")
# company_names = [element.text.strip() for element in company_elements]

# # print(company_names)  # Should print all loaded names
# # Extract Locations
# # locations = [element.text.strip() for element in driver.find_elements(By.CSS_SELECTOR, ".row-1-item.locations")]
# location = driver.find_elements(By.CSS_SELECTOR, ".row-1-item.locations")

# # Extract text from each parent element
# text_list = [element.text.strip() for element in location]
# # print(text_list)
# locations = text_list
# # Create Array of Objects
# jobs = []
# for i in range(len(job_titles)):  # Use the shortest list length to avoid index errors
#     job = {
#         "title": job_titles[i] if i < len(job_titles) else None,
#         "link": job_links[i] if i < len(job_links) else None,
#         "image_link": image_links[i] if i < len(image_links) else None,
#         "location": locations[i] if i < len(locations) else None,
#         "company_name": company_names[i] if i < len(company_names) else None
#     }
#     jobs.append(job)

# # Print Final Job Objects
# print(jobs)

# # Close browser
# driver.quit()
