# -*- coding: utf-8 -*-
"""
@author: Pavan Kumar
"""


import numpy as np
import pickle
import pandas as pd
#from flasgger import Swagger
import streamlit as st 
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from PIL import Image

#app=Flask(__name__)
#Swagger(app)

pickle_in = open("model3.pkl","rb")
classifier=pickle.load(pickle_in)

#@app.route('/')
def welcome():
    return "Welcome All"

#@app.route('/predict',methods=["Get"])
def predict_churn(tenure,PhoneService,Contract,PaperlessBilling,PaymentMethod,MonthlyCharges,TotalCharges,gender,SeniorCitizen,Partner,Dependents,MultipleLines,InternetService,OnlineSecurity,OnlineBackup,DeviceProtection,TechSupport,StreamingTV,StreamingMovies):
    
    """Let's Authenticate the Banks Note 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: variance
        in: query
        type: number
        required: true
      - name: skewness
        in: query
        type: number
        required: true
      - name: curtosis
        in: query
        type: number
        required: true
      - name: entropy
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
        
    """
   
    prediction=classifier.predict([[tenure,PhoneService,Contract,PaperlessBilling,PaymentMethod,MonthlyCharges,TotalCharges,gender,SeniorCitizen,Partner,Dependents,MultipleLines,InternetService,OnlineSecurity,OnlineBackup,DeviceProtection,TechSupport,StreamingTV,StreamingMovies]])
    print(prediction)
    return prediction

def main():
    st.title("App to predict churn")
    html_temp = """
    <div style="background-color: orange;padding:10px">
    <h2 style="color:white;text-align:center;"> Please enter the values.</h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)

   
    
    tenure = st.text_input("Enter tenure","Type Here")

    PhoneService = st.text_input("Enter phoneservice","Type Here")

    
    
    display = ("Month-to-Month", "One year","Two year")
    options = list(range(len(display)))
    value = st.selectbox("Contract type", options, format_func=lambda x: display[x])
    Contract=value

    display = ("Yes", "No")
    options = list(range(len(display)))
    value = st.selectbox("Type of billing?", options, format_func=lambda x: display[x])
    PaperlessBilling=value

    display = ("Bank transfer (automatic)", "Credit card (automatic)","Electronic check","Mailed check")
    options = list(range(len(display)))
    value = st.selectbox("Mode of payment?", options, format_func=lambda x: display[x])
    PaymentMethod=value
    
    MonthlyCharges = st.text_input("Monthly charges","Type Here")
    
    TotalCharges = st.text_input("Total charges","Type Here")

    display = ("Male","Female")
    options = list(range(len(display)))
    value = st.selectbox("Gender", options, format_func=lambda x: display[x])
    gender=value

    display = ("0","1")
    options = list(range(len(display)))
    value = st.selectbox("SeniorCitizen", options, format_func=lambda x: display[x])
    SeniorCitizen=value

    display = ("Yes","No")
    options = list(range(len(display)))
    value = st.selectbox("Partner", options, format_func=lambda x: display[x])
    Partner=value

    display = ("Yes","No")
    options = list(range(len(display)))
    value = st.selectbox("Dependents", options, format_func=lambda x: display[x])
    Dependents=value

    display = ("Yes","No")
    options = list(range(len(display)))
    value = st.selectbox("Multiple lines", options, format_func=lambda x: display[x])
    MultipleLines=value

    display = ("DSL","FIBER OPTIC","No")
    options = list(range(len(display)))
    value = st.selectbox("Type of internet service", options, format_func=lambda x: display[x])
    InternetService=value

    display = ("Yes","No")
    options = list(range(len(display)))
    value = st.selectbox("Online Security", options, format_func=lambda x: display[x])
    OnlineSecurity=value

    display = ("Yes","No")
    options = list(range(len(display)))
    value = st.selectbox("Online Backup", options, format_func=lambda x: display[x])
    OnlineBackup=value

    display = ("Yes","No")
    options = list(range(len(display)))
    value = st.selectbox("Device protection", options, format_func=lambda x: display[x])
    DeviceProtection=value

    display = ("Yes","No")
    options = list(range(len(display)))
    value = st.selectbox("Tech support", options, format_func=lambda x: display[x])
    TechSupport=value

    display = ("Yes","No")
    options = list(range(len(display)))
    value = st.selectbox("Streaming tv", options, format_func=lambda x: display[x])
    StreamingTV=value

    display = ("Yes","No")
    options = list(range(len(display)))
    value = st.selectbox("Streaming movies", options, format_func=lambda x: display[x])
    StreamingMovies=value
   
    result=""
    if st.button("Predict"):
      tenure=float(tenure)
      PhoneService=float(PhoneService)
      Contract=float(Contract)
      PaperlessBilling=float(PaperlessBilling)
      PaymentMethod=float(PaymentMethod)
      MonthlyCharges=float(MonthlyCharges)
      TotalCharges=float(TotalCharges)
      gender=float(gender)
      SeniorCitizen=float(SeniorCitizen)
      Partner=float(Partner)
      Dependents=float(Dependents)
      MultipleLines=float(MultipleLines)
      InternetService=float(InternetService)
      OnlineSecurity=float(OnlineSecurity)
      OnlineBackup=float(OnlineBackup)
      DeviceProtection=float(DeviceProtection)
      TechSupport=float(TechSupport)
      StreamingTV=float(StreamingTV)
      StreamingMovies=float(StreamingMovies)

      result=predict_churn(tenure,PhoneService,Contract,PaperlessBilling,PaymentMethod,MonthlyCharges,TotalCharges,gender,SeniorCitizen,Partner,Dependents,MultipleLines,InternetService,OnlineSecurity,OnlineBackup,DeviceProtection,TechSupport,StreamingTV,StreamingMovies)
    st.success('The status is {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()
