from flask import Flask, render_template, request, jsonify
from config import supabase

app = Flask(__name__)

# Sample product data
products = [
    {"id": 1, "name": "Laptop", "price": 599.99, "image": "https://via.placeholder.com/150"},
    {"id": 2, "name": "Smartphone", "price": 299.99, "image": "https://via.placeholder.com/150"},
    {"id": 3, "name": "Headphones", "price": 49.99, "image": "https://via.placeholder.com/150"}
]

@app.route('/')
def home():
    return render_template('index.html', products=products)

@app.route('/submit_order', methods=['POST'])
def submit_order():
    data = request.json
    name = data.get('name')
    address = data.get('address')
    payment = data.get('payment')
    product = data.get('product')

    try:
        # Insert data into Supabase
        response = supabase.table("orders").insert({
            "name": name,
            "address": address,
            "payment": payment,
            "product": product
        }).execute()

        print("Supabase Response:", response)  # Debugging line

        # Ensure response has "data" and it's not empty
        if response and "data" in response and response["data"]:
            return jsonify({"message": f"Unexpected Supabase response: {response}"}), 201
        else:
            return jsonify({"message": "Order placed successfully!"}), 500 

    except Exception as e:
        return jsonify({"message": f"Error: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
