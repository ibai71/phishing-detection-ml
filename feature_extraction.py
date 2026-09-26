from bs4 import BeautifulSoup
import os
import features

def open_file(file_name):
    with open(file_name, "r", encoding="utf-8") as f:
        return f.read()

def create_soup(text):
    return BeautifulSoup(text, "html.parser")

def create_vector(soup):
    vector = [
        # Características binarias
        features.has_title(soup),
        features.has_input(soup),
        features.has_button(soup),
        features.has_image(soup),
        features.has_submit(soup),
        features.has_link(soup),
        features.has_password(soup),
        features.has_email_input(soup),
        features.has_hidden_element(soup),
        features.has_audio(soup),
        features.has_video(soup),
        # Características cuantitativas
        features.number_of_inputs(soup),
        features.number_of_buttons(soup),
        features.number_of_images(soup),
        features.number_of_option(soup),
        features.number_of_list(soup),
        features.number_of_TH(soup),
        features.number_of_TR(soup),
        features.number_of_href(soup),
        features.number_of_paragraph(soup),
        features.number_of_script(soup),
        features.length_of_title(soup)
    ]
    return vector