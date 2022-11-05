# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 18:22:02 2022

@author: User
"""

import streamlit as st
import pickle
import numpy as np
import pandas as pd
import sklearn
model=pickle.load(open('C:/Users/User/Documents/college_prediction/pipe2.pkl','rb' ))
type_school=['Academic', 'Vocational']
school_accreditation=['A', 'B']
gender=['Male', 'Female']
interest=['Less Interested', 'Very Interested', 'Uncertain', 'Not Interested', 'Quiet Interested']
residence=['Urban', 'Rural']
parent_was_in_college=[False,  True]
st.title('College Admision  Prediction ')
st.selectbox('type_of_school',(type_school))
st.selectbox('Accreditaion',sorted(school_accreditation))
st.selectbox('Gender', sorted(gender))
st.selectbox('interest',sorted(interest))
st.selectbox('Type of Residence',sorted(residence))
st.selectbox('was parant in college',sorted(parent_was_in_college))
average_grades=st.number_input('Average grades')
if st.button('Predict '):
    input_df=pd.DataFrame({'type_school':[type_school],'school_accreditation':[school_accreditation],'gender':[gender],'interest':[interest],'residence':[residence],'average_grades':[average_grades],'parent_was_in_college':[parent_was_in_college]})
    result=model.predict(input_df)   