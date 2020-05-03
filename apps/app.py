# Import our dependencies
from flask import Flask, render_template
from flask_pymongo import PyMongo
import scraping

# Initialize app
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
# tells Python our app will connect to Mongo using URI (uniform resource identified), similar to URL
app.config['MONGO_URI'] = 'mongodb://localhost:27017/mars_app'
mongo = PyMongo(app)

# Set base app route
# This function is what links our visual representation of our work,
# our web app, to the code that powers it
@app.route('/')
def index():
    mars = mongo.db.mars.find_one() # uses PyMongo to find the 'mars' collection in the db
    return render_template('index.html', mars = mars)

# Set up scraping route
# This will be the button that will scrape updated data when clicked
@app.route('/scrape')
def scrape():
    mars = mongo.db.mars
    mars_data = scraping.scrape_all()
    mars.update({}, mars_data, upsert = True)
    return 'Scraping Succussful!'

# Run code
if __name__ == '__main__':
    app.run(debug=True)
