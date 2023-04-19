# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 16:30:57 2022

@author: psair
"""
#DIABETES PREDICTION SYSTEM

#run command: streamlit run "C:\Users\197r1\OneDrive\Desktop\Major\disease_prediction.py"

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

#loading saved models

diabetes_model = pickle.load(open("C:/Users/197r1/OneDrive/Desktop/Major/mdps_diabetes_model.sav", "rb"))
kidney_model = pickle.load(open("C:/Users/197r1/OneDrive/Desktop/Major/kidney_disease_model.sav", "rb"))
heart_model = pickle.load(open("C:/Users/197r1/OneDrive/Desktop/Major/mdps_heart_model.sav", "rb"))
cancer_model = pickle.load(open("C:/Users/197r1/OneDrive/Desktop/Major/cancer_pred_dataset.sav", "rb"))

# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                          ['Diabetes Prediction',
                           'Heart Disease Prediction',
                           'Kidney Disease Prediction',
                           'Cancer Disease Prediction'],
                          icons=['activity','activity','activity','activity'],
                          default_index=0)

# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
        
    st.title("Diabetes Prediction System")
    
    # getting the input data from the user
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Glucose Level')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    
    with col2:
        Insulin = st.text_input('Insulin Level')
    
    with col3:
        BMI = st.text_input('BMI value')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    
    with col2:
        Age = st.text_input('Age of the Person')
    
    
    # code for Prediction
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
          st.info('The person is diabetic')
        else: 
          st.success('The person is NOT diabetic')
        

# Kidney Disease Prediction Page
if (selected == 'Kidney Disease Prediction'):
        
    st.title("Kidney Disease Prediction System")
    
    # getting the input data from the user
   								
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('age')
        
    with col2:
        bp = st.text_input('blood_pressure')
    
    with col3:
        sg = st.text_input('specific_gravity')
    
    with col1:
        al = st.text_input('albumin')
    
    with col2:
        su = st.text_input('sugar')
    
    with col3:
        rbc = st.text_input('red_blood_cells')
        rbc = 1 if rbc=="normal" else 0
    
    with col1:
        pc = st.text_input('pus_cell')
        pc = 1 if pc=="normal" else 0
    
    with col2:
        pcc = st.text_input('pus_cell_clumps')
        pcc = 1 if pcc=="present" else 0
    
    with col3:
        ba = st.text_input('bacteria')
        ba = 1 if ba=="present" else 0
        
    with col1:     							
        bgr = st.text_input('blood_glucose_random')
    
    with col2:
        bu = st.text_input('blood_urea')
    
    with col3:
        sc = st.text_input('serum_creatinine')
        
    with col1:
        sod = st.text_input('sodium')
    
    with col2:
        pot = st.text_input('potassium')
    
    with col3:
        hemo = st.text_input('haemoglobin')
        
    with col1:
        pcv = st.text_input('packed_cell_volume')
    
    with col2:
        wc = st.text_input('white_blood_cell_count')
    
    with col3:
        rc = st.text_input('red_blood_cell_count')
        
    with col1:
        htn = st.text_input('hypertension')
        htn = 1 if htn=="yes" else 0
    
    with col2:
        dm = st.text_input('diabetes_mellitus')
        dm = 4 if dm=="yes" else 3
    
    with col3:
        cad = st.text_input('coronary_artery_disease')
        cad = 1 if cad=="no" else 0
    
    with col1:
        appet = st.text_input('appetite')
        appet = 1 if appet=="poor" else 0
    
    with col2:
        pe = st.text_input('peda_edema')
        pe = 1 if pe=="yes" else 0
    
    with col3:
        ane = st.text_input('aanemia')
        ane = 1 if ane=="yes" else 0
    
    
    # code for Prediction
    kid_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Kidney Disease Test Result'):
        kid_prediction = kidney_model.predict([[age,bp,sg,al,su,rbc,pc,pcc,ba,bgr,bu,sc,sod,pot,hemo,pcv,wc,rc,htn,dm,cad,appet,pe,ane]])
        print(kid_prediction)
        if (kid_prediction[0] == 0):
          kid_diagnosis = 'The person is having kidney disease'
          st.info(kid_diagnosis)
        else:
          kid_diagnosis = 'The person is NOT having kidney disease'
          st.success(kid_diagnosis)
        
        
# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    
    st.title("Heart Disease Prediction System")
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Age = st.text_input('Age of the Person')
        
    with col2:
        Sex = st.text_input('Sex')
        if Sex == "M":
            Sex = 1
        else:
            Sex = 0
    
    with col3:
        ChestPainType = st.text_input('Chest Pain Type')
        if ChestPainType == "ATA":
            ChestPainType = 1
        elif ChestPainType == "NAP":
            ChestPainType = 2
        else:
            ChestPainType = 0
    
    with col1:
        RestingBp = st.text_input('Resting BP Value')
        
    
    with col2:
        Cholesterol = st.text_input('Cholesterol Level')
    
    with col3:
        FastingBS = st.text_input('Fasting BS value')
    
    with col1:
        RestingECG = st.text_input('Resting ECG value')
        if RestingECG == "Normal":
            RestingECG = 1
        else:
            RestingECG = 2
    
    with col2:
        MaxHR = st.text_input('Max HR Value')

    with col3:
        ExerciseAngina = st.text_input('Exercise Angina value')
        if ExerciseAngina == "N":
            ExerciseAngina = 0
        else:
            ExerciseAngina = 1
    
    with col1:
        OldPeak = st.text_input('Old Peak value')

    with col2:
        Stslope = st.text_input('St Slope value')
        if Stslope == "Up":
            Stslope = 2
        else:
            Stslope = 1
        
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        
        heart_prediction = heart_model.predict([[Age,Sex,ChestPainType,RestingBp,Cholesterol,FastingBS,RestingECG,MaxHR,ExerciseAngina,OldPeak,Stslope]])
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
          st.info(heart_diagnosis)
        else:
          heart_diagnosis = 'The person is NOT having heart disease'
          st.success(heart_diagnosis)
        
        
# Cancer Disease Prediction Page
if (selected == 'Cancer Disease Prediction'):
    
    st.title("Cancer Disease Prediction System")
    
    # getting the input data from the user
    col1, col2 = st.columns(2)
    
    with col1:
        mr = st.text_input('Mean Radius')
        
    with col2:
        mt = st.text_input('Mean Texture')
    
    with col1:
        mp = st.text_input('Mean Perimeter')
    
    with col2:
        ma = st.text_input('Mean Area')
    
    with col1:
        ms = st.text_input('Mean Smoothness')

    # code for Prediction
    cancer_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Cancer Disease Test Result'):
        cancer_prediction = cancer_model.predict([[mr,mt,mp,ma,ms]])
        
        if (cancer_prediction[0] == 1):
          cancer_diagnosis = 'The person is having cancer disease'
          st.info(cancer_diagnosis)
        else:
          cancer_diagnosis = 'The person is NOT having cancer disease'
          st.success(cancer_diagnosis)
        