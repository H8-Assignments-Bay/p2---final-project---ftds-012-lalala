import streamlit as st
from streamlit_option_menu import option_menu
import requests
from PIL import Image
import json
import numpy as np
import tensorflow as tf
import pandas as pd

#with st.sidebar:


title = '<h1 style="font-family:sans-serif; color:#000000; text-align:center;">GuideGet</h1>'
st.markdown(title, unsafe_allow_html=True)
selected = option_menu(
        menu_title=None, 
        options = ["Explore", "Sell", "Buy", "Trade"],
        orientation = "horizontal",
    )    


df = pd.read_csv("mobile.csv")


def load_prep_img(filename):
  
  pred = np.array(filename)[:, :, :3]
  pred = tf.image.resize(pred, size=(224, 224))
  pred = pred / 255.0
  return pred


    
# s_p=st.sidebar.selectbox('Select Page',['Explore',
#                                         'Sell',
#                                         'Buy',
#                                         'Trade',
#                                         ])

if selected == "Explore":
    
    st.image("GG Logo.png")
    st.header('We Guide You Get')
    st.subheader('Getting update and trading gadget')
    
    col1, col2, col3 = st.columns([1,1,1])
    with col1:
        image1 = Image.open("1635055123055_Apple iPhone 11 128GB New for sale.jpg")
        st.image(image1, caption= "Iphone 11", width=162)
        st.markdown("Latest Gadget")
    
    with col2:
        image2 = Image.open("Iphone XS.jpg")
        st.image(image2, caption= "Iphone XS", width=100)
        st.markdown("Most Popular Gadget")
    
    with col3:
        image3 = Image.open("galaxy-s10.jpg")
        st.image(image3, caption= "Samsung Galaxy S10 Plus", width=100)
        st.markdown("Most Inexpensive Gadget")
    
elif selected == "Sell":
    
    uploadpict = st.file_uploader("Upload an image..", type=["jpg", "png"])

    submitted = st.button('Predict')

    if submitted:
        filepict = Image.open(uploadpict)
        image = load_prep_img(filepict)
        image_ex = tf.expand_dims(image, axis=0)
        new_data = image_ex.numpy().tolist()
        
        input_data_json = json.dumps({
            'signature_name':'serving_default',
            'instances':new_data
        })

        #URL = "http://127.0.0.1:5000/sales_prediction" # sebelum push backend
        URL = "https://guideget.herokuapp.com/v1/models/guideget:predict" # URL Heroku

        # # komunikasi
        r = requests.post(URL, data=input_data_json)
        res = r.json()
        
            
        # # st.write(res)
        resultz = np.argmax(res['predictions'][0])
        # st.write(resultz)
        if resultz == 0:
            text_hasil = '<h1 style="font-family:Helvetica; color:#8c8c00; text-align:center;">Iphone 11</h1>'
            st.markdown(text_hasil, unsafe_allow_html=True)
            model = "Iphone 11"
            st.write(df[df["model"]== model][["color","storage","memory","used_price_buy"]])
            
        elif resultz == 1:
            text_hasil = '<h1 style="font-family:Helvetica; color:#8c8c00; text-align:center;">Iphone XR</h1>'
            st.markdown(text_hasil, unsafe_allow_html=True)
            model = "Iphone XR"
            st.write(df[df["model"]== model][["color","storage","memory","used_price_buy"]])
            
        elif resultz == 2:
            text_hasil = '<h1 style="font-family:Helvetica; color:#8c8c00; text-align:center;">Iphone XS</h1>'
            st.markdown(text_hasil, unsafe_allow_html=True)
            model = "Iphone XS"
            st.write(df[df["model"]== model][["color","storage","memory","used_price_buy"]])
                                  
        else:
            text_hasil1 = '<h1 style="font-family:Helvetica; color:#8c8c00; text-align:center;">Samsung Galaxy S10 Plus</h1>'
            st.markdown(text_hasil1, unsafe_allow_html=True)
            model = "Galaxy S10 Plus"
            st.write(df[df["model"]== model][["color","storage","memory","used_price_buy"]])

elif selected == "Buy":
    
    with st.form("Buy_form"):
        radio = st.radio("select gadget condition", ("new_price", "used_price_sell"))
        budget = st.number_input("insert budget", min_value= 9000000, max_value= 25000000, step=200000)
        submitted = st.form_submit_button("Search")
        data_buy = df.copy()
        cart_data = []
        if submitted:
            if radio == "new_price":
                data_buy = data_buy[data_buy["new_price"] <= budget]
                st.markdown("<br>", unsafe_allow_html=True)
                for i, idx in data_buy.iterrows():
                    col1, col2, col3, col4, col5= st.columns([1,1,1,1,1])
                    with col1:
                        st.write(data_buy['model'][i])
                    with col2:
                        st.write(data_buy['color'][i])
                    with col3:
                        st.write(data_buy['storage'][i])
                    with col4:
                        st.write(data_buy['store_loc'][i])
                    with col5:
                        st.markdown("""<h6>IDR {}</h6>""".format(data_buy['new_price'][i]), unsafe_allow_html=True)
                    col6, col7, col8= st.columns([1,1,1])
                    with col6:
                        cart = st.number_input( "Add Quantity", key=i, step=1)
                        if cart:
                            cart_data.append(data_buy.iloc[i])
                    
                    st.markdown('___', unsafe_allow_html=True)

            else :
                st.markdown("<br>", unsafe_allow_html=True)
                data_buy = data_buy[data_buy["used_price_sell"] <= budget]
                for i, idx in data_buy.iterrows():
                    col1, col2, col3, col4, col5, col6 = st.columns([1,1,1,1,1,1])
                    with col1:
                        st.write(data_buy['model'][i])
                    with col2:
                        st.write(data_buy['color'][i])
                    with col3:
                        st.write(data_buy['storage'][i])
                    with col4:
                        st.write(data_buy['store_loc'][i])
                    with col5:
                        st.markdown("""<h6>IDR {}</h6>""".format(data_buy['used_price_sell'][i]), unsafe_allow_html=True)
                    col6, col7, col8= st.columns([1,1,1])
                    with col6:
                        cart = st.number_input("Add Quantity", key=i, step=1)
                        if cart:
                            cart_data.append(data_buy.iloc[i])
                    
                    st.markdown('---', unsafe_allow_html=True)
                    
            st.form_submit_button("Buy")

                    
elif selected == "Trade":
    
    uploadpict = st.file_uploader("Upload an image..", type=["jpg", "png"])

    submitted = st.button('Predict')
    
    if submitted:
        filepict = Image.open(uploadpict)
        image = load_prep_img(filepict)
        image_ex = tf.expand_dims(image, axis=0)
        new_data = image_ex.numpy().tolist()
        
        input_data_json = json.dumps({
            'signature_name':'serving_default',
            'instances':new_data
        })
        
        URL = "https://guideget.herokuapp.com/v1/models/guideget:predict" # URL Heroku
        
         # # komunikasi
        r = requests.post(URL, data=input_data_json)
        res = r.json()
        
            
        # # st.write(res)
        resultz = np.argmax(res['predictions'][0])
        # st.write(resultz)
        if resultz == 0:
            text_hasil = '<h1 style="font-family:Helvetica; color:#8c8c00; text-align:center;">Iphone 11</h1>'
            st.markdown(text_hasil, unsafe_allow_html=True)
            model = "Iphone 11"
            st.write(df[df["model"]== model][["color","storage","memory","used_price_buy"]])
                                   
        elif resultz == 1:
            text_hasil = '<h1 style="font-family:Helvetica; color:#8c8c00; text-align:center;">Iphone XR</h1>'
            st.markdown(text_hasil, unsafe_allow_html=True)
            model = "Iphone XR"
            st.write(df[df["model"]== model][["color","storage","memory","used_price_buy"]])
                        
        elif resultz == 2:
            text_hasil = '<h1 style="font-family:Helvetica; color:#8c8c00; text-align:center;">Iphone XS</h1>'
            st.markdown(text_hasil, unsafe_allow_html=True)
            model = "Iphone XS"
            st.write(df[df["model"]== model][["color","storage","memory","used_price_buy"]])
                                              
        else:
            text_hasil1 = '<h1 style="font-family:Helvetica; color:#8c8c00; text-align:center;">Samsung Galaxy S10 Plus</h1>'
            st.markdown(text_hasil1, unsafe_allow_html=True)
            model = "Galaxy S10 Plus"
            st.write(df[df["model"]== model][["color","storage","memory","used_price_buy"]])
            
        if model == "Iphone XR":
            options = st.selectbox("Select Your Next Gadget", ("Iphone XS", "Galaxy S10 Plus"))
            st.write('You selected:', options)
            st.write(df[df["model"] == options][["color","storage","memory","used_price_sell","new_price"]])
        else:
            options = st.selectbox("Select Your Next Gadget", ("Iphone XR","Iphone XS", "Galaxy S10 Plus"))
            st.write('You selected:', options)
            st.write(df[df["model"] == options][["color","storage","memory","used_price_sell","new_price"]])

    # if r.status_code == 200:
    #     st.title(res['result']['label_idx'])
    # else:
    #     st.title("ERROR BOSS")
    #     st.write(res['message'])