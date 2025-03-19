import os
import time
import pickle
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from flask import Flask, jsonify

app = Flask(__name__)

CACHE_FILE_TEMPLATE = "jobs_cache_{}.pkl"
CACHE_EXPIRY = 2 * 3600  # Cache expires in 2 hours


def load_cache(user_field):
    """Loads cached jobs for a specific user field if the cache is still valid."""
    cache_file = CACHE_FILE_TEMPLATE.format(user_field)
    if os.path.exists(cache_file):
        with open(cache_file, "rb") as f:
            cache_data = pickle.load(f)
            if time.time() - cache_data["timestamp"] < CACHE_EXPIRY:
                return cache_data["jobs"]
    return None 


def save_cache(user_field, jobs):
    """Saves jobs to a cache file for a specific user field."""
    cache_file = CACHE_FILE_TEMPLATE.format(user_field)
    with open(cache_file, "wb") as f:
        pickle.dump({"timestamp": time.time(), "jobs": jobs}, f)


@app.route("/index")
def index():
    """Returns a list of job categories with icons and paths."""
    job_categories = [
        {"link": "https://cdn-icons-png.flaticon.com/128/518/518705.png", "name": "Android", "path": "android-app-development-jobs"},
        {"link": "https://cdn-icons-png.flaticon.com/128/3178/3178285.png", "name": "Web Development", "path": "web-development-jobs"},
        {"link": "https://cdn-icons-png.flaticon.com/128/5278/5278402.png", "name": "AI", "path": "artificial-intelligence-ai-jobs"},
        {"link": "https://cdn-icons-png.flaticon.com/128/12602/12602187.png", "name": "UI/UX", "path": "ui-ux-jobs"},
        {"link": "https://cdn-icons-png.flaticon.com/128/15714/15714837.png", "name": "Backend Development", "path": "backend-development-jobs"},
        {"link": "https://cdn-icons-png.flaticon.com/128/5423/5423094.png", "name": "Big Data", "path": "big-data-jobs"},
        {"link": "https://cdn-icons-png.flaticon.com/128/5757/5757816.png", "name": "Blockchain Development", "path": "blockchain-development-jobs"},
        {"link": "https://cdn-icons-png.flaticon.com/128/2318/2318784.png", "name": "Cloud Computing", "path": "cloud-computing-jobs"},
        {"link": "https://cdn-icons-png.flaticon.com/128/1691/1691940.png", "name": "Cyber Security", "path": "cyber-security-jobs"},
        {"link": "https://cdn-icons-png.flaticon.com/128/2821/2821637.png", "name": "Data Science", "path": "data-science-jobs"},
        {"link": "https://cdn-icons-png.flaticon.com/128/9018/9018925.png", "name": "Digital Marketing", "path": "digital-marketing-jobs"},
        {"link": "https://cdn-icons-png.flaticon.com/128/4489/4489681.png", "name": "Game Development", "path": "game-development-jobs"},
        {"link": "https://cdn-icons-png.flaticon.com/128/2554/2554812.png", "name": "Graphic Design", "path": "graphic-design-jobs"}
        
    ]
    return jsonify(job_categories), 200


@app.route("/check")
def check():
    """Checks if Selenium WebDriver is working by fetching Google's homepage title."""
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.google.com")
    title = driver.title
    driver.quit()

    return jsonify({"title": title}), 200


@app.route("/internshala/<user_field>")
def internshala(user_field):
    """Fetches job listings for a specific field from Internshala."""
    
    cached_jobs = load_cache(user_field) 
    if cached_jobs:
        return jsonify(cached_jobs), 200 
    
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=chrome_options)
    driver.get(f"https://internshala.com/jobs/{user_field}")
    driver.maximize_window()
    time.sleep(2)

    try:
        driver.find_element(By.ID, 'close_popup').click()
    except:
        pass 

    time.sleep(2)

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
    image_links = [img["src"] if img and "src" in img.attrs else None for div in soup.find_all("div", class_="internship_logo") if (img := div.find("img"))]
    company_names = [element.text.strip() for element in driver.find_elements(By.CLASS_NAME, "company-name")]
    locations = [element.text.strip() for element in driver.find_elements(By.CSS_SELECTOR, ".row-1-item.locations")]

    jobs = []
    for i in range(len(job_titles)):  
        jobs.append({
            "title": job_titles[i] if i < len(job_titles) else None,
            "link": job_links[i] if i < len(job_links) else None,
            "image_link": image_links[i] if i < len(image_links) else None,
            "location": locations[i] if i < len(locations) else None,
            "company_name": company_names[i] if i < len(company_names) else None
        })

    driver.quit()

    save_cache(user_field, jobs)  

    return jsonify(jobs), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=False)
