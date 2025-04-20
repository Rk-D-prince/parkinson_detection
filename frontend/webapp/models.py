from django.db import models


import numpy as np
import pickle



import joblib
import numpy as np
import pandas as pd
#from sklearn.preprocessing import LabelEncoder

from sklearn.preprocessing import LabelEncoder

svm = pickle.load(open(r'C:\Users\RAJA KANNAN\Music\PARKINSON\CODING\frontend\svc_park.pkl', 'rb'))
# log = pickle.load(open('G:\PYTHON 2020-21 BACKUPS\ITML09_FLIGHT_DELAYS\FINAL CODE\FRONT END\Flight_Delays_Prediction\flight_delays_log.pkl', 'rb'))
# svm = pickle.load(open('G:\PYTHON 2020-21 BACKUPS\ITML09_FLIGHT_DELAYS\FINAL CODE\FRONT END\Flight_Delays_Prediction\flight_delays_svm.pkl', 'rb'))
xgb = pickle.load(open(r'C:\Users\RAJA KANNAN\Music\PARKINSON\CODING\frontend\xgb_park.pkl', 'rb'))



data = pd.read_csv('Parkinsons_test.csv')

# x = data.drop(['Unnamed: 0'],axis=1)

def predict(algo,row):
	#print(x.columns)
	test_data=data.iloc[row].values.reshape(1,-1)
	print(test_data.shape)
	#print(test_data.columns)
	if algo == 'dt':
		y_pred = dtc.predict(test_data)
	elif algo == 'log':
		y_pred = log.predict_proba(test_data)
	elif algo == 'svm':
		y_pred = svm.predict(test_data)
	elif algo == 'xgb':
		y_pred = xgb.predict(test_data)
	return y_pred

	

