#import necessary libraries 
#flask-class
#render_template- show web page or html file
#request -to request information from users
#pickle- to undump model-pickle

import pickle
from flask import Flask, render_template, request

app = Flask(__name__)

# Load the trained model
model = pickle.load(open("model.pkl", "rb"))

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    # Get the input from the form
    temperature_str = request.form.get("Temperature")

    try:
        # Convert input to float
        temperature = float(temperature_str)

        # Make prediction
        prediction = model.predict([[temperature]])
        output = round(prediction[0], 2)

        return render_template("index.html", prediction_text=f'Revenues in $ {output}/-')

    except ValueError:
        # Handle the case where temperature_str cannot be converted to float
        return render_template("index.html", prediction_text='Please enter a valid temperature.')

if __name__ == '__main__':
    app.run(debug=True)






