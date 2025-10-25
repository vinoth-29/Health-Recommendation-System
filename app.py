import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template, redirect, flash, send_file
import pickle
from werkzeug.utils import secure_filename
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, BaggingClassifier, AdaBoostClassifier, VotingClassifier

app = Flask(__name__)  # Initialize the flask App

# Load the pickled models
drug = pickle.load(open('drug.pkl', 'rb'))
dosage = pickle.load(open('dosage.pkl', 'rb'))
side = pickle.load(open('side.pkl', 'rb'))

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/analysis')
def analysis():
    return render_template('analysis.html')

@app.route('/chart')
def chart():
    return render_template('chart.html')

@app.route('/upload')
def upload():
    return render_template('upload.html')

@app.route('/preview', methods=["POST"])
def preview():
    if request.method == 'POST':
        dataset = request.files['datasetfile']
        df = pd.read_csv(dataset, encoding='unicode_escape')
        return render_template("preview.html", df_view=df)

@app.route('/prediction', methods=['GET', 'POST'])
def prediction():
    return render_template('prediction.html', prediction_text="Please fill the details and click on predict")

@app.route('/predict', methods=['POST'])
def predict():
    # Retrieve input values from the form
    int_feature = [x for x in request.form.values()]
    
    # Ensure input is converted into the correct format for prediction
    final_features = np.array([int_feature])

    try:
        # Making predictions using the models
        drug_pred = drug.predict(final_features)
        dosage_pred = dosage.predict(final_features)
        side_pred = side.predict(final_features)

        # Format the prediction results
        dose = str(round(dosage_pred[0], 2))
        label = f"Drug: {drug_pred[0]}, Dosage: {dose} mg, Side-effects: {side_pred[0]}"

        return render_template('prediction.html', prediction_text=label)
    
    except Exception as e:
        # Handle errors in case models or inputs are not as expected
        return render_template('prediction.html', prediction_text=f"Error in prediction: {str(e)}")

@app.route('/login', methods=['GET', "POST"])
def login():
    # Output message if something goes wrong...
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        # Here, replace with your database query or authentication logic
        # Simulating a login check (in reality, check the database)
        if username == "test" and password == "test":
            return redirect(url_for('index'))
        else:
            flash('Incorrect username/password!')
            return redirect(url_for('login'))
    return render_template('login.html', msg=msg)

@app.route('/register', methods=['GET', "POST"])
def register():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form and 'age' in request.form:
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        age = request.form['age']
        # Add validation logic here if needed
        # Simulate registration success
        flash('You have successfully registered! Please proceed to login!')
        return redirect(url_for('login'))
    return render_template('register.html', msg=msg)

if __name__ == "__main__":
    app.run(debug=True)
