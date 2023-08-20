from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)

# Configure the database connection
config = {
    'user': 'admin',
    'password': 'v4eHqwAsEQ2DjWOmewET',
    'host': 'mysql-rds.cnbcotqskdhk.us-east-1.rds.amazonaws.com',
    'database': 'a3'
}

@app.route("/store-products", methods=["POST"])
def store_products():
    json_data = request.get_json()
    response = {
        "message": "Success."
    }
    if not json_data:
        return "No JSON data provided", 400
    products = json_data.get("products", [])

    if not isinstance(products, list):
        return "Invalid JSON format: 'products' should be a list.", 400

    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()

    try:
        for product in products:
            name = product.get("name")
            price = product.get("price")
            availability = product.get("availability")

            # Insert the product into the database
            query = "INSERT INTO products (name, price, availability) VALUES (%s, %s, %s)"
            values = (name, price, availability)
            cursor.execute(query, values)

        # Commit the changes to the database
        connection.commit()
    except mysql.connector.Error as error:
        return f"Database error: {error}", 500
    finally:
        # Close the cursor and connection
        cursor.close()
        connection.close()

    return jsonify(response), 200

@app.route('/list-products', methods=['GET'])
def list_products():
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()

    try:
        # Execute the query to fetch the products
        query = "SELECT name, price, availability FROM products"
        cursor.execute(query)

        # Fetch the results
        products = []
        for (name, price, availability) in cursor:
            product = {
                'name': name,
                'price': price,
                'availability': bool(availability)
            }
            products.append(product)
    except mysql.connector.Error as error:
        return f"Database error: {error}", 500
    finally:
        # Close the cursor and connection
        cursor.close()
        connection.close()

    # Create the response JSON
    response = {'products': products}

    return jsonify(response), 200

if __name__ == "__main__":
    # app.run(host="0.0.0.0", port=5000)
    # app.run(host="0.0.0.0", port=443)

    app.run(host="0.0.0.0", port=80)
    # app.run(port=80)
    # app.run( port=5000)
    # app.run()
