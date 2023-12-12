import pickle
import streamlit as st

## Importar el Modelo

with open('clasificador_credito_rf.pkl', 'rb') as file:
    clasificador = pickle.load(file)
    
@st.cache()

## Definir la Funciòn de predicciòn

def prediction(Gender,	Married,	ApplicantIncome	,LoanAmount,	Credit_History):
    if (Gender=="Male"):
        Gender=0
    else:
        Gender=1
    if (Married=="Unmarried"):
        Married=0
    else:
        Married=1
    if (Credit_History=="Unclear Debts"):
        Credit_History=0
    else:
        Credit_History=1
        
    LoanAmount=LoanAmount/1000
    prediccion=clasificador.predict([[Gender,	Married,	ApplicantIncome	,LoanAmount,	Credit_History]])
    if prediccion==0:
        pred="Rejected"
    else:
        pred="Approved"
    return pred

## Definir la App para consumir el modelo

def main():
    html_temp="""
    <div style ="background-color:yellow;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Streamlit Loan Prediction ML App</h1> 
    </div> 
    """
    st.markdown(html_temp, unsafe_allow_html = True)
    Gender=st.selectbox("Gender",("Male","Female"))
    Married=st.selectbox("Marital Status",("Unmarried","Married"))
    ApplicantIncome=st.number_input("Applicants monthly income")
    LoanAmount = st.number_input("Total loan amount")
    Credit_History = st.selectbox('Credit_History',("Unclear Debts","No Unclear Debts"))
    result=""
    if st.button("Predict"):
        result=prediction(Gender,Married,ApplicantIncome,LoanAmount,Credit_History)
        st.success('Your loan is {}'.format(result))
        print(LoanAmount)

if __name__=='__main__': 
    main()
