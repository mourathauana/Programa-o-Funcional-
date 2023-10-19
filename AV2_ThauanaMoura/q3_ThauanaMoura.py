from PIL import Image, ImageEnhance

img = Image.open ("POO.png")

aumentarbrilho = ImageEnhance.Brightness(img).enhance(2)
aumentarbrilho.save("POO_.png")

