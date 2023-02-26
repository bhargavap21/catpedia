import streamlit as st
import requests

# Define a function to retrieve a random cat image using the Cat API
def get_cat_image():
    response = requests.get("https://api.thecatapi.com/v1/images/search")
    data = response.json()
    return data[0]["url"]

# Define a dictionary of cat breeds and their personalities
cat_breeds = {
    "Siamese": "You are vocal and intelligent, and you enjoy being the center of attention.",
    "Maine Coon": "You are sociable and friendly, and you have a big personality.",
    "Persian": "You are laid-back and enjoy a relaxed lifestyle.",
    "Sphynx": "You are adventurous and curious, and you enjoy being the center of attention.",
    "Bengal": "You are active and playful, and you enjoy being around people.",
    "British Shorthair": "You are calm and collected, and you enjoy a quiet lifestyle.",
    "Russian Blue": "You are reserved and independent, and you prefer a small group of close friends.",
    "Scottish Fold": "You are easygoing and affectionate, and you get along well with others.",
    "Norwegian Forest Cat": "You are adventurous and independent, and you enjoy exploring your surroundings.",
    "American Shorthair": "You are sociable and friendly, and you have a big personality."
}

# Define a function to ask the user a question and return their response
def ask_question(question):
    return st.radio(question, ("Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"))

# Define the questions for the quiz
questions = [
    "I enjoy spending time alone.",
    "I prefer a quiet and relaxed lifestyle.",
    "I like to be active and play sports.",
    "I enjoy spending time outdoors.",
    "I like to be the center of attention.",
    "I am affectionate and enjoy physical touch.",
    "I am independent and enjoy exploring new places.",
    "I enjoy socializing with others.",
    "I am intelligent and enjoy problem-solving.",
    "I prefer a small group of close friends."
]

# Define the main function that will run the quiz
def run_quiz():
    # Initialize a dictionary to keep track of the user's responses
    responses = {}

    # Ask the user each question and store their response in the dictionary
    for question in questions:
        response = ask_question(question)
        responses[question] = response

    # Calculate the user's scores for each cat breed
    scores = {breed: 0 for breed in cat_breeds}
    for question, response in responses.items():
        for breed, personality in cat_breeds.items():
            if response == "Strongly Agree" or response == "Agree":
                if breed in personality:
                    scores[breed] += 1

    # Determine the cat breed with the highest score
    top_breed = max(scores, key=scores.get)

    # Display the user's result
    st.write("Based on your responses, we think the best cat breed for you is the **{}**!".format(top_breed))
    st.write(cat_breeds[top_breed])
    st.write("Here is a picture of your recommended cat:")
    st.image(get_cat_image())

# Run the quiz
st.title("Find Your Perfect Cat!")
st.write("Answer the following questions to find out which cat breed would best suit your personality.")
run_quiz()
