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

if __name__ == "__main__":
    # Run the app on all network interfaces (0.0.0.0) and set the port (use port 5000 or any port Render provides)
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=False)
