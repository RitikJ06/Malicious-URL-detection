from flask import Flask, redirect, render_template, request
import pickle

# load saved model
with open('model_pkl' , 'rb') as f:
    model = pickle.load(f)
# load count vectorizer
with open('count_vectorizer' , 'rb') as f:
    cv = pickle.load(f)

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        URL = request.form["urlinput"]

        # remove http:// OR https://
        if URL.find('//') != -1:
            URL = URL[URL.find('//')+2: ]
        # remove www.
        if URL.startswith('www.'):
            URL = URL[4:]

        # predict the result
        result = model.predict(cv.transform([URL]))[0]

        return render_template("index.html", r = result)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=False)
