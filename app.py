# importing required modules
import streamlit as st
import numpy as np
import pandas as pd
import import_ipynb
import Functions 

# defining the title of the app
st.title("LOAN APPROVAL PREDICTION")
st.markdown("Please answer the questions below to know if you are eligible for loan approval or not.")

# in the below code with if-else statements we are converting categorical data, which will be given from the user into numeric

# asking gender of the user
gender = st.selectbox('Select your gender.', ('', 'Female', 'Male'))
if gender == "Female":
    gender = 0
else:
    gender = 1

# asking age of the user
age = st.selectbox('Select your age.', list(range(18, 101)))

# asking marriage status of the user
marriage = st.radio("Are you married ?", ('No', 'Yes'))
if marriage == "Yes":
    marriage = 1
else:
    marriage = 0

# asking number of children of the user
dependents = st.selectbox('How many children do you have ?', (0,1,2,"3+"))
if dependents == 0:
    dependents = 0
elif dependents == 1:
    dependents = 1
elif dependents == 2:
    dependents = 2
else:
    dependents = 3
       
        
# asking education status of the user
education = st.radio("Are you graduate or not ?", ('Graduate', 'Not Graduate'))
if education == "Graduate":
    education = 0
else:
    education = 1

    
# asking if the user is self employed or not
self_employed = st.radio("Are you self employed or not ?", ('Yes', 'No'))
if self_employed == "Yes":
    self_employed = 1
else:
    self_employed = 0    

    
# asking annual income of the user(in dollars)
income = st.number_input('What is your annual income ($) ?')
    

# asking annual income of the co-applicant(in dollars)
coap_income = st.number_input("What is your co-applicant's annual income ($) ?")
    
# asking the desired amount of loan(in dollars and in thousands)
loan_amount = st.number_input('What is your expected amount of loan in thousands ($) ?')
    
# asking the desired period of time for paying off the loan(in days)
loan_amount_term = st.number_input('What is your desired period of time for paying off the loan in days ?')


# asking credit history of the user
credit = st.selectbox('Have you previously been given loan and properly followed rules and guidelines regarding payment details ?',("", "Yes", "No"))
if credit == "Yes":
    credit = 1.0
else:
    credit = 0.0 

    
# asking property area of the user
property_area = st.selectbox('Select the area you live in.', ("", "Urban", "Semiurban", "Rural"))
if property_area == "Rural":
    property_area = 0
elif property_area == "Urban":
    property_area = 2
else:
    property_area = 1



# defining loan_id, which is just a number in range of 1 to 613 
loan_id = np.random.randint(1,614)


# collecting all answers of the user and making it ready to give input to our model for loan approval prediction
user_info = [loan_id, gender, marriage, dependents, education, self_employed, income, coap_income, loan_amount, loan_amount_term, credit, property_area]
user_info = np.array(user_info)
user_info = user_info.reshape(1,-1)    
 
    
# if the model predicts 0, it means user is not eligible for loan approval, if it is 1, it means user is eligible for loan approval  
if st.button("Submit the survey to see the result!"):
    if Functions.model_tree.predict(user_info) == 0:
        st.title("You are NOT eligible for loan approval.")
    elif Functions.model_tree.predict(user_info) == 1:
        st.title("You are eligible for loan approval.")


    

    


    
