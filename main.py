from flask import Flask, render_template

app = Flask(__name__)

@app.route('/home',methods=["POST","GET"])
def home():
    print("Welcome to my Blog")
    return render_template('home.html')

@app.route('/comment', methods=["POST","GET"])
def about():
    return render_template('comment.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)