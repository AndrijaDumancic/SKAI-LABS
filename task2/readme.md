# Unauthorized Sales API

## Overview

This project implements a Flask API to detect unauthorized sales based on provided product listings and sales transactions. It uses Flask, to create an HTTP server that listens for POST requests on the `/unauthorized-sales` endpoint. Upon receiving a POST request, the API analyzes the provided data to identify unauthorized sales and returns a JSON response containing information about the unauthorized sales.

## How It Works

The Flask API consists of a single route `/unauthorized-sales`, which accepts POST requests. Upon receiving a POST request, the API expects JSON data containing product listings and sales transactions. It then compares the seller IDs from the sales transactions with the authorized seller IDs specified in the product listings to identify unauthorized sales. The API constructs a JSON response containing information about the unauthorized sales, including the product ID and the seller IDs of unauthorized sellers.

## Getting Started

To run the Flask Unauthorized Sales API, follow these steps:

1. **Clone the Repository**: First, clone or download this repository to your PC.

2. **Navigate to the Project Directory**: Using your terminal or command prompt, navigate to the directory containing the Flask application files.

3. **Install Dependencies**: Before running the application, install the required dependencies by executing the following command:

pip install flask

4. **Run the Application**: Once the dependencies are installed, run the Flask application by executing the following command:

python main.py

5. **Make Requests**: The Flask API will now be running and listening for requests on `http://127.0.0.1:5000/`. You can make POST requests to the `/unauthorized-sales` endpoint with JSON data containing product listings and sales transactions to detect unauthorized sales.

## Example Request

You can make a POST request to the `/unauthorized-sales` endpoint with JSON data similar to the following example:

```json
{
  "productListings": [{"productID": "123", "authorizedSellerID": "A1"}],
  "salesTransactions": [{"productID": "123", "sellerID": "B2"}]
}
```
