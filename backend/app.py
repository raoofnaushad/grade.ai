from flask import Flask, request, jsonify

from src import grader

app = Flask(__name__)

# Default route for GET request
@app.route('/', methods=['GET'])
def home():
    try:
        message = "grader.ai is working successfullyy"
        print("Home route accessed successfully.")
        return jsonify({"status": True, "message": message})
    except Exception as e:
        print(f"Error in home route: {e}")
        return jsonify({"status": False, "message": str(e)})

# Default route for GET request
@app.route('/raoof', methods=['GET'])
def raoof():
    try:
        message = "Raoof is awesome!"
        print("Raoof route accessed successfully.")
        return jsonify({"status": True, "message": message})
    except Exception as e:
        print(f"Error in raoof route: {e}")
        return jsonify({"status": False, "message": str(e)})

# Route for POST request
@app.route('/evaluate', methods=['POST'])
def evaluate():
    try:
        # Extract parameters from the request
        data = request.get_json()
        print(f"Received data for evaluation: {data}")
        questions = data.get('questions')
        rubrics = data.get('rubrics')
        answers = data.get('answers')
        
        # Call the evaluation function
        result = grader.evaluate_grader(questions, rubrics, answers)
        print(f"Evaluation result: {result}")
        
        # Return the result as a JSON response
        return jsonify({"status": True, "message": result})
    except Exception as e:
        print(f"Error in evaluate route: {e}")
        return jsonify({"status": False, "message": str(e)})

if __name__ == '__main__':
    app.run(debug=True)