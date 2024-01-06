import csv
import pandas as pd
import selenium

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

data = pd.read_csv('links.csv')

ratings = []

csv_file_path = 'links.csv'  # Replace with the path to your CSV file


def scrapper(imdb_id):
    id = str(int(imdb_id))
    n_zeroes = 7 - len(id)
    new_id = "0" * n_zeroes + id
    URL = f"https://www.imdb.com/title/tt{new_id}/"
    driver.get(url=URL)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "ipc-rating-star")))

    # Extract the IMDb rating
    rating_element = driver.find_element(By.CLASS_NAME, "ipc-rating-star")
    rating = rating_element.text

    return [rating,imdb_id] if rating else np.nan

with open(csv_file_path, 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip header if it exists
    for row in reader:
        imdb_id = row[1]
        rating = scrapper(imdb_id)
        ratings.append(rating)
print(ratings)

time.sleep(2)
