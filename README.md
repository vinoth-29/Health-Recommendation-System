Adaptive Health Recommendation System

* A machine learning-based health recommendation system that predicts diseases based on
* user-entered symptoms and provides personalized drug and treatment suggestions.
* Built with Python and Linear SVC for classification.

Features

* Predicts potential diseases based on user-entered symptoms
* Provides tailored drug and treatment recommendations
* Reduces prescription errors and improves healthcare accessibility
* Built using Linear SVC for classification and pandas for data handling

Tech Stack

* Programming Language: Python
* Machine Learning: scikit-learn (Linear SVC), Pandas, NumPy
* Data: drug.csv, dosage.pkl
* Notebook: side.ipynb for exploration and testing

Getting Started
Prerequisites
* Make sure Python 3.x is installed on your system.
* It is recommended to use a virtual environment.

Install Dependencies
* pip install -r requirements.txt

requirements.txt includes:
* scikit-learn
* pandas
* numpy
* streamlit

Run the Application
* python app.py
* The app loads the trained model dosage.pkl and drug data drug.csv
* Users can input symptoms and receive predicted diseases with recommended medications

Project Structure
* app.py       - Main backend application
* dosage.pkl   - Pre-trained Linear SVC model
* drug.csv     - Drug and treatment dataset
* side.ipynb   - Jupyter Notebook for experimentation and testing
