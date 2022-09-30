from flask import  request
from db import Database
import numpy as np
import pickle
class Task:
    def __init__(self):
        self.prediction_db = Database().get_database()

    def predict(self):
        float_features = [float(x) for x in request.form.values()]
        model = pickle.load(open("model.pkl", "rb"))
 
        features = [np.array(float_features)]
        prediction = model.predict(features)

        model_prediction = {
            "wine_prediction": str(prediction[0]),
            "wine_features": str(float_features)
        }

        # check for existing task
        try: 
        
            self.prediction_db.classifications.insert_one(model_prediction)
        except:
            return {'error': 'Cannot delete.'}
        else:
            return {'error': 'Cannot delete.'}
        

    def get_all(self):
            all_classifications = self.prediction_db.classifications.find({})
            if all_classifications:
                return list(all_classifications)
            else:
                return {'error': 'No classifications available'}
   