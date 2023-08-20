from flask import Flask, jsonify, request
import os, csv

import requests

app = Flask(__name__)

#if the input json is empty (or)'file' key is not in json (or) 'file' is null => return 
def validate_json(data):
    if data is None or 'file' not in data or not isinstance(data['file'], str) or data['file'] == '':
        return False
    return True

#check if the 'file' exists in the current directory
def check_file_exists(file_name):
    file_path = os.path.join("..", "files", file_name)
    if os.path.exists(file_path):
        return True
    return False
    
#send the json input to container2
def send_data_to_container2(file_name, product):
    payload = {
        'file': file_name,
        'product': product
    }

    container2_url = 'http://container2:8001/calculate'  
    
    response = requests.post(container2_url, json=payload)
    
    return response.json()

@app.route('/calculate', methods=['POST']) 
def handle_request():
    if request.method == 'POST':
        data = request.get_json()
        if not validate_json(data):
            error_message = 'Invalid JSON input.'
            print(error_message)
            response_data = {
                'file': None,
                'error': error_message
            }
            return jsonify(response_data), 400

        file_name = data['file']
        print('Received POST request. File:', file_name)

        if check_file_exists(file_name) == False:
            error_message = 'File not found.'
            print(error_message)
            response_data = {
                'file': data['file'],
                'error': error_message
            }
            return jsonify(response_data), 404
        product = data['product']
        
        response = send_data_to_container2(file_name, product)
        return jsonify(response)

    return 'OK'
    
if __name__ == '__main__':
    app.run(host="0.0.0.0",port=6000)