import streamlit as st
import joblib

st.title('Heart Disease Prediction')

clf = joblib.load('hdp.joblib')

a = st.number_input('Enter Age')
b = st.number_input('Enter Sex Male:0 Female:1')
c = st.number_input('Enter Chest Pain Type [1,2,3,4]')
d = st.number_input('Enter BP')
e = st.number_input('Cholestrol')
f = st.number_input('Enter FBS')
g = st.number_input('Enter EKG results[0,1,2]')
h = st.number_input('Enter Max HR')
i = st.number_input('Enter Exercise Angina[0,1]')
j = st.number_input('Enter ST Depression')
k = st.number_input('Enter Slope of ST[1,2,3]')
l = st.number_input('Enter number of vessels Fluro [0,1,2,3]')
m = st.number_input('Enter Thallimum [3,6,7] ')

if st.button('Predict'):
    prediction = clf.predict([[a,b,c,d,e,f,g,h,i,j,k,l,m]])
    if prediction=='Presence':
        st.text('Heart Disease is Present')
    else:
        st.text('Heart Disease is Absent')
