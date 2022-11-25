# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 19:55:49 2022

@author: User
"""

import streamlit as st
import pickle
import pandas as pd
import sklearn
model=pickle.load(open('pipe2.pkl','rb' ))
st.title('Admission Prediction')
def user_input():
    school=st.selectbox('course type', ('Academic', 'Vocational'))
    accreditation=st.selectbox('accreditation',('A', 'B'))
    Gender=st.selectbox('gender', ('Male', 'Female'))
    Interest=st.selectbox('interest', ('Less Interested', 'Very Interested', 'Uncertain', 'Not Interested', 'Quiet Interested'))
    Residence=st.selectbox('residence', ('Urban', 'Rural'))
    grades=st.slider('average grades(bellow 100)',20.0,99.9,50.0)
    parent_in_college=st.selectbox(('was parent in college'), ('False','True'))
    data={'type_school':school,'school_accreditation':accreditation ,
          'gender':Gender,'interest':Interest,'residence':Residence,'average_grades':grades,
          'parent_was_in_college':parent_in_college}
    features=pd.DataFrame(data,index=[0])
    return features
input_df=user_input()
prediction=model.predict(input_df)
predict=st.button('Prediction')
if  predict:

    if prediction==1 :
        st.header('You Will Get Admission')
    else:
        st.header('Sorry You wiil not get Admission')