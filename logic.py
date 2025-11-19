from pyntrest import PinterestClient
import random
import requests
from io import BytesIO
import webbrowser

# Pinterest client
client = PinterestClient()

# Global variable to store current image URL
current_url = None

# Function to fetch a random image
def fetch_random_image(name):
    global current_url
    # Fetch 20 image links from Pinterest (you can specify search term)
    images = client.get_image_links(name, num_images=20)
    random_image = random.choice(images)
    current_url = random_image['url']  # store the URL
    return current_url

# Function to open the current image URL in browser
def open_link():
    if current_url:
        webbrowser.open(current_url)
    else:
        print("No URL available!")




