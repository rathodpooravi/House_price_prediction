from flask import Flask, jsonify, request, render_template
import config
import My_API
from My_API.utills import HousePrice

app = Flask(__name__)


@app.route('/')
def price_model():
    print('Welcome to the House Price Prediction Model')
    return render_template('index.html')


@app.route('/predict_price', methods = ['POST','GET'])
def get_price_rate():
    if request.method == 'POST':
        print('We are in POST Method')
        data = request.form
        area = eval(data['area'])
        bedrooms = data['bedrooms']
        bathrooms = eval(data['bathrooms'])
        stories =  eval(data['stories'])
        mainroad = data['mainroad']
        guestrooms = data['guestrooms']
        basement = data['basement']
        hotwaterheating = data['hotwaterheating']
        airconditioning = data['airconditioning']
        parking =  eval(data['parking'])
        prefarea = data['prefarea']
        furnishingstatus = data['furnishingstatus']
        
        house_pr =  HousePrice(area, bedrooms, bathrooms, stories, mainroad,guestrooms,basement,hotwaterheating,airconditioning,parking,prefarea,furnishingstatus)
        Rates = house_pr.get_prdict_price()
        return jsonify({'Result': f'House rate are: Rs. {round(Rates,2)}'})
    
    else:
        print('We are in GET Method')
        data1 = request.args
        area = eval(data1.get('area'))
        bedrooms = data1.get('bedrooms')
        bathrooms = data1.get('bathrooms')
        stories = eval(data1.get('stories'))
        mainroad = data1.get('mainroad')
        guestrooms = data1.get('guestrooms')
        basement = data1.get('basement')
        hotwaterheating = data1.get('hotwaterheating')
        airconditioning = data1.get('airconditioning')
        parking = data1.get('parking')
        prefarea = data1.get('prefarea')
        furnishingstatus = data1.get('furnishingstatus')
        
        house_pr1=  HousePrice(area, bedrooms, bathrooms, stories, mainroad,guestrooms,basement,hotwaterheating,airconditioning,parking,prefarea,furnishingstatus)
        Rates1 = house_pr1.get_prdict_price()
        return jsonify({'Result': f'House rate are: Rs. {round(Rates1,2)}'})

        print(data1)




if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = config.PORT_NUMBER, debug=True)