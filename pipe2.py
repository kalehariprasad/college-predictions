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
data=pickle.load(open('C:/Users/User/Documents/college_prediction/data.pkl','rb' ))
type_school=data['type_school'].unique()
school_accreditation=data['school_accreditation'].unique()
gender=data['gender'].unique()
interest=data['interest'].unique()
residence=data['residence'].unique()
parent_was_in_college=data['parent_was_in_college'].unique()
st.title('College Admision  Prediction ')
st.selectbox('type_of_school',type_school)
st.selectbox('Accreditaion',school_accreditation)
st.selectbox('Gender', gender)
st.selectbox('interest',interest)
st.selectbox('Type of Residence',residence)
st.selectbox('was parant in college',parent_was_in_college)
parent_age=st.number_input('Parent Age')
parent_salary=st.number_input('Parent Salary')
house_area=st.number_input('House area')
average_grades=st.number_input('Average grades')
if st.button('predict'):
    input_df=np.array([type_school,school_accreditation,gender,interest,residence,parent_age,parent_salary,house_area,average_grades,parent_was_in_college])
    input_df=input_df.reshape(1,10)
    st.title(model.predict(input_df))