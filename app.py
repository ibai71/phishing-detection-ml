import streamlit as st
import machine_learning as ml
import feature_extraction as fe
from bs4 import BeautifulSoup
import requests as re
import matplotlib.pyplot as plt

st.title('Phishing Website Detection using Machine Learning')
st.write('This ML-based app is developed for educational purposes. Objective of the app is detecting phishing websites only using content data. Not URL!')

with st.expander("PROJECT DETAILS"):
    st.subheader('Approach')
    st.write('I used supervised learning to classify phishing and legitimate websites. I benefit from content-based approach and focus on html of the websites. Also, I used scikit-learn for the ML models.')
    
    st.subheader('Data set')
    st.write('I used "phishtank.org" & "tranco-list.eu" as data sources.')
    
    # Gráfico circular
    labels = 'phishing', 'legitimate'
    phishing_rate = int(ml.phishing_df.shape[0] / (ml.phishing_df.shape[0] + ml.legitimate_df.shape[0]) * 100)
    legitimate_rate = 100 - phishing_rate
    sizes = [phishing_rate, legitimate_rate]
    explode = (0.1, 0)
    fig, ax = plt.subplots()
    ax.pie(sizes, explode=explode, labels=labels, shadow=True, startangle=90, autopct='%1.1f%%')
    ax.axis('equal')
    st.pyplot(fig)

    st.write('Features + URL + Label ==> Dataframe')
    st.markdown('label is 1 for phishing, 0 for legitimate')
    number = st.slider("Select row number to display", 0, 100)
    st.dataframe(ml.legitimate_df.head(number))

    @st.cache_data
    def convert_df(df):
        return df.to_csv().encode('utf-8')
        
    csv = convert_df(ml.df)
    st.download_button(
        label="Download data as CSV",
        data=csv,
        file_name='phishing_legitimate_structured_data.csv',
        mime='text/csv',
    )

    st.subheader('Results')
    st.table(ml.df_results)
    
choice = st.selectbox("Please select your machine learning model",
    [
        'Gaussian Naive Bayes', 'Support Vector Machine', 'Decision Tree', 'Random Forest',
        'AdaBoost', 'Neural Network', 'K-Neighbours'
    ]
)

if choice == 'Gaussian Naive Bayes':
    model = ml.nb_model
    st.write('GNB model is selected!')
elif choice == 'Support Vector Machine':
    model = ml.svm_model
    st.write('SVM model is selected!')
elif choice == 'Decision Tree':
    model = ml.dt_model
    st.write('DT model is selected!')
elif choice == 'Random Forest':
    model = ml.rf_model
    st.write('RF model is selected!')
elif choice == 'AdaBoost':
    model = ml.ab_model
    st.write('AB model is selected!')
elif choice == 'Neural Network':
    model = ml.nn_model
    st.write('NN model is selected!')
else:
    model = ml.kn_model
    st.write('KN model is selected!')

url = st.text_input('Enter the URL')

if st.button('Check!'):
    try:
        response = re.get(url, verify=False, timeout=4)
        if response.status_code != 200:
            st.error("HTTP connection was not successful for the URL.")
        else:
            soup = BeautifulSoup(response.content, "html.parser")
            vector = [fe.create_vector(soup)]
            result = model.predict(vector)
            
            if result[0] == 0:
                st.success("This web page seems legitimate!")
                st.balloons()
            else:
                st.warning("Attention! This web page is a potential PHISHING!")
                st.snow()
    except re.exceptions.RequestException as e:
        st.error(f"Error connecting to the URL: {e}")