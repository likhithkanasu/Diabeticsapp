import numpy as np
import pickle
import pandas as pd
import streamlit as st

# Loading saved model
loaded_model = pickle.load(open('trained_model.pkl', 'rb'))

def diabetesPrediction(input):
    # Changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input)

    # Reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if prediction[0] == 0:
        return 'The person is not diabetic'
    else:
        return 'The person is diabetic'

def main():
    # Custom CSS
    st.markdown(
        """
        <style>
        body {
            background-color: #112D41;
        }
        .main {
            background-color: #112D41;
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
        }
        h1 {
            color: #4CAF50;
            font-family: 'Arial';
        }
        .stButton button {
            background-color: #4CAF50;
            color: white;
            border-radius: 5px;
            padding: 10px 20px;
        }
        .stButton button:hover {
            background-color: #45a049;
        }
        </style>
        """, 
        unsafe_allow_html=True
    )

    # Title
    st.title('Diabetes Prediction Web App')
    
    # Getting input from users
    Pregnancies = st.number_input('Number Of Pregnancies', min_value=0, step=1)
    Glucose = st.number_input('Glucose Level', min_value=0)
    BloodPressure = st.number_input('Blood Pressure value', min_value=0)
    SkinThickness = st.number_input('Skin Thickness value', min_value=0)
    Insulin = st.number_input('Insulin Level', min_value=0)
    BMI = st.number_input('BMI Value', min_value=0.0, format="%.1f")
    DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function value', min_value=0.0, format="%.3f")
    Age = st.number_input('Age of person', min_value=0, step=1)
    
    # Code for prediction
    diagnosis = ''
    
    # Creating a button for prediction
    if st.button('Diabetes Test Result'):
        diagnosis = diabetesPrediction([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])
        
        # Adding animation
        st.markdown(
            """
            <div style="text-align: center;">
                <lottie-player src="https://assets2.lottiefiles.com/private_files/lf30_hy4txm7l.json"  background="transparent"  speed="1"  style="width: 300px; height: 300px;"  loop  autoplay></lottie-player>
            </div>
            """, 
            unsafe_allow_html=True
        )
        
    st.success(diagnosis)

if __name__ == '__main__':
    main()