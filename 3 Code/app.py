from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import pickle
import math

app = Flask(__name__)
model = pickle.load(open('build.pkl', 'rb'))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
		val1 = request.form['age']
		val2 = request.form['bmi']
		val3 = request.form['children']
		val4 = request.form['gender']
		val5 = request.form['smoker']
		val6 = request.form['region']
		#arr = np.array([[val1,val2,val3,val4,val5,val6]])
		row_df = pd.DataFrame([pd.Series([val1,val2,val3,val4,val5,val6])])

		#arr = arr.astype(np.float)
		#pred = model.predict(row_df)
		prediction=model.predict(row_df)
		#output='{0:.{1}f}'.format(prediction[0][1], 2)
		output = float(prediction)
		

		#return render_template('index.html', predict="Price will be:".format(math.floor(pred)))
		return render_template('index.html', predict=f'Your Insurance Price is {output}')
		

if __name__ == '__main__':
    app.run(debug=True)


	