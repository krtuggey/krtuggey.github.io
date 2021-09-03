#import dependencies and set up Flask
from flask import Flask, render_template
app = Flask(__name__)

#Define the route for the HTML page
@app.route("/")
def index():
   return render_template("index.html")

#Tell Flask to run
if __name__ == "__main__":
   app.run()