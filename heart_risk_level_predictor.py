from flask import Flask,render_template,request
import joblib
import numpy as np

model=joblib.load('heart_risk_prediction_regression_model.sav')
#The machine learning model was already trained earlier

#It is saved as a .sav file

#joblib.load() loads it into memory

#👉 Interview line:

#“We load a pre-trained regression model using Joblib to make predictions.”

app=Flask(__name__) #application

@app.route('/')
def index():

	# Landing / welcome page
	return render_template('welcome.html')

@app.route('/predict')
def predict():

	# Shows the patient details / input form
	return render_template('patient_details.html')

@app.route('/getresults',methods=['POST'])
def getresults():

	result=request.form   #This collects all input fields from the HTML form.

	name=result['name']
	gender=float(result['gender'])
	age=float(result['age'])
	tc=float(result['tc'])
	hdl=float(result['hdl'])
	sbp=float(result['sbp'])
	smoke=float(result['smoke'])
	bpm=float(result['bpm'])
	diab=float(result['diab'])

	#Why float()?

#ML models only understand numbers

#HTML sends values as strings

#👉 Interview line:

#“Form inputs are converted into numerical values for model compatibility.”

	test_data=np.array([gender,age,tc,hdl,smoke,bpm,diab]).reshape(1,-1)
	#“The input data is reshaped into a 2D array before prediction.”

	prediction=model.predict(test_data)
	#The model calculates the heart disease risk

    #Output is usually an array like [[23.5678]]

	resultDict={"name":name,"risk":round(prediction[0][0],2)}
	#Rounds risk to 2 decimal places

#Stores name + risk together

	return render_template('patient_results.html',results=resultDict)

app.run(debug=True)

#Starts Flask server

#debug=True:

#Shows errors

#Auto-reloads code changes

#👉 Interview line:

#“Debug mode helps during development.”