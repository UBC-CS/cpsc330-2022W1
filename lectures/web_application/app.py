# 1. Imports
from flask import Flask, render_template, session, url_for, redirect
from flask_wtf import FlaskForm
from wtforms import TextField, SubmitField
import joblib

# 2. create an instance of the Flask class
app = Flask(__name__)
app.config['SECRET_KEY'] = 'asecretkey'

# 3. define a prediction function
def return_prediction(model, input_json):

    features = ['length', 'diameter', 'height', 'whole_weight']
    input_data = [[input_json[k] for k in features]]
    prediction = model.predict(input_data)[0]

    return prediction

# 4. load our abalone age predictor model
model = joblib.load('abalone_predictor.joblib')

# 5. create a WTForm Class
class PredictForm(FlaskForm):

    length = TextField("Shell length")
    diameter = TextField("Shell diameter")
    height = TextField("Shell height")
    whole_weight = TextField("Whole weight")
    submit = SubmitField("Predict")

# 6. set up our home page
@app.route("/", methods=["GET", "POST"])
def index():

    # Create instance of the form
    form = PredictForm()

    # Validate the form
    if form.validate_on_submit():
        session['length'] = form.length.data
        session['diameter'] = form.diameter.data
        session['height'] = form.height.data
        session['whole_weight'] = form.whole_weight.data
        return redirect(url_for("prediction"))

    return render_template('home.html', form=form)

# 7. define a new "prediction" route that processes form input and returns a model prediction
@app.route('/prediction')
def prediction():

    content = {}
    content['length'] = float(session['length'])
    content['diameter'] = float(session['diameter'])
    content['height'] = float(session['height'])
    content['whole_weight'] = float(session['whole_weight'])
    results = return_prediction(model, content)
    return render_template('prediction.html', results=results)

# 8. allows us to run flask using $ python app.py
if __name__ == '__main__':
    app.run()

