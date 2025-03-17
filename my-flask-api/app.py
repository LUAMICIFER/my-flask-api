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
if __name__ =="__main__":
    app.run(debug=True)