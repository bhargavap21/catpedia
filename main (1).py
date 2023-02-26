import streamlit as st
from st_pages import Page, show_pages, add_page_title
from streamlit_extras.app_logo import add_logo

show_pages(
    [
        Page("main.py", "Incomegenie Information", "🏠"),
        Page("pages/Catquiz.py", "Cat Quiz", "📝"),
        Page("pages/Breeder.py", "Breeder", "❤️"),
        Page("pages/Purchase.py", "Purchase", "🛒"),
        Page("pages/Help.py", "Help", "🏥")

    ]
)
from PIL import Image

image = Image.open('catpedia.png')
st.image(image, use_column_width= True )
st.title("Catpedia Information")
st.header("How it Works")
st.write("""
Our cat breed information web app provides users with information about different cat breeds, including a description, origin, and temperament. Here's how the app works:

Homepage
When you first visit the app, you'll see the homepage. The homepage displays a welcome message and a dropdown menu that allows you to select a cat breed. You can select a breed by clicking on the dropdown menu and choosing a breed from the list. Once you've selected a breed, click on the "Submit" button to display information about the breed.

Breed Information
After you've selected a breed and clicked on the "Submit" button, you'll see information about that breed. This includes a description, origin, and temperament. You'll also see an image of the selected breed. If you want to learn about another breed, simply return to the homepage and select a new breed from the dropdown menu.

Mixed Breed Information
In addition to providing information about purebred cat breeds, our app also allows you to generate information about a mixed breed of two selected breeds. To do this, click on the "Mixed Breed" tab in the navigation menu. You'll be prompted to select two cat breeds from dropdown menus. Once you've selected two breeds, click on the "Submit" button to generate a name, description, and temperament for the mixed breed. You can generate as many mixed breeds as you like by repeating this process.

Cat API and Cohere API
To retrieve information about cat breeds and images of those breeds, our app uses the Cat API. The Cat API is a web service that provides data about cats, including breeds, images, and more. Our app also uses the Cohere API to generate a name, description, and temperament for a mixed breed of two selected breeds. The Cohere API is a natural language processing API that can be used to generate text based on given prompts.

Streamlit
Our app is built using the Streamlit library, which is a Python library that makes it easy to create web apps with Python. Streamlit provides a simple syntax for creating web apps and allows developers to easily incorporate data and visualizations into their apps.

That's how our cat breed information web app works! We hope you enjoy using it to learn more about different cat breeds.
""")
