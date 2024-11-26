import uvicorn
from fastapi import FastAPI
from HeartDisease import HeartDisease
import numpy as np
import pickle
import pandas as pd
import xgboost as xgb


app = FastAPI()
pickle_in = open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)

"""classifier = xgb.Booster()
classifier.load_model("classifier.json")
"""

@app.get('/')
def index():
    return {'message': 'Hello, World'}

# 4. Route with a single parameter, returns the parameter within a message
#    Located at: http://127.0.0.1:8000/AnyNameHere
@app.get('/{name}')
def get_name(name: str):
    return {'Welcome To My Project': f'{name}'}

# 3. Expose the prediction functionality, make a prediction from the passed
#    JSON data and return the predicted Bank Note with the confidence

@app.post('/predict')
async def predict_heartdisease(data: dict):
    try:

        Age=int(data['Age'])
        Sex=int(data['Sex'])
        RestingBP=int(data['RestingBP'])
        Cholesterol=int(data['Cholesterol'])
        FastingBS=int(data['FastingBS']) 
        MaxHR=int(data['MaxHR'])
        ExerciseAngina=int(data['ExerciseAngina'])
        Oldpeak=float(data['Oldpeak'])
        ST_Slope=float(data['ST_Slope'])
        ChestPainType_ATA=int(data['ChestPainType_ATA'])
        ChestPainType_NAP=int(data['ChestPainType_NAP'])
        ChestPainType_TA=int(data['ChestPainType_TA'])
        RestingECG_Normal=int(data['RestingECG_Normal'])
        RestingECG_ST=int(data['RestingECG_ST'])

        input_data = [[Age, Sex, RestingBP, Cholesterol, FastingBS, MaxHR, ExerciseAngina, Oldpeak, ST_Slope, ChestPainType_ATA, ChestPainType_NAP, ChestPainType_TA, RestingECG_Normal, RestingECG_ST]] 
        prediction = classifier.predict(input_data)
        return {"prediction": int(prediction[0])}

    except ValueError as e:
        return {"error": f"Veri türü hatası: {str(e)}"}    

    """prediction = classifier.predict([[Age, Sex, RestingBP, Cholesterol, FastingBS, MaxHR, ExerciseAngina, Oldpeak, ST_Slope, ChestPainType_ATA, ChestPainType_NAP, ChestPainType_TA, RestingECG_Normal, RestingECG_ST]])
    
    if(prediction[0]>0.5):
        prediction="Heart disease detected"
    else:
        prediction="No heart disease detected"

    return {
        'prediction': prediction
    }"""


# 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)