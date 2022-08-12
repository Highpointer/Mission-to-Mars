#!/usr/bin/env python
# coding: utf-8

# In[14]:

# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

# In[2]:

executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

# In[3]:

# Visit the Mars nasa news site 10.3.3
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)

# In[4]:

# 10.3.3 Set up the HTML parser

html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')

# In[5]:

slide_elem.find('div', class_='content_title')

# In[6]:

# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title

# In[7]:

# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p

# In[8]:

# 10.3.4 Visit URL
# In your Jupyter notebook, use markdown to separate the article scraping from the image scraping
url = 'https://spaceimages-mars.com'
browser.visit(url)

# In[9]:

#10.3.4 Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()

# In[10]:

# 10.3.4 Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')

# In[12]:

# 19.3.4 Find the relative image url
# <img class="headerimage fade-in" src="image/featured/mars3.jpg"> == $0
# Tell BeautifulSoup to look inside the <img /> tag for an image with a class of fancybox-image
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel

# In[13]:

# 10.3.4 Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url

# In[15]:

# 10.3.5 scrape the entire table with Pandas' .read_html() function.
df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df

# In[16]:

# 10.3.5 convert our DataFrame back into HTML-ready code
df.to_html()

# In[17]:

# 10.3.5 Add browser.quit() and execute that cell to end the session
browser.quit()

# In[ ]: