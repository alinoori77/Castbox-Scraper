from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import requests
from bs4 import BeautifulSoup
import time
import os
import subprocess

try:
    podcast_name = "jason"
    base_url = f"https://castbox.fm/podcasts/{podcast_name}?country=us"

    response = requests.get(base_url)

    soup = BeautifulSoup(response.text, 'html.parser')

    podcast_link = soup.find("div", class_="topCover").find('a').get('href')

    Channel_link = f"https://castbox.fm{podcast_link}?country=us"



    # Set Chrome options for headless mode
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")  # Run in headless mode
    chrome_options.add_argument("--disable-gpu")  # Disable GPU usage for headless mode

    # Initialize Chrome WebDriver with the specified options
    driver = webdriver.Chrome(options=chrome_options)





    # driver = webdriver.Chrome()
    driver.get(Channel_link)



    element_found = False

    # Set a counter to limit the number of scrolls (optional, for safety)
    scroll_counter = 0
    max_scroll_attempts = 500  # Adjust as needed

    while not element_found and scroll_counter < max_scroll_attempts:
        # Scroll down the page
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        # Check if the element is present
        try:
            element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="LoadInline"]/img')))
            scroll_counter += 1
        except:
            print("Element not found, scrolling again...")
            # element_found = True


    
    print(driver.page_source)
    soup_full_page = BeautifulSoup(driver.page_source, 'html.parser')
    episode_title = soup_full_page.findAll("span", class_="ellipsis")
    for title in episode_title:
        print(title.text)
    time.sleep(10)


    
except Exception as error:
    print("Error", error)
    