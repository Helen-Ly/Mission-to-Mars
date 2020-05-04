# Mission to Mars

Our universe has a lot to offer! One planet we have a particular interest in is the Red Planet, Mars. We keep ourselves in the loop with new information by going through several websites for their latest articles and images. 

Grateful that we have many resources to learn new things about Mars, it is time consuming going through each individual website to get information. We decided to scrape the sites we use and load it all into a Flask webpage.

1. Create a python file that will scrape the information we want (scraping.py).

    - Visit each browser
    - Parse through HTML
    - Find most recent article (title and summary), facts about Mars (table format) and a featured Mars image (some may need you to use .click() to get more information)

2. Assign your newly obtained information to its own variable and save these variables into your MongoDB.
3. Create a template of how your webpage will render (index.html).
4. Create a Flask application that has a root and scrape route (app.py).
    
    - The root route will pull the information from MongoDB and render the page from your *index.html*
    - The scrape route will call the scrap_all() from your *scraping.py* file.
    

## Resources

  - Data Source: http://mars.nasa.gov/news/, https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars, https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars, http://space-facts.com/mars/
  - Software: Python 3.7.6, Jupyter Lab 1.2.6, Visual Studio Code 1.43.0, MongoDB 4.2.6, HTML, CSS, Bootstrap
  - Libraries: Pandas, Splinter, BeautifulSoup4, Datetime, PyMongo, Flask

## Challenge

The webpage looks great! It scrapes the most recent data, displays facts about Mars and is responsive to different sized screens. We want to provide a little more information for visitors who may want more information. We decided to include high-resolution images of Mars's hemispheres, along with adding a few Bootstrap components.

## Summary

![](https://github.com/Helen-Ly/Mission-to-Mars/blob/master/mars_webpage.png)

In the image above, it is the top of the webpage. As you can see, we have the title and the button to scrape new data. Originally, the button was blue, but we thought it would be nice to have a **red button** for the **Red Planet**. When this button is clicked, the web scraping begins. We have added a line that once the scraping has completed, the page will redirect you back to the homepage with the newly scraped data. As well, included on this page, an alert to welcome all of our visitors and a sign in form for when we launch a personal account for our visitors.

![](https://github.com/Helen-Ly/Mission-to-Mars/blob/master/mars_webpage_bottom.png)

In the image above, it is the bottom on the webpage. This newly added section provides Mars's hemispheres, both image and title. We have wrapped these photos within a thumbnail tag to provide this neat display.


## Portfolio

Think this project was cool? Want to meet the creator and see what other projects she has? Here is a quick screenshot of her portfolio.

Having a portfolio is a great way to display a bit about yourself and the projects you have worked on.

![](https://github.com/Helen-Ly/Mission-to-Mars/blob/master/helen_portfolio.png)

## Usage

**Note:** Please ensure you have all the required and updated softwares on your computer.

1. Download the following files into the same folder for the project.

   - scraping.py
   - index.html (create a subfolder called *templates* and add the file into the folder)
   - app.py

2. Open Visual Studio Code from your projects folder.

3. In your Anaconda prompt (inside your development environment), navigate to the project folder and type "python app.py".

4. This will run the file and provide you with a URL. Copy and paste it into your browser.

5. When you are on the page, click the *Scrape New Data* button, the page will scrape the data and redirect you back to the homepage with the newly scraped information.

6. If you would also like to create a portfolio, you can access the template from https://github.com/Helen-Ly/portfolio.

    - Save the files locally
    - Fill in your own information and images
