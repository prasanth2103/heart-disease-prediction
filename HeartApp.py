from flask import Flask, request, render_template    
import pickle  
import numpy as np  
app = Flask(__name__)  
model = pickle.load(open('model.pkl','rb'))
sc=pickle.load(open('scale.pkl','rb'))
@app.route('/')  
def home():
    return render_template('index.html')  
@app.route("/predict", methods=["POST"])  
def predict():  
   age = request.form["age"]  
   sex = request.form["sex"]  
   trestbps = request.form["trestbps"]  
   chol = request.form["chol"]  
   oldpeak = request.form["oldpeak"]  
   thalach = request.form["thalach"]  
   fbs = request.form["fbs"]  
   exang = request.form["exang"]  
   slope = request.form["slope"]  
   cp = request.form["cp"]  
   thal = request.form["thal"]  
   ca = request.form["ca"]  
   restecg = request.form["restecg"]  
   arr = np.array([[age, sex, cp, trestbps,  
            chol, fbs, restecg, thalach,  
            exang, oldpeak, slope, ca,  
            thal]])  
   pred = model.predict(sc.transform(arr))  
   if pred == 0:  
     res_val = "NO HEART PROBLEM"  
   else:  
     res_val = "HEART PROBLEM"  
   return render_template('index.html', Prediction='PATIENT HAS {}'.format(res_val))  
if __name__ == "__main__":  
   app.run(debug=True)  