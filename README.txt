Fish Weight Predictor

Introduction
The Fish Weight Predictor is a web application that predicts the weight of a fish based on its measurements. This project leverages a machine learning model trained on the Fish Market dataset to perform regression analysis and provide weight predictions.

Features
User-Friendly Interface: Simple and intuitive web interface for inputting fish measurements.
Accurate Predictions: Utilizes a regression model to predict fish weight based on length, height, and width measurements.
Deployment: Hosted on Heroku for easy access and use.
Dataset
The dataset used in this project is the Fish Market dataset from Kaggle. It includes measurements and weights of different fish species, which are used to train the regression model.

Model
The model is a linear regression model built using Python's scikit-learn library. The features used for prediction are:

1)Length1
2)Length2
3)Length3
4)Height
5)Width
The target variable is the weight of the fish.

Installation
To run this project locally, follow these steps:

Clone the repository:

git clone https://github.com/human351/fish-weight-predictor
cd fish-weight-predictor

Install the required dependencies:

pip install -r requirements.txt

Run the Flask application:

python app.py

Access the application:
Open your web browser and go to http://127.0.0.1:5000.

Usage
To use the deployed application:

Visit the Heroku URL.
Enter the fish measurements (Length1, Length2, Length3, Height, Width) in the provided form.
Click on the "Predict Weight" button to get the predicted weight of the fish.

Deployment
The application is deployed on Heroku. Follow these steps to deploy the application:

Create a Heroku account: If you don't have one, sign up at Heroku.
Install the Heroku CLI: Follow the instructions here.
Login to Heroku:

heroku login

Create a new Heroku app:

heroku create [your-app-name]
Push the code to Heroku:

git push heroku main
Scale the dynos:

heroku ps:scale web=1
Open the app:

heroku open