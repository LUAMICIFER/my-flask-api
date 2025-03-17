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
    my_array = [
        {"link": "https://cdn-icons-png.flaticon.com/128/518/518705.png", "name": "Android"},
        {"link": "https://cdn-icons-png.flaticon.com/128/3178/3178285.png", "name": "Web Development"},
        {"link": "https://cdn-icons-png.flaticon.com/128/5278/5278402.png", "name": "AI"},
        {"link": "https://cdn-icons-png.flaticon.com/128/12602/12602187.png", "name": "UI/UX"}
    ]
    # my_array = ["Android", "Web_Development", "AI", "UI/UX"]
    return jsonify(my_array),200

    
@app.route("/internshala/<user_feild>")
def internshala(user_feild):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
        
    driver = webdriver.Chrome(options=chrome_options)
    variable = ""
    if user_feild == "android":
        variable = "android-app-development-jobs/"
    elif user_feild == "web":
        variable = "web-development-jobs/"
    else:
        variable = "user_feild"

    driver.get("https://internshala.com/jobs/" + variable)
    driver.maximize_window()
    time.sleep(2)

    try:
        driver.find_element(By.ID, 'close_popup').click()
    except:
        pass
    time.sleep(2)

    # driver.find_element(By.XPATH, "/html/body/div[1]/div[19]/div/nav/div[3]/ul/li[4]/a").click()
    # driver.find_element(By.ID, 'header_login_modal_button').click()
    # driver.find_element(By.ID, 'modal_email').send_keys("your_email@example.com")
    # driver.find_element(By.ID, 'modal_password').send_keys("your_password")
    # driver.find_element(By.ID, 'modal_login_submit').click()
    # time.sleep(2)

    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    job_titles = [element.text.strip() for element in soup.find_all("a", class_="job-title-href")]
    job_links = ["https://internshala.com" + a["href"] for a in soup.find_all("a", class_="job-title-href", href=True)]
    
    image_links = []
    for div in soup.find_all("div", class_="internship_logo"):
        img = div.find("img")
        image_links.append(img["src"] if img and "src" in img.attrs else None)

    company_elements = driver.find_elements(By.CLASS_NAME, "company-name")
    company_names = [element.text.strip() for element in company_elements]

    location = driver.find_elements(By.CSS_SELECTOR, ".row-1-item.locations")
    text_list = [element.text.strip() for element in location]
    locations = text_list

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

    driver.quit()
    return jsonify(jobs), 200
if __name__ == "__main__":
    # Run the app on all network interfaces (0.0.0.0) and set the port (use port 5000 or any port Render provides)
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=False)
