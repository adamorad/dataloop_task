import requests
import json
import pandas as pd
from datetime import datetime
import mysql

# Connect to the MySQL database
mydb = mysql.connector.connect(
  host="172.17.0.2",
  user="root",
  password="root",
  database="flickrdb"
)

def scrape(keyword='', size=10):
    # Use the Flickr API to search for images matching the keyword
    url = 'https://api.flickr.com/services/rest'
    params = {  
        'method': 'flickr.photos.search',
        'api_key': 'db6de4d465761dc89227abac63579fa5',
        'text': keyword,
        'per_page': size,
        'format': 'json',
        'nojsoncallback': 1
    }
    response = requests.get(url, params=params)
    data = json.loads(response.text)
    images = data['photos']['photo']
    
    # Insert the images into the MySQL database
    cursor = mydb.cursor()
    for image in images:
        url = f'https://farm{image["farm"]}.staticflickr.com/{image["server"]}/{image["id"]}_{image["secret"]}.jpg'
        scrape_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sql = f"INSERT INTO images (imageUrl, scrapeTime, keyword) VALUES ('{url}', '{scrape_time}', '{keyword}')"
        cursor.execute(sql)
        mydb.commit()
    cursor.close()

def search(min_scrape_time='', max_scrape_time='', keyword='', size=10):
    # Retrieve the images from the MySQL database that match the search criteria
    cursor = mydb.cursor()
    sql = f"SELECT * FROM images WHERE scrapeTime >= '{min_scrape_time}' AND scrapeTime <= '{max_scrape_time}' AND keyword = '{keyword}' LIMIT {size}"
    cursor.execute(sql)
    results = cursor.fetchall()
    cursor.close()
    
    # Convert the results to a pandas DataFrame
    column_names = ['imageUrl', 'scrapeTime', 'keyword']
    df = pd.DataFrame(results, columns=column_names)
    return df
