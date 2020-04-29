#!/usr/bin/env python
# coding: utf-8

# Import dependencies
from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import datetime as dt

# Define function for scrape all and initiate the browser
def scrape_all():

    # Initiate headless driver for deployment
    browser = Browser('chrome', executable_path = 'chromedriver', headless = True)

    # Set news title and paragraph variables
    news_title, news_paragraph = mars_news(browser)

    # Runn all scraping functions and store results in dictionary
    data = {
        'news_title': news_title, 
        'news_paragraph': news_paragraph,
        'featured_image': featured_image(browser),
        'facts': mars_facts(),
        'last_modified': dt.datetime.now()
    }


# Set the executable path and initialize the chrome browser in splinter
executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path)

#-----------------
# Article Scraping
#-----------------

# Create function for article scraping
def mars_news(browser):

    # Visit the mars nasa news site
    url = 'http://mars.nasa.gov/news/'
    browser.visit(url)

    # Optional delay for loading the page
    # for pages that take a while to load, especially if image-heavy
    # tells the browser to wait a second before searching for components
    browser.is_element_present_by_css('ul.item_list li.slide', wait_time = 1)

    # Set up HTML parser
    html = browser.html
    news_soup = BeautifulSoup(html, 'html.parser')

    # Add try/except for error handling
    try:

        # Parent element that holds all other elements within it
        # Reference it to filter search results even further
        # ul tag with class 'item_list', li tag with class 'slide'
        slide_elem = news_soup.select_one('ul.item_list li.slide')

        # Use the parent element to find the first 'a' tag and save it as news_title
        news_title = slide_elem.find('div', class_ = 'content_title').get_text()

        # Use the parent element to find the paragraph text
        news_p = slide_elem.find('div', class_ = 'article_teaser_body').get_text()

    except AttributeError:
        return None, None

    # Print the title and paragraph at the end of our function
    return news_title, news_p

#----------------
# Image Scraping
# Featured Images
#----------------

# Declare function for featured image
def featured_image(browser):

    # Visit URL
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)

    # Find and click the full image button
    full_image_elem = browser.find_by_id('full_image')
    full_image_elem.click()

    # Find the more info button and click that
    browser.is_element_present_by_text('more info', wait_time = 1)
    more_info_elem = browser.find_link_by_partial_text('more info')
    more_info_elem.click()

    # Parse the resulting html with soup
    html = browser.html
    img_soup = BeautifulSoup(html, 'html.parser')

    # Add try/except for error handling
    try:

        # Find the relative image url
        img_url_rel = img_soup.select_one('figure.lede a img').get('src')
    
    except AttributeError:
        return None
    
    # Use the base URL to create an absolute URL
    img_url = f'https://www.jpl.nasa.gov{img_url_rel}'

    return img_url

#---------------
# Facts Scraping
#---------------

# Declare function for mars facts
def mars_facts():

    # Add tr/except for error handling
    try:

        # Scrape the entire table with Pandas
        df = pd.read_html('http://space-facts.com/mars/')[0] # read html table into DF, [0] = read the first table it encounters
    
    except BaseException:
        return None
    
    # Assign columns and set index of DF
    df.columns = ['description', 'value'] # columns for the new DF
    df. set_index('description', inplace = True)

    # return DF back into html, add bootstrap
    return df.to_html()

# End automated browsing session
browser.quit()

# Run code
if __name__ == '__main__':

    # If running as script, print scraped data
    print(scrape_all())

