from flask import Flask,render_template,request
import joblib
import numpy as np

model=joblib.load('heart_risk_prediction_regression_model.sav')

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


	test_data=np.array([gender,age,tc,hdl,smoke,bpm,diab]).reshape(1,-1)
	

	prediction=model.predict(test_data)
	# calculates  heart disease risk

   

	resultDict={"name":name,"risk":round(prediction[0][0],2)}
	#Rounds risk to 2 decimal places

#Stores name + risk together

	return render_template('patient_results.html',results=resultDict)

app.run(debug=True)

