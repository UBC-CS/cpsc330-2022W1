from flask import Flask, request, jsonify
import joblib

# 1. create an instance of the Flask class
app = Flask(__name__)

# 2. define a prediction function
def return_prediction(pipe_lr, text):   
    print('text: ', text)
    prediction = pipe_lr.predict([text])[0]    
    return prediction

# 3. load our moment predictor model
model = joblib.load('moment_predictor.joblib')

# 4. set up our home page
@app.route("/")
def index():
    return """
    <h1>Welcome to our moment prediction service</h1>
    To use this service, write your moment text here. 
    </ul>
    """

# 5. define a new route which will accept POST requests and return our model predictions
@app.route('/predict', methods=["GET", "POST"])
def moment_prediction():
    content = request.json
    results = return_prediction(model, content['text'])
    return jsonify(results)

# 6. allows us to run flask using $ python app.py
if __name__ == '__main__':
    app.run()
