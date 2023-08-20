import os
from flask import Flask, jsonify, request
import csv
app = Flask(__name__)

#check if the date file is in proper CSV format
def check_csv_file_format(file_name):

    required_columns = ['product', 'amount']
    filepath = os.path.join("..", "files", file_name)
    # filepath = "../files/"+file_name

    with open(filepath, 'r') as file:
        csv_reader = csv.DictReader(file)
        
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

#find the macthing product's quantity and calculate the sum
def calculate_sum(file_name, product):
    total_sum = 0
    #filepath = "/app/"+file_name
    filepath = os.path.join("..", "files", file_name)
    # filepath = "../files/"+file_name

    with open(filepath, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            if row['product'] == product:
                amount = int(row['amount'])
                total_sum += amount

    return total_sum

@app.route('/calculate', methods=['POST']) #wait for POST request from container 1 on PORT 8001
def handle_request():
    data = request.get_json()
    response_data ={"file": data['file'],"sum": 0}
    
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
