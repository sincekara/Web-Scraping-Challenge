# Dependencies
import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup

def scrape():
    
    #Creating a path to chrome draver.
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)

    title_news_first, parag_news_first = newsMars(browser)

    results = {
         "title": title_news_first,
         "paragraph": parag_news_first,
         "image_URL": mars_image(browser),
         "weather": weather_tweet(browser),
         "facts": mars_facts(),
         "hemispheres": four_hemispheres(browser),
    }

    browser.quit()
    return results

def newsMars(browser):

    # URL of page to be scraped
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    quotes = soup.find_all('span', class_='text')

    # Scrape the NASA webpage and collect the latest news, title and paragraph
    #text. Assign the text to variables that you can reference later.

    title_news_first = soup.find('div', class_='content_title').text
    parag_news_first = soup.find('div', class_='article_teaser_body').text
    
    return title_news_first, parag_news_first

def mars_image(browser):
    
    #Visiting url for JPL Featured Space Image
    browser = Browser('chrome', headless = False)
    browser.visit('https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars')

    #Futured image url
    featured_image_url = 'https://photojournal.jpl.nasa.gov/jpeg/PIA19980.jpg'
    browser.visit(featured_image_url)

    return featured_image_url

def weather_tweet(browser):

    #Visiting Mars weather twitter webpage
    browser = Browser('chrome', headless = False)
    browser.visit('https://twitter.com/marswxreport?lang=en')

    soup = BeautifulSoup(browser.html, 'html.parser')
    soup.find(class_='tweet-text').text

    return tweet-text

def mars_facts():
    
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    url = 'https://space-facts.com/mars/'
    browser.visit(url)

    mars_facts = pd.read_html(url)
    mars_facts[1]
    mars_profile = mars_facts[1]
    mars_profile.columns = ["Mars Planet Profile", "Features"]
    
    mars_profile = mars_profile = mars_facts[1].to_html()
    mars_profile = mars_profile.replace("\n","")
  
    return mars_profile.to_html()

def four_hemispheres(browser):

    #Visiting the Mars facts webpage
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)

    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)

    hemisphere1_image_url = 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg'
    browser.visit(hemisphere1_image_url)

    hemisphere2_image_url = 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg'
    browser.visit(hemisphere2_image_url)

    hemisphere3_image_url = 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg'
    browser.visit(hemisphere3_image_url)

    hemisphere4_image_url = 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg'
    browser.visit(hemisphere4_image_url)

    hemisphere_images = [
        {"Title": "Valles Marineris Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg"},
        {"Title": "Cerberus Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg"},
        {"Title": "Schiaparelli Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg"},
        {"Title": "Syrtis Major Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg"},
        ]

     
    return hemisphere_images
