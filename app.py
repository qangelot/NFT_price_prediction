from flask import Flask, request, jsonify
import numpy as np
import pandas as pd 
from src.predict import make_predictions


app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():

    # Get the input data from the JSON payload
    data_json = request.get_json(force=True) 

    # Convert the JSON object to a Pandas DataFrame
    data = pd.DataFrame([data_json], index=[0])

    # Make a prediction using the loaded model
    prediction = make_predictions(data)
    
    # Return the prediction as a JSON response
    return jsonify({"prediction": prediction.tolist()})

if __name__ == "__main__":
    app.run(debug=True)

    