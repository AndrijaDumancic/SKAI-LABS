# Maximum Non-overlapping Interviews API

## Overview

This Flask API calculates the maximum number of non-overlapping interviews based on provided start and end times. It provides a single endpoint `/calculate_max_interviews` that accepts POST requests with JSON data containing lists of start times and end times. Upon receiving a request, the API validates the input data, sorts the intervals based on end times, iterates through them, and counts the maximum number of non-overlapping interviews. The result is returned as a JSON response.

## How It Works

This Flask API calculates the maximum number of non-overlapping interviews based on provided start and end times. When a POST request is made to the /calculate_max_interviews endpoint with JSON data containing lists of start times and end times, the API first validates the input data. It checks if both start_times and end_times lists are provided and ensures that they have the same number of elements. Next, the intervals (start and end times) are sorted based on their end times. Then, the API iterates through the sorted intervals and counts the maximum number of non-overlapping interviews by tracking the end time of the current interview. Finally, the result (the maximum number of non-overlapping interviews), is returned as a JSON response.

## Getting Started

To run the Flask Maximum Non-overlapping Interviews API, follow these steps:

1. **Clone the Repository**: First, clone or download this repository to your PC.

2. **Navigate to the Project Directory**: Using your terminal or command prompt, navigate to the directory containing the Flask application files.

3. **Install Dependencies**: Before running the application, install the required dependencies by executing the following command:

pip install flask

4. **Run the Application**: Once the dependencies are installed, run the Flask application by executing the following command:

python main.py

5. **Make Requests**: The API will now be running and listening for requests on `http://127.0.0.1:5000/`. You can make POST requests to the `/calculate_max_interviews` endpoint with JSON data containing `start_times` and `end_times` lists to calculate the maximum number of non-overlapping interviews.

## Example Request

You can make a POST request to the `/calculate_max_interviews` endpoint with JSON data similar to the following example:

```json
{
  "start_times": [10, 20, 30, 40, 50, 60],
  "end_times": [15, 25, 35, 45, 55, 65]
}
```
