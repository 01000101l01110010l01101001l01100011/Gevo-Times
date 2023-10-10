import PIL
from PIL import Image
PIL.features.pilinfo()
img = Image.open("FR.svg")
img.save("FR.png")
img = Image.open("S.svg")
img.save("S.png")
img = Image.open("G.svg")
img.save("G.png")