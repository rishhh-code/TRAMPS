from lastpost import r
import json
import joblib
import numpy as np
json_data = r.replace('\r', '').replace('\n', '')
data = json.loads(json_data)
N_stv = int(data['soilRatings'][0]['N_STV'])
P_stv = int(data['soilRatings'][0]['P_STV'])
K_stv = int(data['soilRatings'][0]['K_STV'])
pH = float(data['soilRatings'][0]['pH'])
crop = 17
model = joblib.load('model.pkl')

x_new = np.array([[N_stv,P_stv,K_stv,pH,crop]])

model.predict(x_new)