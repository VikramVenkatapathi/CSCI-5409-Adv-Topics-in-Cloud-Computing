import os
from flask import Flask, jsonify, request
import csv
app = Flask(__name__)
 
#if the input json is empty (or)'file' key is not in json (or) 'file' is null => return 
def validate_json(data):
    if data is None or 'file' not in data or not isinstance(data['file'], str) or data['file'] == '':
        return False
    return True


def check_csv_file_format(file_name):
    required_columns = ['product', 'amount']
    filepath = os.path.join("..", "vikram_PV_dir",file_name)

    try:
        with open(filepath, 'r') as file:
            csv_reader = csv.DictReader(file)
            content = file.read().strip()

            # Check if the content is a valid CSV format
            if not content.startswith("product,amount"):
                return False
            
            for row_number, row in enumerate(csv_reader, start=2):
                # Check if the row has the required number of columns
                if len(row) != len(required_columns):
                    return False

                # Check if the columns match the required columns
                if set(row.keys()) != set(required_columns):
                    return False

                # Check if any column value is missing or empty
                if any(not row[column] for column in required_columns):
                    return False

                try:
                    # Check if the 'amount' column is an integer
                    int(row['amount'])
                except ValueError:
                    return False

                # Check if any column value is missing or empty
                if any(not row[column] for column in required_columns):
                    return False

        return True

    except FileNotFoundError:
        return False


# find the macthing product's quantity and calculate the sum
def calculate_sum(file_name, product):
    total_sum = 0
    #filepath = "/app/"+file_name
    filepath = os.path.join("..", "vikram_PV_dir",file_name)
    # filepath = "../files/"+file_name

    with open(filepath, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            if row['product'] == product:
                amount = int(row['amount'])
                total_sum += amount

    return str(total_sum)

#check if the 'file' exists in the current directory
def check_file_exists(file_name):
    file_path = os.path.join("..", "vikram_PV_dir", file_name)
    if os.path.exists(file_path):
        return True
    return False
    # if os.path.exists(file_name):
    #     return True
    # return False

@app.route('/calculate', methods=['POST']) #wait for POST request from container 1 on PORT 8001
def handle_request():
    data = request.get_json()

    file_name = data['file']
    
    if not validate_json(data):
        error_message = 'Invalid JSON input.'
        print(error_message)
        error_response_data = {
            'file': None,
            'error': error_message
        }
        return jsonify(error_response_data), 400
    
    response_data ={"file": file_name,"sum": "0"}
    
    if check_file_exists(data['file']) == False:
            error_message = 'File not found.'
            print(error_message)
            response_data = {
                'file': data['file'],
                'error': error_message
            }
            return jsonify(response_data), 404
            
    if not check_csv_file_format(data['file']):
        error_response = {
            'file': data['file'],
            'error': 'Input file not in CSV format.'
            }
        return jsonify(error_response)
    
    print('Received data:', data)
    response_data['sum'] = calculate_sum(data['file'], data['product'])
    return response_data

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8001)
