#Import Libraries
from flask import Flask, request, render_template
import Model # load model.py
 
app = Flask(__name__)
 
# render htmp page
@app.route('/')
def home():
    return render_template('frontend.html')
 
# get user input and the predict the output and return to user
@app.route('/predict',methods=['POST'])
def predict():
     
    #take data from form and store in each feature    
    input_features = [x for x in request.form.values()]
    bath = input_features[0]
    balcony = input_features[1]
    total_sqft_int = input_features[2]
    bhk = input_features[3]
    area_type = input_features[4]
    location = input_features[5]
     
    # predict the price of house by calling model.py
    predicted_price = Model.predict_house_price(bath,balcony,total_sqft_int,bhk,area_type,location)       
 
 
    # render the html page and show the output
    return render_template('frontend.html', prediction_text='The Predicted Price of House is : {}'.format(predicted_price))
 
# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port="8080")
     
if __name__ == "__main__":
    app.run()