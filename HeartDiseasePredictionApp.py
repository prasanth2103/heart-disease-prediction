from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
#import pickle  
import numpy as np
import pandas as pd

data=pd.read_csv('heart.csv')

x=data.drop(columns=['target'])
y=data['target']

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=2)

from sklearn.preprocessing import MinMaxScaler
s=MinMaxScaler()
x_train=s.fit_transform(x_train)
x_test=s.transform(x_test)

from sklearn.ensemble import RandomForestClassifier
RFmodel=RandomForestClassifier(n_estimators=50,random_state=0)
RFmodel.fit(x_train,y_train)

#model = pickle.load(open('model.pkl','rb'))
#sc=pickle.load(open('scale.pkl','rb'))


def predict():
    age = e1.get()  
    sex = e2.get()  
    cp = e3.get()
    trestbps = e4.get()
    chol = e5.get()
    fbs = e6.get()
    restecg = e7.get()
    thalach = e8.get()
    exang = e9.get()
    oldpeak = e10.get()
    slope = e11.get()
    ca = e12.get()
    thal = e13.get()
    arr = np.array([[age, sex, cp, trestbps,  
            chol, fbs, restecg, thalach,  
            exang, oldpeak, slope, ca,  
            thal]])
    pred = RFmodel.predict(s.transform(arr))
    if pred == 0:
        messagebox.showinfo("Prediction","PATIENT DOES NOT HAS HEART PROBLEM!")
    else:
        messagebox.showinfo("Prediction","PATIENT HAS HEART PROBLEM!\nPLEASE CONSULT THE DOCTOR") 


root=Tk()
root.geometry("600x600")
root.title("HEART DISEASE PREDICTION")

bg = ImageTk.PhotoImage(Image.open("heart.png"))
canvas1 = Canvas( root, width = 600,
                 height = 600)
  
canvas1.pack(fill = "both", expand = True)
canvas1.create_image( 0, 0, image = bg,anchor=NW)


ttk.Label(root, text = "Heart Disease Prediction", 
          background = 'black', foreground ="white", 
          font = ("Times New Roman", 15)).place(x=130,y=10)

global e1
global e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13

Label(root,text="AGE").place(x=100,y=50)
e1=Entry(root,width=20)
e1.place(x=160,y=50)
Label(root,text="(1-100)").place(x=285,y=50)

Label(root,text="SEX").place(x=100,y=80)
e2=Entry(root,width=20)
e2.place(x=160,y=80)
Label(root,text="(Male : 1 & Female : 0)").place(x=285,y=80)

Label(root,text="CP").place(x=100,y=110)
e3=Entry(root,width=20)
e3.place(x=160,y=110)
Label(root,text="(Chest Pain Type : 0-3)").place(x=285,y=110)

Label(root,text="TRESTBPS").place(x=100,y=140)
e4=Entry(root,width=20)
e4.place(x=160,y=140)
Label(root,text="(Resting Blood Pressure:Non-Decimal)").place(x=285,y=140)

Label(root,text="CHOL").place(x=100,y=170)
e5=Entry(root,width=20)
e5.place(x=160,y=170)
Label(root,text="(Serum Cholesterol:Non-Decimal)").place(x=285,y=170)

Label(root,text="FBS").place(x=100,y=200)
e6=Entry(root,width=20)
e6.place(x=160,y=200)
Label(root,text="(Fasting Blood Sugar : 0-1)").place(x=285,y=200)

Label(root,text="RESTECG").place(x=100,y=230)
e7=Entry(root,width=20)
e7.place(x=160,y=230)
Label(root,text="(Resting Electrocardiographic Result : 0-2)").place(x=285,y=230)

Label(root,text="THALACH").place(x=100,y=260)
e8=Entry(root,width=20)
e8.place(x=160,y=260)
Label(root,text="(Max Heart Rate)").place(x=285,y=260)

Label(root,text="EXANG").place(x=100,y=290)
e9=Entry(root,width=20)
e9.place(x=160,y=290)
Label(root,text="(Exercise-Induced Angina : 0-1)").place(x=285,y=290)

Label(root,text="OLDPEAK").place(x=100,y=320)
e10=Entry(root,width=20)
e10.place(x=160,y=320)
Label(root,text="(ST Depression:Decimal)").place(x=285,y=320)

Label(root,text="SLOPE").place(x=100,y=350)
e11=Entry(root,width=20)
e11.place(x=160,y=350)
Label(root,text="(Slope of the Peak : 0-2)").place(x=285,y=350)

Label(root,text="CA").place(x=100,y=380)
e12=Entry(root,width=20)
e12.place(x=160,y=380)
Label(root,text="(Number of Major Vessels : 0–3)").place(x=285,y=380)

Label(root,text="THAL").place(x=100,y=410)
e13=Entry(root,width=20)
e13.place(x=160,y=410)
Label(root,text="(Thalassemia : 1-3)").place(x=285,y=410)

predict=Button(root,text="PREDICT",command=predict,bg="green",fg="white").place(x=200,y=450)

root.mainloop()
