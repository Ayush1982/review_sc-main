from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
import requests
from bs4 import BeautifulSoup as bs
import pymongo

application = Flask(__name__)  # Initializing a Flask app
app = application

@app.route('/', methods=['GET'])  # Route to display the home page
@cross_origin()
def homePage():
    return render_template("index.html")

@app.route('/review', methods=['POST', 'GET'])  # Route to show the review comments in a web UI
@cross_origin()
def index():
    if request.method == 'POST':
        try:
            searchString = request.form['content'].replace(" ", "")
            flipkart_url = "https://www.flipkart.com/search?q=" + searchString
            print(flipkart_url)
            # Use 'requests.get' for making the HTTP request
            response = requests.get(flipkart_url)

            if response.status_code == 200:
                # You can now use 'response.text' to get the HTML content of the page
                flipkartPage = response.text
                flipkart_html = bs(flipkartPage, "html.parser")

                # Rest of your code for web scraping goes here
                # ...

            else:
                return "Failed to fetch data from the URL."

        except Exception as e:
            print('The Exception message is: ', e)
            return 'something is wrong'

    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000, debug=True)
