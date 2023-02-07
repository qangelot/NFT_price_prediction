import requests
import json
import pandas as pd

# Define the endpoint URL
url = "http://localhost:5000/predict"

# Generate test data 
data = pd.read_csv('data/filtered_data.csv' , index_col=None, header=0, lineterminator='\n')
data = data.drop(['price_label', 'avg_selling_price', 'sale_label'],axis=1)

# Get the first row of data and define the JSON payload
data_json = data.iloc[0].to_dict()

# Send the request with the JSON payload
response = requests.post(url, json=data_json)

# Get the prediction from the response
prediction = response.json()["prediction"]

# Print the prediction
print(prediction)