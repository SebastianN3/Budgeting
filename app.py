from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # You don't have to specify the name of the folder. 
    # It knows it has to look into templates folder
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)