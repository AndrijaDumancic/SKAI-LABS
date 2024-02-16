from flask import Flask, request, jsonify

app = Flask(__name__)

# API endpoint to calculate the maximum number of non-overlapping interviews


@app.route('/calculate_max_interviews', methods=['POST'])
def calculate_max_interviews():
    try:
        data = request.json

        # Ensuring both lists are provided in the request
        if 'start_times' not in data or 'end_times' not in data:
            return jsonify({"error": "Both start_times and end_times lists are required"}), 400

        startTimes = data['start_times']
        endTimes = data['end_times']

        # Ensuring both lists have the same length
        if len(startTimes) != len(endTimes):
            return jsonify({"error": "The number of start_times must be equal to the number of end_times"}), 400

        # Sorting the intervals based on their end times
        intervals = sorted(zip(startTimes, endTimes), key=lambda x: x[1])

        # Initializing variables
        maxInterviews = 0
        currentEnd = 0

        # Iterating through the sorted intervals to find the maximum non-overlapping interviews
        for start, end in intervals:
            if start >= currentEnd:
                maxInterviews += 1
                currentEnd = end

        # Return the response with status code 200 (OK)
        return jsonify({"max_interviews": maxInterviews}), 200

    except Exception as e:
        # Return error message with status code 400 (Bad Request) if an exception occurs
        return jsonify({'error': str(e)}), 400


if __name__ == '__main__':
    app.run(debug=True)
