
#request for get and post
#from flask import Flask,request
import pandas as pd
import numpy as np
import pickle
#import flasgger
#from flasgger import Swagger
import streamlit as st

from PIL import Image

#app=Flask(__name__)
#Swagger(app)

pickle_in=open('classifier.pkl','rb')
#read bytes,rb,importing classifier.pkl
classifier=pickle.load(pickle_in)

#@app.route('/')
def welcome():
    return "Welcome all"

#@app.route('/predict')
def predict_note_authentication(variance,skewness,curtosis,entropy):
    
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
    prediction=classifier.predict([[variance,skewness,curtosis,entropy]])
    print(prediction)
    return prediction
def main():
    st.title("Bank Authenticator")
    html_temp="""
    <div style="background-color:green;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Bank Authenticator ML App</h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    variance=st.text_input("Variance","Type Here")
    skewness=st.text_input("Skewness","Type Here")
    curtosis=st.text_input("Curtosis","Type Here")
    entropy=st.text_input("Entropy","Type Here")
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(variance,skewness,curtosis,entropy)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets Learn")
        st.text("Built with Streamlit")
if __name__=='__main__':
    main()



