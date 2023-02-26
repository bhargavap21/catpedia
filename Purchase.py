import streamlit as st
from twilio.rest import Client
st.title("Looking to buy a cat for yourself?🛒")
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
      Hello and thank you for contacting Catpedia! We are happy to help you find the perfect breed of cat for you. We have a great selection of cats and their attributes available for you to view on our website. If you are looking to purchase these cats we encourage you to use the following websites. For pure bred cats, we recommend you visit https://purebredcatrescue.org/available-cats/. For other breeds, please visit https://www.kittensup4sale.com/. Let us know if we can help you in any way!

Step 1️⃣: Visit our website to view the different cats breeds available. 

Step 2️⃣: Play around with our website, and see if you like any cat breeds, and if you cant choose use our cat breed mixer to get the best of both cats!

Step 3️⃣: Choose the breed of cat that you would like to purchase. 

Step 4️⃣: Visit https://purebredcatrescue.org/available-cats/ to find a pure bred cat that meets your requirements. For other breeds, please visit https://www.kittensup4sale.com/.

Step 5️⃣: Make sure to examine the cat's attributes and patterns carefully before deciding to purchase.

Step 6️⃣: If the cat meets all your requirements, purchase it and enjoy your new furry friend 🐱!
      """,
      from_ = twilio_number,
      to = phone_number
    )