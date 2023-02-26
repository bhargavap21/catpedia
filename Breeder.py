import streamlit as st
import requests
from PIL import Image
from io import BytesIO
from random import randint
import cohere
from twilio.rest import Client

# Define function to get information for a single breed
def get_breed_info(breed_id):
    url = f"https://api.thecatapi.com/v1/breeds/{breed_id}"
    response = requests.get(url)
    breed_info = response.json()
    return breed_info


# Define function to get image for a single breed
def get_breed_image(breed_id):
    url = f"https://api.thecatapi.com/v1/images/search?breed_id={breed_id}"
    response = requests.get(url)
    breed_image_info = response.json()[0]
    breed_image_url = breed_image_info["url"]
    return breed_image_url


# Define function to get information for a mixed breed
def get_mixed_breed_info(breed_1_id, breed_2_id):
    url = f"https://api.thedogapi.com/v1/breeds/search?q={breed_1_id}-{breed_2_id}"
    response = requests.get(url)
    mixed_breed_info = {}
    if len(response.json()) > 0:
        mixed_breed_info = response.json()[0]
    return mixed_breed_info


# Define function to get image for a mixed breed
def get_mixed_breed_image(breed_1_id, breed_2_id):
    url = f"https://api.thecatapi.com/v1/images/search?breed_ids={breed_1_id},{breed_2_id}"
    response = requests.get(url)
    mixed_breed_image_info = response.json()[0]
    mixed_breed_image_url = mixed_breed_image_info["url"]
    return mixed_breed_image_url

cohere_api_key = 'Jdckza9gDmn1hGHWRTbwKhG6vEcWTE6PMDC189Hr'
def generate_mixed_breed_name(breed_1_name, breed_2_name):
    co = cohere.Client('Jdckza9gDmn1hGHWRTbwKhG6vEcWTE6PMDC189Hr') #your cohere api key here
    mixed_breed_name = co.generate(
    model='command-xlarge-20221108',
    prompt= f"Generate a name for a mixed breed between {breed_1_name} and {breed_2_name}.",
    max_tokens=300,
    temperature=0.9,
    k=0,
    p=0.75,
    frequency_penalty=0,
    presence_penalty=0,
    stop_sequences=[],
    return_likelihoods='NONE')
    return (mixed_breed_name.generations[0].text)
  

def generate_mixed_breed_description(breed_1_description, breed_2_description, mixed_breed_name):
    co = cohere.Client('Jdckza9gDmn1hGHWRTbwKhG6vEcWTE6PMDC189Hr') #your cohere api key here
    mixed_breed_description = co.generate(
    model='command-xlarge-20221108',
    prompt= f"Generate a description for a mixed breed that is a cross between {breed_1_description} and {breed_2_description} that has the name of {mixed_breed_name}.",
    max_tokens=300,
    temperature=0.9,
    k=0,
    p=0.75,
    frequency_penalty=0,
    presence_penalty=0,
    stop_sequences=[],
    return_likelihoods='NONE')
    return (mixed_breed_description.generations[0].text)

def generate_mixed_breed_temperament(breed_1_temperament, breed_2_temperament):
    co = cohere.Client('Jdckza9gDmn1hGHWRTbwKhG6vEcWTE6PMDC189Hr') #your cohere api key here
    mixed_breed_temperament = co.generate(
    model='command-xlarge-20221108',
    prompt= f"Generate 3 temperaments for a mixed breed that is a cross between {breed_1_temperament} and {breed_2_temperament}.",
    max_tokens=300,
    temperature=0.9,
    k=0,
    p=0.75,
    frequency_penalty=0,
    presence_penalty=0,
    stop_sequences=[],
    return_likelihoods='NONE')
    return (mixed_breed_temperament.generations[0].text)

# Define function for homepage layout and functionality
def homepage():
    # Set up homepage layout
    st.title("Welcome to the Cat App!")
    st.write("Use the navigation on the left to explore different cat-related features.")

# Define function for breed information layout and functionality
def breed_information():
    # Get list of cat breeds
    url = "https://api.thecatapi.com/v1/breeds"
    response = requests.get(url)
    breeds = response.json()

    # Create dropdown menu for breed selection
    breed_name = st.selectbox("Select Breed", [breed["name"] for breed in breeds])

    # Get breed ID from breed name
    breed_id = next((breed["id"] for breed in breeds if breed["name"] == breed_name), None)

    # Check if breed ID was successfully retrieved
    if breed_id:
        # Get information and image for breed
        breed_info = get_breed_info(breed_id)
        breed_name = breed_info["name"]
        breed_description = breed_info["description"]
        breed_temperament = breed_info["temperament"]
        breed_image_url = get_breed_image(breed_id)
        breed_image_response = requests.get(breed_image_url)
        breed_image = Image.open(BytesIO(breed_image_response.content))

        # Display breed information and image
        st.write(f"**Breed:** {breed_name}")
        st.image(breed_image, use_column_width=True)
        st.write(f"**Description** {breed_description}")
        st.write(f"**Temperament** {breed_temperament}")     
    else:
        st.write("Breed not found.")


# Define function for mixed breed information layout and functionality
# Define function for mixed breed information layout and functionality
def mixed_breed_information():
    # Get list of cat breeds
    url = "https://api.thecatapi.com/v1/breeds"
    response = requests.get(url)
    breeds = response.json()
    
    # Create dropdown menus for breed selection
    breed_1_name = st.selectbox("Select First Breed", [breed["name"] for breed in breeds])
    breed_1_id = next((breed["id"] for breed in breeds if breed["name"] == breed_1_name), None)
    breed_1_info = get_breed_info(breed_1_id)
    breed_1_description = breed_1_info["description"]
    breed_1_temperament= breed_1_info["temperament"]
  
    breed_2_name = st.selectbox("Select Second Breed", [breed["name"] for breed in breeds])
    breed_2_id = next((breed["id"] for breed in breeds if breed["name"] == breed_2_name), None)
    breed_2_info = get_breed_info(breed_2_id)
    breed_2_description = breed_2_info["description"]
    breed_2_temperament = breed_2_info["temperament"]
    # Get breed IDs from breed names

    # Check if breed IDs were successfully retrieved
    if breed_1_id and breed_2_id:
        # Get information and image for mixed breed
        mixed_breed_info = get_mixed_breed_info(breed_1_name, breed_2_name)
        mixed_breed_name = generate_mixed_breed_name(breed_1_name,breed_1_name)
        mixed_breed_description = generate_mixed_breed_description(breed_1_description, breed_2_description, mixed_breed_name)
        mixed_breed_temperament = mixed_breed_info.get(breed_1_temperament, breed_2_temperament)
        mixed_breed_image_url = get_mixed_breed_image(breed_1_id, breed_2_id)
        mixed_breed_image_response = requests.get(mixed_breed_image_url)
        mixed_breed_image = Image.open(BytesIO(mixed_breed_image_response.content))

        # Display mixed breed information and image
        st.write(f"**Mixed Breed:** {mixed_breed_name}")
        st.image(mixed_breed_image, use_column_width=True)
        st.write(f"**Description:** {mixed_breed_description}")
        st.write(f"**Temperament:** {mixed_breed_temperament}")
    else:
        st.write("One or both breeds not found.")
# def gym():
  
#   st.title("GYM")
#   global strength
#   global strengthlim
#   st.write(strength)
#   st.write(strengthlim)
#   if 'count' not in st.session_state:
#       st.session_state.count = 0
        
#   def increment_counter():
#       st.session_state.count += 1
        
#   st.button('Increment', on_click=increment_counter)
#   if(strength<strengthlim):
#       strength+=st.session_state.count
#   else:
#       st.write('<p style="font-family:Courier; color:Red; font-size: 20px;">Sorry Genetic Limit Reached</p>')
#   st.write('Strength = ', strength)
PAGES = {
"Breed Information": breed_information,
"Mixed Breed Information": mixed_breed_information,
}
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page()



