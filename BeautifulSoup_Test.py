import requests
from bs4 import BeautifulSoup

#let's take some interpretation for the Hafiz's poems!

def get_interpretation(URL):
    page = requests.get(URL)
    if page.status_code != 200:
        print("Failed to fetch page. Status code:", page.status_code)
    soup = BeautifulSoup(page.content, "html.parser")
    desired_class = "wp-block-group gtafsir-hafez is-layout-constrained wp-block-group-is-layout-constrained"
    elements = soup.find_all(class_=desired_class)
    for element in elements:
        print(element.get_text().strip())
URL = "https://satinmod.com/ghazal-494/"  
get_interpretation(URL)

