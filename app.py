from flask import Flask, request, url_for, redirect, render_template
import tensorflow as tf
import keras
from keras.models import load_model
from keras import layers

import numpy as np
import os
import pandas as pd
from werkzeug.utils import secure_filename

app = Flask(__name__)
model = load_model('model.keras')

num_classes = 12  

model = keras.Sequential([
    layers.BatchNormalization(),
#     layers.Dense(units=64, activation='relu', input_shape=[79]),
#     layers.BatchNormalization(),  
#     layers.Dropout(0.5),  
    layers.Dense(units=64, activation='relu'),
    layers.BatchNormalization(), 
    layers.Dropout(0.5), 
    layers.Dense(units=16, activation='relu'),
    layers.BatchNormalization(),  
    layers.Dropout(0.5), 
    layers.Dense(units=num_classes, activation='softmax')  
])

def is_value_prevalent(dataset, value):
    return all(item == value for item in dataset)

def map_values(dataset, mapping):
    mapped_values = [mapping.get(item) for item in dataset if item in mapping]
    return mapped_values

mapping = {0: "ARP Spoofing",1: "Be", 2: "DNS Flood", 3: "Dictionary Attack", 4: "ICMP Flood", 5: "OS Scan", 6: "Ping Sweep", 7: "Port Scan", 8: "SYN Flood", 9: "Slowloris", 10: "UDP Flood", 11: "Vulnerability Scan"}

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/predict', methods=['POST','GET'])
def predict():
    if request.method == 'POST':
        csvf = request.files['csv-file']
        if 'csv-file' not in request.files:
            return redirect(request.url)
        
        if csvf.filename == '':
            return redirect(request.url)
        
        filename = secure_filename(csvf.filename)
        file_path = os.path.join('uploads', filename)

        if not os.path.exists('uploads'):
            os.makedirs('uploads')


        csvf.save(file_path)
        
        df = pd.read_csv(file_path)
        predict = model.predict(df)
        probabilities = predict
        max_prob_indices = np.argmax(probabilities, axis=1)


        binary_predictions = (np.arange(probabilities.shape[1]) == max_prob_indices[:, None]).astype(int)

        binary_preds = pd.DataFrame(binary_predictions, columns = ['ARP Spoofing', 'Benign', 'DNS Flood', 'Dictionary Attack','ICMP Flood', 'OS Scan', 'Ping Sweep', 'Port Scan', 'SYN Flood','Slowloris', 'UDP Flood', 'Vulnerability Scan'])
        binary_preds_encoded= pd.from_dummies(binary_preds)
        #binary_preds_encoded.iloc[:,0] = binary_preds_encoded.iloc[:,0].map({'ARP Spoofing': 0,'Benign': 1,'DNS Flood': 2,'Dictionary Attack': 3,'ICMP Flood': 4,'OS Scan': 5,'Ping Sweep': 6,'Port Scan': 7,'SYN Flood': 8,'Slowloris': 9,'UDP Flood': 10,'Vulnerability_Scan': 11})
        # Assuming predict is a numpy array of predictions
        #mapped_values = map_values(binary_preds_encoded, mapping)
        if is_value_prevalent(binary_preds_encoded, 'Benign') == True:
            result = "System under normal condition"
        else:
            unique_values, counts = np.unique(binary_preds_encoded, return_counts=True)
            result_string = ',\n '.join([f"attack {value}: attempts {count}" for value, count in zip(unique_values, counts)])
            result = f"System was under attack by:\n{result_string}"
        
        return render_template('index.html', csvf=csvf, result=result)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
