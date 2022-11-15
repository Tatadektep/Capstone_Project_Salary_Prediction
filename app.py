from operator import mod
import pandas as pd
import streamlit as st
import pickle
import sklearn
import plotly
import plotly.graph_objs as go
import random


@st.cache
def load_model():
  with open('models/author_ridge.pkl', 'rb') as f:
    the_model = pickle.load(f)
  return the_model

model = load_model()

#unique = random.sample(range(1, 99),1)
page = st.sidebar.selectbox("Salary Prediction or Explore the Dataset", ("Predict", "Explore"), key = 0)

def show_predict_page():
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
        st.title(f"The estimate minimum salary is ${salary[0]:.2f}")
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
        st.title(f"The estimate minimum salary is ${salary[0]:.2f}")


def show_explore_page():
    st.title("Explore the Baseline of the Dataset and Exploratory Data Analysis")
    
    def load_data(): 
        data_df = pd.read_csv("dataset/Combined_Data.csv")

        return data_df
    data_df = load_data()

    st.write(""" ### State Summary""")
    states = data_df['State'].unique().tolist()
    fig = go.Figure()
    min_sal =  data_df.groupby('State')['Min_Salary']
    max_sal =  data_df.groupby('State')['Max_Salary']
    fig.add_trace(go.Bar(x = states,
                        y = min_sal.mean(),
                        name = 'Min Salary' , marker_color = '#bd3939'))

    fig.add_trace(go.Bar(x = states,
                        y = max_sal.mean(),
                        name = 'Max Salary' , marker_color = '#399ba3'))
    fig.update_layout(template = 'ggplot2', barmode = 'group',
                    xaxis={'categoryorder':'total ascending'})
    fig.show()

    st.write(""" ### Industry Summary""")
    ind = data_df[~data_df['Industry'].isnull()]
    fig = go.Figure()
    fig.add_trace(go.Bar(x = ind.groupby("Industry")['Min_Salary'].mean().to_list(),
    y = ind.groupby("Industry")['Min_Salary'].mean().index.to_list(), marker_color = 'goldenrod',
    orientation = 'h' , name = "Min Avg Salary"
    ))
    fig.add_trace(go.Bar(x = ind.groupby("Industry")['Max_Salary'].mean().to_list(),
    y = ind.groupby("Industry")['Max_Salary'].mean().index.to_list(), marker_color = 'deepskyblue'
    ,orientation = 'h' ,name = "Max Avg Salary"))
    fig.update_layout( template = 'plotly',
                    title = 'Minimal And Maximal Average Annual Salaries according to industries' ,
                    barmode = 'group',
                    yaxis={'categoryorder':'total ascending'})
    fig.show()


# Change Page

