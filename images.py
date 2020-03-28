from PIL import Image, ImageFilter

img = Image.open('./POKEDEX/pikachu.jpg')
filtered_image = img.filter(ImageFilter.SMOOTH)
filtered_image.save("smooth.png", "png")

