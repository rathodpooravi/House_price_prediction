import pickle
import json
import config
import numpy as np

class HousePrice():

    def __init__(self, area, bedrooms, bathrooms, stories, mainroad, guestrooms,
                basement, hotwaterheating, airconditioning, parking, prefarea, furnishingstatus) :
        self.area = area
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.stories = stories
        self.mainroad = mainroad
        self.guestrooms = guestrooms
        self.basement = basement
        self.hotwaterheating = hotwaterheating
        self.airconditioning = airconditioning
        self.parking = parking
        self.prefarea = prefarea
        self.furnishingstatus = furnishingstatus
    
    def load_model(self):
        with open(config.MODEL_FILE_PATH, 'rb') as f:
            self.model = pickle.load(f)

        with open(config.JSON_FILE_PATH, 'r') as f:
            self.project_data = json.load(f)
            
    
    def get_prdict_price(self):
        self.load_model()
        
        test_array=np.zeros(len(self.project_data['columns']))
        test_array[0]=self.area
        test_array[1]=self.bedrooms
        test_array[2]=self.bathrooms
        test_array[3]=self.stories
        test_array[4]=self.project_data['mainroad'][self.mainroad]
        test_array[5]=self.project_data['guestrooms'][self.guestrooms]
        test_array[6]=self.project_data['basement'][self.basement]
        test_array[7]=self.project_data['hotwaterheating'][self.hotwaterheating]
        test_array[8]=self.project_data['airconditioning'][self.airconditioning]
        test_array[9]=self.parking
        test_array[10]=self.project_data['prefarea'][self.prefarea]
        test_array[11]=self.project_data['furnishingstatus'][self.furnishingstatus]
        print('Test Array :',test_array)
        
        predicted_price = self.model.predict([test_array])[0]
        print(f'Rate of House is: Rs. {round(predicted_price,2)}')
        return predicted_price

if __name__=='__main__':
    area = 1000
    bedrooms=3
    bathrooms=2
    stories=2
    mainroad='yes'
    guestrooms='yes'
    basement='no'
    hotwaterheating='no'
    airconditioning='yes'
    parking=1
    prefarea='no'
    furnishingstatus='furnished'

        
    
    