# from selenium import webdriver
# import pickle
# import time

# driver = webdriver.Chrome()
# # driver.get("google.com")
# driver.get("https://www.linkedin.com/jobs/search/?currentJobId=4159233899&f_E=1&f_TPR=r604800&keywords=android%20development&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true")  
# time.sleep(50) 

# # Save cookies after login
# pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))
# print("done")
# driver.quit()

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
# driver.get("https://www.linkedin.com/jobs/search/?currentJobId=4159233899&f_E=1&f_TPR=r604800&keywords=android%20development&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true")
# driver.maximize_window()
# cookies = pickle.load(open("cookies.pkl", "rb"))
# for cookie in cookies:
#     driver.add_cookie(cookie)
# driver.refresh()
# time.sleep(5)
# html = driver.page_source
# soup = BeautifulSoup(html, "html.parser")
# # job_cards = soup.find_all(attrs={"data-view-name": "job-card"})
# job_links = []
# job_cards = soup.find_all(attrs={"data-view-name": "job-card"})
# for job_card in job_cards:
#     link_tag = job_card.find("a", href=True)  # Find <a> tag with href
#     if link_tag:
#         full_link = "https://www.linkedin.com" + link_tag["href"]  # Convert to absolute URL
#         job_links.append(full_link)

# # Print extracted job links separately
# print("\nExtracted Job Links:")
# for link in job_links:
#     print(link +"\n")

# for link in job_links:
#     time.sleep(5)
#     message = f"🔗 New Job Listing Android Development \n LinkedIn: {link}"
#     url = f"https://api.telegram.org/bot5086944407:AAGSvOf9K8mBipbkMDK6rfqwmcjtsGcNXcw/sendMessage"
#     data = {"chat_id": -1002398388043, "text": message}
#     response = requests.post(url, data=data)
#     print(response.json())  