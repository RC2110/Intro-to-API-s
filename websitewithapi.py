import streamlit as st
import requests

key = "Euz89cBPl9q6HZ0UuDZcbHvRzaGgDbxOaznm0vqz"
url = f"https://api.nasa.gov/planetary/apod?api_key={key}"
imageurl="https://apod.nasa.gov/apod/image/2309/Arp142_HubbleChakrabarti_2627.jpg"
request = requests.get(url)
data = request.json()
print(data)
request1= requests.get(imageurl)
imgdata = request1.content

with open ("nasaimg.jpeg", 'wb') as file:
    file.write(imgdata)

st.set_page_config(layout="centered")
st.header("Pic & News of the day")
st.subheader(data['title'])
st.image("nasaimg.jpeg")
st.write(data['explanation'])





