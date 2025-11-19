it utilizes the API of pinterest to look for an image, it can be applied into the same program or as a module (localy) into any other program you need.

for example:

from logic import fetch_random_image

def image ( name: str):
  value = fetch_random_image(name)
  url = requests.get(value)
  return url.content

it can be used in other areas as you might need it.
