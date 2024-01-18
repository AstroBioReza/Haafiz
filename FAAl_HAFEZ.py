import tkinter as tk
from tkinter import scrolledtext
import requests
from bs4 import BeautifulSoup
import random

All = range(1, 496)
Answer = random.choice(All)
FAAL = Answer + 2129
url = f"https://ganjoor.net/t6e?p={FAAL}"

def get_web_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        return f"Error fetching content: {e}"

def exclude_elements(html_content, elements_to_exclude=['p']):
    soup = BeautifulSoup(html_content, 'html.parser')
    for element_to_exclude in elements_to_exclude:
        for element in soup.find_all(element_to_exclude):
            element.decompose()
    return str(soup)

def exclude_elements_by_id(html_content, id_to_exclude):
    soup = BeautifulSoup(html_content, 'html.parser')
    div_to_exclude = soup.find('div', id=id_to_exclude)
    if div_to_exclude:
        div_to_exclude.decompose()
    return str(soup)

def show_web_content(url, width=800, height=600):
    root = tk.Tk()
    root.title(f"غزل شمارۀ {Answer}")
    root.geometry(f"{width}x{height}")
    text_widget = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=100, height=40, font= ("Tahoma", 12))
    text_widget.pack(expand=True, fill="both")
    content = get_web_content(url)
    
    elements_to_exclude = ['head', 'a']
    modified_content = exclude_elements_by_id(content, id_to_exclude='t6e-footer')
    modified_content = exclude_elements(modified_content, elements_to_exclude)
    soup = BeautifulSoup(modified_content, 'html.parser')
    text_content = soup.get_text().strip()
    text_widget.insert(tk.END, text_content)
    root.mainloop()

show_web_content(url, width=400, height=500)
