# Dependencies
import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup
import os
import pymongo
from flask_pymongo import PyMongo

def init_browser():

    executable_path = {"executable_path": "chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

def scrape():

    #Creating a path to chrome driver.
    browser = Browser('chrome', headless=False)
    browser.visit('https://mars.nasa.gov/news/')
    html = browser.html
    nasa_soup = BeautifulSoup(html, 'html.parser')


    # Scrape the NASA webpage and collect the latest news, title and paragraph
    #text. Assign the text to variables that you can reference later.
    title_news = nasa_soup.find('div', class_='content_title').text
    parag_news = nasa_soup.find('div', class_='article_teaser_body').text

    # JPL MARS SPACE IMAGES - FEATURED IMAGE

    #Visiting url for JPL Featured Space Image
    browser = Browser('chrome', headless = False)
    browser.visit('https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars')

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    imag=soup.find("img", class_="thumb")["src"]
    featured_image_url = "https://www.jpl.nasa.gov" + imag
    
    # MARS WEATHER

    #Visiting Mars weather twitter webpage
    browser = Browser('chrome', headless = False)
    browser.visit('https://twitter.com/marswxreport?lang=en')

    soup = BeautifulSoup(browser.html, 'html.parser')
    mars_tweet = soup.find(class_='tweet-text').text

    # MARS FACTS

    #Visiting the Mars facts webpage
    browser = Browser('chrome', headless = False)
    url = "https://space-facts.com/mars/"
    browser.visit(url)

    mars_facts = pd.read_html(url)
    mars_profile = mars_facts[1]
    mars_profile.columns = ["Mars Planet Profile", "Features"]

    mars_profile.set_index("Mars Planet Profile", inplace=True)
    html_table = mars_profile.reset_index().to_html(index=False)
    
    
    # MARS HEMISPHERES

    #Visiting the Mars facts webpage
    browser = Browser('chrome', headless=False)

    hemis_urls = []
    browser.visit('https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars')
    CerberusEnhn = browser.find_by_text('Cerberus Hemisphere Enhanced')
    Cerb = CerberusEnhn.click()
    browser.url
    hemis_urls.append(browser.url)

    browser.visit('https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars')
    SchiaparelliEnhn = browser.find_by_text('Schiaparelli Hemisphere Enhanced')
    Schiap = SchiaparelliEnhn.click()
    browser.url
    hemis_urls.append(browser.url)

    browser.visit('https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars')
    SyrtisEnhn = browser.find_by_text('Syrtis Major Hemisphere Enhanced')
    Syrtis = SyrtisEnhn.click()
    browser.url
    hemis_urls.append(browser.url)

    browser.visit('https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars')
    VallesEnhn = browser.find_by_text('Valles Marineris Hemisphere Enhanced')
    Valles = VallesEnhn.click()
    browser.url
    hemis_urls.append(browser.url)

    #naming and listing the hemisphere images

    browser.visit(hemis_urls[0])
    hemisurl_1 = browser.find_by_text('Sample')['href']

    browser.visit(hemis_urls[1])
    hemisurl_2 = browser.find_by_text('Sample')['href']

    browser.visit(hemis_urls[2])
    hemisurl_3 = browser.find_by_text('Sample')['href']

    browser.visit(hemis_urls[3])
    hemisurl_4 = browser.find_by_text('Sample')['href']

    #common dictionary including all parsed internet data
    common_dictionary = {
        "Updated_title": title_news, 
        "Updated_news": parag_news,
        "Featured_image": featured_image_url,
        "Weather_update": mars_tweet,
        "Facts_Mars": html_table,
        "Cerberus_hemisphere": hemisurl_1,
        "Schiaparelli_hemisphere": hemisurl_2,
        "Syrtis_hemisphere": hemisurl_3,
        "Valler_hemisphere": hemisurl_4
    }

    hemisphere_images = [
        {"Title": "Valles Marineris Hemisphere", "img_url": "hemisphere4_image_url"},
        {"Title": "Cerberus Hemisphere", "img_url": "hemisphere1_image_url"},
        {"Title": "Schiaparelli Hemisphere", "img_url": "hemisphere2_image_url"},
        {"Title": "Syrtis Major Hemisphere", "img_url": "hemisphere3_image_url"},
    ]

    browser.quit()

    return common_dictionary
