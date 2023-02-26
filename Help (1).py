import streamlit as st
from twilio.rest import Client
st.title("Looking for help?📙")
st.write("Catpedia not working as expected? If you need any support fill out the field below to get answers to commonly asked questions or to contact Catpedia's Support team" )
with st.form("my_form"):
   phone_number = st.text_input('Enter your Phone Number Below:')
   # Every form must have a submit button.
   submitted = st.form_submit_button("Submit")
   if submitted:
    twilio_number = "+1 276 500 8487"
    account_sid = "AC948326b53900455adb85589523182421"
    auth_token = "47ef47ddb5e403598bfd0f87d9b1231d"
    client = Client(account_sid, auth_token)
    message = client.messages.create(
      body = """
      Having trouble using the Cat Breed Information web app? Here is a list of tips to help you troubleshoot the issue:/n 

✅Check the breed selection dropdown menus: Make sure you have selected a breed from the dropdown menu before clicking the "Submit" button. If you do not select a breed, the app will not display any results./n

✅Check your internet connection: If your internet connection is weak or intermittent, the app may not load properly. Try reloading the page or visiting the app from a different location./n

✅Try a different browser: Sometimes certain browsers have issues with the app. Try using a different browser, such as Chrome or Firefox, to see if the app works properly./n

✅Contact customer support at CatBreedInfoSupport@gmail.com: If you've tried these steps and still can't use the app, contact customer support for further assistance. Be sure to include details about the issue you're experiencing, including any error messages you may be seeing./n
      """,
      from_ = twilio_number,
      to = phone_number
    )