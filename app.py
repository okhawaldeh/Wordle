
from flask import Flask, render_template, request, session, redirect, url_for, flash
from definition import definition_finder

##### Flask intialization #####
app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':
        definition = definition_finder()
        return render_template('index.html', definition = definition)
    return render_template('index.html')
if __name__ == "__main__":
    app.run(debug=True)