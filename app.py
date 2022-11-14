from operator import mod
import pandas as pd
import streamlit as st
import pickle
import sklearn

# @st.cache
def load_model():
  with open('models/author_ridge.pkl', 'rb') as f:
    the_model = pickle.load(f)
  return the_model

model = load_model()

st.title("Salary Prediction of Data Position in the US")

st.write(""" ### Select your information """ )

state = (
        "CA","TX","NY","VA","MD","DC","NJ"
    )

company = (
    "Amazon", "Apple" , "Facebook", "Twitter", 
    "AstraZeneca", "Genentech", "Seen by Indeed"
)

industry = (
        "Information Technology","Business Services","Education","Finance",
        "Government","Insurance","Media", "Retail"
    )

state = st.selectbox("State", state)
company = st.selectbox("Company", company)
industry = st.selectbox("Industry", industry)
st.write(""" ###### Please Select for Senior-Level """ )
senior = st.checkbox("Senior-Level")
st.write(""" ###### Please Select Data Roles for Data Scientist, Data Engineer and Data Analyst """ )
data = st.checkbox("Data Roles")
scientist = st.checkbox("Scientist")
engineer = st.checkbox("Engineer")
analyst = st.checkbox("Analyst")
rating = st.slider("Rating", 0.0, 5.0, 3.7)
    
ok = st.button("Calculate Salary")

if ok:
    
    to_predict = pd.DataFrame(columns= ['Rating', 'is_senior', 'is_scientist', 'is_analyst', 'is_engineer',
    'is_manager', 'is_data', 'is_lead', 'is_principal', 'is_data_scientist',
    'is_data_analyst', 'is_data_engineer', 'Company_Amazon',
    'Company_Amgen', 'Company_Apple',
    'Company_Applied Research Laboratories', 'Company_AstraZeneca',
    'Company_BAE Systems USA', 'Company_Booz Allen Hamilton',
    'Company_Booz Allen Hamilton Inc.', 'Company_Capital One',
    'Company_Facebook', 'Company_Freenome', 'Company_Genentech',
    'Company_Guidehouse', 'Company_LMI', 'Company_Lawrence Berkeley Lab',
    'Company_Leidos', 'Company_Merck KGaA', 'Company_Navigant Consulting',
    'Company_Noblis', 'Company_SAIC', 'Company_Seen by Indeed',
    'Company_Solekai Systems Corp', 'Company_Southwest Research Institute',
    'Company_Stitch Fix', 'Company_The Aerospace Corporation',
    'Company_Tiger Analytics', 'Company_Twitter',
    'Company_UC San Francisco',
    'Company_University of Texas Medical Branch', 'State_CA', 'State_DC',
    'State_MD', 'State_NJ', 'State_NY', 'State_TX', 'State_VA',
    'Industry_Accounting & Legal', 'Industry_Aerospace & Defense',
    'Industry_Biotech & Pharmaceuticals', 'Industry_Business Services',
    'Industry_Education', 'Industry_Finance', 'Industry_Government',
    'Industry_Health Care', 'Industry_Information Technology',
    'Industry_Insurance', 'Industry_Manufacturing', 'Industry_Media',
    'Industry_Non-Profit', 'Industry_Oil, Gas, Energy & Utilities',
    'Industry_Retail', 'Industry_Transportation & Logistics',
    'Job_Type_FULL_TIME']) 
    to_predict.loc[0,'Rating'] = rating
    to_predict.loc[0,f'State_{state}'] = 1 
    to_predict.loc[0,f'Industry_{industry}'] = 1
    to_predict.loc[0,f'Company_{company}'] = 1

    if senior == True:
        to_predict.loc[0,'is_senior'] = 1

    if data == True:
        to_predict.loc[0,'is_data'] = 1
        
        if scientist == True: # Check interaction term of data scientist
            to_predict.loc[0,'is_data_scientist'] = 1
        
        if engineer == True: # Check interaction term of data engineer
            to_predict.loc[0,'is_data_engineer'] = 1
        
        if analyst == True: # Check interaction term of data analyst
            to_predict.loc[0,'is_data_analyst'] = 1

    if scientist == True:
        to_predict.loc[0,'is_scientist'] = 1

    if engineer == True:
        to_predict.loc[0,'is_engineer'] = 1
    
    if analyst == True:
        to_predict.loc[0,'is_analyst'] = 1

    to_predict = to_predict.fillna(0)
    salary = model.predict(to_predict)
    st.write(f"The estimate minimum salary is ${salary[0]:.2f}")

