from flask import Flask,jsonify
from wordtune import CRAWLER
app=Flask(__name__)
scraper = CRAWLER()

@app.route('/')
def index():
    return jsonify(scraper.process_logic())
if __name__=="__main__":
    app.run(debug=True)