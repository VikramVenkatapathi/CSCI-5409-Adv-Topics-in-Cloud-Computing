from flask import Flask, jsonify, request
import os, csv
import requests

import requests
 
app = Flask(__name__)


#if the input json is empty (or)'file' key is not in json (or) 'file' is null => return 
def validate_json(data):
    if data is None or 'file' not in data or not isinstance(data['file'], str) or data['file'] == '':
        return False
    return True

def validate_data_format(data):
    try:
        lines = data.strip().split('\n')
        if len(lines) < 2:
            return False
        
        reader = csv.reader(lines)
        headers = next(reader)
        if len(headers) != 2:
            return False
        
        for row in reader:
            if len(row) != 2:
                return False
        
        return True
    
    except csv.Error:
        return False

def remove_spaces(data):
    # Remove leading and trailing spaces from each line
    lines = [line.strip() for line in data.split('\n')]
    
    # Remove spaces within each line
    cleaned_lines = [line.replace(' ', '') for line in lines]
    
    # Join the cleaned lines back into a single string
    cleaned_data = '\n'.join(cleaned_lines)
    
    return cleaned_data


# create a file with the specified name and contents
def create_file(file_name, data):
    data = remove_spaces(data)
    file_path = os.path.join("..", "vikram_PV_dir", file_name)
    f = open(file_path, "w")
    f.write(data)
 
        
#send the json input to container2
def send_data_to_container2(file_name, product):
    payload = {
        'file': file_name,
        'product': product
    }

    container2_url = 'http://vikram-service-2:8001/calculate'

    response = requests.post(container2_url, json=payload)
    
    return response.json()

@app.route('/store-file', methods=['POST']) 
def handle_store_file_request():
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
        try:
            create_file(file_name, data['data'])
            message = 'Success.'
            response_data = {
                'file': file_name,
                'message': message
            }
            return jsonify(response_data)
        except Exception as e:
            error_message = 'Error while storing the file to the storage.'
            print(error_message)
            response_data = {
                'file': file_name,
                'error': error_message
            }
            return jsonify(response_data), 500
        
    return 'OK'

@app.route('/calculate', methods=['POST']) 
def handle_calculate_request():
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

        product = data['product']
        
        response = send_data_to_container2(file_name, product)
        return jsonify(response)

    return 'OK'

@app.route('/hello-world', methods=['POST']) 
def handle_hello_world_request():
    print("Hello world")
    return jsonify({"data":"hello"}),400

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=6000)