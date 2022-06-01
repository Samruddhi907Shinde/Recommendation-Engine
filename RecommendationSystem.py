import pandas as pd
import numpy as np
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors
import streamlit as st
from PIL import Image
from datetime import datetime

#insert image in frontend
st.title("Resturant Recommendation system")
img = Image.open("resturant.jpg")
img1 = img.resize((400,200))
st.image(img1)

# read csv file
hotels = pd.read_csv("zomato.csv", encoding='latin-1')
ratings = pd.read_csv("Ratings.csv")

# define pivot table
dataset = ratings.pivot_table(index='Resturant_ID', columns='User_ID', values='Rating')
dataset.fillna(0, inplace=True)

#Function Add Resturant in csv file
def add_resturant(p_Resturant_ID:object,p_Resturant_Name: object,p_Country_Code:object,p_City:object,p_Address:object,p_Locality:object,
                  p_Locality_Verbose:object,p_Longitude:object,p_Latitude:object,p_Cuisines:object,p_Average_Cost_for_two:object,
                  p_Currency:object,p_Has_Table_booking:object,p_Has_Online_delivery:object,p_Is_delivering_now:object,p_Switch_to_order_menu:object,
                  p_Price_range:object,p_Aggregate_rating:object,p_Rating_color:object,p_Rating_text:object,p_Votes:object) -> object:


    data_add_resturant = {
        'Resturant_ID' : [p_Resturant_ID],'Resturant_Name': [p_Resturant_Name],
        'Country_Code': [p_Country_Code],'City': [p_City],
        'Address': [p_Address],'Locality': [p_Locality],
        'Locality_Verbose': [p_Locality_Verbose], 'Longitude': [p_Longitude],
        'Latitude' : [p_Latitude],'Cuisines': [p_Cuisines],
        'Average_Cost_for_two': [p_Average_Cost_for_two],'Currency': [p_Currency],
        'Has_Table booking': [p_Has_Table_booking],'Has_Online delivery': [p_Has_Online_delivery],
        'Is_delivering now': [p_Is_delivering_now],'Switch_to_order_menu': [p_Switch_to_order_menu],
        'Price_range': [p_Price_range],'Aggregate_rating': [p_Aggregate_rating],
        'Rating_color': [p_Rating_color],'Rating_text': [p_Rating_text],
        'Votes': [p_Votes]
    }

    # Make data frame of above data
    df_add_resturant = pd.DataFrame(data_add_resturant)

    # append data frame to CSV file
    df_add_resturant.to_csv('zomato.csv', mode='a', index=False, header=False)


#Function to Add rating in CSV file
def add_resturant_rating(p_User_ID:object,p_Resturant_Id: object, p_Rating: object) -> object:

    # data of resturant rating
    Timestamp = datetime.now()

    data_resturant_rating = {
        'User_ID' : [p_User_ID],
        'Resturant_ID': [p_Resturant_Id],
        'Rating': [p_Rating],
        'Timestamp': [Timestamp]
    }

    # Make data frame of above data
    df_resturant_rating = pd.DataFrame(data_resturant_rating)

    # append data frame to CSV file
    df_resturant_rating.to_csv('Ratings.csv', mode='a', index=False, header=False)


# main recommendation function
def resturant_recommendation(Resturant_Name: object) -> object:
    no_of_recommendations = 10
    Resturant_List = hotels[hotels['Resturant_Name'].str.contains(Resturant_Name)]
    if len(Resturant_List):
        Resturanti = Resturant_List.iloc[0]['Resturant_ID']

        Resturanti = dataset[dataset['Resturant_ID'] == Resturanti].index[0]
        distances, indices = model.kneighbors(csr_dataset[Resturanti], n_neighbors=no_of_recommendations + 1)

        Resturant_indices = sorted(list(zip(indices.squeeze().tolist(), distances.squeeze().tolist())),
                                   key=lambda x: x[1], reverse=True)

        Recommendations = []
        for val in Resturant_indices:
            Resturanti = dataset.iloc[val[0]]['Resturant_ID']
            i_count = hotels[hotels['Resturant_ID'] == Resturanti].index
            Recommendations.append({'Resturant_Name': hotels.iloc[i_count]['Resturant_Name'].values[0], 'Distance': val[1]})
        df = pd.DataFrame(Recommendations)
        return df['Resturant_Name']
    else:
        return "No Similar Resturants Found"


# remove sparsity
csr_dataset = csr_matrix(dataset.values)
dataset.reset_index(inplace=True)


# using algorithm
model = NearestNeighbors(metric='cosine', algorithm='brute', n_neighbors=20, n_jobs=-1)
model.fit(csr_dataset)


# Search the Resturant on frontend and show it's recommendations
typehotel = st.text_input("Search for the Resturant of your choice")
typehotelL = typehotel.lower()

if st.button("Submit"):
    st.write(typehotel)
    st.write("The recommended resturants for you are as follows : ")
    st.write(resturant_recommendation(typehotelL))



# Accepting features of the new resturant to be added
st.sidebar.subheader("Add Resturant")
a_resturantid = st.sidebar.text_input("Resturant ID to be Added")
a_resturantname = st.sidebar.text_input("Resturant Name to be Added")
a_resturant_country_code = st.sidebar.text_input("Resturant Country Code")
a_resturantcity = st.sidebar.text_input("Resturant City")
a_resturantaddress = st.sidebar.text_input("Resturant Address")
a_resturantlocality = st.sidebar.text_input("Resturant Locality")
a_resturantlocalityVer = st.sidebar.text_input("Resturant Locality_Verbose")
a_resturantlongitude = st.sidebar.text_input("Resturant Longitude")
a_resturantlatitude = st.sidebar.text_input("Resturant Latitude")
a_resturantcuisines = st.sidebar.text_input("Resturant Cuisines")
a_resturantaveragecost = st.sidebar.text_input("Resturant Average Cost For Two")
a_resturantcurrancy = st.sidebar.text_input("Resturant Currancy")
a_resturant_tablebooking = st.sidebar.selectbox("Resturant has Table Booking",('yes','no'))
a_resturant_onlinedelivery = st.sidebar.selectbox("Resturant has Online Delivery",('yes','no'))
a_resturant_onlinedelivery_now = st.sidebar.selectbox("Resturant has Online Delivery Now",('yes','no'))
a_resturant_switchorder = st.sidebar.selectbox("Resturant has Switch to order Menu",('yes','No'))
a_resturant_pricerating = st.sidebar.selectbox("Resturant Price Range",('1','2','3','4'))
a_resturant_aggregaterating = st.sidebar.text_input("Resturant Aggregate Rating")
a_resturant_Ratingcolor = st.sidebar.selectbox("Resturant Rating Color",('Green','Dark Green'))
a_resturant_ratingtext = st.sidebar.selectbox("Resturant Rating Color",('Not rated','Poor','Average','Good','Very Good','Excellent'))
a_resturantvotes = st.sidebar.text_input("No of Votes For The Resturant")
button_addResturant = st.sidebar.button("Add Resturant")
if button_addResturant:
    add_resturant(a_resturantid,a_resturantname.lower(),a_resturant_country_code.lower(),a_resturantcity.lower(),a_resturantaddress.lower(),a_resturantlocality.lower(),a_resturantlocalityVer.lower(),
             a_resturantlongitude,a_resturantlatitude,a_resturantcuisines.lower(),a_resturantaveragecost.lower(),a_resturantcurrancy.lower(),a_resturant_tablebooking,a_resturant_onlinedelivery,
             a_resturant_onlinedelivery_now,a_resturant_switchorder,a_resturant_pricerating,a_resturant_aggregaterating,a_resturant_Ratingcolor,a_resturant_ratingtext,a_resturantvotes)


#Accepting details to add ratings for a resturant
st.sidebar.subheader("Add Resturant Rating")
a_resturant_user_id = st.sidebar.text_input("User_ID for rating")
a_resturantid_r = st.sidebar.text_input("Resturant ID for rating")
a_resturantrating = st.sidebar.text_input("Resturant Rating")
button_addRating = st.sidebar.button("Add Resturant Rating")
if button_addRating:
    add_resturant_rating(a_resturant_user_id,a_resturantid_r,a_resturantrating)

