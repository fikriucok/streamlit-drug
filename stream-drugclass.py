import pickle
import streamlit as st

# membaca model
drug_model =  pickle.load(open('drug_model.sav', 'rb'))

#Judul Web
st.title('Klasifikasi Jenis Narkotika Yang Dikonsumsi')

# Form Input


Age = st.slider('Masukan Umur', 15, 75)
Sex = st.selectbox('Jenis Kelamin', ('0','1'))
BP = st.text_input('Masukan Jumlah Tekanan Darah')
Cholesterol = st.text_input('Jumlah Kolesterol')
Na_to_K = st.number_input('Rasio Natrium ke Kalium dalam Darah')


drug_class = ''

# membuat tombol untuk prediksi
if st.button('Test Prediksi Jenis Narkoba'):
    drug_prediction = drug_model.predict([[Age, Sex, BP, Cholesterol, Na_to_K]])
    
    if(drug_prediction[0]==0):
        drug_class = 'Jenis Drug A'
    elif(drug_prediction[0]==1):
        drug_class = 'Jenis Drug B'
    elif(drug_prediction[0]==2):
        drug_class = 'Jenis Drug C'
    elif(drug_prediction[0]==3):
        drug_class = 'Jenis Drug X'
    else:
        drug_class = 'Jenis Drug Y'
st.success(drug_class)