
from flask import Flask, request, jsonify
import csv
from flask_cors import CORS, cross_origin
import json

app = Flask(__name__)

CORS(app)

@app.route("/", methods=["GET", "POST"])
# Load CSV data into memory
def load_data():
    data = {}
    # Assuming you have a CSV file named products.csv
    with open('C:/Users/aalili002/Desktop/Oued kniss watches.csv', 'r',newline='', encoding="utf-8") as file:
        reader = csv.DictReader(file)
        data['products'] = list(reader)
    return data

# Global variable to hold the loaded data
loaded_data = load_data()

@app.route("/api", methods = ["GET", "POST"])
def parse():
    return {"test": "json"}



# API endpoint to fetch price and URL for matching/similar products
@app.route('/fetch-products', methods=["GET","POST"])
def fetch_products():

    product_name = request.get_json()

    #print(json.loads(jsonify(product_name)))
    if not product_name:
        return jsonify({'error': 'Product name is required'})
    
    #print(product_name)


    for key, value in product_name.items():
        #print(key)
        value = value

    print(value)

    products = loaded_data.get('products', []) 
  
    # Filter products based on product name (case-insensitive)
    matching_products = [product for product in products if product.get('Products').lower().strip() == product_name["Products"].lower().strip()]

    # Extract price and URL for matching/similar products
    

    if len(matching_products) == 0 :
        return jsonify([{"Product availability status":"0"}])
    else :
        result = [{ 'Product availability status': '1' ,"Name":product.get('Products').strip(),'Price': product.get('Price').strip(), 'URL': product.get('URL')} for product in matching_products]
    #print(products[0].get('Products').lower())
    #print(type(jsonify(result)))
        return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)