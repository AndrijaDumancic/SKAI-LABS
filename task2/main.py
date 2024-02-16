from flask import Flask, request, jsonify

app = Flask(__name__)

# API endpoint to check for unauthorized sales


@app.route('/unauthorized-sales', methods=['POST'])
def unauthorized_sales():
    try:
        # Extracting JSON data from the request
        data = request.get_json()

        # Extracting product listings and sales transactions from the data
        productListings = data.get('productListings', [])
        salesTransactions = data.get('salesTransactions', [])

        # Create a dictionary to store authorized sellers for each product
        authorizedSales = {
            listing['productID']: listing['authorizedSellerID'] for listing in productListings
        }

        # Create a dictionary to store unauthorized sellers for each product
        unauthorizedSales = {}

        # Check each sales transaction for unauthorized sellers
        for transaction in salesTransactions:
            productID = transaction['productID']
            sellerID = transaction['sellerID']
            authorizedSellerID = authorizedSales.get(productID)

            # If the seller is not authorized for the product, add them to the unauthorized sales
            if authorizedSellerID and authorizedSellerID != sellerID:
                if productID not in unauthorizedSales:
                    unauthorizedSales[productID] = []
                unauthorizedSales[productID].append(sellerID)

        # Prepare the response JSON
        response = {
            'unauthorizedSales': [
                {
                    'productID': productID,
                    'unauthorizedSellerIDs': unauthorizedSellers
                }
                for productID, unauthorizedSellers in unauthorizedSales.items()
            ]
        }

        # Return the response with status code 200 (OK)
        return jsonify(response), 200

    except Exception as e:
        # Return error message with status code 400 (Bad Request) if an exception occurs
        return jsonify({'error': str(e)}), 400


if __name__ == '__main__':
    app.run(debug=True)
