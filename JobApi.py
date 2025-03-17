import os
import time
import pickle
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import requests
from bs4 import BeautifulSoup
from flask import Flask, request, jsonify
app = Flask(__name__)
@app.route("/index")
def index():
    my_array = ["Android", "Web_Development", "AI", "UI/UX"]
    return jsonify(my_array)

#web development jobs
@app.route("/internshalaWebdevelopmentJobs")
def iwebjobs():
    os.environ['PATH'] += r"/home/advik/python/selenium/chromedriver_linux64 (1)"
    driver = webdriver.Firefox()
    driver.get("https://internshala.com/jobs/web-development-jobs/")
    driver.maximize_window()
    time.sleep(2)
    driver.find_element(By.ID,'close_popup').click()
    htm= driver.page_source
    soup = BeautifulSoup(htm,"html.parser")
    driver.quit()

    internlinks = []
    for a_tag in soup.find_all("a", class_="job-title-href", href=True):
        full_link = "https://internshala.com" + a_tag["href"]  # Convert relative URL to absolute
        internlinks.append(full_link)
    return jsonify(internlinks), 200

@app.route("/internshalaAiJobs")
def iAiJobs():
    os.environ['PATH'] += r"/home/advik/python/selenium/chromedriver_linux64 (1)"
    driver = webdriver.Firefox()
    driver.get("https://internshala.com/jobs/artificial-intelligence-ai-jobs/")
    driver.maximize_window()
    time.sleep(2)
    driver.find_element(By.ID,'close_popup').click()
    htm= driver.page_source
    soup = BeautifulSoup(htm,"html.parser")
    driver.quit()
    internlinks = []
    for a_tag in soup.find_all("a", class_="job-title-href", href=True):
        full_link = "https://internshala.com" + a_tag["href"]  # Convert relative URL to absolute
        internlinks.append(full_link)
    return jsonify(internlinks) , 200

@app.route("/internshala/<user_feild>")
def internshala(user_feild):
    os.environ['PATH'] += r"/home/advik/python/selenium/chromedriver_linux64 (1)"
#     driver = webdriver.Firefox()
    # options = webdriver.ChromeOptions()
    # options.add_argument("--headless")  # Run in headless mode to avoid UI issues
    driver = webdriver.Chrome()
    variable = ""
    if user_feild == "android":
        variable = "android-app-development-jobs/" 
    elif user_feild == "web":
        variable = "web-development-jobs/"
    else:
        variable = ""

    driver.get("https://internshala.com/jobs/"+variable)
    driver.maximize_window()
    time.sleep(2)

    # Close popup if exists
    try:
        driver.find_element(By.ID, 'close_popup').click()
    except:
        pass
    time.sleep(2)
    # hover = driver.find_element(By.ID,'select_category_chosen').click()
    # writer = driver.find_element(By.XPATH,'/html/body/div[1]/div[22]/div[3]/div/div[4]/div[1]/div/div/div/form[1]/div[1]/div/div[1]/ul/li/input').send_keys(user_feild)
    # time.sleep(1)
    # choosen = driver.find_element(By.CLASS_NAME,'active-result').click()
    # Login
    driver.find_element(By.XPATH, "/html/body/div[1]/div[19]/div/nav/div[3]/ul/li[4]/a").click()
    driver.find_element(By.ID, 'header_login_modal_button').click()
    driver.find_element(By.ID, 'modal_email').send_keys("music.addict3052@gmail.com")
    driver.find_element(By.ID, 'modal_password').send_keys("_YzicJ*4hf7bDmU")
    driver.find_element(By.ID, 'modal_login_submit').click()
    time.sleep(2)
    # Scroll to load all jobs
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    # Get the updated HTML after scrolling
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    # Extract Job Titles
    job_titles = [element.text.strip() for element in soup.find_all("a", class_="job-title-href")]

    # Extract Job Links
    job_links = ["https://internshala.com" + a["href"] for a in soup.find_all("a", class_="job-title-href", href=True)]

    # Extract Image Links
    image_links = []
    for div in soup.find_all("div", class_="internship_logo"):
        img = div.find("img")
        image_links.append(img["src"] if img and "src" in img.attrs else None)

    # Extract Company Names
    # company_names = [element.text.strip() for element in driver.find_elements(By.CLASS_NAME, "company-name")]
    company_elements = driver.find_elements(By.CLASS_NAME, "company-name")
    company_names = [element.text.strip() for element in company_elements]

    # print(company_names)  # Should print all loaded names
    # Extract Locations
    # locations = [element.text.strip() for element in driver.find_elements(By.CSS_SELECTOR, ".row-1-item.locations")]
    location = driver.find_elements(By.CSS_SELECTOR, ".row-1-item.locations")

    # Extract text from each parent element
    text_list = [element.text.strip() for element in location]
    # print(text_list)
    locations = text_list
    # Create Array of Objects
    jobs = []
    for i in range(len(job_titles)):  # Use the shortest list length to avoid index errors
        job = {
            "title": job_titles[i] if i < len(job_titles) else None,
            "link": job_links[i] if i < len(job_links) else None,
            "image_link": image_links[i] if i < len(image_links) else None,
            "location": locations[i] if i < len(locations) else None,
            "company_name": company_names[i] if i < len(company_names) else None
        }
        jobs.append(job)

    # Print Final Job Objects
    # print(jobs)
    return jsonify(jobs),200

    # Close browser
    driver.quit()
if __name__ =="__main__":
    app.run(debug=True)
# import os
# import time
# import requests
# from bs4 import BeautifulSoup
# from flask import Flask, jsonify
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# app = Flask(__name__)

# @app.route("/index")
# def index():
#     my_array = ["Android", "Web_Development", "AI", "UI/UX"]
#     return jsonify(my_array)

# @app.route("/internshala/<user_field>")
# def internshala(user_field):
#     # Set up WebDriver
#     # driver_path = "/home/advik/python/selenium/chromedriver_linux64/chromedriver"  # Update correct path
#     os.environ['PATH'] += r"/home/advik/python/selenium/chromedriver_linux64 (1)"
#     options = webdriver.ChromeOptions()
#     options.add_argument("--headless")  # Run in headless mode to avoid UI issues
#     driver = webdriver.Chrome(options=options)

#     try:
#         driver.get("https://internshala.com/jobs")
#         driver.maximize_window()
#         wait = WebDriverWait(driver, 10)

#         # Close popup if exists
#         try:
#             popup = wait.until(EC.element_to_be_clickable((By.ID, "close_popup")))
#             popup.click()
#         except:
#             pass

#         # # Select category
#         # time.sleep(2)
#         # hover = driver.find_element(By.ID,'select_category_chosen').click()
#         # writer = driver.find_element(By.XPATH,'/html/body/div[1]/div[22]/div[3]/div/div[4]/div[1]/div/div/div/form[1]/div[1]/div/div[1]/ul/li/input').send_keys(user_feild)
#         # time.sleep(1)
#         # choosen = driver.find_element(By.CLASS_NAME,'active-result').click()

#         # Login
#         driver.find_element(By.XPATH, "/html/body/div[1]/div[19]/div/nav/div[3]/ul/li[4]/a").click()
#         driver.find_element(By.ID, "header_login_modal_button").click()
#         wait.until(EC.presence_of_element_located((By.ID, "modal_email"))).send_keys("music.addict3052@gmail.com")
#         wait.until(EC.presence_of_element_located((By.ID, "modal_password"))).send_keys("_YzicJ*4hf7bDmU")
#         wait.until(EC.element_to_be_clickable((By.ID, "modal_login_submit"))).click()

#         # Scroll to load all jobs
#         last_height = driver.execute_script("return document.body.scrollHeight")
#         while True:
#             driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#             time.sleep(2)
#             new_height = driver.execute_script("return document.body.scrollHeight")
#             if new_height == last_height:
#                 break
#             last_height = new_height

#         # Get page source for parsing
#         html = driver.page_source
#         soup = BeautifulSoup(html, "html.parser")

#         # Extract data
#         job_titles = [element.text.strip() for element in soup.find_all("a", class_="job-title-href")]
#         job_links = ["https://internshala.com" + a["href"] for a in soup.find_all("a", class_="job-title-href", href=True)]
#         image_links = [img["src"] for img in soup.find_all("img", class_="internship_logo") if "src" in img.attrs]

#         company_elements = driver.find_elements(By.CLASS_NAME, "company-name")
#         company_names = [element.text.strip() for element in company_elements]

#         locations = [element.text.strip() for element in driver.find_elements(By.CSS_SELECTOR, ".row-1-item.locations")]

#         # Combine data into objects
#         jobs = [
#             {
#                 "title": job_titles[i] if i < len(job_titles) else None,
#                 "link": job_links[i] if i < len(job_links) else None,
#                 "image_link": image_links[i] if i < len(image_links) else None,
#                 "location": locations[i] if i < len(locations) else None,
#                 "company_name": company_names[i] if i < len(company_names) else None
#             }
#             for i in range(min(len(job_titles), len(job_links), len(image_links), len(locations), len(company_names)))
#         ]

#         return jsonify(jobs), 200

#     finally:
#         driver.quit()

# if __name__ == "__main__":
#     app.run(debug=True)
